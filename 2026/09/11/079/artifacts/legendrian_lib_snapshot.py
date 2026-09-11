"""
legendrian.py

Python implementation of Legendrian knot and link invariants,
with an object-oriented interface.

Original algorithms from a Mathematica notebook by Paul Melvin (core Z/2),
extended by Kirk Mangels, Alden Walker, Lenny Ng, Josh Sabloff, and Sumana Shrestha.

Classes
-------
GroundRing    Coefficient ring: Z/2, Z[λ], or Z/p for prime p.
Leg           A Legendrian knot or link given as a plat-closure braid.
DGA           The contact-homology DGA of a Leg over a chosen GroundRing.
Augmentation  A single augmentation of a DGA.

Quick start
-----------
    from legendrian import Leg, GroundRing

    k = Leg([2, 2, 2])          # trefoil by braid word
    k = Leg('mK3_1')            # trefoil from atlas
    print(k.tb, k.rot)

    d = k.dga()                 # DGA over Z/2 (default)
    augs = d.augmentations()
    for a in augs:
        print(a.lin_hom)

    d2 = k.dga('Zlambda')       # DGA over Z[λ]
    d2.check_d_squared()

Atlas naming convention
-----------------------
    'K3_1'        unique Legendrian rep of knot 3_1 (Rolfsen table)
    'K3_1.0'      same, with explicit 0-based index
    'mK5_2'       unique rep of mirror of 5_2
    'mK5_2.0'     first of two reps of mirror of 5_2
    'mK5_2.1'     second rep
    'K11n38'      knot 11n38 (Hoste-Thistlethwaite table)
    Mirror prefix 'm', knot prefix 'K', link prefix 'L'.
    Legendrian index is 0-based; omit when unique.

Input format
------------
Leg accepts four input forms.

Braid word — a list of positive integers encoding the plat closure of a positive
braid.  Generator i represents a positive crossing between strands i and i+1
(counting from the top, 1-indexed).  All left cusps share one x-coordinate and
all right cusps share another.

    Leg([2, 2, 2])    standard Legendrian right-handed trefoil

Tangle decomposition — a list of tuples describing a general front diagram as a
left-to-right sequence of elementary moves:

    ('<', h)   left cusp at height h (0-indexed from the top, current strand count)
    ('>', h)   right cusp at height h
    ('X', h)   positive crossing between strands h and h+1

The code converts the tangle to plat form internally using Legendrian Reidemeister
II moves, and stores the original sequence as self.tangle.

    Leg([('<', 0), ('<', 0), ('X', 1), ('X', 0), ('X', 1), ('>', 0), ('>', 0)])

Grid diagram — a pair of permutations (X_perm, O_perm) passed as a 2-tuple of
lists.  X_perm[j] is the row of the X marker in column j; O_perm[j] is the row
of the O marker in column j.  Rows are 0-indexed from the bottom; columns are
0-indexed from the left.  Vertical strands pass over horizontal strands.  The
Legendrian front projection is obtained by rotating the grid 45° counter-
clockwise, which maps horizontal segments to slope +1 and vertical segments to
slope -1.  The algorithm detects left cusps, right cusps, crossings, and kinks
(transitions between horizontal and vertical strands), produces a tangle
sequence, and converts it to plat form via Legendrian Reidemeister moves.

    Leg(([1, 0], [0, 1]))   2×2 grid for the Legendrian unknot (tb = -1)

Atlas name — a string key into the built-in ATLAS dictionary.

    Leg('mK3_1')      mirror trefoil (unique representative)
    Leg('mK5_2.0')    first of two reps of mirror 5_2 (0-indexed)

Dependencies (install via pip):
    matplotlib    -- for Leg.draw()
    numpy         -- for Leg.draw()
    scipy         -- for smooth spline curves (optional; falls back to polyline)

License
-------
This file is part of the Legendrian knot invariants library.
Copyright (C) 2025  Robert Lipshitz and contributors.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from __future__ import annotations

__version__ = "0.5.0"

import re
from collections import Counter
from fractions import Fraction
from functools import cached_property, reduce
from itertools import combinations, product
from math import gcd, inf
from typing import Any, ClassVar, Dict, Iterable, List, Literal, NamedTuple, Optional, Tuple, Union, cast, overload


# ============================================================
# Section 1: GroundRing
# ============================================================

class GroundRing:
    """
    Coefficient ring for a DGA computation.

    Pre-defined class attributes (singletons):
        GroundRing.Z2      -- the field F_2 = Z/2Z
        GroundRing.ZLAMBDA -- the polynomial ring Z[λ]

    Factory for other primes:
        GroundRing.Zn(p)   -- the field F_p = Z/pZ  (p prime)

    The constructor also accepts a string:
        GroundRing('Z2'), GroundRing('Zlambda'), GroundRing('Z3')
    """

    Z2: ClassVar[GroundRing]
    ZLAMBDA: ClassVar[GroundRing]

    def __init__(self, modulus_or_str: Union[int, str]) -> None:
        if isinstance(modulus_or_str, str):
            other = GroundRing.from_str(modulus_or_str)
            self.modulus: int = other.modulus
        else:
            self.modulus = int(modulus_or_str)

    def __repr__(self) -> str:
        if self.modulus == 0:
            return 'GroundRing.ZLAMBDA'
        if self.modulus == 2:
            return 'GroundRing.Z2'
        return f'GroundRing.Zn({self.modulus})'

    def __hash__(self) -> int:
        return hash(self.modulus)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GroundRing) and self.modulus == other.modulus

    @classmethod
    def Zn(cls, n: int) -> 'GroundRing':
        """Return the ring Z/nZ.

        Augmentation enumeration works for any n ≥ 2.  Row reduction and
        linearized-homology computations additionally require n to be prime
        (so that Z/nZ is a field); those methods raise NotImplementedError
        for composite n.
        """
        return cls(n)

    @classmethod
    def from_str(cls, s: str) -> 'GroundRing':
        """Parse 'Z2', 'Zlambda', 'Z3', etc. into a GroundRing."""
        s = s.strip()
        if s in ('Z2', 'z2', 'F2', 'f2'):
            return cls.Z2
        if s.lower() in ('zlambda', 'z[lambda]', 'zlam'):
            return cls.ZLAMBDA
        m = re.match(r'[ZzFf](\d+)$', s)
        if m:
            return cls(int(m.group(1)))
        raise ValueError(
            f'Unknown ground ring {s!r}. Use "Z2", "Zlambda", "Z3", "F3", etc.'
        )


GroundRing.Z2 = GroundRing(2)
GroundRing.ZLAMBDA = GroundRing(0)

DEFAULT_GROUND_RING: GroundRing = GroundRing.Z2

# Maximum brute-force search-space size (post-presolve) before augmentations()
# raises AugSearchLimitError.
#
# This bounds the number of augmentation CANDIDATES evaluated, not the number
# of augmentations found: the product of per-variable ranges over the free
# variables that survive linear pre-reduction (2^k for Z/2, since each free
# variable there ranges over {0,1} -- Z/2 uses the same linear-presolve +
# brute-force algorithm as every other Z/n).
#
# Per-candidate cost is dominated by evaluating every grade-1 condition, so it
# scales with the knot's condition count -- it is NOT a fixed few-ns constant.
# Tiny knots run in tens of ns/candidate; for large knots (dozens-to-~100+
# grade-0 generators), measurement across the atlas found
# ~2.5-7.7 µs/candidate, roughly ring-independent. The default of 3*10**7
# targets a several-minute wall-clock budget in that regime; raise the limit
# or pass max_search=None to DGA.augmentations() if you need results for knots
# with larger search spaces, or use DGA.one_aug to find a single augmentation
# (or certify none) far faster than enumerating.
DEFAULT_AUG_SEARCH_LIMIT: int = 3 * 10**7

# Sentinel for the `max_search` default. Distinguishes "caller omitted
# max_search" (resolve to the *current* module-level DEFAULT_AUG_SEARCH_LIMIT at
# call time) from an explicit `max_search=None` (disable the limit). Binding
# DEFAULT_AUG_SEARCH_LIMIT directly as the default value would freeze its value
# into the function object at definition time, so reassigning the module global
# after import would have no effect; the sentinel reads the global on each call.
_USE_DEFAULT_AUG_LIMIT: Optional[int] = object()  # type: ignore[assignment]

# Backtracking-node budget for DGA.one_aug, reusing the _USE_DEFAULT_AUG_LIMIT
# sentinel (omitted -> resolve this global at call time; one_aug(max_nodes=None)
# disables the cap).  This counts search-tree nodes -- one constraint-propagation
# step each -- NOT static candidate evaluations like DEFAULT_AUG_SEARCH_LIMIT.
# The two are different quantities: a backtracking search with strong propagation
# visits far fewer nodes than the product bound it replaces, so the much larger
# DEFAULT_AUG_SEARCH_LIMIT candidate cap would be meaningless here (it would
# never trip in any realistic wall-clock window).  Under fail-first
# propagation a *satisfiable* mid-size instance resolves in well under
# 10**4 nodes, so 10**5 almost never trips on a real diagram while still
# bounding a pathological (usually unsatisfiable) blow-up.  This is a
# runaway-search guard, not a wall-clock SLA.
DEFAULT_ONE_AUG_NODE_LIMIT: int = 10**5


class AugSearchLimitError(RuntimeError):
    """Raised by DGA.augmentations() when the brute-force search space exceeds
    the configured *max_search* limit after iterative linear pre-reduction.

    The search-space size is the number of augmentation candidates the brute
    force would evaluate: 2^k for Z/2 (k free generators) or the product of
    per-variable ranges for Z/n.  It bounds candidate *evaluations*, not the
    number of augmentations found nor wall-clock time directly.

    The exception message states the computed size and the limit.
    Pass ``max_search=None`` to DGA.augmentations() to disable the check.
    """


class _AugSystem(NamedTuple):
    """The Z/n augmentation-search system for a DGA at a fixed grading_mod.

    Built by DGA._augmentation_system and consumed by both the brute-force
    aug_zn path inside DGA.augmentations() and the backtracking DGA.one_aug
    search, so the two agree on variables, value ranges, and conditions.

    Fields:
      conditions   list of polynomial conditions, one per grade-1 generator
                   (same order as grade1_gens); each is a list of (word, coeff)
                   terms that must sum to 0 mod n under any augmentation
                   (words filtered to grade-0 candidate letters).
      var_ranges   dict var_key -> list of admissible values: range(n) for a
                   grade-0 generator index; the units of Z/n (or a fixed value)
                   for a ('lambda', c) key.
      all_vars     ordered variable keys: grade-0 generators then ('lambda', c).
      grade0_gens  the 1-indexed grade-0 generator keys (subset of all_vars).
      grade1_gens  the 1-indexed grade-1 generator keys, in the same order as
                   conditions (conditions[i] is grade1_gens[i]'s equation).
      lambda_keys  the ('lambda', c) keys (the remainder of all_vars).
      units        the units of Z/n (admissible lambda / pivot-lambda values).
    """
    conditions: List[List[Tuple[tuple, int]]]
    var_ranges: Dict[Any, List[int]]
    all_vars: List[Any]
    grade0_gens: List[int]
    grade1_gens: List[int]
    lambda_keys: List[Tuple[str, int]]
    units: List[int]


# ============================================================
# Section 2: Private algorithmic subroutines
# ============================================================
# These are low-level building blocks used by multiple class methods.
# They are NOT 1-to-1 duplicates of any class member.

# --- Linear algebra over F_2 (used by DGA.lin_hom and Augmentation) ---

def _rref_f2(mat):
    """Row-reduce mat over F_2. Returns (rref_matrix, pivot_column_indices)."""
    m = [row[:] for row in mat]
    rows = len(m)
    if not rows or not m[0]:
        return m, []
    cols = len(m[0])
    pivot_cols, pivot_row = [], 0
    for col in range(cols):
        found = next((r for r in range(pivot_row, rows) if m[r][col] % 2), -1)
        if found == -1:
            continue
        m[pivot_row], m[found] = m[found], m[pivot_row]
        pivot_cols.append(col)
        for r in range(rows):
            if r != pivot_row and m[r][col] % 2:
                m[r] = [(m[r][j] ^ m[pivot_row][j]) for j in range(cols)]
        pivot_row += 1
    return m, pivot_cols


def _rank_f2(mat) -> int:
    if not mat or not mat[0]:
        return 0
    _, pivots = _rref_f2(mat)
    return len(pivots)


def _is_prime(n: int) -> bool:
    """Return True iff n is a prime integer."""
    return n >= 2 and not any(n % k == 0 for k in range(2, int(n**0.5) + 1))


def _rref_zn(mat, n):
    """Row-reduce mat over Z/nZ. Raises NotImplementedError if n is not prime."""
    if not _is_prime(n):
        raise NotImplementedError(
            f'Row reduction requires a field; Z/{n} is not a field (n must be prime).'
        )
    m = [[x % n for x in row] for row in mat]
    rows = len(m)
    if not rows or not m[0]:
        return m, []
    cols = len(m[0])
    pivot_cols, pivot_row = [], 0
    for col in range(cols):
        found = next((r for r in range(pivot_row, rows) if m[r][col] % n), -1)
        if found == -1:
            continue
        m[pivot_row], m[found] = m[found], m[pivot_row]
        inv = pow(m[pivot_row][col], -1, n)
        m[pivot_row] = [(x * inv) % n for x in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and m[r][col] % n:
                factor = m[r][col]
                m[r] = [(m[r][j] - factor * m[pivot_row][j]) % n for j in range(cols)]
        pivot_cols.append(col)
        pivot_row += 1
    return m, pivot_cols


def _rank_zn(mat, n) -> int:
    if not mat or not mat[0]:
        return 0
    _, pivots = _rref_zn(mat, n)
    return len(pivots)


# --- Integer linear algebra (Smith normal form) -- used by DGA.bilin_hom_z ---
#
# Unlike the Z/p code above, homology over Z can have torsion, so rank alone
# isn't enough: we need the full Smith normal form U*A*V = D (D diagonal,
# d_1 | d_2 | ... | d_r, U and V unimodular) to read off free ranks (zero
# diagonal entries) and torsion (diagonal entries > 1).

def _select_pivot(mat: List[List[int]], U: List[List[int]], V: List[List[int]], k: int) -> bool:
    """Find the smallest-|value| nonzero entry in mat[k:,k:] and swap it to
    (k,k) via row/column swaps (mirrored onto U/V). Returns False (no-op) iff
    mat[k:,k:] is entirely zero."""
    nrows, ncols = len(mat), len(mat[0]) if mat else 0
    best = None
    for i in range(k, nrows):
        for j in range(k, ncols):
            v = mat[i][j]
            if v != 0 and (best is None or abs(v) < abs(best[0])):
                best = (v, i, j)
    if best is None:
        return False
    _, bi, bj = best
    if bi != k:
        mat[k], mat[bi] = mat[bi], mat[k]
        U[k], U[bi] = U[bi], U[k]
    if bj != k:
        for row in mat:
            row[k], row[bj] = row[bj], row[k]
        for row in V:
            row[k], row[bj] = row[bj], row[k]
    return True


def _clear_column(mat: List[List[int]], U: List[List[int]], k: int) -> bool:
    """Zero mat[i][k] for i>k, mirrored onto U -- via *multi-way* reduction:
    repeatedly find whichever row in k..end currently has the smallest
    nonzero |entry| at column k, swap it to row k, and reduce every other row
    against it by floor division. This matters for more than just efficiency:
    reducing everything against a single fixed row k (even via a correct
    extended-gcd combine) lets already-inflated entries elsewhere in row k
    propagate into every other row every time this is called, and since
    _clear_row's column operations touch every row too, that inflation
    compounds across pivot steps into doubly-exponential blowup. Always
    reducing against the *current* smallest keeps every row close to the
    scale of the smallest surviving value, the same reason the Euclidean
    algorithm's remainders stay small. Returns whether any row was combined."""
    changed = False
    while True:
        idxs = [i for i in range(k, len(mat)) if mat[i][k] != 0]
        if len(idxs) <= 1:
            break
        best = min(idxs, key=lambda i: abs(mat[i][k]))
        if best != k:
            mat[k], mat[best] = mat[best], mat[k]
            U[k], U[best] = U[best], U[k]
        for i in idxs:
            if i == k:
                continue
            factor = mat[i][k] // mat[k][k]
            if factor:
                mat[i] = [bi - factor * ai for ai, bi in zip(mat[k], mat[i])]
                U[i] = [bi - factor * ai for ai, bi in zip(U[k], U[i])]
        changed = True
    return changed


def _clear_row(mat: List[List[int]], V: List[List[int]], k: int) -> bool:
    """Zero mat[k][j] for j>k, mirrored onto V -- the column analogue of
    _clear_column (see its docstring for why multi-way reduction against the
    current smallest entry, not a fixed column, is essential to avoid
    coefficient blowup). Returns whether any column was combined."""
    changed = False
    ncols = len(mat[0]) if mat else 0
    while True:
        idxs = [j for j in range(k, ncols) if mat[k][j] != 0]
        if len(idxs) <= 1:
            break
        best = min(idxs, key=lambda j: abs(mat[k][j]))
        if best != k:
            for row in mat:
                row[k], row[best] = row[best], row[k]
            for row in V:
                row[k], row[best] = row[best], row[k]
        for j in idxs:
            if j == k:
                continue
            factor = mat[k][j] // mat[k][k]
            if factor:
                for row in mat:
                    row[j] -= factor * row[k]
                for row in V:
                    row[j] -= factor * row[k]
        changed = True
    return changed


def _smith_normal_form(A: List[List[int]]) -> Tuple[List[List[int]], List[List[int]], List[List[int]]]:
    """Exact integer Smith normal form: returns (D, U, V) with U*A*V = D,
    U (len(A) x len(A)) and V (ncols x ncols) unimodular (det = +-1), D
    diagonal with d_1 | d_2 | ... | d_r (r = rank), all other entries 0.

    At each step k: _select_pivot finds the globally-smallest nonzero entry in
    the remaining submatrix and swaps it to (k,k); _clear_column/_clear_row
    then zero out the rest of column/row k via multi-way row/column reduction
    (repeated, since clearing the row can reintroduce nonzeros below the
    pivot -- see _clear_column's docstring for why multi-way, not a fixed
    pivot row/column, is needed to keep entries from blowing up). That alone
    gives *a* diagonalization, but not one where each diagonal entry divides
    the next -- if some remaining entry mat[i][j] (i,j>k) isn't divisible by
    the pivot, adding row i into row k and re-clearing injects that entry
    into the pivot position, strictly shrinking |pivot| via gcd; this is the
    divisibility-chain fixup, repeated until the pivot divides everything
    left in the submatrix.
    """
    nrows = len(A)
    ncols = len(A[0]) if nrows else 0
    mat = [row[:] for row in A]
    U = [[1 if i == j else 0 for j in range(nrows)] for i in range(nrows)]
    V = [[1 if i == j else 0 for j in range(ncols)] for i in range(ncols)]

    r = min(nrows, ncols)
    k = 0
    while k < r:
        if not _select_pivot(mat, U, V, k):
            break
        while True:
            c1 = _clear_column(mat, U, k)
            c2 = _clear_row(mat, V, k)
            if not c1 and not c2:
                break

        while True:
            bad = next(((i, j) for i in range(k + 1, nrows) for j in range(k + 1, ncols)
                        if mat[i][j] % mat[k][k] != 0), None)
            if bad is None:
                break
            bi, _ = bad
            for c in range(ncols):
                mat[k][c] += mat[bi][c]
            for c in range(nrows):
                U[k][c] += U[bi][c]
            while True:
                c1 = _clear_column(mat, U, k)
                c2 = _clear_row(mat, V, k)
                if not c1 and not c2:
                    break

        if mat[k][k] < 0:
            mat[k] = [-x for x in mat[k]]
            U[k] = [-x for x in U[k]]
        k += 1

    return mat, U, V


def _int_rank(A: List[List[int]]) -> int:
    """Rank of an integer matrix via Smith normal form (# nonzero invariant
    factors) -- the Z analogue of _rank_zn."""
    if not A or not A[0]:
        return 0
    D, _, _ = _smith_normal_form(A)
    r = min(len(D), len(D[0]))
    return sum(1 for i in range(r) if D[i][i] != 0)


def _int_kernel_basis(A: List[List[int]], ncols: Optional[int] = None) -> List[List[int]]:
    """Z-basis of the saturated lattice ker(A) subset Z^ncols, as a list of
    integer vectors (each of length ncols = number of columns of A). Given
    U*A*V = D, A*v = 0 iff D*(V^{-1}*v) = 0, which holds exactly at the
    zero-diagonal positions of D (including every column beyond D's diagonal,
    when A has more columns than rows) -- so the kernel is spanned by V's
    columns at those positions.

    ncols: the domain dimension, i.e. the number of columns of A. Inferred
    from len(A[0]) when omitted -- but a list of *zero rows* carries no width
    information at all (A = [] looks the same regardless of the intended
    domain size), so callers that might pass such an A (a map into an empty
    codomain, e.g. the bilin_hom_z_gens top grading with nothing above it)
    must pass ncols explicitly, or this silently returns an empty basis for a
    nonempty domain."""
    if ncols is None:
        ncols = len(A[0]) if A else 0
    if not A:
        return [[1 if i == j else 0 for i in range(ncols)] for j in range(ncols)]
    D, _, V = _smith_normal_form(A)
    nrows = len(A)
    r = min(nrows, ncols)
    zero_cols = [i for i in range(r) if D[i][i] == 0] + list(range(r, ncols))
    return [[V[row][i] for row in range(ncols)] for i in zero_cols]


def _int_solve_in_basis(K: List[List[int]], cols: List[List[int]]) -> List[List[int]]:
    """Given a lattice basis K (m vectors, each of length n, assumed saturated
    -- e.g. from _int_kernel_basis) and vectors `cols` (each of length n)
    already known to lie in span_Z(K), return each vector's integer
    coordinates in the K-basis (length-m lists).

    Writes K as an n x m matrix and takes its Smith normal form U*K_mat*V = D;
    since K is saturated, D = [I_m; 0] (m unit diagonal entries, no torsion).
    For v = K_mat @ x, U*v = D*(V^{-1}*x), so (U*v)[:m] == V^{-1}*x, giving
    x = V @ (U*v)[:m]."""
    m = len(K)
    if m == 0:
        return [[] for _ in cols]
    n = len(K[0])
    K_mat = [[K[j][i] for j in range(m)] for i in range(n)]
    _, U, V = _smith_normal_form(K_mat)
    result = []
    for col in cols:
        u_col = [sum(U[i][t] * col[t] for t in range(n)) for i in range(n)]
        y = u_col[:m]
        x = [sum(V[i][t] * y[t] for t in range(m)) for i in range(m)]
        result.append(x)
    return result


def _unimodular_inverse(M: List[List[int]]) -> List[List[int]]:
    """Inverse of a unimodular integer matrix M (det = +-1), computed exactly
    via Gauss-Jordan elimination over the rationals (Fraction) -- guaranteed
    to land on integers since det(M) = +-1. Used by DGA.bilin_hom_z_gens to
    invert a Smith-normal-form change-of-basis matrix back onto the original
    kernel basis."""
    m = len(M)
    aug = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(m)]
           for i, row in enumerate(M)]
    for col in range(m):
        piv = next(r for r in range(col, m) if aug[r][col] != 0)
        aug[col], aug[piv] = aug[piv], aug[col]
        inv = 1 / aug[col][col]
        aug[col] = [x * inv for x in aug[col]]
        for r in range(m):
            if r != col and aug[r][col] != 0:
                factor = aug[r][col]
                aug[r] = [x - factor * y for x, y in zip(aug[r], aug[col])]
    return [[int(x) for x in row[m:]] for row in aug]


def _term_type(word: tuple):
    """Classify a word for _linear_presolve_zn's linear/nonlinear split:
    'const' (empty word), 'gen' (a single chord letter), ('lambda', c) (a single
    bare basepoint letter t_c^1 -- power exactly 1), or None (nonlinear: multiple
    letters, λ^k with |k|>1, λ⁻¹, or λ×generator)."""
    if len(word) == 0:
        return 'const'
    if len(word) == 1:
        letter = word[0]
        if isinstance(letter, int):
            return 'gen'
        _, c, k = letter
        return ('lambda', c) if k == 1 else None
    return None


def _linear_presolve_zn(conditions, all_vars, n):
    """
    Gaussian elimination pre-reduction for Z/p (p prime) augmentation search.

    Extracts purely linear conditions — those where every term is a constant
    ``()``, a single generator ``(gi,)``, or a bare lambda ``(('lambda', c, 1),)``
    — and row-reduces the resulting augmented system [A | b] over Z/p. Everything
    else (products, λ^k with |k|>1, λ⁻¹, λ×generator) is nonlinear and excluded;
    it falls through to brute force.

    Returns None if the linear subsystem is inconsistent (certifying no
    augmentations exist).

    Otherwise returns (pivot_map, free_keys):
      pivot_map  dict {var_key: (const, [(neg_coeff, free_key), ...])} giving
                 x_pivot ≡ const + Σ neg_coeff·x_free  (mod p)
      free_keys  list of variable keys not determined by the linear subsystem
    """
    num_vars = len(all_vars)
    var_idx = {v: i for i, v in enumerate(all_vars)}

    rows = []
    for cond in conditions:
        if not cond:
            continue
        row = [0] * (num_vars + 1)
        linear = True
        for word, coeff in cond:
            t = _term_type(word)
            if t is None:
                linear = False
                break
            if t == 'const':
                row[num_vars] = (row[num_vars] - coeff) % n
            elif t == 'gen':
                col = var_idx.get(word[0])
                if col is not None:
                    row[col] = (row[col] + coeff) % n
            else:  # bare lambda: t is ('lambda', c)
                col = var_idx.get(t)
                if col is not None:
                    row[col] = (row[col] + coeff) % n
        if linear and any(row):
            rows.append(row)

    if not rows:
        return {}, list(all_vars)

    rref, pivot_cols = _rref_zn(rows, n)

    if num_vars in pivot_cols:
        return None  # inconsistent: a row reduces to 0 = nonzero

    pivot_set = set(pivot_cols)
    free_col_indices = [i for i in range(num_vars) if i not in pivot_set]
    free_keys = [all_vars[i] for i in free_col_indices]

    pivot_map = {}
    for row_idx, col in enumerate(pivot_cols):
        piv_key = all_vars[col]
        const = rref[row_idx][num_vars]
        coeff_list = [
            ((-rref[row_idx][fc]) % n, all_vars[fc])
            for fc in free_col_indices
            if rref[row_idx][fc] != 0
        ]
        pivot_map[piv_key] = (const, coeff_list)

    return pivot_map, free_keys


def _substitute_conds_zn(conditions, fixed, n):
    """Substitute fixed variable values into Z/n polynomial conditions.

    fixed maps variable keys (int generator index or ('lambda', c)) to values.
    Returns simplified conditions; zero-coefficient terms are dropped.
    Conditions that become empty (0 = 0) are kept as [] — harmless for
    _linear_presolve_zn.  Conditions that reduce to a nonzero constant are
    kept as [((), c)] so that _linear_presolve_zn detects inconsistency.
    """
    result = []
    for cond in conditions:
        merged: Dict[tuple, int] = {}
        for word, coeff in cond:
            new_coeff = coeff
            new_word = []
            for letter in word:
                if new_coeff == 0:
                    break
                if isinstance(letter, int):
                    if letter in fixed:
                        new_coeff = (new_coeff * fixed[letter]) % n
                    else:
                        new_word.append(letter)
                else:
                    _, c, k = letter
                    lam_key = ('lambda', c)
                    if lam_key in fixed:
                        lam_val = fixed[lam_key]
                        new_coeff = 0 if lam_val == 0 else (new_coeff * pow(lam_val, k, n)) % n
                    else:
                        new_word.append(letter)
            if new_coeff == 0:
                continue
            key = _normalize_word(tuple(new_word))
            merged[key] = (merged.get(key, 0) + new_coeff) % n
        result.append([(w, c) for w, c in merged.items() if c != 0])
    return result


def _iterative_presolve_zn(conditions, all_vars, n):
    """Iterative linear pre-reduction for Z/p (p prime) augmentation search.

    After each call to _linear_presolve_zn, any variable that is now fully
    determined (pivot with no free-variable dependencies) is substituted back
    into all conditions — including nonlinear ones.  Partially-specialized
    nonlinear terms can then collapse into new linear constraints, which the
    next round picks up.  Repeats until no new variables are pinned.

    Returns (pivot_map, free_keys) or None if the system is inconsistent.
    The pivot_map combines all rounds: fully-determined entries have an empty
    coeff_list; partially-determined entries express the variable as a linear
    combination of the final free_keys.
    """
    fixed: dict = {}
    current_conds = [list(c) for c in conditions]
    remaining_vars = list(all_vars)

    while remaining_vars:
        result = _linear_presolve_zn(current_conds, remaining_vars, n)
        if result is None:
            return None
        pivot_map, free_keys = result

        new_fixed = {var: const
                     for var, (const, coeff_list) in pivot_map.items()
                     if not coeff_list}

        if not new_fixed:
            # For Z/2: propagate "1 + x₁·x₂·…·xₖ = 0 mod 2" → all xᵢ = 1.
            # Conditions where every generator is in free_keys (not yet determined
            # by the linear system) are the only safe targets.
            if n == 2:
                free_set = set(free_keys)
                for cond in current_conds:
                    if len(cond) != 2:
                        continue
                    has_unit_const = any(word == () and c % 2 == 1 for word, c in cond)
                    if not has_unit_const:
                        continue
                    prod_terms = [(w, c) for w, c in cond if w != ()]
                    if len(prod_terms) == 1:
                        w, c = prod_terms[0]
                        if c % 2 == 1 and all(isinstance(g, int) and g in free_set for g in w):
                            for g in w:
                                new_fixed[g] = 1

        if not new_fixed:
            # Truly converged: no new assignments from linear or product passes.
            final_pivot_map = {var: (val, []) for var, val in fixed.items()}
            final_pivot_map.update(pivot_map)
            return final_pivot_map, free_keys

        fixed.update(new_fixed)
        remaining_vars = [v for v in remaining_vars if v not in fixed]
        current_conds = _substitute_conds_zn(current_conds, new_fixed, n)

    return {var: (val, []) for var, val in fixed.items()}, []


def _null_space_f2(m):
    """Null space (kernel basis) of an F_2 matrix m (list of row lists)."""
    if not m or not m[0]:
        return []
    c = len(m[0])
    rref, pivot_cols = _rref_f2(m)
    pivot_set = set(pivot_cols)
    free_cols = [j for j in range(c) if j not in pivot_set]
    basis = []
    for fc in free_cols:
        vec = [0] * c
        vec[fc] = 1
        for pi, pc in enumerate(pivot_cols):
            if pi < len(rref):
                vec[pc] = rref[pi][fc] % 2
        basis.append(vec)
    return basis


def _dual_cocycle_basis_f2(cocycle_ker, chain_cycle_sets, n):
    """Over F_2: cochain-cocycle reps in Z/2^n, Kronecker-dual to chain-cycle reps.

    cocycle_ker: basis for ker(d1^T) as a list of 0/1 row-vectors of length n.
    chain_cycle_sets: list of frozensets of 0-indexed positions (chain-cycle supports).

    Returns one dual cochain-cocycle vector per chain-cycle set, such that
    <dual_j, chain_k> = delta_{jk} over F_2.
    """
    m = len(chain_cycle_sets)
    r = len(cocycle_ker)
    if m == 0:
        return []
    # Kronecker pairing matrix K[i][j] = dot(cocycle_ker[i], chain_cycle_sets[j]) mod 2
    K = [[sum(cocycle_ker[i][p] for p in chain_cycle_sets[j]) % 2
          for j in range(m)]
         for i in range(r)]
    # Augment [K | I_r], row-reduce K portion to identity to extract dual vectors.
    aug = [list(K[i]) + [1 if i == ii else 0 for ii in range(r)] for i in range(r)]
    pivot_rows: List[tuple] = []
    pivot_set: set = set()
    for col in range(m):
        pivot = next((row for row in range(r)
                      if row not in pivot_set and aug[row][col] == 1), None)
        if pivot is None:
            raise ValueError(f'Kronecker pairing degenerate at column {col}')
        pivot_rows.append((pivot, col))
        pivot_set.add(pivot)
        for row in range(r):
            if row != pivot and aug[row][col] == 1:
                aug[row] = [(aug[row][k] + aug[pivot][k]) % 2 for k in range(m + r)]
    result = []
    for pivot_row, _ in sorted(pivot_rows, key=lambda x: x[1]):
        coeffs = aug[pivot_row][m:]
        dual_vec = [sum(coeffs[i] * cocycle_ker[i][p] for i in range(r)) % 2 for p in range(n)]
        result.append(dual_vec)
    return result


def _null_space_zn(m, n):
    """Null space (kernel basis) of a Z/n matrix m (list of row lists), n prime."""
    if not m or not m[0]:
        return []
    c = len(m[0])
    rref, pivot_cols = _rref_zn(m, n)
    pivot_set = set(pivot_cols)
    free_cols = [j for j in range(c) if j not in pivot_set]
    basis = []
    for fc in free_cols:
        vec = [0] * c
        vec[fc] = 1
        for pi, pc in enumerate(pivot_cols):
            if pi < len(rref):
                vec[pc] = (-rref[pi][fc]) % n
        basis.append(vec)
    return basis


def _quotient_basis_zn(ker_vecs, im_vecs, sz, n):
    """Basis for ker/im over Z/n (n prime; both subspaces of (Z/n)^sz, im ⊆ ker)."""
    if not ker_vecs:
        return []
    pivots: dict = {}

    def reduce_vec(v):
        reduced = list(v)
        for pc in sorted(pivots):
            factor = reduced[pc] % n
            if factor:
                reduced = [(reduced[j] - factor * pivots[pc][j]) % n for j in range(sz)]
        return reduced

    def record_pivot(reduced):
        pc = next((j for j, x in enumerate(reduced) if x % n), None)
        if pc is not None:
            inv = pow(reduced[pc], -1, n)
            pivots[pc] = [(x * inv) % n for x in reduced]
        return pc

    for v in im_vecs:
        record_pivot(reduce_vec(v))
    result_vecs = []
    for v in ker_vecs:
        if record_pivot(reduce_vec(v)) is not None:
            result_vecs.append(v)
    return result_vecs


def _lin_diff_mat_f2(domain, rng, ld_out):
    """F_2 linearized-differential matrix: domain → rng.

    ld_out maps each generator index to the set of generators in its support.
    """
    return [[1 if rg in ld_out.get(dg, frozenset()) else 0
             for dg in domain] for rg in rng]


def _letter_grading(letter, gr: List[int]) -> int:
    """Grading of one word letter: gr[g-1] for a chord g, 0 for any basepoint power
    (basepoint letters have degree 0 regardless of power)."""
    return gr[letter - 1] if isinstance(letter, int) else 0


def _eval_letter(letter, augm_dict: dict, p: int) -> int:
    """ε(letter) mod p: a chord generator evaluates via augm_dict; a basepoint
    power ('lambda', c, k) evaluates to ε(t_c)^k via augm_dict[('lambda', c)]."""
    if isinstance(letter, int):
        return augm_dict.get(letter, 0)
    _, c, k = letter
    return pow(augm_dict[('lambda', c)], k, p)


def _eval_letter_z(letter, augm_dict: dict) -> int:
    """ε(letter) over Z: a chord generator evaluates via augm_dict; a basepoint
    power ('lambda', c, k) evaluates to ε(t_c)**(k % 2) via augm_dict[('lambda', c)]
    -- exact for every integer k, since a Z-augmentation forces ε(t_c) in {1, -1}.

    Deliberately not _eval_letter(letter, augm_dict, None): pow(x, k, None) with
    negative k returns a Python float, which would silently corrupt the integer
    matrices this feeds into."""
    if isinstance(letter, int):
        return augm_dict.get(letter, 0)
    _, c, k = letter
    return augm_dict[('lambda', c)] ** (k % 2)


def _is_z_augmentation(dga: 'DGA', data: dict, grading_mod: int) -> Optional[Any]:
    """Check whether `data` is a genuine Z-valued augmentation of dga (which
    must be over Z[λ]): {gen: int} on grade-0 generators (for grading_mod),
    {('lambda', c): value} with value in {1, -1} per component, and ε∘∂ = 0
    over Z for every grade-1 generator (only grade-1 generators can have a
    nonzero equation, for grading reasons -- the same restriction
    DGA._augmentation_system's `conditions` already encodes, reused here via
    n=2 as an arbitrary placeholder modulus: conditions/grade0_gens/grade1_gens
    don't depend on n, only var_ranges/units do, which aren't used here).

    Returns None if valid; otherwise a key identifying the first failure, so
    the caller can build a precise error message without re-scanning:
      ('lambda', c)  -- data[('lambda', c)] is not in {1, -1} (or missing)
      g (int)        -- either a non-grade-0 generator with nonzero data, or
                        a grade-1 generator whose ε∘∂ = 0 equation fails
    """
    for c in range(dga.num_components):
        if data.get(('lambda', c)) not in (1, -1):
            return ('lambda', c)

    sysm = dga._augmentation_system(dga.differential, grading_mod, 2, None)
    grade0_set = set(sysm.grade0_gens)
    for g in range(1, len(dga.gradings) + 1):
        if g not in grade0_set and data.get(g, 0) != 0:
            return g

    for g1, cond in zip(sysm.grade1_gens, sysm.conditions):
        total = 0
        for word, coeff in cond:
            term = coeff
            for letter in word:
                term *= _eval_letter_z(letter, data)
            total += term
        if total != 0:
            return g1

    return None


def _bilin_diff_mat_zp(domain, rng, zn_d, aug0_dict, aug1_dict, p):
    """Z/p bilinearized-differential matrix: domain → rng, w.r.t. the ordered
    pair (aug0, aug1). For the distinguished chord at position pos in a word,
    aug0 evaluates every letter to its left and aug1 every letter to its
    right; aug0=aug1 recovers the single-augmentation linearized matrix."""
    rng_idx = {g: i for i, g in enumerate(rng)}
    mat = [[0] * len(domain) for _ in range(len(rng))]
    for col, gen_d in enumerate(domain):
        for word, coeff in zn_d[gen_d - 1].items():
            for pos, a in enumerate(word):
                if a in rng_idx:
                    prod = coeff % p
                    for li, letter in enumerate(word):
                        if li < pos:
                            prod = (prod * _eval_letter(letter, aug0_dict, p)) % p
                        elif li > pos:
                            prod = (prod * _eval_letter(letter, aug1_dict, p)) % p
                    mat[rng_idx[a]][col] = (mat[rng_idx[a]][col] + prod) % p
    return mat


def _bilin_diff_mat_z(domain, rng, z_d, aug0_dict, aug1_dict):
    """Z bilinearized-differential matrix: domain → rng, w.r.t. the ordered
    pair (aug0, aug1) -- the integer analogue of _bilin_diff_mat_zp (no
    modulus, and _eval_letter_z instead of _eval_letter -- see its docstring
    for why). z_d is the un-reduced dga('Zlambda').differential. Same
    distinguished-chord split (aug0 left / aug1 right) and order-sensitivity;
    aug0=aug1 recovers the single-augmentation linearized matrix over Z."""
    rng_idx = {g: i for i, g in enumerate(rng)}
    mat = [[0] * len(domain) for _ in range(len(rng))]
    for col, gen_d in enumerate(domain):
        for word, coeff in z_d[gen_d - 1].items():
            for pos, a in enumerate(word):
                if a in rng_idx:
                    prod = coeff
                    for li, letter in enumerate(word):
                        if li < pos:
                            prod *= _eval_letter_z(letter, aug0_dict)
                        elif li > pos:
                            prod *= _eval_letter_z(letter, aug1_dict)
                    mat[rng_idx[a]][col] += prod
    return mat


def _homotopy_mat_zp(domain, rng, zn_d, gr, aug0_dict, aug1_dict, p):
    """Z/p DGA-homotopy matrix: for the K-derivation linear system A·K = b,
    domain = G_0 (one column per equation a_j), rng = G_{-1} (one row per
    K-unknown c) -- so mat[c-index][j-index], the transpose of the usual
    "rows = equations" layout (the augmented system must append b as an
    extra row, not column, to match). Identical to
    _bilin_diff_mat_zp except for the extra (-1)^{prefix degree} derivation
    sign, via _letter_grading; basepoints contribute 0 to that sign regardless
    of power, same as in check_d_squared's Leibniz expansion."""
    rng_idx = {g: i for i, g in enumerate(rng)}
    mat = [[0] * len(domain) for _ in range(len(rng))]
    for col, gen_d in enumerate(domain):
        for word, coeff in zn_d[gen_d - 1].items():
            for pos, a in enumerate(word):
                if a in rng_idx:
                    sign = -1 if sum(_letter_grading(letter, gr) for letter in word[:pos]) % 2 else 1
                    prod = (coeff * sign) % p
                    for li, letter in enumerate(word):
                        if li < pos:
                            prod = (prod * _eval_letter(letter, aug0_dict, p)) % p
                        elif li > pos:
                            prod = (prod * _eval_letter(letter, aug1_dict, p)) % p
                    mat[rng_idx[a]][col] = (mat[rng_idx[a]][col] + prod) % p
    return mat


def _divisible(a: int, b: int) -> bool:
    """True iff a divides b. 0 divides only 0."""
    return b == 0 if a == 0 else b % a == 0


def _lch_divides(m: int, M: int) -> bool:
    """True iff an aug with maximal grading modulus M is m-graded.
    m=0 (Z-graded) only holds when M=0; otherwise M=0 (universally graded)
    or m | M."""
    if m == 0:
        return M == 0
    return M == 0 or M % m == 0


def _lch_coarsen(poly: Dict[int, int], m: int) -> Dict[int, int]:
    """Image of a Poincaré polynomial under the ring map Z[Z/M] -> Z[Z/m] (m | M).
    Exponents are reduced mod m; dimensions in the same target grade are summed.
    m=0 is the identity (source must already live in Z[Z])."""
    if m == 0:
        return dict(poly)
    out: Dict[int, int] = {}
    for e, dim in poly.items():
        out[e % m] = out.get(e % m, 0) + dim
    return out


def _format_poincare(poly: Dict[int, int]) -> str:
    """Format a Poincaré polynomial dict {degree: dim} as a string in t."""
    if not poly:
        return "0"
    terms = []
    for g in sorted(poly, reverse=True):
        d = poly[g]
        terms.append(f"t^{g}" if d == 1 else f"{d}*t^{g}")
    return " + ".join(terms)


def _format_z_group(free_rank: int, torsion: List[int]) -> str:
    """Format one grading's (free_rank, torsion_factors) -- as returned per
    grading by DGA.bilin_hom_z -- as e.g. "Z^2 + Z/3" ("Z" for free_rank=1,
    "0" for the trivial group)."""
    parts = []
    if free_rank == 1:
        parts.append("Z")
    elif free_rank > 1:
        parts.append(f"Z^{free_rank}")
    parts.extend(f"Z/{d}" for d in torsion)
    return " + ".join(parts) if parts else "0"


def _format_ruling(poly: Dict[int, int]) -> str:
    """Format a ruling polynomial dict {z-power: coeff} as a string in z."""
    if not poly:
        return "0"
    terms = []
    for power in sorted(poly, reverse=True):
        c = poly[power]
        terms.append(f"z^{power}" if c == 1 else f"{c}*z^{power}")
    return " + ".join(terms)


# --- Noncommutative word algebra and polynomial arithmetic on the word -> coeff
# format, used by DGA.simplify ---

def _normalize_word(word: tuple) -> tuple:
    """Enforce the only semi-free relations: merge adjacent same-component basepoint
    powers (t_c^a * t_c^b = t_c^{a+b}), dropping the letter if the merged power is 0.
    Chords and basepoints of different components never merge or reorder."""
    result: list = []
    for letter in word:
        if (result and isinstance(letter, tuple) and isinstance(result[-1], tuple)
                and letter[1] == result[-1][1]):
            c = letter[1]
            k = result[-1][2] + letter[2]
            result.pop()
            if k != 0:
                result.append(('lambda', c, k))
        else:
            result.append(letter)
    return tuple(result)


def _word_mul(w1: tuple, w2: tuple) -> tuple:
    """Concatenation product of two noncommutative words, then normalize."""
    return _normalize_word(w1 + w2)


def _invert_basepoint_word(word: tuple) -> tuple:
    """Inverse of a word consisting entirely of basepoint letters: reverse the
    letters and negate each power."""
    return tuple(('lambda', c, -k) for _, c, k in reversed(word))


def _poly_reduce(poly: Dict[tuple, int], ring: GroundRing) -> Dict[tuple, int]:
    """Drop zero coefficients; reduce mod ring.modulus for Z/n (no-op for Z[lambda])."""
    n = ring.modulus
    if n == 0:
        return {k: v for k, v in poly.items() if v != 0}
    return {k: v % n for k, v in poly.items() if v % n != 0}


def _poly_add(p1: Dict[tuple, int], p2: Dict[tuple, int], ring: GroundRing) -> Dict[tuple, int]:
    """p1 + p2, as polynomials in the word -> coeff format."""
    result = dict(p1)
    for k, v in p2.items():
        result[k] = result.get(k, 0) + v
    return _poly_reduce(result, ring)


def _poly_mul(p1: Dict[tuple, int], p2: Dict[tuple, int], ring: GroundRing) -> Dict[tuple, int]:
    """Non-commutative product p1 * p2 (word concatenation via _word_mul)."""
    result: Dict[tuple, int] = {}
    for w1, c1 in p1.items():
        for w2, c2 in p2.items():
            key = _word_mul(w1, w2)
            result[key] = result.get(key, 0) + c1 * c2
    return _poly_reduce(result, ring)


def _apply_phi(poly: Dict[tuple, int], x: int, y: int, Y: Dict[tuple, int], ring: GroundRing) -> Dict[tuple, int]:
    """Image of poly under the algebra map x -> 0, y -> Y, other generators fixed."""
    result: Dict[tuple, int] = {}
    for word, coeff in poly.items():
        if x in word:
            continue
        acc: Dict[tuple, int] = {(): coeff}
        for g in word:
            factor = Y if g == y else {(g,): 1}
            acc = _poly_mul(acc, factor, ring)
        result = _poly_add(result, acc, ring)
    return result


def _is_unit(coeff: int, ring: GroundRing) -> bool:
    """True iff coeff is a unit of ring (+-1 for Z[lambda]; coprime to n for Z/n)."""
    if ring == GroundRing.ZLAMBDA:
        return coeff in (1, -1)
    return gcd(coeff % ring.modulus, ring.modulus) == 1


def _inv_unit(coeff: int, ring: GroundRing) -> int:
    """Multiplicative inverse of a unit coeff of ring."""
    if ring == GroundRing.ZLAMBDA:
        return coeff  # +-1 is self-inverse
    return pow(coeff, -1, ring.modulus)


def _find_simplify_pivot(diff: Dict[int, Dict[tuple, int]], alive: set, ring: GroundRing):
    """First eligible (x, y) pivot for simplify()'s word -> coeff dict path, else None.

    x: a generator with no constant term in diff[x] (no term with empty chord-content,
       i.e. a term that is purely basepoint letters or literally empty).
    y: a generator whose chord-content occurs in diff[x] in exactly one monomial -- the
       "y not in u" termination guard -- that monomial's chord-content being exactly
       [y] (basepoint letters may sandwich y on either side) with a unit coefficient.
    Returns (x, y, lam_l, lam_r, coeff): lam_l/lam_r are the basepoint subwords found
    to the left/right of y in that monomial.
    """
    for x in sorted(alive):
        poly = diff[x]
        if any(not any(isinstance(g, int) for g in word) for word in poly):
            continue
        occurrences: Dict[int, list] = {}
        for word, coeff in poly.items():
            chords = {g for g in word if isinstance(g, int)}
            for g in chords:
                occurrences.setdefault(g, []).append((word, coeff))
        if x in occurrences:
            # x in u: Y would carry x, leaving a dangling reference to a
            # deleted generator (x not in u is automatic for geometric DGAs via
            # the action filtration, but guard it for abstract inputs).
            continue
        for y in sorted(occurrences):
            if y == x:
                continue
            monos = occurrences[y]
            if len(monos) != 1:
                continue
            word, coeff = monos[0]
            chord_positions = [i for i, g in enumerate(word) if isinstance(g, int)]
            if len(chord_positions) != 1 or not _is_unit(coeff, ring):
                continue
            i = chord_positions[0]
            return x, y, word[:i], word[i + 1:], coeff
    return None


def _simplify_dict_diff(diff_list: List[Dict], gradings: List[int], ring: GroundRing,
                         names: Optional[List[str]] = None, verbose: bool = False):
    """Greedy algebraic handle cancellation on the word -> coeff format.

    Returns (new_gradings, new_diff_list, new_names, remap, proj) for the
    surviving generators, renumbered 1..k in increasing order of original
    generator number.  A surviving generator keeps its original label in
    new_names (it is still "the same" generator, now with extra differential
    terms); new_names is None when names is None.

    remap maps each surviving original (1-indexed) generator to its new index.
    proj records the destabilization projection π on the cancelled generators:
    it maps each removed original generator to its image (a poly over the
    new-indexed survivors) under the algebra map x -> 0, y -> Y.  Together
    (remap, proj) determine π on every original generator, so an augmentation
    of the result can be pulled back to one of the input (see
    DGA.pullback_augmentation).
    """
    n = len(diff_list)
    alive = set(range(1, n + 1))
    diff = {g: dict(diff_list[g - 1]) for g in alive}
    proj: Dict[int, Dict[tuple, int]] = {}  # removed gen -> poly over live gens

    while True:
        pivot = _find_simplify_pivot(diff, alive, ring)
        if pivot is None:
            break
        x, y, lam_l, lam_r, coeff = pivot
        u = {k: v for k, v in diff[x].items() if k != lam_l + (y,) + lam_r}
        scale_coeff = -_inv_unit(coeff, ring)
        Y = _poly_mul(_poly_mul({_invert_basepoint_word(lam_l): scale_coeff}, u, ring),
                      {_invert_basepoint_word(lam_r): 1}, ring)
        del diff[x]
        del diff[y]
        alive.discard(x)
        alive.discard(y)
        for z in alive:
            gens_z = {g for word in diff[z] for g in word}
            if x in gens_z or y in gens_z:
                diff[z] = _apply_phi(diff[z], x, y, Y, ring)
        # Record this step of π (x -> 0, y -> Y) and push it through the images
        # already recorded, so every stored image stays expressed in live gens.
        for r in proj:
            proj[r] = _apply_phi(proj[r], x, y, Y, ring)
        proj[x] = {}
        proj[y] = Y
        if verbose:
            print(f'simplify: cancelled generators ({x}, {y})')

    survivors = sorted(alive)
    remap = {old: i + 1 for i, old in enumerate(survivors)}
    new_gradings = [gradings[old - 1] for old in survivors]
    new_names = [names[old - 1] for old in survivors] if names is not None else None

    def _remap_word(word):
        return tuple(remap[g] if isinstance(g, int) else g for g in word)

    new_diff = [
        {_remap_word(word): c for word, c in diff[old].items()}
        for old in survivors
    ]
    proj_remapped = {
        r: {_remap_word(word): c for word, c in poly.items()}
        for r, poly in proj.items()
    }
    return new_gradings, new_diff, new_names, remap, proj_remapped


# ============================================================
# Section 3: Leg
# ============================================================

class Leg:
    """
    A Legendrian knot or link in the front-projection plat form.

    Construction
    ------------
    Leg([2, 2, 2])      braid word — list of positive integers (plat closure)
    Leg('mK3_1')        atlas name — unique Legendrian representative
    Leg('mK5_2.0')      first of two reps of mirror of 5_2 (0-indexed)
    Leg([('<', 0), ('X', 0), ('>', 0)])
                        tangle decomposition — list of (op, height) tuples where
                        op is '<' (left cusp), '>' (right cusp), or 'X' (crossing);
                        heights are 0-indexed from the top at the current strand count.
                        Converted to plat form internally; stored as self.tangle.
    Leg((X_perm, O_perm))
                        grid diagram — a pair of permutations (as lists of ints).
                        X_perm[j] is the row of the X marker in column j,
                        O_perm[j] is the row of the O marker in column j,
                        with rows 0-indexed from the bottom and columns
                        0-indexed from the left.  Vertical strands go over
                        horizontal strands.  The Legendrian front is obtained
                        by rotating the grid 45° counter-clockwise; the result
                        is converted to a tangle and then to plat form.
                        Stored as self.grid; the intermediate tangle is stored
                        as self.tangle.

    Classical invariants  (computed once, cached as properties)
    -----------------------------------------------------------
    num_components     int
    strand_potentials  List[int]   Maslov potential, one value per braid strand
    grading            List[int]
    tb                 int   (Thurston-Bennequin number)
    rot                int for knots; Tuple[int,...] for links (one per component)
    ruling_invariant(grading_mod=0)  Dict[int, int]  (ruling polynomial in z;
                       works for links when maslov is specified)

    DGA and augmentations
    ---------------------
    dga(ring)           DGA over ring (default: DEFAULT_GROUND_RING = Z/2);
                        cached per ring
    augmentations(...)  shorthand for self.dga(Z/modulus).augmentations(...)
    all_lin_hom(...)    shorthand for self.dga(Z/modulus).all_lin_hom(...)
    rulings(grading_mod) cached per grading_mod

    Link support: differential works for links over Z/2 and Z[λ₁,…,λₗ] (one
    variable per component, basepoint at the last right cusp of each component).
    Augmentations and all_lin_hom work for links over Z/2 when maslov is set and
    grading_mod | 2*rot_c for every component. Z/n links are deferred.

    Visualization
    -------------
    draw(label_generators, method, color)  returns matplotlib Figure
    export_svg(filename)                   writes SVG, returns filename
    """

    def __init__(
        self,
        input: Union[List[int], List[tuple], str, tuple],
        name: Optional[str] = None,
        maslov: Optional[List[int]] = None,
    ) -> None:
        _is_grid = (
            isinstance(input, tuple) and len(input) == 2
            and isinstance(input[0], (list, tuple))
            and isinstance(input[1], (list, tuple))
        )
        _is_tangle = (
            not _is_grid
            and isinstance(input, list) and bool(input) and isinstance(input[0], tuple)
        )
        if _is_grid:
            X_perm = list(cast(Iterable[int], input[0]))
            O_perm = list(cast(Iterable[int], input[1]))
            Leg._validate_grid(X_perm, O_perm)
            _tangle = Leg._grid_to_tangle(X_perm, O_perm)
            Leg._validate_tangle(_tangle)
            _braid, _ncusps = Leg._tangle_to_braid(_tangle)
            self.grid: Tuple[List[int], List[int]] = (X_perm, O_perm)
            self.tangle: List[tuple] = _tangle
            self.braid: List[int] = _braid
            self.num_cusps: int = _ncusps
            self.name: str = name if name is not None else repr(input)
        elif _is_tangle:
            Leg._validate_tangle(input)
            _braid, _ncusps = Leg._tangle_to_braid(input)
            self.tangle = cast(List[tuple], list(input))
            self.braid = _braid
            self.num_cusps = _ncusps
            self.name = name if name is not None else repr(self.tangle)
        elif isinstance(input, list):
            self.braid = list(input)  # type: ignore[assignment]  # runtime-checked: braid word
            self.name = name if name is not None else repr(self.braid)
        elif isinstance(input, str):
            m = re.match(r'^(.+)\.(\d+)$', input)
            canon, idx = (m.group(1), int(m.group(2))) if m else (input, None)
            if canon not in ATLAS:
                raise ValueError(
                    f'Unknown knot name {canon!r}. '
                    'Call list(ATLAS) to see available names.'
                )
            entries = ATLAS[canon]
            if idx is None:
                if len(entries) == 1:
                    idx = 0
                else:
                    raise ValueError(
                        f'{canon!r} has {len(entries)} Legendrian representatives; '
                        f'specify an index 0..{len(entries) - 1}, '
                        f'e.g. "{canon}.0" or "{canon}.{len(entries) - 1}"'
                    )
            elif not (0 <= idx < len(entries)):
                raise IndexError(
                    f'Legendrian index {idx} out of range for {canon!r} '
                    f'({len(entries)} representative(s), indexed 0..{len(entries) - 1})'
                )
            self.braid = list(entries[idx])
            self.name = name if name is not None else input
        else:
            raise TypeError(
                f'Expected a braid word (list of int), tangle sequence (list of tuples), '
                f'atlas name (str), or grid diagram (tuple of two lists), '
                f'got {type(input).__name__!r}'
            )
        if not _is_tangle and not _is_grid:
            self.num_cusps = max(self.braid) // 2 + 1 if self.braid else 1
        assert self.num_cusps >= 1, f"num_cusps={self.num_cusps} is invalid"
        self._dga_cache: Dict[GroundRing, DGA] = {}
        self._rulings_cache: Dict[int, List[List[int]]] = {}
        self._ruling_summary_cache: Optional[Dict[int, Dict[int, int]]] = None
        self._maslov_seeds: Optional[List[int]] = maslov

    def __repr__(self) -> str:
        if hasattr(self, 'grid'):
            return f'Leg({self.grid!r})'
        if hasattr(self, 'tangle'):
            return f'Leg({self.tangle!r})'
        m = re.match(r'^(.+)\.\d+$', self.name)
        canon = m.group(1) if m else self.name
        if canon in ATLAS:
            return f'Leg({self.name!r})'
        return f'Leg({self.braid!r})'

    @staticmethod
    def _validate_grid(X_perm, O_perm) -> None:
        """Raise ValueError if the grid diagram is invalid."""
        n = len(X_perm)
        if len(O_perm) != n:
            raise ValueError('X and O permutations must have the same length')
        if n < 2:
            raise ValueError(f'Grid size must be at least 2, got {n}')
        if sorted(X_perm) != list(range(n)) or sorted(O_perm) != list(range(n)):
            raise ValueError('X and O must each be a permutation of {0, …, n-1}')
        if any(X_perm[j] == O_perm[j] for j in range(n)):
            raise ValueError('X and O markers cannot occupy the same cell')

    @staticmethod
    def _grid_to_tangle(X_perm, O_perm) -> List[tuple]:
        """
        Convert a grid diagram (two permutations, row 0 at bottom) to a tangle sequence.

        X_perm[j] = row of the X marker in column j.
        O_perm[j] = row of the O marker in column j.

        After a 45° CCW rotation, the diagram becomes a Legendrian front whose events
        are read left-to-right by new_x = col − row.  Horizontal grid segments become
        slope +1 strands; vertical segments become slope −1 strands.  Each marker is
        either a left cusp, a right cusp, or a kink (slope change with no new_x extremum).
        Each interior cell whose row lies strictly between the two markers in its column
        and whose column lies within its row's horizontal span is a crossing.
        """
        n = len(X_perm)

        # Inverse permutations: x_col[r] / o_col[r] = column of X/O in row r
        x_col = [0] * n
        o_col = [0] * n
        for j in range(n):
            x_col[X_perm[j]] = j
            o_col[O_perm[j]] = j

        # Collect all events as (new_x, new_z, type, col j, row r)
        # new_x = j - r, new_z = j + r
        events: List[tuple] = []

        for j in range(n):
            for r, is_x in [(X_perm[j], True), (O_perm[j], False)]:
                other_col = o_col[r] if is_x else x_col[r]
                other_row = O_perm[j] if is_x else X_perm[j]
                nx, nz = j - r, j + r

                if other_col > j and other_row < r:
                    events.append((nx, nz, 'LC', j, r))
                elif other_col < j and other_row > r:
                    events.append((nx, nz, 'RC', j, r))
                elif other_col > j:  # other_row > r: V_j → H_r (V ends, H starts)
                    events.append((nx, nz, 'KVH', j, r))
                else:               # other_col < j, other_row < r: H_r → V_j
                    events.append((nx, nz, 'KHV', j, r))

        # Crossings: cell (j, r) where vertical in col j spans row r strictly,
        # horizontal in row r spans col j, and (j, r) is not a marker.
        for j in range(n):
            lo, hi = min(X_perm[j], O_perm[j]), max(X_perm[j], O_perm[j])
            for r in range(lo + 1, hi):
                L_r = min(x_col[r], o_col[r])
                R_r = max(x_col[r], o_col[r])
                if L_r <= j <= R_r:
                    events.append((j - r, j + r, 'X', j, r))

        # Process top-to-bottom within each new_x value (descending new_z)
        events.sort(key=lambda e: (e[0], -e[1]))

        # Active strands: mutable [intercept, slope, label]
        # Horizontal in row r : slope=+1, intercept=2r  → new_z = new_x + 2r
        # Vertical   in col j : slope=−1, intercept=2j  → new_z = −new_x + 2j
        active: List[List] = []

        def nz_of(strand, nx):
            return strand[1] * nx + strand[0]

        def height_above(nx, nz_ref):
            return sum(1 for s in active if nz_of(s, nx) > nz_ref)

        def find(label):
            for s in active:
                if s[2] == label:
                    return s
            raise AssertionError(f'strand {label} missing from active set')

        tangle: List[tuple] = []

        for nx, nz, etype, j, r in events:
            if etype == 'LC':
                h = height_above(nx, nz)
                tangle.append(('<', h))
                # horizontal (above, slope+1) then vertical (below, slope−1)
                active.append([2 * r, +1, ('H', r)])
                active.append([2 * j, -1, ('V', j)])

            elif etype == 'RC':
                h = height_above(nx, nz)
                tangle.append(('>', h))
                active.remove(find(('H', r)))
                active.remove(find(('V', j)))

            elif etype == 'KVH':   # vertical in col j → horizontal in row r
                s = find(('V', j))
                s[0], s[1], s[2] = 2 * r, +1, ('H', r)

            elif etype == 'KHV':   # horizontal in row r → vertical in col j
                s = find(('H', r))
                s[0], s[1], s[2] = 2 * j, -1, ('V', j)

            else:   # crossing
                h = height_above(nx, nz)
                tangle.append(('X', h))

        return tangle

    @staticmethod
    def _validate_tangle(tangle) -> None:
        """Raise ValueError if tangle is not a valid closed Legendrian tangle sequence."""
        count = 0
        for idx, item in enumerate(tangle):
            if not (isinstance(item, tuple) and len(item) == 2):
                raise ValueError(
                    f'Tangle element {idx} must be a 2-tuple (op, h), got {item!r}'
                )
            op, h = item
            if op not in ('<', '>', 'X'):
                raise ValueError(
                    f"Tangle element {idx}: op must be '<', '>', or 'X', got {op!r}"
                )
            if not isinstance(h, int) or h < 0:
                raise ValueError(
                    f'Tangle element {idx}: height must be a non-negative int, got {h!r}'
                )
            if op == '<':
                if h > count:
                    raise ValueError(
                        f'Tangle element {idx}: LC height {h} out of range '
                        f'({count} strands present, valid 0..{count})'
                    )
                count += 2
            elif op == '>':
                if count < 2 or h + 1 >= count:
                    raise ValueError(
                        f'Tangle element {idx}: RC height {h} out of range '
                        f'({count} strands present, need at least {h + 2})'
                    )
                count -= 2
            else:  # 'X'
                if count < 2 or h + 1 >= count:
                    raise ValueError(
                        f'Tangle element {idx}: crossing height {h} out of range '
                        f'({count} strands present, need at least {h + 2})'
                    )
        if count != 0:
            raise ValueError(
                f'Tangle is not closed: {count} strand(s) remain at the end'
            )

    @staticmethod
    def _tangle_to_braid(tangle, debug_dir: Optional[str] = None) -> Tuple[List[int], int]:
        """
        Convert a validated tangle sequence to (braid_word_1indexed, num_cusps).
        Applies LR-II commutation rules until plat form, then extracts braid word.

        If debug_dir is a path, saves a tangle picture after each rule application.
        """
        import os
        seq = list(tangle)
        num_cusps = sum(1 for op, _ in seq if op == '<')
        max_iters = max(10000, len(seq) ** 2 * 50)
        step = 0

        def _save_debug(rule_name):
            nonlocal step
            assert debug_dir is not None
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            stub = object.__new__(Leg)
            stub.tangle = seq[:]
            fig = stub.draw(method='tangle', color=False)
            fig.axes[0].set_title(f'Step {step}: {rule_name}\n{seq}', fontsize=7)
            path = os.path.join(debug_dir, f'step_{step:04d}_{rule_name}.png')
            fig.savefig(path, dpi=80, bbox_inches='tight')
            plt.close(fig)
            step += 1

        if debug_dir:
            os.makedirs(debug_dir, exist_ok=True)
            _save_debug('initial')

        for _ in range(max_iters):
            for i in range(len(seq) - 1):
                op_a, h_a = seq[i]
                op_b, h_b = seq[i + 1]

                # Rule A: X(h) · LC(j) — move LC left past X
                if op_a == 'X' and op_b == '<':
                    h, j = h_a, h_b
                    if h <= j - 2:
                        seq[i], seq[i + 1] = ('<', j), ('X', h)
                        rule = 'A_commute'
                    elif h == j - 1:
                        # LR-II: cusp rises by 1, two extra crossings in post-LC config
                        seq[i:i + 2] = [('<', j - 1), ('X', j + 1), ('X', j), ('X', j - 1)]
                        rule = 'A_LR2'
                    else:  # h >= j
                        seq[i], seq[i + 1] = ('<', j), ('X', h + 2)
                        rule = 'A_commute'
                    if debug_dir: _save_debug(rule)
                    break

                # Rule B: RC(j) · X(h) — move RC right past X (h in post-RC config)
                elif op_a == '>' and op_b == 'X':
                    j, h = h_a, h_b
                    if h == j - 1:
                        # LR-II: h+1 == j is a removed position, so strands are
                        # non-adjacent in pre-RC config; RC falls by 1
                        seq[i:i + 2] = [('X', j + 1), ('X', j), ('X', j - 1), ('>', j + 1)]
                        rule = 'B_LR2'
                    elif h < j:
                        seq[i], seq[i + 1] = ('X', h), ('>', j)
                        rule = 'B_commute'
                    else:  # h >= j
                        seq[i], seq[i + 1] = ('X', h + 2), ('>', j)
                        rule = 'B_commute'
                    if debug_dir: _save_debug(rule)
                    break

                # Rule C: RC(k) · LC(j) — move LC left past RC
                elif op_a == '>' and op_b == '<':
                    k, j = h_a, h_b
                    # j < k means LC is above RC (j = k-1 is an edge case, treated as j < k)
                    if j < k:
                        seq[i], seq[i + 1] = ('<', j), ('>', k + 2)
                    else:
                        seq[i], seq[i + 1] = ('<', j + 2), ('>', k)
                    if debug_dir: _save_debug('C')
                    break

                # LC-LC far-commutation: LC(m)·LC(n) with n > m+1 → LC(n-2)·LC(m)
                elif op_a == '<' and op_b == '<' and h_b > h_a + 1:
                    seq[i], seq[i + 1] = ('<', h_b - 2), ('<', h_a)
                    if debug_dir: _save_debug('LC_LC_commute')
                    break

                # Rule D: LC(k) · LC(k+1) — fix nested left cusps (R2 move)
                elif op_a == '<' and op_b == '<' and h_b == h_a + 1:
                    k = h_a
                    seq[i:i + 2] = [('<', k), ('<', k + 2), ('X', k + 1), ('X', k)]
                    if debug_dir: _save_debug('D_R2')
                    break

                # RC-RC far-commutation: RC(n)·RC(m) with n > m+1 → RC(m)·RC(n-2)
                elif op_a == '>' and op_b == '>' and h_a > h_b + 1:
                    seq[i], seq[i + 1] = ('>', h_b), ('>', h_a - 2)
                    if debug_dir: _save_debug('RC_RC_commute')
                    break

                # Rule F: RC(k+1) · RC(k) — fix nested right cusps (R2 move)
                elif op_a == '>' and op_b == '>' and h_a == h_b + 1:
                    k = h_b
                    seq[i:i + 2] = [('X', k), ('X', k + 1), ('>', k), ('>', k)]
                    if debug_dir: _save_debug('F_R2')
                    break

            else:
                break  # no violation found: sequence is in plat form
        else:
            raise RuntimeError(
                f'Tangle-to-braid conversion did not terminate after {max_iters} '
                'iterations — the tangle may be very complex or there is a bug.'
            )

        # Verify the result is valid plat form
        seen_x = False
        seen_rc = False
        for op, h in seq:
            if op == '<':
                if seen_x or seen_rc:
                    raise AssertionError(f'LC after X or RC in plat-form output: {seq}')
                if h % 2 != 0:
                    raise AssertionError(f'LC at odd height {h} in plat-form output: {seq}')
            elif op == 'X':
                if seen_rc:
                    raise AssertionError(f'X after RC in plat-form output: {seq}')
                seen_x = True
            elif op == '>':
                if h % 2 != 0:
                    raise AssertionError(f'RC at odd height {h} in plat-form output: {seq}')
                seen_rc = True

        braid = [h + 1 for op, h in seq if op == 'X']
        return braid, num_cusps

    # --- Classical invariants ---

    @cached_property
    def num_components(self) -> int:
        return len(set(self._comp_and_perm[0]))

    @cached_property
    def _comp_and_perm(self) -> Tuple[List[int], List[int]]:
        """
        Returns (comp_of, final_perm) where:
          comp_of[s]    = component index of 0-indexed strand s (ordered by first
                          appearance scanning strands 0 … 2p-1)
          final_perm[i] = strand at 0-indexed braid position i after the full braid
        """
        p = self.num_cusps
        n = 2 * p

        final_perm = list(range(n))
        for gen in self.braid:
            final_perm[gen - 1], final_perm[gen] = final_perm[gen], final_perm[gen - 1]

        parent = list(range(n))

        def _find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def _union(x: int, y: int) -> None:
            px, py = _find(x), _find(y)
            if px != py:
                parent[px] = py

        for j in range(p):
            _union(2 * j, 2 * j + 1)
        for j in range(p):
            _union(final_perm[2 * j], final_perm[2 * j + 1])

        root_to_comp: Dict[int, int] = {}
        comp_of = [0] * n
        for s in range(n):
            r = _find(s)
            if r not in root_to_comp:
                root_to_comp[r] = len(root_to_comp)
            comp_of[s] = root_to_comp[r]

        return comp_of, final_perm

    @cached_property
    def strand_potentials(self) -> List[int]:
        """
        Maslov potential on braid strands (0-indexed, length 2*num_cusps).

        strand_potentials[s] is the Maslov potential of strand s.  Strands are
        numbered 0 … 2p-1.  Left cusp j (j=0…p-1) connects upper strand 2j and
        lower strand 2j+1; right cusp j connects final_perm[2j] (upper) and
        final_perm[2j+1] (lower).  At every cusp: μ[upper] = μ[lower] + 1.

        Seeds (one integer per component, ordered by first appearance from the
        top of the diagram) are taken from the maslov constructor argument; if
        omitted, all seeds default to 0.  The seed for component i is the
        Maslov potential of the lower strand of the topmost left cusp in that
        component.
        """
        p = self.num_cusps
        n = 2 * p
        seeds = self._maslov_seeds if self._maslov_seeds is not None else [0] * self.num_components
        if len(seeds) != self.num_components:
            raise ValueError(
                f'maslov must have length num_components={self.num_components}, '
                f'got {len(seeds)}'
            )

        comp_of, final_perm = self._comp_and_perm

        # Seed each component from the topmost left cusp in that component.
        mu: List[Optional[int]] = [None] * n
        seeded: set = set()
        for j in range(p):
            c = comp_of[2 * j]
            if c not in seeded:
                mu[2 * j + 1] = seeds[c]        # lower strand = seed
                mu[2 * j] = seeds[c] + 1        # upper strand = seed + 1
                seeded.add(c)

        # BFS: propagate through cusp constraints until all strands are assigned.
        changed = True
        while changed:
            changed = False
            for j in range(p):
                # Left cusp j: upper = 2j, lower = 2j+1
                up, lo = 2 * j, 2 * j + 1
                if mu[up] is None and mu[lo] is not None:
                    mu[up] = cast(int, mu[lo]) + 1
                    changed = True
                elif mu[lo] is None and mu[up] is not None:
                    mu[lo] = cast(int, mu[up]) - 1
                    changed = True
                # Right cusp j: upper = final_perm[2j], lower = final_perm[2j+1]
                up, lo = final_perm[2 * j], final_perm[2 * j + 1]
                if mu[up] is None and mu[lo] is not None:
                    mu[up] = cast(int, mu[lo]) + 1
                    changed = True
                elif mu[lo] is None and mu[up] is not None:
                    mu[lo] = cast(int, mu[up]) - 1
                    changed = True

        return mu  # type: ignore[return-value]  # all entries are filled

    @staticmethod
    def _trugrad(b: List[int], i: int) -> int:
        """Maslov grading of crossing i (1-indexed) in braid b."""
        def grading_height(lst, height):
            for index in lst:
                if height == index or height == index + 1:
                    height += 1 if (height + index) % 2 == 0 else -1
            return height

        def cusp(t):
            return [t[0] - 1, 1] if t[0] % 2 == 0 else [t[0] + 1, -1]

        beginlist = list(reversed(b[:i]))
        endlist = b[i:]
        startheight = beginlist[0]
        result = 0
        temp = [startheight, 0]
        while True:
            temp[0] = grading_height(endlist, temp[0])
            temp = cusp(temp)
            result += temp[1]
            temp[0] = grading_height(list(reversed(endlist)), temp[0])
            if temp[0] in (startheight, startheight + 1):
                break
            temp[0] = grading_height(beginlist, temp[0])
            temp = cusp(temp)
            result += temp[1]
            temp[0] = grading_height(list(reversed(beginlist)), temp[0])
            if temp[0] == startheight + 1:
                break
        return result

    @cached_property
    def grading(self) -> List[int]:
        mu = self.strand_potentials
        perm = list(range(2 * self.num_cusps))
        gr = []
        for gen in self.braid:
            s_upper = perm[gen - 1]
            s_lower = perm[gen]
            gr.append(mu[s_upper] - mu[s_lower])
            perm[gen - 1], perm[gen] = perm[gen], perm[gen - 1]
        gr.extend([1] * self.num_cusps)
        return gr

    @cached_property
    def tb(self) -> int:
        return sum(1 if x % 2 == 0 else -1 for x in self.grading)

    @cached_property
    def rot(self) -> Union[int, Tuple[int, ...]]:
        """
        Rotation number.

        For a knot (num_components == 1): returns an int.
        For a link: returns a tuple of ints, one per component, in the same
        order as the maslov seeds (components ordered by first appearance from
        the top of the front diagram).

        Each value is non-negative (the sign depends on an orientation choice
        that is not fixed by the plat-form data).
        """
        if self.num_components == 1:
            b = self.braid
            if not b:
                return 0
            m = max(b)
            h = m + 2 if m % 2 == 0 else m + 1
            backend = list(reversed([h - x for x in b]))
            return abs((self._trugrad(b, 1) + self._trugrad(backend, len(b))) // 2)

        # Each component is a single cycle of strands joined by cusp edges (every
        # strand meets exactly one left cusp and one right cusp).  At every cusp the
        # expected potential difference is +1 (μ[upper] = μ[lower] + 1).
        # strand_potentials seeds one strand per component and propagates this
        # constraint around the cycle, so all edges except the one that closes the
        # cycle are consistent; the entire rotation defect lands on that closing edge,
        # which may be a left OR a right cusp depending on propagation order.  Summing
        # the defect over all cusps (left and right) therefore captures it in every
        # case; the component's rotation number is half the total defect.
        mu = self.strand_potentials
        comp_of, final_perm = self._comp_and_perm
        totals = [0] * self.num_components
        for j in range(self.num_cusps):
            # Left cusp j: upper = 2j, lower = 2j+1.
            up, lo = 2 * j, 2 * j + 1
            totals[comp_of[up]] += mu[up] - mu[lo] - 1
            # Right cusp j: upper = final_perm[2j], lower = final_perm[2j+1].
            up, lo = final_perm[2 * j], final_perm[2 * j + 1]
            totals[comp_of[up]] += mu[up] - mu[lo] - 1
        return tuple(abs(t // 2) for t in totals)

    def ruling_invariant(self, grading_mod: int = 0) -> Dict[int, int]:
        """Ruling polynomial as a dict mapping z-power to coefficient. See [CP05], [Fu03].
        If ruling_summary() has been computed, derives the answer from it (a
        divisibility filter on N(r)); otherwise enumerates rulings directly.
        Both paths raise ValueError for out-of-domain grading_mod."""
        if self._ruling_summary_cache is not None:
            rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
            if not all(_divisible(grading_mod, 2 * r) for r in rots):
                raise ValueError(
                    f"grading_mod={grading_mod} is out of domain for this diagram; "
                    f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
                )
            total: Counter = Counter()
            for N, poly in self._ruling_summary_cache.items():
                keep = (N == 0) if grading_mod == 0 else (N % grading_mod == 0)
                if keep:
                    total.update(poly)
            return dict(total)
        c = self.num_cusps
        return dict(Counter(len(r) - c + 1 for r in self.rulings(grading_mod=grading_mod)))

    def ruling_summary(self, format: bool = False):
        """
        Compact summary of all graded ruling polynomials at once.

        Enumerates every normal ruling once (rulings(grading_mod=1)) and groups
        them by N(r) = gcd of the Maslov degrees of the switched crossings (gcd
        of the empty set := 0). A ruling r is Z/n-graded iff n | N(r); since only
        a few distinct N(r) occur, this is a compact form from which every graded
        ruling polynomial is recovered (see ruling_invariant).

        Returns a dict mapping each distinct N to a ruling polynomial
        (z-power -> coefficient) counting just the rulings r with N(r) == N,
        or to that polynomial's string form in z if format=True. The key
        N == 0 collects rulings graded for every grading.

        Bucket keys N are canonical only for rot = 0; for rot != 0 the derived
        invariants are still correct on the valid grading domain (n | 2*rot_c).
        """
        if self._ruling_summary_cache is None:
            gr = self.grading
            c = self.num_cusps
            buckets: Dict[int, Counter] = {}
            for r in self.rulings(grading_mod=1):
                N = reduce(gcd, (abs(gr[i - 1]) for i in r), 0)
                buckets.setdefault(N, Counter())[len(r) - c + 1] += 1
            self._ruling_summary_cache = {N: dict(cnt) for N, cnt in buckets.items()}
        if format:
            return {N: _format_ruling(poly) for N, poly in self._ruling_summary_cache.items()}
        return self._ruling_summary_cache

    # --- DGA access ---

    def dga(
        self,
        ground_ring: Union[GroundRing, str, None] = None,
    ) -> 'DGA':
        """
        Return the DGA of this Leg over ground_ring.
        Defaults to DEFAULT_GROUND_RING (currently Z/2) when ground_ring is None.
        Results are cached: repeated calls with the same ring return the same object.
        ground_ring may be a GroundRing instance or a string ('Z2', 'Zlambda', 'Z3').
        """
        if ground_ring is None:
            ground_ring = DEFAULT_GROUND_RING
        if isinstance(ground_ring, str):
            ground_ring = GroundRing.from_str(ground_ring)
        if ground_ring not in self._dga_cache:
            self._dga_cache[ground_ring] = DGA(self, ground_ring)
        return self._dga_cache[ground_ring]

    # --- Convenience delegators ---

    def augmentations(
        self,
        grading_mod: int = 0,
        modulus: int = 2,
        max_search: Optional[int] = _USE_DEFAULT_AUG_LIMIT,
    ) -> List['Augmentation']:
        """
        All augmentations over Z/modulus.
        Delegates to self.dga(Z/modulus).augmentations(grading_mod).
        grading_mod: 0 = Z-graded, 1 = ungraded, n >= 2 = Z/n-graded.
        max_search: forwarded to DGA.augmentations (see its docstring).
        """
        ring = GroundRing.Z2 if modulus == 2 else GroundRing.Zn(modulus)
        return self.dga(ring).augmentations(grading_mod=grading_mod, max_search=max_search)

    def one_aug(
        self,
        grading_mod: int = 0,
        modulus: int = 2,
        simplify: bool = True,
        max_nodes: Optional[int] = _USE_DEFAULT_AUG_LIMIT,
    ) -> Optional['Augmentation']:
        """
        A single augmentation over Z/modulus, or None if there are none.
        Delegates to self.dga(Z/modulus).one_aug(...); see that method for the
        backtracking search, the simplify option, and max_nodes.
        """
        ring = GroundRing.Z2 if modulus == 2 else GroundRing.Zn(modulus)
        return self.dga(ring).one_aug(grading_mod=grading_mod, simplify=simplify,
                                      max_nodes=max_nodes)

    @staticmethod
    def _propagate_rulings(crossings_with_indices, sw: set, p: int,
                           verbose: bool = False, label: str = '') -> List:
        """Propagate partial rulings forward through a sequence of crossings."""
        def valid_ruling_q(r, xing, switch):
            if not switch:
                return all(pair[0] < pair[1] for pair in r)
            t = next((pair for pair in r if xing in pair), None)
            bp = next((pair for pair in r if xing + 1 in pair), None)
            if t is None or bp is None:
                return False
            if not all(pair[0] < pair[1] for pair in r):
                return False
            t = sorted(t); bp = sorted(bp)
            t0, t1, b0, b1 = t[0], t[1], bp[0], bp[1]
            return (t0 < t1 < b0 < b1) or (t0 < b0 < b1 < t1) or (b0 < t0 < t1 < b1)

        def update_ruling(ar, xing, switch, i):
            switches, r = ar[0], ar[1]
            if not switch:
                new_r = [[xing + 1 if x == xing else (xing if x == xing + 1 else x)
                          for x in pair] for pair in r]
                newr = [switches, new_r]
            else:
                newr = [switches + [i], r]
            return newr if valid_ruling_q(newr[1], xing, switch) else None

        initial_r = [[2*i+1, 2*i+2] for i in range(p)]
        current = [[[], initial_r]]
        prefix = f"  [{label}] " if label else "  "
        for global_i, xing in crossings_with_indices:
            if global_i in sw:
                candidates = []
                for ar in current:
                    for sw_bool in (False, True):
                        upd = update_ruling(ar, xing, sw_bool, global_i)
                        if upd is not None:
                            candidates.append(upd)
            else:
                candidates = [upd for ar in current
                              for upd in [update_ruling(ar, xing, False, global_i)]
                              if upd is not None]
            seen, deduped = set(), []
            for ar in candidates:
                key = (tuple(ar[0]), tuple(tuple(pair) for pair in ar[1]))
                if key not in seen:
                    seen.add(key)
                    deduped.append(ar)
            current = deduped
            if verbose:
                sw_marker = " [switchable]" if global_i in sw else ""
                print(f"{prefix}crossing {global_i} (σ_{xing}){sw_marker}: "
                      f"{len(current)} candidate(s)")
        return current

    def rulings(
        self,
        grading_mod: int = 0,
        verbose: bool = False,
    ) -> List[List[int]]:
        """
        All graded rulings, computed with meet-in-the-middle. See [CP05], [Fu03].
        Cached per grading_mod (verbose output is not cached).
        grading_mod: 0 = Z-graded, 1 = ungraded, n >= 2 = Z/n-graded.
        Requires grading_mod | 2*rot_c for every component c (grading_mod=0
        requires rot_c = 0); raises ValueError otherwise.
        """
        rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
        if not all(_divisible(grading_mod, 2 * r) for r in rots):
            raise ValueError(
                f"grading_mod={grading_mod} is out of domain for this diagram; "
                f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
            )
        if grading_mod not in self._rulings_cache:
            b = self.braid
            n = len(b)
            cut = n // 2
            gr = self.grading
            if grading_mod == 0:
                sw = set(i + 1 for i, x in enumerate(gr) if x == 0)
            else:
                sw = set(i + 1 for i, x in enumerate(gr) if x % grading_mod == 0)
            p = self.num_cusps

            if verbose:
                print(f"rulings: braid length {n}, cut at {cut} "
                      f"({cut} left / {n - cut} right), "
                      f"{len(sw)} switchable crossing(s)")

            left = self._propagate_rulings(
                [(i + 1, b[i]) for i in range(cut)], sw, p,
                verbose=verbose, label='left')
            right = self._propagate_rulings(
                [(n - i, b[n - 1 - i]) for i in range(n - cut)], sw, p,
                verbose=verbose, label='right')

            def _config_key(r):
                return tuple(tuple(sorted(pair)) for pair in sorted(r))

            left_by_config: Dict = {}
            for switches, r in left:
                left_by_config.setdefault(_config_key(r), []).append(switches)

            right_by_config: Dict = {}
            for switches, r in right:
                right_by_config.setdefault(_config_key(r), []).append(switches)

            if verbose:
                n_matched = sum(1 for k in left_by_config if k in right_by_config)
                print(f"  left:  {len(left)} candidate(s), "
                      f"{len(left_by_config)} distinct config(s)")
                print(f"  right: {len(right)} candidate(s), "
                      f"{len(right_by_config)} distinct config(s)")
                print(f"  matching configs: {n_matched}")

            result = []
            for config, left_sw_lists in left_by_config.items():
                if config in right_by_config:
                    for l_sw in left_sw_lists:
                        for r_sw in right_by_config[config]:
                            result.append(sorted(l_sw + r_sw))

            if verbose:
                print(f"  => {len(result)} ruling(s) total")

            self._rulings_cache[grading_mod] = result
        return self._rulings_cache[grading_mod]

    def format_ruling_invariant(self, grading_mod: int = 0) -> str:
        """Format self.ruling_invariant as a polynomial string in z."""
        return _format_ruling(self.ruling_invariant(grading_mod))

    def all_lin_hom(
        self,
        grading_mod: int = 0,
        modulus: int = 2,
        as_str: bool = False,
        max_search: Optional[int] = _USE_DEFAULT_AUG_LIMIT,
    ):
        """
        Set of distinct Poincaré-Chekanov polynomials over all augmentations.
        Delegates to self.dga(Z/modulus).all_lin_hom(grading_mod).
        Returns List[Dict[int,int]], or List[str] if as_str=True.
        max_search: forwarded to DGA.all_lin_hom / augmentations (see their docstrings).
        """
        ring = GroundRing.Z2 if modulus == 2 else GroundRing.Zn(modulus)
        return self.dga(ring).all_lin_hom(grading_mod=grading_mod, as_str=as_str,
                                          max_search=max_search)

    # --- Visualization ---

    def _trace_braid(self) -> List[List[float]]:
        """Strand paths for plotting: each strand is a list of y-values."""
        def next_level(i, bi):
            if i == bi:
                return i + 1
            elif i == bi + 1:
                return i - 1
            return i

        b = self.braid
        strand_num = 2 * self.num_cusps
        strands = []
        for i in range(1, strand_num + 1):
            start = -i - 0.5 if i % 2 == 1 else -i + 0.5
            strands.append([start, -i])
        for bi in b:
            strands = [s + [-next_level(-int(s[-1]), bi)] for s in strands]
        result = []
        for s in strands:
            last = int(s[-1])
            result.append(s + [last - 0.5 if abs(last) % 2 == 1 else last + 0.5])
        return result

    def _trace_tangle(self) -> List[List[Tuple[float, float, bool]]]:
        """
        (x, y, cusp_tip) waypoints for each strand arc.
        cusp_tip=True marks a left/right cusp extremum, where the tangent is
        vertical; cusp_tip=False marks a regular waypoint with a horizontal tangent.
        """
        segments: List[List[Tuple[float, float, bool]]] = []
        active: List[int] = []   # active[height] = segment index
        x = 0.0
        W = 2.0

        for op, h in self.tangle:
            x_L, x_R = x, x + W

            if op == '<':
                for i, seg_idx in enumerate(active):
                    if segments[seg_idx][-1][0] < x_L:
                        segments[seg_idx].append((x_L, -float(i), False))
                    y_new = float(i + 2) if i >= h else float(i)
                    segments[seg_idx].append((x_R, -y_new, False))
                cusp_x = x_L + W * 0.5
                seg_top = len(segments)
                segments.append([(cusp_x, -(h + 0.5), True), (x_R, -float(h), False)])
                seg_bot = len(segments)
                segments.append([(cusp_x, -(h + 0.5), True), (x_R, -float(h + 1), False)])
                active = active[:h] + [seg_top, seg_bot] + active[h:]

            elif op == '>':
                cusp_x = x_R - W * 0.5
                for i, seg_idx in enumerate(active):
                    if segments[seg_idx][-1][0] < x_L:
                        segments[seg_idx].append((x_L, -float(i), False))
                    if i in (h, h + 1):
                        segments[seg_idx].append((cusp_x, -(h + 0.5), True))
                    else:
                        y_new = float(i - 2) if i > h + 1 else float(i)
                        segments[seg_idx].append((x_R, -y_new, False))
                active = active[:h] + active[h + 2:]

            elif op == 'X':
                for i, seg_idx in enumerate(active):
                    if segments[seg_idx][-1][0] < x_L:
                        segments[seg_idx].append((x_L, -float(i), False))
                active[h], active[h + 1] = active[h + 1], active[h]
                for i, seg_idx in enumerate(active):
                    segments[seg_idx].append((x_R, -float(i), False))

            x = x_R

        return segments

    def debug_tangle_to_braid(self, debug_dir: str) -> None:
        """Save a picture after each step of the tangle→plat conversion to debug_dir."""
        if not hasattr(self, 'tangle'):
            raise AttributeError('No tangle stored on this Leg.')
        Leg._tangle_to_braid(self.tangle, debug_dir=debug_dir)

    @staticmethod
    def _trace_grid_components(X_perm, O_perm):
        """Return list of (segs_h, segs_v) per link component for a grid diagram."""
        n = len(X_perm)
        x_row_to_col: List[Optional[int]] = cast(List[Optional[int]], [None] * n)
        for j in range(n):
            x_row_to_col[X_perm[j]] = j
        visited = [False] * n
        components = []
        for start in range(n):
            if visited[start]:
                continue
            segs_h, segs_v = [], []
            col = start
            while not visited[col]:
                visited[col] = True
                xr, or_ = X_perm[col], O_perm[col]
                segs_v.append((col, min(xr, or_), max(xr, or_)))
                next_col = x_row_to_col[or_]
                segs_h.append((or_, min(col, next_col), max(col, next_col)))
                col = next_col
            components.append((segs_h, segs_v))
        return components

    def draw(self, label_generators: bool = False,
             method: str = 'plat', color: bool = False,
             use_tangle: bool = False):
        """
        Plot the front projection of this Leg. Returns a matplotlib Figure.

        Parameters
        ----------
        label_generators : bool
            Label DGA generators (plat method only).
        method : {'plat', 'tangle', 'grid'}
            'plat'   — braid-plat diagram (default). Always available.
            'tangle' — tangle-sequence diagram. Requires self.tangle
                       (initialize from a tangle sequence or grid).
            'grid'   — XO grid diagram. Requires self.grid
                       (initialize from a grid diagram).
        color : bool
            If True, each strand/component is drawn in a distinct color.
            If False (default), everything is drawn in black.
        use_tangle : bool
            Deprecated. Use method='tangle' instead.
        """
        import matplotlib.pyplot as plt
        import numpy as np

        # Backwards-compatibility shim
        if use_tangle:
            method = 'tangle'

        _cmap = plt.get_cmap('tab10')
        _tab_colors = [_cmap(i) for i in range(10)]

        def _strand_color(k):
            return _tab_colors[k % 10] if color else 'black'

        # ── Grid diagram ──────────────────────────────────────────────────────
        if method == 'grid':
            if not hasattr(self, 'grid'):
                raise AttributeError(
                    'This Leg has no stored grid diagram; '
                    "initialize from a grid diagram to use method='grid'"
                )
            X_perm, O_perm = self.grid
            n = len(X_perm)
            fig, ax = plt.subplots(figsize=(max(3, n * 0.55), max(3, n * 0.55)))
            for i in range(n + 1):
                ax.axhline(i, color='lightgray', lw=0.4, zorder=0)
                ax.axvline(i, color='lightgray', lw=0.4, zorder=0)
            for ci, (segs_h, segs_v) in enumerate(
                    Leg._trace_grid_components(X_perm, O_perm)):
                c = _strand_color(ci)
                for col, r0, r1 in segs_v:
                    ax.plot([col + .5] * 2, [r0 + .5, r1 + .5],
                            color=c, lw=2, zorder=1)
                for row, c0, c1 in segs_h:
                    ax.plot([c0 + .5, c1 + .5], [row + .5] * 2,
                            color=c, lw=2, zorder=2)
            mk = 'black'
            for j in range(n):
                ax.plot(j + .5, X_perm[j] + .5, 'x',
                        color=mk, ms=5, mew=1.5, zorder=3)
                ax.plot(j + .5, O_perm[j] + .5, 'o',
                        color=mk, ms=4, mew=1.2, fillstyle='none', zorder=3)
            ax.set_xlim(0, n)
            ax.set_ylim(0, n)
            ax.set_aspect('equal')
            name_str = getattr(self, 'name', '') or ''
            ax.set_title(f'Grid diagram  {name_str}'.strip(), fontsize=9)
            for s in ax.spines.values():
                s.set_visible(False)
            ax.tick_params(left=False, bottom=False,
                           labelleft=False, labelbottom=False)
            plt.tight_layout()
            return fig

        # ── Tangle diagram ────────────────────────────────────────────────────
        if method == 'tangle':
            if not hasattr(self, 'tangle'):
                raise AttributeError(
                    'This Leg has no stored tangle; '
                    "initialize from a tangle sequence or grid to use method='tangle'"
                )
            segments = self._trace_tangle()
            all_x = [pt[0] for seg in segments for pt in seg]
            fig, ax = plt.subplots(figsize=(max(4, max(all_x) * 0.5), 3))
            t = np.linspace(0, 1, 50)
            for k, seg in enumerate(segments):
                px, py = [], []
                for j in range(len(seg) - 1):
                    x0, y0, tip0 = seg[j]
                    x3, y3, tip3 = seg[j + 1]
                    dx = x3 - x0
                    # horizontal tangent at regular waypoints; zero velocity at cusp tips
                    c1 = (x0, y0) if tip0 else (x0 + dx / 3, y0)
                    c2 = (x3, y3) if tip3 else (x3 - dx / 3, y3)
                    bx = ((1-t)**3 * x0 + 3*(1-t)**2*t * c1[0]
                          + 3*(1-t)*t**2 * c2[0] + t**3 * x3)
                    by = ((1-t)**3 * y0 + 3*(1-t)**2*t * c1[1]
                          + 3*(1-t)*t**2 * c2[1] + t**3 * y3)
                    if px:
                        px.extend(bx[1:].tolist())
                        py.extend(by[1:].tolist())
                    else:
                        px.extend(bx.tolist())
                        py.extend(by.tolist())
                ax.plot(px, py, color=_strand_color(k), linewidth=2,
                        solid_capstyle='round', solid_joinstyle='round')
            ax.yaxis.set_visible(False)
            ax.xaxis.set_visible(False)
            ax.set_title(f'Legendrian Knot  {self.name}')
            plt.tight_layout()
            return fig

        # ── Plat diagram (default) ────────────────────────────────────────────
        b = self.braid
        strands = self._trace_braid()
        extra_w = 0.8 if label_generators else 0.0
        fig, ax = plt.subplots(figsize=(max(4, len(b) * 0.8) + extra_w, 3))
        for k, strand in enumerate(strands):
            xs = np.array(range(1, len(strand) + 1), dtype=float)
            ys = np.array(strand, dtype=float)
            t_fine = np.linspace(xs[0], xs[-1], 300)
            try:
                from scipy.interpolate import make_interp_spline  # type: ignore[import-untyped]
                spl = make_interp_spline(xs, ys, k=min(2, len(xs) - 1))
                ax.plot(t_fine, spl(t_fine), color=_strand_color(k), linewidth=2)
            except Exception:
                ax.plot(xs, ys, color=_strand_color(k), linewidth=2)
        if label_generators:
            _bbox = dict(boxstyle='round,pad=0.15', facecolor='white',
                         edgecolor='gray', alpha=0.85)
            for i in range(1, len(b) + 1):
                ax.text(i + 1.5, -(b[i - 1] + 0.5), str(i),
                        ha='center', va='center', fontsize=7, zorder=5, bbox=_bbox)
            for k in range(1, self.num_cusps + 1):
                ax.text(len(b) + 2.8, -(2 * k - 0.5), str(len(b) + k),
                        ha='left', va='center', fontsize=7, zorder=5, bbox=_bbox)
        ax.set_xticks(range(1, len(b) + 3))
        ax.set_xticklabels([str(i) for i in range(len(b) + 2)])
        ax.yaxis.set_visible(False)
        ax.set_title(f"Legendrian Knot  braid = {b}")
        ax.grid(axis='x', linestyle='--', alpha=0.4)
        plt.tight_layout()
        return fig

    def export_svg(
        self,
        filename: str,
        xstep: float = 80.0,
        ystep: float = 40.0,
        margin: float = 40.0,
        stroke_width: float = 2.0,
    ) -> str:
        """
        Export the front projection as an SVG file. Returns the filename written.

        Each strand becomes a cubic Bezier spline with Catmull-Rom tangents for
        interior segments and a strictly horizontal tangent at each cusp tip,
        producing the classic C-shaped cusp geometry.
        """
        strands = self._trace_braid()
        all_y = [y for s in strands for y in s]
        y_top = max(all_y)
        y_bot = min(all_y)

        def px(x_idx: float) -> float:
            return margin + (x_idx - 1) * xstep

        def py(y_val: float) -> float:
            return margin + (y_top - y_val) * ystep

        n_pts = len(strands[0])
        svg_w = 2 * margin + (n_pts - 1) * xstep
        svg_h = 2 * margin + (y_top - y_bot) * ystep

        palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                   '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

        def _path(pts: List[Tuple[float, float]]) -> str:
            N = len(pts)
            g0 = (pts[0][0] - xstep, pts[0][1])
            gn = (pts[-1][0] + xstep, pts[-1][1])
            apts = [g0] + pts + [gn]
            d = f'M {pts[0][0]:.2f},{pts[0][1]:.2f}'
            for j in range(N - 1):
                p0, p1, p2, p3 = apts[j], apts[j+1], apts[j+2], apts[j+3]
                cp1 = (p1[0] + (p2[0]-p0[0])/6, p1[1] + (p2[1]-p0[1])/6)
                cp2 = (p2[0] - (p3[0]-p1[0])/6, p2[1] - (p3[1]-p1[1])/6)
                if j == 0:
                    cp1 = pts[0]
                    cp2 = (cp2[0], pts[0][1])
                elif j == N - 2:
                    cp2 = pts[-1]
                    cp1 = (cp1[0], pts[-1][1])
                if j == 1 and N > 3:
                    cp1 = (cp1[0], 2*pts[1][1] - pts[0][1])
                if j == N - 3 and N > 3:
                    cp2 = (cp2[0], 2*pts[-2][1] - pts[-1][1])
                d += (f' C {cp1[0]:.2f},{cp1[1]:.2f}'
                      f' {cp2[0]:.2f},{cp2[1]:.2f}'
                      f' {p2[0]:.2f},{p2[1]:.2f}')
            return d

        lines = [
            f'<svg xmlns="http://www.w3.org/2000/svg"'
            f' width="{svg_w:.0f}" height="{svg_h:.0f}"'
            f' viewBox="0 0 {svg_w:.0f} {svg_h:.0f}">',
            f'  <title>Legendrian knot braid={self.braid}</title>',
        ]
        for k, strand in enumerate(strands):
            pts = [(px(i + 1), py(y)) for i, y in enumerate(strand)]
            d = _path(pts)
            color = palette[k % len(palette)]
            lines.append(
                f'  <path d="{d}" stroke="{color}"'
                f' stroke-width="{stroke_width}" fill="none"'
                f' stroke-linecap="round"/>'
            )
        lines.append('</svg>')
        svg_text = '\n'.join(lines) + '\n'
        with open(filename, 'w') as fh:
            fh.write(svg_text)
        return filename


# ============================================================
# Section 4: DGA
# ============================================================

class DGA:
    """
    The contact-homology DGA of a Legendrian knot over a chosen GroundRing.

    Obtain via Leg.dga(ring) rather than constructing directly.

    Differential  (lazily computed, cached)
    ----------------------------------------
    dga.differential   list of word → coeff dicts for every ring (word = tuple
              of letters, each a chord int or a basepoint power ('lambda', c, k)
              meaning t_c^k):
      ZLAMBDA integer coefficients over Z[λ]
      Z/n     same words, integer coefficients reduced mod n (Z/2 included --
              n=2 is just another prime; λ letters stay symbolic, evaluating to
              the only unit 1)

    Methods
    -------
    augmentations(grading_mod, lambda_values)  List[Augmentation], cached per (grading_mod, lambda_values)
    lin_hom(grading_mod)        List[Dict[int,int]], cached per grading_mod
    check_d_squared()           bool  (Z/2 and Z[λ] only)
    aug_count(grading_mod)      float  normalized augmentation number (Z/2, Z/p)
    print_differential()        print d(a[i]) for each generator
    """

    def __init__(self, leg: Optional[Leg], ring: GroundRing) -> None:
        self.leg = leg
        self.ring = ring
        self._differential = None
        self._gradings: Optional[List[int]] = None
        self._rot: Optional[Union[int, Tuple[int, ...]]] = None
        self._num_components: Optional[int] = None
        self.names: Optional[List[str]] = None
        self._augmentations_cache: Dict[tuple, List['Augmentation']] = {}
        self._aug_search_size_cache: Dict[tuple, int] = {}
        self._lin_hom_cache: Dict[int, List[Tuple[Dict[int, int], 'Augmentation']]] = {}
        self._lin_hom_summary_cache: Optional[Dict[int, List[Tuple[Dict[int, int], 'Augmentation']]]] = None
        # Set by simplify() on its result: the destabilization projection back to
        # the source DGA, consumed by pullback_augmentation. None otherwise.
        self._simplify_source: Optional['DGA'] = None
        self._simplify_survivor_map: Optional[Dict[int, int]] = None
        self._simplify_proj: Optional[Dict[int, Any]] = None

    @classmethod
    def abstract(
        cls,
        gradings: List[int],
        differential: List[Dict],
        ring: GroundRing,
        rot: Union[int, Tuple[int, ...]],
        num_components: int,
        names: Optional[List[str]] = None,
    ) -> 'DGA':
        """A Leg-less semifree DGA (e.g. the output of simplify()).

        names, if given, is one display label per generator (used by
        print_differential); it must have the same length as gradings.
        """
        if names is not None and len(names) != len(gradings):
            raise ValueError(
                f'names must have one entry per generator ({len(gradings)}), '
                f'got {len(names)}'
            )
        self = cls.__new__(cls)
        self.leg = None
        self.ring = ring
        self._differential = differential
        self._gradings = list(gradings)
        self._rot = rot
        self._num_components = num_components
        self.names = list(names) if names is not None else None
        self._augmentations_cache = {}
        self._aug_search_size_cache = {}
        self._lin_hom_cache = {}
        self._lin_hom_summary_cache = None
        self._simplify_source = None
        self._simplify_survivor_map = None
        self._simplify_proj = None
        return self

    @property
    def gradings(self) -> List[int]:
        return self._gradings if self._gradings is not None else self.leg.grading

    @property
    def rot(self) -> Union[int, Tuple[int, ...]]:
        return self._rot if self._rot is not None else self.leg.rot

    @property
    def num_components(self) -> int:
        return self._num_components if self._num_components is not None else self.leg.num_components

    def __repr__(self) -> str:
        if self.leg is None:
            return f'DGA.abstract(num_gens={len(self.gradings)}, ring={self.ring!r})'
        return f'DGA({self.leg!r}, ring={self.ring!r})'

    @cached_property
    def _gens_spaces(self) -> List[List[int]]:
        """Generators grouped by grading, highest first. Used by homology computations."""
        gr = self.gradings
        max_g, min_g = max(gr), min(gr)
        return [[i + 1 for i, g in enumerate(gr) if g == k]
                for k in range(max_g, min_g - 1, -1)]

    def _z_diff(self) -> List[Dict]:
        """
        DGA differential over Z[λ^±1].
        Returns a list (one entry per generator) of dicts mapping
          word -> integer_coefficient
        where word is a tuple of letters, each either a chord (int) or a basepoint
        power ('lambda', c, k) meaning t_c^k (c = 0-indexed component).
        Used by self.differential for both ZLAMBDA and Z/n rings.
        """
        b = self.leg.braid

        def pos(lst):
            return [x for x in lst if x > 0]

        def glue_enhanced(u_path, lb_term):
            l_path, coeff = lb_term
            u_abs = {abs(x) for x in u_path if abs(x) > 0}
            l_abs = {abs(x) for x in l_path if abs(x) > 0}
            if u_abs & l_abs:
                return None
            return (list(reversed(pos(u_path))) + pos(l_path), coeff)

        def glue_lists_enhanced(ub, lbenhanced):
            p = len(ub) - 1
            seen, result = set(), []
            for j in range(1, p + 1):
                for u_path in ub[j]:
                    for lb_term in lbenhanced[j]:
                        g = glue_enhanced(u_path, lb_term)
                        if g is not None:
                            key = (tuple(g[0]), g[1])
                            if key not in seen:
                                seen.add(key)
                                result.append(g)
            return result

        def diff_enhanced():
            p = self.leg.num_cusps
            gr_b = self.leg.grading  # len = len(b) + p; correct for multi-component links
            bext = b + list(range(1, 2 * p, 2))
            n = len(bext)

            u = [[[] for _ in range(2 * p + 1)] for _ in range(n + 1)]
            lo = [[[] for _ in range(2 * p + 1)] for _ in range(n + 1)]
            for j in range(1, p + 1):
                u[1][2 * j] = [[j]]
                lo[1][2 * j - 1] = [[j]]

            for i in range(1, n):
                jj = bext[i - 1]
                for s in range(2 * p + 1):
                    u[i + 1][s] = u[i][s][:]
                    lo[i + 1][s] = lo[i][s][:]
                u[i + 1][jj + 1] = [path + [-i] for path in u[i][jj]]
                u[i + 1][jj] = [list(t) for t in
                                 {tuple(path + [-i]) for path in u[i][jj + 1]} |
                                 {tuple(path + [i]) for path in u[i][jj]}]
                lo[i + 1][jj] = [path + [-i] for path in lo[i][jj + 1]]
                lo[i + 1][jj + 1] = [list(t) for t in
                                      {tuple(path + [-i]) for path in lo[i][jj]} |
                                      {tuple(path + [i]) for path in lo[i][jj + 1]}]

            ub = [[[] for _ in range(p + 1)] for _ in range(n + 1)]
            lb = [[[] for _ in range(p + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                c = bext[i - 1]
                for j in range(1, p + 1):
                    ub[i][j] = [path[1:] for path in u[i][c + 1] if path and path[0] == j]
                    lb[i][j] = [path[1:] for path in lo[i][c] if path and path[0] == j]

            lbe = [[[] for _ in range(p + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, p + 1):
                    for path in lb[i][j]:
                        sign = 1
                        for x in path:
                            if 0 < x <= len(gr_b):
                                sign *= (-1) ** (gr_b[x - 1] % 2 + 1)
                        lbe[i][j].append((path, sign))

            bd = [None] + [glue_lists_enhanced(ub[i], lbe[i]) for i in range(1, n + 1)]
            comp_of, final_perm = self.leg._comp_and_perm
            mu = self.leg.strand_potentials
            basepoint: Dict[int, int] = {}  # comp_index -> 0-indexed right cusp j
            for j in range(p):
                basepoint[comp_of[final_perm[2 * j]]] = j  # last right cusp per component
            for i in range(n - p + 1, n + 1):
                j = i - (n - p + 1)  # 0-indexed right cusp (1-indexed k = j+1 in _z_diff terms)
                c = comp_of[final_perm[2 * j]]
                if j == basepoint[c]:
                    # Lower strand's Maslov potential determines cusp orientation:
                    # odd → downward cusp → λ_c; even → upward cusp → λ_c^{-1}
                    lower = final_perm[2 * j + 1]
                    coeff = ('lambda', c) if mu[lower] % 2 == 1 else ('lambda_inv', c)
                else:
                    coeff = 1
                entry = bd[i]
                assert entry is not None
                bd[i] = [([], coeff)] + entry
            return bd[1:]

        result = []
        for terms in diff_enhanced():
            poly: Dict = {}
            assert terms is not None
            for word, coeff in terms:
                if isinstance(coeff, tuple):  # ('lambda', c) or ('lambda_inv', c)
                    assert not word  # geometric λ is always a standalone constant
                    c = coeff[1]
                    sign = 1 if coeff[0] == 'lambda' else -1
                    k = (('lambda', c, sign),)
                    poly[k] = poly.get(k, 0) + 1
                else:
                    k = tuple(word)
                    poly[k] = poly.get(k, 0) + coeff
            result.append({k: v for k, v in poly.items() if v != 0})
        return result

    @property
    def differential(self):
        """
        The DGA differential, computed once and cached.

        The DGA itself is defined over Z/2 in [Ch02] and extended to Z-coefficients
        with coherent orientations in [ENS02]; the plat-form algorithm used here
        follows [Ng03].

        Links are supported over all rings. The returned list of dicts is keyed
        by word, a tuple of letters each either a chord (int) or a basepoint
        power ('lambda', c, k) meaning t_c^k at its position in the word (c =
        0-indexed component; the basepoint cusp's sign depends on the cusp's
        orientation: lower-strand Maslov potential odd → λ_c (k=+1), even → λ_c^{-1}
        (k=-1)). Z/n (including Z/2) integer coefficients are reduced mod n;
        λ_c letters remain symbolic for evaluation at augmentation time.
        """
        if self._differential is not None:
            return self._differential

        if self.ring == GroundRing.ZLAMBDA:
            self._differential = self._z_diff()

        else:
            # Z/n: lift through Z[λ], reduce integer coefficients mod n, keep λ_c symbolic
            n = self.ring.modulus
            zd = self._z_diff()
            result = []
            for poly_dict in zd:
                reduced: Dict[tuple, int] = {}
                for word, coeff in poly_dict.items():
                    c = coeff % n
                    if c:
                        reduced[word] = (reduced.get(word, 0) + c) % n
                result.append({k: v for k, v in reduced.items() if v})
            self._differential = result

        return self._differential

    def check_d_squared(self) -> bool:
        """
        Verify d² = 0, over any ring (Z[λ] exactly; Z/n mod n).

        Expands ∂² via the graded Leibniz rule on self.differential (already
        reduced mod n for Z/n rings, including Z/2): for each generator, for
        every word in its differential and every chord position in that word,
        substitute that chord's own differential and accumulate signed
        monomial counts; d²=0 iff every count vanishes (mod n for Z/n, exactly
        for Z[λ]). Reduction mod n commutes with this accumulation, so working
        from the already-reduced differential and checking the final counts
        mod n is equivalent to reducing at the end.
        """
        d = self.differential
        gr = self.gradings
        n = None if self.ring == GroundRing.ZLAMBDA else self.ring.modulus

        d_pairs = [list(poly.items()) for poly in d]
        for pairs in d_pairs:
            count: Dict[tuple, int] = {}
            for word, coeff in pairs:
                for pos, gen in enumerate(word):
                    if not isinstance(gen, int):
                        continue  # ∂t_c = 0: only chord positions differentiate
                    prefix = word[:pos]
                    suffix = word[pos + 1:]
                    right_sign = (-1) ** sum(
                        _letter_grading(word[j], gr) for j in range(pos + 1, len(word))
                    )
                    for d_word, d_coeff in d_pairs[gen - 1]:
                        new_word = _word_mul(_word_mul(prefix, d_word), suffix)
                        count[new_word] = count.get(new_word, 0) + coeff * right_sign * d_coeff
            if n is None:
                if any(v != 0 for v in count.values()):
                    return False
            else:
                if any(v % n != 0 for v in count.values()):
                    return False
        return True

    def _augmentation_system(self, zn_d, grading_mod: int, n: int,
                             lv: Optional[Dict[int, int]]) -> _AugSystem:
        """Build the Z/n augmentation-search system at this grading_mod.

        zn_d is the differential in dict form (list of {word: coeff}); for Z/2
        it must already be mod-2 reduced (one {word: 1} per surviving monomial).
        lv optionally fixes some ('lambda', c) values (only used for n > 2).

        Shared by augmentations()'s aug_zn brute force and one_aug's backtracking
        search so they agree on variables, value ranges, and conditions. Pure
        setup: no search, no caching, no max_search/max_nodes accounting.
        See _AugSystem for the returned fields.
        """
        gr = self.gradings
        num_comp = self.num_components

        def is_grade0(x):
            return x == 0 if grading_mod == 0 else x % grading_mod == 0

        def is_grade1(x):
            if grading_mod == 0: return x == 1
            if grading_mod == 1: return True
            return x % grading_mod == 1

        grade0_gens = [i + 1 for i, x in enumerate(gr) if is_grade0(x)]
        grade1_gens = [i + 1 for i, x in enumerate(gr) if is_grade1(x)]
        grade0_set = set(grade0_gens)

        units = [v for v in range(1, n) if gcd(v, n) == 1]
        lambda_keys = [('lambda', c) for c in range(num_comp)]
        var_ranges: Dict[Any, List[int]] = {g: list(range(n)) for g in grade0_gens}
        for c in range(num_comp):
            lk = ('lambda', c)
            var_ranges[lk] = [lv[c]] if (lv is not None and c in lv) else units
        all_vars = grade0_gens + lambda_keys

        # Extract conditions from grade-1 differentials.
        # Basepoint letters in a word are units of degree 0, so they always pass
        # the grade-0 filter (only chord letters are checked).
        conditions = [
            [(w, coeff) for w, coeff in zn_d[g1 - 1].items()
             if all(gi in grade0_set for gi in w if isinstance(gi, int))]
            for g1 in grade1_gens
        ]
        return _AugSystem(conditions, var_ranges, all_vars,
                          grade0_gens, grade1_gens, lambda_keys, units)

    def augmentations(
        self,
        grading_mod: int = 0,
        lambda_values: Optional[Dict[int, int]] = None,
        max_search: Optional[int] = _USE_DEFAULT_AUG_LIMIT,
    ) -> List['Augmentation']:
        """
        All augmentations of this DGA over self.ring.
        Cached per (grading_mod, lambda_values).

        grading_mod: 0 = Z-graded, 1 = ungraded, n >= 2 = Z/n-graded.
        Requires grading_mod | 2*rot_c for every component (same condition as rulings).
        Not supported for Z[λ] (use Z/2 or Z/p instead).

        lambda_values: optional dict {component_index: value} fixing the image of each
        lambda_c under the augmentation.  Only used for Z/n (n > 2).
        - Knot default (1 component): lambda_0 -> n-1 (= -1 mod n).
        - Link default: search over all units in (Z/n)^x for each component.
        Override by passing e.g. lambda_values={0: 1} to fix lambda_0 = 1.
        Z/2 ignores lambda_values (only one unit: 1 = -1 mod 2).

        Uses linear pre-reduction (for prime rings, including Z/2) followed by
        brute force over the remaining free variables -- the same algorithm for
        every ring, 2 included (2 is just another prime).

        max_search: upper bound on the brute-force search-space size (number of
        augmentation candidates to evaluate) after iterative linear pre-reduction,
        i.e. the product of per-variable ranges over the free variables. If the
        residual space exceeds max_search, AugSearchLimitError is raised before
        any brute-force work is done. When omitted, resolves to the current value
        of the module global DEFAULT_AUG_SEARCH_LIMIT (3*10**7) at call time, so
        reassigning that global after import takes effect. Pass max_search=None
        to disable the check entirely.
        """
        if max_search is _USE_DEFAULT_AUG_LIMIT:
            max_search = DEFAULT_AUG_SEARCH_LIMIT
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError(
                'Augmentations are not computed directly over Z[λ]. '
                'Use leg.dga(GroundRing.Z2) or leg.dga(GroundRing.Zn(p)).'
            )
        _rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
        if not all(_divisible(grading_mod, 2 * r) for r in _rots):
            raise ValueError(
                f"grading_mod={grading_mod} is out of domain for this diagram; "
                f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
            )
        modulus = self.ring.modulus
        num_comp = self.num_components
        if modulus > 2:
            if lambda_values is not None:
                lv: Optional[Dict[int, int]] = lambda_values
            elif num_comp == 1:
                lv = {0: modulus - 1}  # knot default: lambda -> -1 mod n
            else:
                lv = None  # links: search over (Z/n)^x for each component
        else:
            lv = None  # Z/2: no lambda tracking needed
        lv_key = frozenset(lv.items()) if lv is not None else None
        cache_key = (grading_mod, lv_key)
        if cache_key not in self._augmentations_cache:
            d = self.differential

            def aug_zn(zn_d, n, lv_inner):
                # grading_mod == 0 implies rot == 0 here (enforced by the domain
                # check above), so no reduction mod 2*rot is ever needed.
                sysm = self._augmentation_system(zn_d, grading_mod, n, lv_inner)
                conditions = sysm.conditions
                var_ranges = sysm.var_ranges
                all_vars = sysm.all_vars
                var_is_lambda = set(sysm.lambda_keys)

                def eval_cond(poly_terms, augm_dict):
                    total = 0
                    for word, coeff in poly_terms:
                        term = coeff % n
                        for letter in word:
                            term = (term * _eval_letter(letter, augm_dict, n)) % n
                        total = (total + term) % n
                    return total

                # Linear pre-reduction for prime n.
                # Include forced-lambda constraints so the solver can detect
                # conflicts between lambda_values and the differential equations.
                if _is_prime(n):
                    presolve_conds = list(conditions)
                    if lv_inner is not None:
                        for c, v in lv_inner.items():
                            presolve_conds.append([
                                ((('lambda', c, 1),), 1),
                                ((), (n - v) % n),
                            ])
                    presolve = _iterative_presolve_zn(presolve_conds, all_vars, n)
                    if presolve is None:
                        return []
                    pivot_map, free_keys = presolve
                else:
                    pivot_map, free_keys = {}, all_vars

                search_size = 1
                for v in free_keys:
                    search_size *= len(var_ranges[v])
                self._aug_search_size_cache[cache_key] = search_size
                if max_search is not None and search_size > max_search:
                    raise AugSearchLimitError(
                        f"Z/{n} augmentation search space after linear pre-reduction "
                        f"is {search_size:,}, which exceeds "
                        f"max_search={max_search:,}. Pass max_search=None to disable."
                    )

                result = []
                for free_vals in product(*[var_ranges[v] for v in free_keys]):
                    assignment: Dict = dict(zip(free_keys, free_vals))
                    for piv_key, (const, coeff_list) in pivot_map.items():
                        val = const
                        for neg_coeff, fk in coeff_list:
                            val = (val + neg_coeff * assignment[fk]) % n
                        assignment[piv_key] = val
                    # Pivot lambda values must be units (nonzero).
                    if any(assignment[lk] == 0 for lk in var_is_lambda if lk in pivot_map):
                        continue
                    if all(eval_cond(cond, assignment) == 0 for cond in conditions):
                        result.append(dict(assignment))
                return result

            raw = aug_zn(d, modulus, lv)
            if modulus == 2:
                # Preserve the established Z/2 Augmentation.data format (a
                # sorted list of generators sent to 1) rather than the general
                # {gen: value} dict -- a public-API/format choice, independent
                # of the (now-unified) search algorithm.
                raw = [sorted(g for g, v in a.items() if isinstance(g, int) and v == 1)
                       for a in raw]
            self._augmentations_cache[cache_key] = [
                Augmentation(a, self, grading_mod) for a in raw
            ]
        # max_search is a resource guard, not part of cache_key (the result is
        # max_search-independent). Re-check it on every call -- including cache
        # hits -- against the cached search size, so a later, stricter max_search
        # is still honored rather than silently bypassed by the cache. (Trivial
        # cases that returned before computing a search size cache nothing here;
        # their effective search size is 0.)
        search_size = self._aug_search_size_cache.get(cache_key, 0)
        if max_search is not None and search_size > max_search:
            raise AugSearchLimitError(
                f"augmentation search space is {search_size:,}, which exceeds "
                f"max_search={max_search:,}. Pass max_search=None to disable."
            )
        return self._augmentations_cache[cache_key]

    def one_aug(
        self,
        grading_mod: int = 0,
        simplify: bool = True,
        max_nodes: Optional[int] = _USE_DEFAULT_AUG_LIMIT,
    ) -> Optional['Augmentation']:
        """
        Return a single augmentation of this DGA over self.ring, or None if it
        has none -- without enumerating all of them as augmentations() does.

        Uses backtracking with constraint propagation and fail-first branching:
        propagate the augmentation equations (the same Z/n system augmentations()
        builds), fix one free variable, re-propagate, prune on conflict, recurse,
        and stop at the first satisfying assignment. On large diagrams this can be
        dramatically faster than augmentations(), which must build the full list.

        grading_mod: as in augmentations() (0 = Z-graded, 1 = ungraded,
        n >= 2 = Z/n-graded; requires grading_mod | 2*rot_c per component).

        simplify (default True): first algebraically simplify the DGA
        (self.simplify(), handle cancellation), search the smaller result, and
        pull the augmentation back to self. Sound because simplify's projection
        is existence-preserving (the simplified DGA has an augmentation iff self
        does). An augmentation produced by this search vanishes on every
        cancelled degree-0 generator. simplify=False searches self directly.

        max_nodes: backtracking-node budget; raises AugSearchLimitError when
        exceeded. Omitted resolves to the module global DEFAULT_ONE_AUG_NODE_LIMIT
        at call time; pass None to disable. This counts search-tree nodes, NOT the
        static candidate count that augmentations()'s max_search bounds, and is a
        runaway-search guard rather than a wall-clock limit.

        If augmentations() has already enumerated the set under this same
        (grading_mod, lambda-convention) -- e.g. a prior augmentations() call, or
        a prior one_aug() that recorded emptiness -- one_aug returns one of the
        cached augmentations directly (or None if that set is empty), skipping
        both the search and the simplify step. The cached convention is the
        default-call one (knot lambda -> -1); a non-default augmentations(
        lambda_values=...) cache does not match and is ignored.

        Returns an Augmentation of self (any one -- not a canonical choice), or
        None. The augmentation itself is not cached (a single-shot query), but a
        None result -- which certifies no augmentation exists, since the search is
        complete unless max_nodes raises -- IS recorded in augmentations()'s cache,
        so a subsequent augmentations() call returns [] immediately (even when its
        own brute force would exceed max_search). Not supported over Z[lambda].
        """
        if max_nodes is _USE_DEFAULT_AUG_LIMIT:
            max_nodes = DEFAULT_ONE_AUG_NODE_LIMIT
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError(
                'Augmentations are not computed directly over Z[λ]. '
                'Use leg.dga(GroundRing.Z2) or leg.dga(GroundRing.Zn(p)).'
            )
        _rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
        if not all(_divisible(grading_mod, 2 * r) for r in _rots):
            raise ValueError(
                f"grading_mod={grading_mod} is out of domain for this diagram; "
                f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
            )

        # Ground-ring modulus and λ-value choice, matching augmentations()'s
        # default-call convention so a proven emptiness can be recorded for it.
        n = 2 if self.ring == GroundRing.Z2 else self.ring.modulus
        if n > 2 and self.num_components == 1:
            lv: Optional[Dict[int, int]] = {0: n - 1}  # knot default: λ -> -1 mod n
        else:
            lv = None  # links search units; Z/2 has no λ tracking
        lv_key = frozenset(lv.items()) if lv is not None else None

        # Reuse an existing augmentations() enumeration under this convention:
        # return any one (the first), or None if it was certified empty, without
        # searching or simplifying.
        cached = self._augmentations_cache.get((grading_mod, lv_key))
        if cached is not None:
            return cached[0] if cached else None

        def _record_empty():
            # one_aug returns None only from a *complete* search (hitting max_nodes
            # raises instead), so None certifies no augmentation exists. Record
            # that in augmentations()'s cache, so a later augmentations() call
            # returns [] at once -- even on a diagram whose brute force would
            # exceed max_search.
            self._augmentations_cache.setdefault((grading_mod, lv_key), [])

        if simplify:
            B = self.simplify()
            found = B.one_aug(grading_mod=grading_mod, simplify=False,
                              max_nodes=max_nodes)
            if found is None:
                _record_empty()
                return None
            return B.pullback_augmentation(found)

        # --- search self directly (simplify=False) ---
        zn_d = self.differential
        sysm = self._augmentation_system(zn_d, grading_mod, n, lv)
        conditions = sysm.conditions
        var_ranges = sysm.var_ranges
        lambda_set = set(sysm.lambda_keys)
        # Admissible values per λ key: a single fixed value for a knot (the λ→-1
        # default, or a caller override), or all units for a link component. A
        # λ pivoted by the linear solver to a unit OUTSIDE this set (e.g. a unit
        # other than the knot default) is NOT a valid augmentation -- mirrors the
        # forced-λ constraint augmentations() feeds into its presolve.
        lambda_ranges = {lk: set(var_ranges[lk]) for lk in lambda_set}
        is_prime = _is_prime(n)

        def var_in_cond(v, cond) -> bool:
            if isinstance(v, tuple):  # ('lambda', c): match basepoint letters of comp c
                c = v[1]
                return any(isinstance(letter, tuple) and letter[1] == c
                           for word, _ in cond for letter in word)
            return any(v in word for word, _ in cond)

        def eval_cond(poly_terms, augm) -> int:
            total = 0
            for word, coeff in poly_terms:
                term = coeff % n
                for letter in word:
                    term = (term * _eval_letter(letter, augm, n)) % n
                total = (total + term) % n
            return total

        def default_value(v):
            # Generators are 0 (augmentations are sparse); λ keys take the first
            # admissible unit (closes the missing-λ KeyError in _eval_letter).
            return var_ranges[v][0] if isinstance(v, tuple) else 0

        def propagate(conds, live):
            """(pivot_map, free_keys) or None on conflict.  Prime: Gaussian
            pre-reduction (which also detects constant-term inconsistency).
            Composite: substitution-only -- no linear solver (its modular inverse
            needs a prime field) -- so just flag nonzero-constant conditions."""
            if is_prime:
                res = _iterative_presolve_zn(conds, live, n)
                if res is None:
                    return None
                pivot_map, free_keys = res
                # A fully-determined λ pivot must land in its admissible set
                # (knot default / link units); prune early if not.
                for lk in lambda_set:
                    if lk in pivot_map:
                        const, deps = pivot_map[lk]
                        if not deps and const not in lambda_ranges[lk]:
                            return None
                return pivot_map, free_keys
            for cond in conds:
                if cond and all(word == () for word, _ in cond):
                    if sum(c for _, c in cond) % n != 0:
                        return None
            return {}, list(live)

        nodes = 0

        def search(conds, live):
            nonlocal nodes
            nodes += 1
            if max_nodes is not None and nodes > max_nodes:
                raise AugSearchLimitError(
                    f"one_aug exceeded max_nodes={max_nodes:,} backtracking nodes. "
                    f"Pass max_nodes=None to disable, or raise it / "
                    f"DEFAULT_ONE_AUG_NODE_LIMIT."
                )
            res = propagate(conds, live)
            if res is None:
                return None
            pivot_map, free_keys = res
            free_appearing = [v for v in free_keys if any(var_in_cond(v, c) for c in conds)]
            if not free_appearing:
                # Leaf: every remaining free variable is unconstrained by conds, so
                # default it; then back-substitute the determined pivots.
                assignment = {v: default_value(v) for v in free_keys}
                for piv, (const, coeff_list) in pivot_map.items():
                    val = const
                    for neg_coeff, fk in coeff_list:
                        val = (val + neg_coeff * assignment[fk]) % n
                    assignment[piv] = val
                if any(assignment[lk] not in lambda_ranges[lk]
                       for lk in lambda_set if lk in assignment):
                    return None
                if all(eval_cond(c, assignment) == 0 for c in conds):
                    return assignment
                return None
            # Fail-first: branch the variable in the most conditions; tie-break to
            # the smallest remaining domain.
            v = max(free_appearing,
                    key=lambda w: (sum(var_in_cond(w, c) for c in conds),
                                   -len(var_ranges[w])))
            for val in var_ranges[v]:   # 0-first for generators; units for λ
                child = search(_substitute_conds_zn(conds, {v: val}, n),
                               [w for w in live if w != v])
                if child is not None:
                    child[v] = val
                    return child
            return None

        found = search(conditions, list(sysm.all_vars))
        if found is None:
            _record_empty()
            return None
        if self.ring == GroundRing.Z2:
            data: Any = sorted(g for g, v in found.items()
                               if isinstance(g, int) and v % 2 == 1)
        else:
            data = dict(found)
        return Augmentation(data, self, grading_mod)

    def _twisted_diff_f2(self, augmentation: 'Augmentation', n: int = 1) -> List[List[List[int]]]:
        """
        Degree-n part of the result of twisting self.differential by augmentation.

        Applies augmentation to self.differential, expanding each generator that
        is sent to 1, then keeps only monomials of output word length n.

        n=2 gives the quadratic part, used by double_products for cup products.
        For n=1 (the linearized differential), prefer the faster, bilinear-ready
        ``_bilin_diff_f2(augmentation, augmentation)`` instead.

        Only implemented over Z/2. For Z/n linearized homology use
        ``_dim_homology_zn`` directly.
        """
        if self.ring != GroundRing.Z2:
            raise NotImplementedError(
                '_twisted_diff_f2 is only implemented over Z/2; '
                'use _dim_homology_zn for Z/n linearized homology.'
            )
        d = self.differential
        aug_set = set(augmentation.data)
        aug_d = []
        for poly in d:
            new_terms = []
            for mono in poly:
                expanded = [[]]
                for x in mono:
                    if isinstance(x, tuple):
                        # Basepoint letter ('lambda', c, k): Z/2's only unit is
                        # 1, so it always evaluates to 1 and drops out of the
                        # word entirely (not a literal element, not a choice).
                        continue
                    if x in aug_set:
                        expanded = [e + [x] for e in expanded] + [e for e in expanded]
                    else:
                        expanded = [e + [x] for e in expanded]
                new_terms.extend(expanded)
            cnt = Counter(tuple(e) for e in new_terms)
            aug_d.append([list(k) for k, v in cnt.items() if v % 2 == 1])
        return [[m for m in poly if len(m) == n] for poly in aug_d]

    def _bilin_diff_f2(self, aug0: 'Augmentation', aug1: 'Augmentation') -> List[List[List[int]]]:
        """Degree-1 part of the bilinearized augmented differential d_{aug0,aug1},
        over Z/2: for each chord position in a monomial, it survives iff every
        letter to its left is sent to 1 by aug0 and every letter to its right is
        sent to 1 by aug1. aug0=aug1 recovers _twisted_diff_f2(aug0, n=1) (only
        the n=1 case generalizes to a bilinear pair; n=2 cup products stay
        single-aug)."""
        d = self.differential
        aug0_set, aug1_set = set(aug0.data), set(aug1.data)
        # Basepoint letters ('lambda', c, k) always evaluate to 1 (Z/2's only
        # unit), so they trivially satisfy the "sent to 1" condition on either
        # side without being chord generators themselves.
        def _ok(g, s):
            return isinstance(g, tuple) or g in s
        result = []
        for poly in d:
            cnt = Counter()
            for mono in poly:
                for i, x in enumerate(mono):
                    if isinstance(x, tuple):
                        continue
                    if all(_ok(g, aug0_set) for g in mono[:i]) and all(_ok(g, aug1_set) for g in mono[i + 1:]):
                        cnt[x] += 1
            result.append([[x] for x, v in cnt.items() if v % 2 == 1])
        return result

    def _diff_matrix_f2(self, which: int, ld: List) -> List[List[int]]:
        """F_2 matrix of the linearized differential ld mapping _gens_spaces[which-1] → _gens_spaces[which]."""
        ld_out = {i + 1: frozenset(x for m in poly for x in m) for i, poly in enumerate(ld)}
        return _lin_diff_mat_f2(self._gens_spaces[which - 1], self._gens_spaces[which], ld_out)

    def _z2_aug_dict(self, data) -> dict:
        """Normalize a Z/2 Augmentation.data value -- a sorted list of
        generators sent to 1 (the established public format; see
        DGA.augmentations) -- to a {gen: value} dict, with every ('lambda', c)
        key sent to the ring's only unit, 1 (Z/2 has no other choice). Lets
        the general Zn(p) homology/cohomology/homotopy code (which expects
        dict-style .get/[] access, like every other Z/n) treat Z/2 uniformly,
        without changing Z/2's public Augmentation.data format."""
        d = {g: 1 for g in data}
        for c in range(self.num_components):
            d[('lambda', c)] = 1
        return d

    def _dim_homology_zn(self, place: int, aug0: 'Augmentation', aug1: 'Augmentation') -> int:
        """Dimension of Z/n bilinearized homology (w.r.t. the ordered pair
        (aug0, aug1)) at grading position place (1-indexed in _gens_spaces).
        aug0=aug1 recovers the single-augmentation linearized homology."""
        zn_d = self.differential
        aug0_dict = self._z2_aug_dict(aug0.data) if self.ring == GroundRing.Z2 else aug0.data
        aug1_dict = self._z2_aug_dict(aug1.data) if self.ring == GroundRing.Z2 else aug1.data
        n = 2 if self.ring == GroundRing.Z2 else self.ring.modulus
        if not _is_prime(n):
            raise NotImplementedError(
                f'Linearized homology dimensions require a field coefficient ring; '
                f'Z/{n} is not a field (n must be prime). '
                f'Augmentation enumeration over Z/{n} is still supported.'
            )
        gs = self._gens_spaces

        def rank_zn(mat):
            return _rank_zn(mat, n)

        def nullity_zn(mat, ncols):
            if not mat:
                return ncols  # zero map into empty space; full domain is the kernel
            if not mat[0]:
                return 0
            return ncols - rank_zn(mat)

        def diff_matrix_zn(which):
            return _bilin_diff_mat_zp(gs[which - 1], gs[which], zn_d, aug0_dict, aug1_dict, n)

        num = len(gs)
        if num == 1:
            return len(gs[0])
        if place == 1:
            return nullity_zn(diff_matrix_zn(1), len(gs[0]))
        if place == num:
            return len(gs[num - 1]) - rank_zn(diff_matrix_zn(num - 1))
        return nullity_zn(diff_matrix_zn(place), len(gs[place - 1])) - rank_zn(diff_matrix_zn(place - 1))

    def dim_homology(self, place: int, aug0: 'Augmentation',
                      aug1: Optional['Augmentation'] = None) -> int:
        """
        Dimension of homology at grading position place, with respect to aug0
        (linearized) or the ordered pair (aug0, aug1) (bilinearized) when aug1
        is given. Same _dim_homology_zn computation for every ring, Z/2
        included (2 is just another prime).
        """
        if aug1 is None:
            aug1 = aug0
        return self._dim_homology_zn(place, aug0, aug1)

    def _lin_hom_as_dict(self, aug0: 'Augmentation', aug1: 'Augmentation',
                          grading_mod: int) -> Dict[int, int]:
        """
        Poincaré-Chekanov polynomial for the ordered pair (aug0, aug1) at
        grading_mod -- bilinearized in general, aug0=aug1 recovers the
        single-augmentation linearized polynomial.

        For grading_mod=0 uses the integer-graded chain complex (differential is
        strictly degree -1 in ℤ, so adjacent-grade matrices are exact).
        For grading_mod≥1 builds merged ℤ/n spaces and includes every ld_ε
        contribution between the merged classes, which is required when skip-in-ℤ
        terms still land in the correct ℤ/n grade.
        """
        gr = self.gradings
        n = grading_mod

        # One loop for every ring (Z/2 included -- 2 is just another prime) and
        # for grading_mod=0 and grading_mod>=1 alike -- grading_mod=0 keys
        # spaces by literal grade (no wraparound, contiguous over the full
        # [min_g, max_g] range so interior gaps still appear as empty spaces);
        # grading_mod=n wraps keys mod n. A neighbor grade absent from spaces
        # (out of range, or an empty gap) contributes an empty domain/range to
        # _bilin_diff_mat_zp, whose rank is 0 -- this is what the old
        # grading_mod=0 code's boundary-cased top/bottom grades amounted to.
        if n == 0:
            max_g, min_g = max(gr), min(gr)
            spaces = {g: [] for g in range(min_g, max_g + 1)}
            for i, g in enumerate(gr):
                spaces[g].append(i + 1)

            def grade_key(g: int) -> int:
                return g
        else:
            from collections import defaultdict
            spaces = defaultdict(list)
            for i, g in enumerate(gr):
                spaces[g % n].append(i + 1)

            def grade_key(g: int) -> int:
                return g % n

        zn_d = self.differential
        if self.ring == GroundRing.Z2:
            aug0_dict, aug1_dict = self._z2_aug_dict(aug0.data), self._z2_aug_dict(aug1.data)
            p = 2
        else:
            aug0_dict, aug1_dict = aug0.data, aug1.data
            p = self.ring.modulus
        result = {}
        for j in list(spaces):
            mat_out = _bilin_diff_mat_zp(spaces[j], spaces.get(grade_key(j - 1), []),
                                          zn_d, aug0_dict, aug1_dict, p)
            mat_in  = _bilin_diff_mat_zp(spaces.get(grade_key(j + 1), []), spaces[j],
                                          zn_d, aug0_dict, aug1_dict, p)
            dim = (len(spaces[j]) - _rank_zn(mat_out, p) - _rank_zn(mat_in, p))
            if dim:
                result[j] = dim
        return result

    def _bilin_hom_z_as_dict(self, aug0: 'Augmentation', aug1: 'Augmentation',
                             grading_mod: int) -> Dict[int, Tuple[int, List[int]]]:
        """{grading: (free_rank, [torsion_factors])} for the ordered pair
        (aug0, aug1) at grading_mod over Z -- the Z analogue of
        _lin_hom_as_dict's Z/n branch, reusing the exact same grade_key-dict
        loop shape, but Smith normal form of mat_in in place of a bare rank,
        since Z-homology can have torsion: free_rank = dim C_j -
        rank(mat_out) - rank(mat_in), torsion = mat_in's invariant factors
        > 1. Gradings with (0, []) omitted."""
        gr = self.gradings
        n = grading_mod
        if n == 0:
            max_g, min_g = max(gr), min(gr)
            spaces: Dict[int, List[int]] = {g: [] for g in range(min_g, max_g + 1)}
            for i, g in enumerate(gr):
                spaces[g].append(i + 1)

            def grade_key(g: int) -> int:
                return g
        else:
            from collections import defaultdict
            spaces = defaultdict(list)
            for i, g in enumerate(gr):
                spaces[g % n].append(i + 1)

            def grade_key(g: int) -> int:
                return g % n

        z_d = self.differential
        aug0_dict, aug1_dict = aug0.data, aug1.data
        result: Dict[int, Tuple[int, List[int]]] = {}
        for j in list(spaces):
            mat_out = _bilin_diff_mat_z(spaces[j], spaces.get(grade_key(j - 1), []),
                                        z_d, aug0_dict, aug1_dict)
            mat_in  = _bilin_diff_mat_z(spaces.get(grade_key(j + 1), []), spaces[j],
                                        z_d, aug0_dict, aug1_dict)
            D_in, _, _ = _smith_normal_form(mat_in)
            r_in = min(len(D_in), len(D_in[0])) if D_in else 0
            diag_in = [D_in[i][i] for i in range(r_in)]
            rank_in = sum(1 for d in diag_in if d != 0)
            torsion = sorted(d for d in diag_in if d not in (0, 1))
            free_rank = len(spaces[j]) - _int_rank(mat_out) - rank_in
            if free_rank or torsion:
                result[j] = (free_rank, torsion)
        return result

    def bilin_hom_z(
        self,
        aug0: 'Augmentation',
        aug1: Optional['Augmentation'] = None,
        grading_mod: int = 0,
        as_str: bool = False,
    ) -> Union[Dict[int, Tuple[int, List[int]]], Dict[int, str]]:
        """
        Free ranks and torsion of bilinearized contact homology over Z, for a
        pair of Z-valued augmentations (aug1 omitted -- the diagonal,
        single-augmentation linearized homology over Z).

        self must be a Z[λ] DGA (self.ring == GroundRing.ZLAMBDA); aug0, aug1
        must be grading_mod-graded augmentations of this DGA (aug0.dga is
        self, aug0.grading_mod == grading_mod, and likewise for aug1 -- same
        guards as DGA.lin_hom). Unlike lin_hom, finding Z-valued augmentations
        automatically is out of scope (impractical/undecidable in general):
        the caller must supply aug0 (and aug1) directly, e.g. as an
        Augmentation over self with integer .data ({gen: int} on grade-0
        generators, {('lambda', c): 1 or -1} per component).

        Both augmentations are validated (ε∘∂ = 0 over Z and λ ∈ {1, -1} for
        each) and a ValueError is raised naming which one and why if not --
        this is a correctness gate, not a formality: d_{aug0,aug1}² = 0
        (Bourgeois-Chantraine) only holds when both inputs are genuine
        augmentations.

        Returns {grading: (free_rank, [torsion_factors])} (gradings with
        (0, []) omitted), e.g. {0: (2, [3])} means Z² ⊕ Z/3 in grading 0.
        as_str=True instead returns {grading: str} with each group formatted
        as e.g. "Z^2 + Z/3" (there is no single combined-gradings string the
        way lin_hom's Poincaré polynomial has, since each grading is its own
        abelian group, not just a dimension).
        """
        aug1 = self._validate_bilin_hom_z_args(aug0, aug1, grading_mod)
        result = self._bilin_hom_z_as_dict(aug0, aug1, grading_mod)
        if as_str:
            return {g: _format_z_group(*fr_t) for g, fr_t in result.items()}
        return result

    def _validate_bilin_hom_z_args(self, aug0: 'Augmentation', aug1: Optional['Augmentation'],
                                    grading_mod: int) -> 'Augmentation':
        """Shared guard for bilin_hom_z/bilin_hom_z_gens: ring, aug0/aug1
        membership, grading_mod consistency and domain, and Z-augmentation
        validity (see DGA.bilin_hom_z's docstring for what each check means
        and why). Returns aug1 defaulted to aug0 if it was None."""
        if aug1 is None:
            aug1 = aug0
        if self.ring != GroundRing.ZLAMBDA:
            raise NotImplementedError(
                'bilin_hom_z requires a Z[λ] DGA (self.ring == GroundRing.ZLAMBDA).'
            )
        if aug0.dga is not self or aug1.dga is not self:
            raise ValueError('aug0 and aug1 must be augmentations of this DGA')
        if aug0.grading_mod != grading_mod or aug1.grading_mod != grading_mod:
            raise ValueError(
                f'aug0 and aug1 must both be grading_mod={grading_mod}-graded '
                f'(got aug0.grading_mod={aug0.grading_mod}, aug1.grading_mod={aug1.grading_mod})'
            )
        _rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
        if not all(_divisible(grading_mod, 2 * r) for r in _rots):
            raise ValueError(
                f"grading_mod={grading_mod} is out of domain for this diagram; "
                f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
            )
        for name, aug in (('aug0', aug0), ('aug1', aug1)):
            bad = _is_z_augmentation(self, aug.data, grading_mod)
            if bad is None:
                continue
            if isinstance(bad, tuple):
                raise ValueError(
                    f'{name} is not a Z-valued augmentation: component {bad[1]} '
                    f"lambda value is not a unit (must be 1 or -1)"
                )
            raise ValueError(
                f'{name} is not a Z-valued augmentation: generator {bad} either has '
                f'nonzero data on a non-grade-0 generator, or its ε∘∂=0 equation fails'
            )
        return aug1

    def bilin_hom_z_gens(
        self,
        aug0: 'Augmentation',
        aug1: Optional['Augmentation'] = None,
        grading_mod: int = 0,
    ) -> Dict[int, List[Tuple[Any, List[Tuple[int, int]]]]]:
        """
        Generating set (with orders) for bilinearized contact homology over Z,
        for the ordered pair (aug0, aug1) (aug1 omitted -- diagonal). Same
        validation and guards as bilin_hom_z; see its docstring.

        For each grading, presents H_j = coker(d_in: C_{j+1} -> ker(d_out)):
        a Z-basis K of ker(d_out) (via _int_kernel_basis), the presentation
        matrix P of d_in's image in that basis (via _int_solve_in_basis, using
        d²=0 to guarantee integer coordinates exist), and the Smith normal
        form of P to read off each class's order and re-express it back in
        the K-basis via the inverse of P's SNF row-transform.

        Returns {grading: [(order, [(gen, coeff), ...]), ...]} -- one entry
        per generating class: order is math.inf for a free class or the
        integer torsion order d>1 for a torsion class (order-1 classes are
        the identity of the quotient and are never listed), and the
        representative is a cycle in C_j (mat_out @ rep == 0 over Z) given as
        integer (generator, coefficient) pairs -- the Z analogue of
        Augmentation.cohomology_basis's (gen, coeff) pairs. This is a
        *generating set*, not a basis: unlike a vector-space basis, the
        specific representative and the split between which classes get
        which order are artifacts of the SNF computation, not canonical.
        Gradings with no generators are omitted.
        """
        aug1 = self._validate_bilin_hom_z_args(aug0, aug1, grading_mod)

        gr = self.gradings
        n = grading_mod
        if n == 0:
            max_g, min_g = max(gr), min(gr)
            spaces: Dict[int, List[int]] = {g: [] for g in range(min_g, max_g + 1)}
            for i, g in enumerate(gr):
                spaces[g].append(i + 1)

            def grade_key(g: int) -> int:
                return g
        else:
            from collections import defaultdict
            spaces = defaultdict(list)
            for i, g in enumerate(gr):
                spaces[g % n].append(i + 1)

            def grade_key(g: int) -> int:
                return g % n

        z_d = self.differential
        aug0_dict, aug1_dict = aug0.data, aug1.data
        result: Dict[int, List[Tuple[Any, List[Tuple[int, int]]]]] = {}
        for j in list(spaces):
            domain = spaces[j]
            mat_out = _bilin_diff_mat_z(domain, spaces.get(grade_key(j - 1), []),
                                        z_d, aug0_dict, aug1_dict)
            mat_in  = _bilin_diff_mat_z(spaces.get(grade_key(j + 1), []), domain,
                                        z_d, aug0_dict, aug1_dict)
            K = _int_kernel_basis(mat_out, len(domain))
            m = len(K)
            if m == 0:
                continue
            in_ncols = len(mat_in[0]) if mat_in else 0
            cols = [[row[c] for row in mat_in] for c in range(in_ncols)]
            coords = _int_solve_in_basis(K, cols)
            q = len(coords)
            P = [[coords[c][row] for c in range(q)] for row in range(m)]
            D_p, U_p, _ = _smith_normal_form(P)
            r_p = min(len(D_p), len(D_p[0])) if D_p else 0
            diag = [D_p[i][i] for i in range(r_p)] + [0] * (m - r_p)
            Uinv = _unimodular_inverse(U_p)
            gens: List[Tuple[Any, List[Tuple[int, int]]]] = []
            for i in range(m):
                d = diag[i]
                if d == 1:
                    continue
                order: Any = inf if d == 0 else d
                w = [Uinv[t][i] for t in range(m)]
                rep_full = [sum(w[t] * K[t][c] for t in range(m)) for c in range(len(domain))]
                rep = [(domain[c], v) for c, v in enumerate(rep_full) if v != 0]
                gens.append((order, rep))
            if gens:
                result[j] = gens
        return result

    def lin_hom_summary(self, format: bool = False):
        """
        Compact summary of all m-graded linearized-homology collections at once.

        Enumerates every augmentation once (augmentations(grading_mod=1)) and, for
        each, computes its maximal grading modulus M(ε) = gcd of the grading-domain
        modulus G and the absolute degrees of the generators on which ε is nonzero,
        together with its M(ε)-graded Poincaré-Chekanov polynomial.

        Returns a dict mapping each modulus m to the list of (poly, rep_aug) pairs
        for the *primitive* m-graded homologies: those realized by an aug with
        M(ε) == m and not coinciding, as an element of Z[Z/m], with the image of a
        strictly finer aug's homology. If format=True, returns {m: [poly_str, ...]}
        instead, formatting each poly as a string in t and dropping the rep_aug.
        The full m-graded collection is recovered by all_lin_hom(m) (union over
        buckets M' with m | M' of coarsen(·, m)). Not supported over Z[λ];
        homology dims require a prime field.
        """
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError('lin_hom_summary not implemented over Z[λ]')
        if self._lin_hom_summary_cache is None:
            gr = self.gradings
            rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
            G = reduce(gcd, (2 * r for r in rots), 0)
            modulus = self.ring.modulus

            records = []  # (M, poly_fine, rep_aug)
            for eps in self.augmentations(grading_mod=1):
                if modulus == 2:
                    support = list(eps.data)
                else:
                    support = [k for k, v in eps.data.items()
                               if isinstance(k, int) and v % modulus != 0]
                M = reduce(gcd, (abs(gr[g - 1]) for g in support), G)
                # M can differ from eps.grading_mod (that's the point of this
                # bucketing); the public lin_hom's domain check would reject
                # that mismatch, so this must call the private helper directly.
                poly_fine = self._lin_hom_as_dict(eps, eps, M)
                records.append((M, poly_fine, eps))

            summary: Dict[int, List[Tuple[Dict[int, int], 'Augmentation']]] = {}
            for m in sorted({M for M, _, _ in records}):
                chosen: Dict[frozenset, Tuple[Dict[int, int], 'Augmentation']] = {}
                finer: set = set()
                for M, poly, eps in records:
                    if not _lch_divides(m, M):
                        continue
                    q = _lch_coarsen(poly, m)
                    key = frozenset(q.items())
                    chosen.setdefault(key, (q, eps))
                    if M != m:
                        finer.add(key)
                primitive = [chosen[k] for k in chosen if k not in finer]
                if primitive:
                    primitive.sort(key=lambda pr: sorted(pr[0].items()))
                    summary[m] = primitive
            self._lin_hom_summary_cache = summary
        if format:
            return {m: [_format_poincare(poly) for poly, _ in pairs]
                    for m, pairs in self._lin_hom_summary_cache.items()}
        return self._lin_hom_summary_cache

    def all_lin_hom(self, grading_mod: int = 0, as_str: bool = False,
                    max_search: Optional[int] = _USE_DEFAULT_AUG_LIMIT):
        """
        Set of distinct Poincaré-Chekanov polynomials over all augmentations.
        Cached per grading_mod.  Not supported for Z[λ].
        Returns List[Dict[int,int]], or List[str] if as_str=True.

        max_search: forwarded to augmentations() (see its docstring) when the
        underlying augmentation set has to be computed -- pass max_search=None to
        push through DEFAULT_AUG_SEARCH_LIMIT on a large search space.  Because
        the result is cached per grading_mod (and is max_search-independent), this
        only affects the first computation for a given grading_mod.
        """
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError('all_lin_hom not implemented over Z[λ]')
        if grading_mod not in self._lin_hom_cache:
            if self._lin_hom_summary_cache is not None:
                rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
                if not all(_divisible(grading_mod, 2 * r) for r in rots):
                    raise ValueError(
                        f"grading_mod={grading_mod} is out of domain for this diagram; "
                        f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
                    )
                seen: set = set()
                results: List[Tuple[Dict[int, int], 'Augmentation']] = []
                for M, prims in self._lin_hom_summary_cache.items():
                    if not _lch_divides(grading_mod, M):
                        continue
                    for poly, rep in prims:
                        q = _lch_coarsen(poly, grading_mod)
                        key = frozenset(q.items())
                        if key not in seen:
                            seen.add(key)
                            results.append((q, rep))
                results.sort(key=lambda pair: sorted(pair[0].items()))
                self._lin_hom_cache[grading_mod] = results
            else:
                augms = self.augmentations(grading_mod=grading_mod, max_search=max_search)
                seen2, results2 = set(), []
                for augm_obj in augms:
                    poly = self.lin_hom(augm_obj, grading_mod=grading_mod)
                    key = frozenset(poly.items())
                    if key not in seen2:
                        seen2.add(key)
                        results2.append((poly, augm_obj))
                results2.sort(key=lambda pair: sorted(pair[0].items()))
                self._lin_hom_cache[grading_mod] = results2
        pairs = self._lin_hom_cache[grading_mod]
        if as_str:
            return [_format_poincare(poly) for poly, _ in pairs]
        return [poly for poly, _ in pairs]

    def lin_hom_reps(self, grading_mod: int = 0) -> List[Tuple[Dict[int, int], 'Augmentation']]:
        """
        Returns (poly, representative_augmentation) pairs — one per distinct
        Poincaré-Chekanov polynomial.  Not supported for Z[λ].
        """
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError('lin_hom_reps not implemented over Z[λ]')
        self.all_lin_hom(grading_mod=grading_mod)
        return list(self._lin_hom_cache[grading_mod])

    def lin_hom(
        self,
        aug0: 'Augmentation',
        aug1: Optional['Augmentation'] = None,
        grading_mod: int = 0,
        as_str: bool = False,
    ) -> Union[Dict[int, int], str]:
        """
        Poincaré-Chekanov polynomial for aug0 (aug1 omitted -- the diagonal,
        single-augmentation linearized polynomial) or for the ordered pair
        (aug0, aug1) (bilinearized, Bourgeois-Chantraine) when aug1 is given.

        aug0, aug1 must both be grading_mod-graded augmentations of this DGA
        (e.g. drawn from self.augmentations(grading_mod=grading_mod)). The
        noncommutative word format keeps each basepoint letter's position, so
        the aug0/aug1 split is well-defined regardless of whether
        aug0(t_c) == aug1(t_c) -- no agree-on-λ requirement.

        Computes a single pair directly (no all-pairs enumeration); for k
        augmentations an O(k²) sweep is left to a future homotopy-class
        bucketing pass. Not supported over Z[λ] (augmentations aren't computed
        there).
        """
        if aug1 is None:
            aug1 = aug0
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError('lin_hom is not computed directly over Z[λ].')
        if aug0.dga is not self or aug1.dga is not self:
            raise ValueError('aug0 and aug1 must be augmentations of this DGA')
        if aug0.grading_mod != grading_mod or aug1.grading_mod != grading_mod:
            raise ValueError(
                f'aug0 and aug1 must both be grading_mod={grading_mod}-graded '
                f'(got aug0.grading_mod={aug0.grading_mod}, aug1.grading_mod={aug1.grading_mod})'
            )
        _rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
        if not all(_divisible(grading_mod, 2 * r) for r in _rots):
            raise ValueError(
                f"grading_mod={grading_mod} is out of domain for this diagram; "
                f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
            )
        poly = self._lin_hom_as_dict(aug0, aug1, grading_mod)
        return _format_poincare(poly) if as_str else poly

    def aug_homotopic(self, aug0: 'Augmentation', aug1: 'Augmentation', grading_mod: int = 0) -> bool:
        """
        True iff aug0 and aug1 are DGA homotopic: there is a degree +1
        (aug0,aug1)-derivation K with aug0 - aug1 = K o d (cf. [NRSSZ,
        Augmentations are Sheaves, Section 5.3.2 "DGA homotopy"]). For a knot
        with a single basepoint this is equivalent to aug0, aug1 being
        isomorphic in NRSSZ's augmentation category Aug(Λ) (their Prop.
        "prop:Homotopy"); for links this is DGA homotopy on its own terms, with
        no further claim made here.

        aug0, aug1 must both be grading_mod-graded augmentations of this DGA.
        Z/2 and prime Z/p; not Z[λ] or composite Z/n (the solvability test
        requires a field).
        """
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError('aug_homotopic is not computed directly over Z[λ].')
        if aug0.dga is not self or aug1.dga is not self:
            raise ValueError('aug0 and aug1 must be augmentations of this DGA')
        if aug0.grading_mod != grading_mod or aug1.grading_mod != grading_mod:
            raise ValueError(
                f'aug0 and aug1 must both be grading_mod={grading_mod}-graded '
                f'(got aug0.grading_mod={aug0.grading_mod}, aug1.grading_mod={aug1.grading_mod})'
            )
        _rots = self.rot if isinstance(self.rot, tuple) else (self.rot,)
        if not all(_divisible(grading_mod, 2 * r) for r in _rots):
            raise ValueError(
                f"grading_mod={grading_mod} is out of domain for this diagram; "
                f"requires grading_mod | 2*rot_c for each component (rot={self.rot})"
            )
        if self.ring != GroundRing.Z2 and not _is_prime(self.ring.modulus):
            raise NotImplementedError(
                f'aug_homotopic requires a field coefficient ring; '
                f'Z/{self.ring.modulus} is not a field (n must be prime).'
            )

        gr = self.gradings

        def is_grade(x: int, d: int) -> bool:
            return x == d if grading_mod == 0 else x % grading_mod == d % grading_mod

        g0 = [i + 1 for i, x in enumerate(gr) if is_grade(x, 0)]
        g_minus1 = [i + 1 for i, x in enumerate(gr) if is_grade(x, -1)]

        if self.ring == GroundRing.Z2:
            aug0_dict, aug1_dict = self._z2_aug_dict(aug0.data), self._z2_aug_dict(aug1.data)
            p = 2
        else:
            aug0_dict, aug1_dict = aug0.data, aug1.data
            p = self.ring.modulus
            # Basepoint agreement (Z/2's normalized dict always agrees, since
            # every component is forced to the ring's only unit).
            for c in range(self.num_components):
                if aug0_dict[('lambda', c)] != aug1_dict[('lambda', c)]:
                    return False

        b = [(aug0_dict.get(j, 0) - aug1_dict.get(j, 0)) % p for j in g0]
        if not g_minus1:
            return not any(b)
        mat = _homotopy_mat_zp(g0, g_minus1, self.differential, gr, aug0_dict, aug1_dict, p)
        # mat[c-index][j-index]: rows = G_{-1} (unknowns), columns = G_0
        # (equations) -- the _bilin_diff_mat_zp(domain,rng,...) convention's
        # transpose of the usual layout, so the augmented system appends b as
        # an extra row.
        augmented = mat + [b]
        return _rank_zn(mat, p) == _rank_zn(augmented, p)

    def aug_homotopy_classes(
        self,
        grading_mod: int = 0,
        max_search: Optional[int] = _USE_DEFAULT_AUG_LIMIT,
    ) -> List[List['Augmentation']]:
        """
        Partition augmentations(grading_mod) into DGA-homotopy classes (cf.
        [NRSSZ, Augmentations are Sheaves, Section 5.3.2]) via pairwise
        aug_homotopic tests, unioned by a union-find structure. Not over Z[λ].

        max_search: upper bound on the number of pairwise solvability tests
        (k*(k-1)/2 for k augmentations) attempted; raises AugSearchLimitError
        before doing the work if exceeded, mirroring augmentations()'s own
        guard. When omitted, resolves to DEFAULT_AUG_SEARCH_LIMIT at call time.
        Pass max_search=None to disable the check.
        """
        if max_search is _USE_DEFAULT_AUG_LIMIT:
            max_search = DEFAULT_AUG_SEARCH_LIMIT
        augs = self.augmentations(grading_mod=grading_mod)
        k = len(augs)
        pair_count = k * (k - 1) // 2
        if max_search is not None and pair_count > max_search:
            raise AugSearchLimitError(
                f"aug_homotopy_classes pairwise binning over {k} augmentations is "
                f"{pair_count:,} solvability tests, which exceeds "
                f"max_search={max_search:,}. Pass max_search=None to disable."
            )
        # Classify by testing each augmentation against one representative per
        # existing class, not against every other augmentation. aug_homotopic is
        # an equivalence relation (transitive -- see test_equivalence_relation),
        # so a match against a class's representative places the augmentation in
        # that class. This is O(k * #classes) solvability tests rather than the
        # O(k^2) of the all-pairs union-find it replaces, whose find()-based
        # short-circuit only skipped *within*-class pairs -- every cross-class
        # pair still ran a (failing) aug_homotopic test. For mK3_1 gm=1 that is
        # ~810*30 vs ~810^2/2, a >10x drop in solvability tests.
        classes: List[List['Augmentation']] = []
        for aug in augs:
            for cls in classes:
                if self.aug_homotopic(aug, cls[0], grading_mod):
                    cls.append(aug)
                    break
            else:
                classes.append([aug])
        return classes

    def aug_count(self, grading_mod: int = 0) -> float:
        """
        Normalized graded augmentation number (Ng-Sabloff normalization).
        |ring|^(−χ*_ρ/2) × |Aug_ρ|, where ρ = grading_mod.

        grading_mod=0 (Z-graded): χ*_0 = Σ_{k≥0}(-1)^k a_k + Σ_{k<0}(-1)^{k+1} a_k,
            with an additional −1 shift so the exponent is (−1−χ*_0)/2.
        grading_mod=ρ odd: χ*_ρ = Σ_{k=0}^{ρ-1} (-1)^k a_k (a_k = #generators of degree k mod ρ).
        grading_mod=ρ even, ρ>0: raises NotImplementedError (no well-defined invariant).
        Not supported for Z[λ].
        """
        if self.ring == GroundRing.ZLAMBDA:
            raise NotImplementedError('aug_count not defined over Z[λ]')
        if grading_mod > 0 and grading_mod % 2 == 0:
            raise NotImplementedError(
                f'aug_count not defined for even grading_mod={grading_mod}'
            )
        n = self.ring.modulus
        n_aug = len(self.augmentations(grading_mod=grading_mod))
        gr = self.gradings
        if grading_mod == 0:
            min_g, max_g = min(gr), max(gr)
            chi = sum(((-1) ** k) * gr.count(k) for k in range(0, max_g + 1))
            chi += sum(((-1) ** (k + 1)) * gr.count(k) for k in range(min_g, 0))
            exp = (-1 - chi) / 2
        else:
            rho = grading_mod
            chi = sum(((-1) ** k) * sum(1 for g in gr if g % rho == k) for k in range(rho))
            exp = -chi / 2
        return (n ** int(exp)) * n_aug if exp == int(exp) else (n ** exp) * n_aug

    def _gen_label(self, g: int) -> str:
        """Display label for 1-indexed generator g: its name if set, else a[g]."""
        return self.names[g - 1] if self.names is not None else f'a[{g}]'

    def print_differential(self) -> None:
        """Print d(<gen>) for each generator in human-readable form.

        Generators are labelled by self.names when set (e.g. simplify() carries
        through the original generator labels), otherwise as a[i].
        """
        def format_letter(letter) -> str:
            # Chord: its generator label. Basepoint power ('lambda', c, k): λ_{c+1}
            # (1-indexed component), e.g. λ_1^2, λ_2⁻¹.
            if isinstance(letter, int):
                return self._gen_label(letter)
            _, c, k = letter
            if k == 1:
                return f"λ_{c + 1}"
            if k == -1:
                return f"λ_{c + 1}⁻¹"
            return f"λ_{c + 1}^{k}"

        def format_word(word) -> str:
            return " * ".join(format_letter(g) for g in word) if word else "1"

        if self.ring == GroundRing.ZLAMBDA:
            for i, poly_dict in enumerate(self.differential):
                if not poly_dict:
                    entry = "0"
                else:
                    terms = []
                    for word, coeff in poly_dict.items():
                        if coeff == 0:
                            continue
                        body = format_word(word)
                        s = (body if coeff == 1 else f"-{body}" if coeff == -1
                             else f"{coeff}*{body}")
                        terms.append(s)
                    entry = " + ".join(terms) if terms else "0"
                print(f'  d({self._gen_label(i + 1)}) = {entry}')
        else:
            # Z/n (including Z/2): same dict format as ZLAMBDA; coefficients
            # are non-negative mod n (for Z/2 always 0 or 1)
            for i, poly_dict in enumerate(self.differential):
                if not poly_dict:
                    entry = "0"
                else:
                    terms = []
                    for word, coeff in poly_dict.items():
                        if coeff == 0:
                            continue
                        body = format_word(word)
                        s = body if coeff == 1 else f"{coeff}*{body}"
                        terms.append(s)
                    entry = " + ".join(terms) if terms else "0"
                print(f'  d({self._gen_label(i + 1)}) = {entry}')

    def simplify(self, verbose: bool = False) -> 'DGA':
        """
        Simplify this DGA by algebraic handle cancellation (stable tame equivalence).

        Repeatedly finds a generator x with no constant term in d(x), and a
        generator y occurring in d(x) in exactly one monomial -- namely (y,)
        with a unit coefficient c*lambda^e -- then eliminates the pair (x, y)
        via the algebra map x -> 0, y -> Y := -(c*lambda^e)^-1 * (d(x) - c*lambda^e*y),
        other generators fixed. Stops when no such pivot remains.

        Strictly non-mutating: never edits self.differential/self.gradings, since
        Leg.dga(ring) caches and shares the geometric DGA across callers. Returns
        a new, Leg-less DGA (DGA.abstract(...)) -- the existing augmentations,
        all_lin_hom, lin_hom_summary, aug_count, check_d_squared all work on it
        directly.

        Generator labels carry through: a surviving generator keeps the label it
        had here (self.names, or a[i] by the original numbering when unnamed), so
        print_differential on the result refers back to the original generators.

        The result also records the destabilization projection π back to self,
        so an augmentation of the (smaller) result can be pulled back to one of
        self via result.pullback_augmentation(...).
        """
        base_names = (self.names if self.names is not None
                      else [f'a[{i + 1}]' for i in range(len(self.gradings))])
        new_gradings, new_diff, new_names, remap, proj = _simplify_dict_diff(
            self.differential, self.gradings, self.ring, base_names, verbose=verbose)
        result = DGA.abstract(
            gradings=new_gradings,
            differential=new_diff,
            ring=self.ring,
            rot=self.rot,
            num_components=self.num_components,
            names=new_names,
        )
        result._simplify_source = self
        result._simplify_survivor_map = remap
        result._simplify_proj = proj
        return result

    def pullback_augmentation(self, aug: 'Augmentation') -> 'Augmentation':
        """Pull an augmentation of this simplified DGA back to its source.

        self must be the output of source.simplify().  Given an augmentation ε
        of self (call it B), returns ε∘π, the corresponding augmentation of the
        source DGA (call it A), where π: A → B is the destabilization projection
        recorded by simplify().  Concretely, a surviving generator inherits ε's
        value, while a cancelled generator y is sent to ε(Y) for the image Y that
        simplify() substituted for it (and the partner x to 0); these values are
        exactly the ones forced on A by the augmentation equation ε∘∂_A = 0.

        The map is injective, with inverse (on its image) = restriction to the
        surviving generators.  It is *not* onto in general: each cancelled pair
        whose removed source generator x has degree 0 contributes a free choice
        of ε(x) ∈ ground-ring that pullback always sets to 0, so
        |Aug(A)| = |Aug(B)| · |ring|^(# such pairs).  Existence is preserved,
        though -- Aug(B) is nonempty iff Aug(A) is -- so this is exactly what you
        want to find (or rule out) an augmentation on the smaller B and transport
        it back to A.
        """
        source = self._simplify_source
        if source is None:
            raise ValueError(
                'pullback_augmentation requires a DGA produced by simplify(); '
                'this DGA records no projection.'
            )
        if aug.dga is not self:
            raise ValueError('augmentation does not belong to this DGA')
        survivor_map = cast(Dict[int, int], self._simplify_survivor_map)
        proj = cast(Dict[int, Any], self._simplify_proj)
        gr = source.gradings
        gm = aug.grading_mod

        def is_grade0(x: int) -> bool:
            return x == 0 if gm == 0 else x % gm == 0

        if self.ring == GroundRing.Z2:
            eps = set(aug.data)  # B generators sent to 1
            src_data = []
            for g in range(1, len(gr) + 1):
                if not is_grade0(gr[g - 1]):
                    continue
                if g in survivor_map:
                    val = 1 if survivor_map[g] in eps else 0
                else:
                    val = 0
                    for word in proj[g]:
                        if all(b in eps for b in word):
                            val ^= 1
                if val:
                    src_data.append(g)
            return Augmentation(sorted(src_data), source, gm)

        if self.ring == GroundRing.ZLAMBDA:
            aug_dict = aug.data  # dict over B generators (int) and ('lambda', c) units (+-1)
            src_data = {k: v for k, v in aug_dict.items() if isinstance(k, tuple)}
            for g in range(1, len(gr) + 1):
                if not is_grade0(gr[g - 1]):
                    continue
                if g in survivor_map:
                    src_data[g] = aug_dict.get(survivor_map[g], 0)
                else:
                    val = 0
                    for word, coeff in proj[g].items():
                        term = coeff
                        for letter in word:
                            term *= _eval_letter_z(letter, aug_dict)
                        val += term
                    src_data[g] = val
            return Augmentation(src_data, source, gm)

        n = self.ring.modulus
        aug_dict = aug.data  # dict over B generators and ('lambda', c) units
        # λ-values are basepoint data, untouched by simplify -- copy them through.
        src_data = {k: v for k, v in aug_dict.items() if isinstance(k, tuple)}
        for g in range(1, len(gr) + 1):
            if not is_grade0(gr[g - 1]):
                continue
            if g in survivor_map:
                src_data[g] = aug_dict.get(survivor_map[g], 0)
            else:
                val = 0
                for word, coeff in proj[g].items():
                    term = coeff % n
                    for letter in word:
                        term = (term * _eval_letter(letter, aug_dict, n)) % n
                    val = (val + term) % n
                src_data[g] = val
        return Augmentation(src_data, source, gm)

    def z_augmentations(
        self,
        lo: int,
        hi: int,
        grading_mod: int = 0,
        max_search: Optional[int] = _USE_DEFAULT_AUG_LIMIT,
    ) -> List['Augmentation']:
        """
        The pullback to self of every Z-valued augmentation of self.simplify()
        whose grade-0 generators each take a value in [lo, hi] (inclusive; λ is
        unconstrained by this range, always forced to -1 per the same knot
        convention DGA.augmentations() uses). Knots only
        (self.num_components == 1); self.ring must be GroundRing.ZLAMBDA.

        NOTE this is *not* every Z-augmentation of self in that range. Searching
        the simplified DGA is a large speedup (the cost is
        generator-count-sensitive), but simplify()'s projection pulls back
        injectively, not onto (see pullback_augmentation): a Z-augmentation of
        self that assigns a nonzero value to a generator simplify() cancels does
        not factor through the simplified DGA and is not returned. The [lo, hi]
        bound is on the simplified DGA's generators, so a returned augmentation
        may take a value outside [lo, hi] on a cancelled generator of self.

        Implementation note, not part of the contract (may change): finds every
        Z/p-augmentation of self.simplify() for a set of small primes whose
        product exceeds hi - lo + 1, combines each tuple via the Chinese
        Remainder Theorem into the unique integer in [lo, hi] consistent with it
        (discarding tuples with no representative in that window), then verifies
        each candidate directly. Within that scope it is complete -- it finds
        every range-bounded Z-augmentation of self.simplify() (pulled back), not
        a heuristic subset of those -- but a cleverer search strategy may replace
        it later.

        max_search: upper bound on the total candidate count (the product of
        per-prime augmentation counts); raises AugSearchLimitError before the
        combinatorial work if exceeded (each per-prime augmentations() call
        has its own such guard too). When omitted, resolves to
        DEFAULT_AUG_SEARCH_LIMIT. Pass max_search=None to disable.
        """
        if max_search is _USE_DEFAULT_AUG_LIMIT:
            max_search = DEFAULT_AUG_SEARCH_LIMIT
        if self.ring != GroundRing.ZLAMBDA:
            raise ValueError(
                'z_augmentations requires self.ring == GroundRing.ZLAMBDA'
            )
        if self.num_components != 1:
            raise NotImplementedError(
                'z_augmentations only supports knots (num_components == 1) for now'
            )
        if lo > hi:
            raise ValueError(f'lo={lo} must be <= hi={hi}')

        s = self.simplify()
        window = hi - lo + 1

        primes: List[int] = []
        M = 1
        candidate = 2
        while M < window:
            if _is_prime(candidate):
                primes.append(candidate)
                M *= candidate
            candidate += 1

        aug_lists = []
        for p in primes:
            pdga = DGA.abstract(
                gradings=s.gradings, differential=s.differential,
                ring=GroundRing.Zn(p), rot=s.rot, num_components=1,
            )
            aug_lists.append(pdga.augmentations(grading_mod=grading_mod, max_search=max_search))

        search_size = 1
        for al in aug_lists:
            search_size *= len(al)
        if max_search is not None and search_size > max_search:
            raise AugSearchLimitError(
                f"z_augmentations candidate search space (product of per-prime "
                f"augmentation counts) is {search_size:,}, which exceeds "
                f"max_search={max_search:,}. Pass max_search=None to disable."
            )

        def as_dict(aug: 'Augmentation') -> dict:
            if isinstance(aug.data, list):
                d: dict = {g: 1 for g in aug.data}
                d[('lambda', 0)] = 1
                return d
            return aug.data

        def crt_lift(residues: List[Tuple[int, int]]) -> Optional[int]:
            """Unique integer in [lo, lo + M) matching every (residue, prime)
            pair, or None if it falls outside [lo, hi]."""
            x = 0
            for r, p in residues:
                Mi = M // p
                x += r * Mi * pow(Mi, -1, p)
            x = lo + ((x - lo) % M)
            return x if x <= hi else None

        n_gens = len(s.gradings)
        found = []
        for combo in product(*aug_lists):
            combo_d = [as_dict(a) for a in combo]
            data: dict = {}
            in_range = True
            for gen in range(1, n_gens + 1):
                x = crt_lift([(combo_d[i].get(gen, 0), primes[i]) for i in range(len(primes))])
                if x is None:
                    in_range = False
                    break
                if x != 0:
                    data[gen] = x
            if not in_range:
                continue
            data[('lambda', 0)] = -1
            if _is_z_augmentation(s, data, grading_mod) is None:
                found.append(Augmentation(data, s, grading_mod))

        return [s.pullback_augmentation(a) for a in found]


# ============================================================
# Section 5: Augmentation
# ============================================================

class Augmentation:
    """
    A single augmentation ε: (DGA generators) → (ground ring).

    Obtained via DGA.augmentations() or Leg.augmentations().

    Attributes
    ----------
    data    augmentation data:
              Z/2 : List[int]           generators sent to 1 (others → 0)
              Z/p : Dict[int|tuple,int] generator → value; also ('lambda', c) → unit value
    dga     the parent DGA

    Properties / methods
    --------------------
    lin_hom                Dict[int, int]  Poincaré-Chekanov polynomial (cached)
    cohomology_basis(other=None)
                            basis for (bilinearized, if other given) cohomology;
                            Z/2 and prime Z/p
    bilin_hom_z(other=None)
                            free ranks/torsion of (bilinearized, if other given)
                            homology over Z; self.dga must be Z[λ]
    bilin_hom_z_gens(other=None)
                            generating set (with orders) for the above
    double_products(return_dual_basis=False)
                            (Z/2 only) cup-product table; see method docstring
    """

    def __init__(self, data, dga: DGA, grading_mod: int = 0) -> None:
        self.data = data
        self.dga = dga
        self.grading_mod = grading_mod

    def __repr__(self) -> str:
        if isinstance(self.data, dict):
            gen_data = {k: v for k, v in self.data.items() if isinstance(k, int)}
            lam_data = {k: v for k, v in self.data.items() if isinstance(k, tuple)}
            parts = [f'ring={self.dga.ring!r}', f'grading_mod={self.grading_mod!r}',
                     f'gens={gen_data!r}']
            if lam_data:
                parts.append(f'lambdas={lam_data!r}')
            return f'Augmentation({", ".join(parts)})'
        return f'Augmentation({self.data!r}, ring={self.dga.ring!r}, grading_mod={self.grading_mod!r})'

    @cached_property
    def lin_hom(self) -> Dict[int, int]:
        """
        Poincaré-Chekanov polynomial of linearized contact homology w.r.t. this
        ε -- the diagonal only. See DGA.lin_hom(aug0, aug1) for the
        bilinearized polynomial of an ordered pair of (possibly different)
        augmentations; that's not offered as a method here since, unlike this
        diagonal value, it isn't symmetric in the two augmentations.
        Returns {grading: dimension} (zero dimensions omitted).
        """
        return self.dga.lin_hom(self, grading_mod=self.grading_mod)

    def format_poincare(self) -> str:
        """Format self.lin_hom as a Poincaré polynomial string in t."""
        return _format_poincare(self.lin_hom)

    def cohomology_basis(self, other: Optional['Augmentation'] = None):
        """
        Basis for the (bilinearized, if other is given) linearized cohomology
        of the ordered pair (self, other). other=None (default) is the
        diagonal other=self, recovering the original single-augmentation
        cohomology. Z/2 and prime Z/p; not Z[λ] or composite Z/n (homology
        dimensions require a field).

        Not cached (recomputed on every call) -- matches DGA.bilin_hom's style.

        Order-sensitive when other is given: this is ker(outgoing)/im(incoming)
        of the bilinearized differential d_{self,other}, the same complex
        DGA.bilin_hom(self, other) computes the dimensions of -- unlike those
        dimensions (which satisfy Sabloff/BC duality against the swapped
        pair), the basis itself has no swap symmetry.

        Returns ``List[List[List[Tuple[int, int]]]]``:
          - Outer list: one entry per grading space, ordered highest grade first
            (same order as ``DGA._gens_spaces``).
          - Middle list: basis vectors for the cohomology at that grade.
          - Inner list: the basis vector as ``(generator, coefficient)`` pairs —
            1-indexed generator numbers with their nonzero ``Z/p`` coefficient
            (always ``1`` over Z/2). Zero-coefficient generators are omitted.

        Example: ``[[[(4, 1)]], [[(1, 1), (3, 1)], [(2, 1)]]]`` means the
        highest-grade cohomology is 1-dimensional spanned by ``a_4``, and the
        next grade is 2-dimensional spanned by ``a_1 + a_3`` and ``a_2``. Over
        Z/3 a vector like ``[(1, 2), (2, 1)]`` denotes ``2·a_1 + a_2``.
        """
        if other is None:
            other = self
        elif other.dga is not self.dga:
            raise ValueError('other must be an augmentation of the same DGA')
        ring = self.dga.ring
        if ring == GroundRing.ZLAMBDA:
            raise NotImplementedError('cohomology_basis not implemented over Z[λ]')
        if ring != GroundRing.Z2 and not _is_prime(ring.modulus):
            raise NotImplementedError(
                f'cohomology_basis requires a field coefficient ring; '
                f'Z/{ring.modulus} is not a field (n must be prime).'
            )

        gs = self.dga._gens_spaces
        n_spaces = len(gs)
        result = []

        if ring == GroundRing.Z2:
            p = 2
            self_dict, other_dict = self.dga._z2_aug_dict(self.data), self.dga._z2_aug_dict(other.data)
        else:
            p = ring.modulus
            self_dict, other_dict = self.data, other.data
        zn_d = self.dga.differential
        for k in range(1, n_spaces + 1):
            space = gs[k - 1]
            if not space:
                result.append([])
                continue
            # Kernel of outgoing differential
            if k == n_spaces or not gs[k]:
                ker_basis = [[1 if i == j else 0 for j in range(len(space))]
                             for i in range(len(space))]
            else:
                mat_k = _bilin_diff_mat_zp(space, gs[k], zn_d, self_dict, other_dict, p)
                if mat_k and mat_k[0]:
                    ker_basis = _null_space_zn(mat_k, p)
                else:
                    ker_basis = [[1 if i == j else 0 for j in range(len(space))]
                                 for i in range(len(space))]
            # Image of incoming differential (columns of mat_{k-1})
            if k == 1 or not gs[k - 2]:
                im_vecs = []
            else:
                mat_in = _bilin_diff_mat_zp(gs[k - 2], space, zn_d, self_dict, other_dict, p)
                if mat_in and mat_in[0]:
                    n_cols = len(mat_in[0])
                    im_vecs = [[mat_in[r][c] for r in range(len(mat_in))]
                               for c in range(n_cols)]
                else:
                    im_vecs = []
            # Homology = ker / im
            hom_vecs = _quotient_basis_zn(ker_basis, im_vecs, len(space), p)
            cohom = [[(space[i], v) for i, v in enumerate(vec) if v] for vec in hom_vecs]
            result.append([c for c in cohom if c])
        return result

    def bilin_hom_z(self, other: Optional['Augmentation'] = None):
        """
        Free ranks and torsion of the (bilinearized, if other is given)
        contact homology over Z of the ordered pair (self, other). other=None
        (default) is the diagonal other=self. self.dga must be a Z[λ] DGA
        (self and other are Z-valued augmentations, per DGA.bilin_hom_z).
        Delegates to self.dga.bilin_hom_z(self, other, grading_mod=self.grading_mod);
        see its docstring for validation, guards, and the return format.
        """
        return self.dga.bilin_hom_z(self, other, grading_mod=self.grading_mod)

    def bilin_hom_z_gens(self, other: Optional['Augmentation'] = None):
        """
        Generating set (with orders) for the (bilinearized, if other is
        given) contact homology over Z of the ordered pair (self, other).
        other=None (default) is the diagonal other=self. Delegates to
        self.dga.bilin_hom_z_gens(self, other, grading_mod=self.grading_mod);
        see its docstring for validation, guards, and the return format.
        """
        return self.dga.bilin_hom_z_gens(self, other, grading_mod=self.grading_mod)

    @overload
    def double_products(self, return_dual_basis: Literal[False] = ...) -> Tuple[List[List[Union[List[int], str]]], List[List[int]]]: ...
    @overload
    def double_products(self, return_dual_basis: Literal[True]) -> Tuple[List[List[Union[List[int], str]]], List[List[int]], List[List[int]]]: ...

    def double_products(self, return_dual_basis: bool = False):
        """Cup-product table on linearized cohomology (Z/2 only). See [CEKSW11].

        Returns ``(table, co_basis)`` where ``co_basis`` is a flat list of cohomology basis
        vectors (1-indexed generator lists, highest grade first, matching ``cohomology_basis``)
        and ``table[j][k]`` is the product of ``co_basis[j]`` and ``co_basis[k]``: either
        ``'.'`` (zero) or a list of 0-indexed positions into ``co_basis`` whose F_2 sum equals
        the product class.  Degree convention: |m₂(α,β)| = |α| + |β| + 1.

        If ``return_dual_basis=True``, also returns ``dual_co_basis`` — the list of
        cochain-cocycle representatives (Kronecker-dual to ``co_basis``) used as m₂ inputs.
        These satisfy d₁ᵀ = 0; using chain-cycle reps instead would give wrong products.
        """
        if hasattr(self, '_double_products_cache'):
            table, co_basis, dual_co_basis = self._double_products_cache
            return (table, co_basis, dual_co_basis) if return_dual_basis else (table, co_basis)
        if self.dga.ring != GroundRing.Z2:
            raise NotImplementedError(
                'double_products is only implemented over Z/2'
            )
        double_diff = self.dga._twisted_diff_f2(self, 2)
        ld = self.dga._bilin_diff_f2(self, self)
        gs = self.dga._gens_spaces
        n_spaces = len(gs)

        # co_basis: chain-cycle representatives (for decode and return value).
        # cohomology_basis returns (gen, coeff) pairs; over Z/2 coeff is always 1,
        # so we keep only the generator supports here.
        cohomology_basis = [[[g for g, _ in vec] for vec in space]
                            for space in self.cohomology_basis()]
        co_basis = [gen for space in cohomology_basis for gen in space]
        co_basis_sets = [set(cb) for cb in co_basis]

        # dual_co_basis: cochain-cocycle representatives, Kronecker-dual to co_basis.
        # The m2 formula is the adjoint of d2 and requires cochain-cocycle inputs;
        # chain-cycle reps that are not cochain-cocycles give wrong products.
        dual_co_basis: List[List[int]] = []
        for k in range(1, n_spaces + 1):
            space = gs[k - 1]
            space_chain_cycles = cohomology_basis[k - 1]
            if not space or not space_chain_cycles:
                continue
            n_k = len(space)
            gen_to_idx = {g: i for i, g in enumerate(space)}
            # ker(d1^T: space → gs[k-2]) = null space of (d1: gs[k-2] → space)^T
            if k == 1 or not gs[k - 2]:
                cocycle_ker: List[List[int]] = [
                    [1 if i == j else 0 for j in range(n_k)] for i in range(n_k)
                ]
            else:
                mat_in = self.dga._diff_matrix_f2(k - 1, ld)  # gs[k-2] → space
                if mat_in and mat_in[0]:
                    n_prev = len(mat_in[0])
                    mat_in_T = [[mat_in[j][i] for j in range(n_k)]
                                for i in range(n_prev)]
                    cocycle_ker = _null_space_f2(mat_in_T) or [
                        [1 if i == j else 0 for j in range(n_k)] for i in range(n_k)
                    ]
                else:
                    cocycle_ker = [
                        [1 if i == j else 0 for j in range(n_k)] for i in range(n_k)
                    ]
            chain_sets = [frozenset(gen_to_idx[g] for g in cc) for cc in space_chain_cycles]
            dual_vecs = _dual_cocycle_basis_f2(cocycle_ker, chain_sets, n_k)
            for dv in dual_vecs:
                dual_co_basis.append([space[i] for i in range(n_k) if dv[i]])

        # Precompute: ordered pair (a,b) → generators whose d2 contains (a,b).
        # DGA.differential's word order is the reverse of the m2 formula's
        # left-to-right product convention (see check_d_squared's
        # suffix-graded sign -- the internal word order is consistently the
        # opposite-algebra one), so a 2-letter monomial (x, y) here encodes
        # the pair (y, x) for m2 purposes.
        pair_to_gens: Dict[tuple, List[int]] = {}
        for i, poly in enumerate(double_diff):
            for m in poly:
                if len(m) == 2:
                    pair_to_gens.setdefault((m[1], m[0]), []).append(i + 1)

        def decode_product(result_gens):
            """Decode m2 output via Kronecker pairing with the chain-cycle co_basis.

            <psi, c_j> = sum_{g in c_j} psi(g) mod 2 is well-defined on cohomology
            because d1(c_j) = 0, so adding a coboundary to psi does not change the
            pairing.
            """
            if not result_gens:
                return '.'
            result_set = set(result_gens)
            coords = [j for j, cb_set in enumerate(co_basis_sets)
                      if sum(1 for g in cb_set if g in result_set) % 2]
            return coords if coords else '.'

        def multiply_once(first, second):
            count = Counter()
            for a_gen in first:
                for b_gen in second:
                    for gen in pair_to_gens.get((a_gen, b_gen), []):
                        count[gen] += 1
            result_gens = [g for g, c in count.items() if c % 2 == 1]
            return decode_product(result_gens)

        n = len(co_basis)
        table = [[multiply_once(dual_co_basis[j], dual_co_basis[k])
                  for k in range(n)]
                 for j in range(n)]
        self._double_products_cache = (table, co_basis, dual_co_basis)
        return (table, co_basis, dual_co_basis) if return_dual_basis else (table, co_basis)


# ============================================================
# Section 6: Atlas
# ============================================================
# Keys follow the naming convention described in the module docstring.
# Values are lists of braid words, one per Legendrian isotopy class (0-indexed).
# Data from the Legendrian knot atlas (https://sites.math.duke.edu/~ng/atlas/).

ATLAS: Dict[str, List[List[int]]] = {
    'mK3_1': [[2, 3, 1, 3, 1, 3, 2]],
    'K4_1': [[2, 3, 1, 3, 1, 2, 2]],
    'mK5_1': [[2, 3, 1, 1, 3, 1, 1, 3, 2]],
    'mK5_2': [
        [2, 3, 1, 3, 4, 5, 1, 2, 3, 4, 2, 4],
        [2, 3, 1, 3, 1, 2, 2, 3, 1, 3, 2],
    ],
    'K6_1': [[2, 3, 1, 1, 3, 1, 1, 2, 2]],
    'mK6_1': [
        [4, 5, 3, 5, 6, 7, 3, 4, 2, 1, 3, 2, 5, 6, 2, 4, 6],
        [2, 3, 1, 3, 1, 2, 2, 1, 3, 2, 2],
    ],
    'K6_2': [
        [2, 1, 1, 3, 2, 2, 1, 3, 1, 2, 2],
        [4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 1, 7, 6, 5, 4, 3, 9, 3, 2, 1, 5, 7, 2, 3, 7,
         6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8,
         7, 6, 7, 8],
        [6, 5, 5, 4, 3, 2, 1, 7, 6, 6, 5, 4, 3, 2, 2, 4, 6],
    ],
    'mK6_2': [[4, 5, 3, 3, 5, 3, 2, 1, 4, 1, 3, 4, 3, 2]],
    'mK7_1': [[2, 3, 1, 1, 3, 1, 1, 1, 1, 3, 2]],
    'mK7_2': [
        [6, 7, 7, 5, 8, 9, 5, 4, 6, 3, 5, 2, 4, 7, 8, 3, 1, 2, 2, 4, 6, 8],
        [2, 3, 3, 1, 1, 2, 2, 3, 1, 2, 2, 1, 3, 3, 2],
        [4, 5, 5, 3, 4, 6, 7, 2, 3, 1, 5, 6, 2, 4, 5, 3, 5, 6, 3, 4, 2],
        [4, 5, 3, 5, 3, 2, 1, 4, 4, 5, 3, 2, 1, 4, 2, 4, 3, 5, 4, 2],
    ],
    'K7_3': [
        [2, 3, 1, 1, 3, 4, 5, 1, 1, 2, 3, 4, 2, 4],
        [2, 3, 1, 3, 1, 1, 1, 2, 2, 1, 3, 3, 2],
    ],
    'K7_4': [
        [4, 5, 5, 3, 6, 7, 2, 1, 4, 5, 6, 8, 9, 7, 8, 1, 3, 2, 4, 5, 3, 4, 6, 8, 4, 2],
        [6, 7, 7, 5, 6, 6, 5, 4, 3, 2, 1, 7, 5, 3, 1, 7, 6, 5, 4, 1, 2],
        [6, 7, 7, 5, 4, 3, 6, 5, 3, 2, 4, 1, 3, 6, 2, 5, 7, 4, 6, 2, 4, 5, 6, 3, 4],
        [2, 3, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 3, 2],
    ],
    'mK7_5': [
        [4, 5, 3, 5, 3, 6, 3, 7, 2, 1, 4, 5, 6, 1, 3, 4, 6, 3, 2],
        [2, 3, 3, 1, 1, 1, 2, 2, 1, 3, 1, 3, 2],
    ],
    'mK7_6': [
        [4, 5, 3, 5, 3, 2, 1, 4, 1, 3, 4, 1, 2, 4, 3, 5, 4, 2],
        [6, 7, 5, 7, 5, 4, 3, 3, 6, 2, 1, 5, 6, 3, 1, 1, 2, 5, 4],
        [4, 5, 3, 3, 5, 2, 1, 4, 1, 3, 1, 2, 4, 2],
    ],
    'mK7_7': [
        [6, 7, 5, 5, 7, 4, 3, 6, 3, 5, 2, 1, 4, 1, 3, 6, 4, 3, 2],
        [4, 5, 3, 3, 5, 2, 1, 4, 1, 3, 4, 1, 5, 2, 3, 2, 5, 4],
    ],
    'K8_19': [[4, 5, 2, 1, 3, 2, 1, 5, 2, 4, 1, 5, 2, 1, 2, 3, 1, 2, 5, 4]],
    'K8_21': [
        [4, 3, 3, 2, 1, 5, 4, 3, 1, 4, 3, 2, 4, 2],
        [4, 3, 3, 2, 1, 5, 4, 1, 3, 2, 4, 3, 2, 5, 3, 2, 3, 4],
        [4, 3, 8, 7, 6, 5, 4, 3, 3, 2, 1, 7, 4, 6, 9, 1, 3, 7, 4, 5, 7, 6, 5, 4, 3, 2, 1,
         8, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
    ],
    'mK8_21': [[4, 5, 3, 2, 1, 5, 1, 3, 4, 1, 2, 4, 3, 5, 4, 2]],
    'K9_42': [[4, 5, 3, 2, 5, 1, 4, 3, 4, 3, 1, 4, 3, 4, 1, 2]],
    'mK9_42': [[4, 5, 3, 2, 1, 5, 1, 3, 4, 2, 3, 3, 4, 2]],
    'K9_43': [[4, 5, 3, 5, 3, 2, 1, 4, 1, 3, 4, 1, 3, 4, 3, 2]],
    'mK9_44': [[4, 5, 5, 3, 3, 2, 1, 4, 3, 4, 1, 2, 5, 2, 3, 1, 5, 4, 1, 2]],
    'mK9_45': [
        [6, 7, 7, 5, 6, 4, 3, 6, 2, 5, 4, 6, 4, 7, 5, 3, 2, 7, 6, 5, 4],
        [4, 5, 3, 2, 1, 5, 3, 1, 2, 4, 2, 3, 1, 2, 4, 2],
    ],
    'K9_46': [[4, 5, 2, 1, 3, 2, 1, 5, 2, 4, 1, 5, 2, 3, 1, 4, 3, 4, 1, 2]],
    'mK9_46': [[4, 5, 2, 1, 3, 1, 2, 5, 2, 3, 1, 4, 2, 4, 3, 5, 4, 2]],
    'mK9_47': [[6, 7, 4, 3, 5, 3, 2, 4, 3, 1, 7, 2, 2, 6, 4, 2, 1, 3, 6, 5, 1, 2, 4, 7, 6]],
    'K9_48': [
        [6, 7, 5, 7, 4, 3, 2, 1, 6, 5, 3, 6, 1, 3, 4, 2, 3, 5, 4, 1, 2, 6, 4],
        [6, 7, 8, 9, 5, 7, 8, 4, 3, 2, 1, 9, 3, 2, 8, 6, 9, 7, 5, 2, 1, 8, 7, 6, 4,
         8, 7, 3, 5, 6, 9, 8, 1, 2, 5, 4],
        [4, 3, 6, 7, 5, 6, 3, 7, 8, 9, 4, 6, 2, 1, 5, 7, 8, 6, 7, 9, 8, 5, 7, 1, 3,
         8, 1, 2, 7, 6, 5, 4],
        [6, 7, 5, 7, 4, 3, 6, 2, 1, 5, 6, 1, 3, 5, 6, 7, 1, 2, 3, 4, 5, 7, 6],
    ],
    'K9_49': [
        [4, 5, 5, 3, 6, 7, 4, 2, 1, 5, 6, 1, 3, 4, 6, 3, 4, 5, 6, 1, 2, 3, 4, 7, 5, 7, 6],
        [4, 5, 3, 5, 2, 1, 4, 1, 3, 2, 4, 3, 5, 2, 1, 3, 4, 2, 5, 1, 2, 3, 1, 2, 5, 4],
    ],
    'K10_124': [[4, 5, 2, 1, 3, 2, 1, 2, 5, 1, 2, 4, 1, 5, 2, 1, 2, 3, 1, 2, 5, 4]],
    'K10_128': [
        [4, 5, 3, 5, 6, 7, 4, 2, 1, 5, 6, 3, 4, 3, 1, 6, 4, 3, 4, 3, 2],
        [6, 7, 5, 8, 9, 4, 3, 2, 1, 7, 9, 6, 3, 2, 1, 5, 6, 2, 4, 5, 1, 2, 3, 6, 9,
         8, 1, 2, 5, 4],
    ],
    'K10_132': [
        [4, 3, 6, 5, 4, 3, 3, 4, 3, 4, 7, 3, 2, 1, 6, 4, 1, 3, 4, 5, 5, 4, 3, 2, 1, 6, 5,
         4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6],
    ],
    'K10_136': [
        [4, 5, 5, 6, 7, 3, 4, 2, 1, 5, 3, 2, 4, 7, 6, 3, 2, 3, 5, 2, 6, 3, 2, 5, 4],
        [8, 9, 7, 6, 5, 9, 4, 3, 5, 4, 3, 8, 2, 1, 7, 8, 6, 4, 7, 1, 3, 4, 5, 8, 1,
         2, 3, 4, 7, 6],
        [6, 7, 5, 4, 3, 7, 2, 1, 6, 3, 2, 5, 1, 2, 4, 6, 1, 2, 3, 5, 1, 2, 6, 3, 4,
         7, 5, 7, 6],
        [4, 5, 3, 2, 5, 1, 4, 3, 4, 3, 1, 4, 3, 2, 4, 2],
    ],
    'K10_139': [[2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 4, 1, 5, 3, 1, 2, 5, 4]],
    'mK10_140': [
        [4, 5, 5, 3, 4, 6, 7, 2, 1, 5, 6, 3, 2, 2, 4, 6, 1, 3, 5, 7, 1, 2, 3, 7, 6,
         3, 4],
        [2, 3, 1, 3, 4, 5, 2, 3, 4, 2, 1, 4, 3, 5, 1, 4, 2, 4, 3, 5, 4, 2],
    ],
    'K10_142': [
        [6, 7, 5, 7, 4, 3, 6, 8, 9, 2, 1, 5, 7, 8, 4, 6, 7, 3, 4, 8, 1, 3, 5, 7, 4,
         8, 3, 2, 7, 6],
        [4, 5, 3, 5, 2, 1, 4, 3, 4, 1, 3, 2, 5, 1, 2, 4, 5, 1, 4, 3, 5, 4, 1, 2],
    ],
    'mK10_145': [
        [2, 1, 4, 3, 2, 1, 1, 5, 1, 2, 4, 3, 3, 2, 4, 1, 3, 5, 3, 2, 1, 4, 3, 2, 3, 4],
        [2, 1, 8, 7, 6, 5, 5, 4, 3, 2, 1, 7, 9, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 1, 3, 9,
         4, 7, 2, 6, 8, 4],
        [2, 1, 4, 3, 2, 1, 8, 7, 7, 6, 5, 4, 2, 5, 9, 4, 3, 5, 2, 4, 6, 3, 5, 7, 7, 6, 5,
         4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
    ],
    'K10_160': [
        [6, 7, 5, 7, 4, 6, 3, 5, 2, 1, 3, 2, 4, 3, 6, 1, 5, 3, 6, 5, 1, 2, 6, 5, 4],
        [6, 7, 7, 5, 8, 9, 4, 3, 2, 6, 7, 5, 3, 6, 2, 9, 1, 3, 4, 7, 2, 3, 5, 1, 2,
         6, 5, 4, 9, 8],
    ],
    'mK10_161': [
        [2, 1, 4, 3, 2, 1, 1, 5, 1, 2, 4, 3, 1, 5, 3, 2, 4, 1, 3, 5, 3, 2, 1, 4, 3, 2, 3, 4],
        [2, 1, 6, 5, 8, 7, 6, 5, 5, 4, 3, 2, 1, 9, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 1, 3,
         9, 4, 7, 2, 6, 4, 7, 8],
        [8, 7, 2, 1, 4, 3, 2, 1, 10, 9, 8, 7, 7, 11, 10, 9, 6, 5, 8, 4, 7, 9, 2, 5, 8, 11,
         4, 3, 2, 7, 6, 5, 8, 7, 6, 3, 4, 9, 8, 7, 10, 9, 8, 9, 10],
    ],
    'mK11n19': [[4, 5, 2, 1, 3, 2, 1, 2, 5, 1, 4, 2, 3, 1, 2, 5, 3, 2, 3, 2, 5, 4]],
    'K11n38': [[4, 5, 3, 5, 2, 1, 4, 3, 4, 3, 1, 4, 3, 4, 3, 4, 1, 2]],
    'K11n95': [[6, 7, 5, 4, 3, 2, 1, 7, 3, 2, 5, 6, 1, 2, 4, 5, 6, 3, 5, 7, 4, 1, 2,
                6, 5, 3, 7, 6, 2, 5, 4]],
    'K11n118': [[2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 3, 5, 1, 3, 4, 2, 4, 3, 5, 4, 2]],
    'K12n242': [[4, 5, 2, 1, 3, 2, 1, 2, 5, 1, 4, 2, 5, 1, 2, 4, 5, 1, 2, 3, 1, 2, 5, 4]],
    'K12n591': [
        [2, 1, 4, 3, 2, 1, 1, 2, 5, 1, 4, 2, 3, 5, 1, 3, 2, 4, 1, 5, 2, 3, 3, 2, 1, 4, 3,
         2, 3, 4],
        [2, 1, 6, 5, 8, 7, 6, 5, 5, 6, 9, 5, 4, 3, 2, 1, 8, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3,
         9, 1, 3, 7, 4, 6, 1, 2, 7, 8],
        [2, 1, 4, 3, 2, 1, 1, 5, 2, 4, 1, 3, 5, 2, 4, 3, 2, 4, 3, 2, 4, 1, 3, 2, 5, 1, 4,
         2, 5, 1, 2, 3, 3, 2, 1, 4, 3, 2, 3, 4],
    ],
    'K15n41185': [[4, 5, 2, 1, 6, 7, 5, 6, 3, 2, 4, 5, 1, 7, 2, 6, 1, 3, 7, 5, 2, 1, 6,
                   7, 3, 2, 5, 4, 6, 1, 5, 2, 3, 7, 6, 1, 2, 5, 4]],
    # ---- entries derived from grid atlas (rot != 0 or previously missing) ----
    'K3_1': [[4, 3, 2, 1, 1, 3, 5, 3, 2, 1, 4, 3, 2, 3, 4]],
    'K5_1': [
        [2, 1, 1, 3, 2, 2, 1, 3, 2, 2],
        [8, 7, 6, 5, 4, 3, 2, 1, 1, 3, 5, 7, 9, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2,
         7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
    ],
    'K5_2': [[4, 3, 3, 3, 2, 1, 5, 1, 3, 3, 2, 1, 4, 3, 2, 3, 4]],
    'K6_3': [
        [4, 3, 2, 1, 1, 3, 5, 1, 2, 2, 2, 3, 4],
        [4, 3, 5, 3, 2, 1, 5, 4, 4, 3, 2, 2, 4],
    ],
    'K7_1': [
        [6, 5, 4, 3, 3, 2, 1, 5, 4, 3, 2, 2, 4, 7, 1, 3, 2, 2, 5, 6],
        [6, 5, 5, 7, 6, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 2, 4, 6],
        [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 3, 5, 7, 9, 11, 13, 11, 10, 9, 8, 7, 6,
         5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3,
         12, 11, 10, 9, 8, 7, 6, 5, 4, 11, 10, 9, 8, 7, 6, 5, 12, 11, 10, 9, 8, 7, 6, 11,
         10, 9, 8, 7, 12, 11, 10, 9, 8, 11, 10, 9, 12, 11, 10, 11, 12],
    ],
    'K7_2': [[4, 3, 3, 3, 3, 5, 3, 2, 1, 1, 3, 3, 2, 1, 4, 3, 2, 3, 4]],
    'K7_5': [
        [8, 7, 7, 6, 5, 5, 4, 3, 2, 1, 9, 8, 7, 1, 3, 5, 8, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2,
         5, 4, 3, 6, 5, 4, 5, 6],
        [4, 3, 2, 1, 8, 7, 7, 6, 5, 4, 3, 2, 1, 1, 7, 6, 5, 4, 3, 9, 3, 2, 1, 5, 7, 2, 3,
         7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5,
         8, 7, 6, 7, 8],
        [4, 3, 3, 3, 2, 1, 5, 4, 1, 3, 2, 4, 4, 3, 2, 1, 5, 4, 3, 1, 2],
        [8, 7, 6, 5, 5, 7, 7, 6, 5, 4, 3, 2, 1, 9, 1, 3, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 8,
         7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
    ],
    'K7_6': [
        [8, 7, 7, 6, 5, 4, 3, 3, 2, 1, 9, 5, 7, 1, 3, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4,
         3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
        [4, 3, 6, 5, 4, 3, 3, 7, 6, 5, 3, 2, 1, 4, 3, 2, 5, 4, 3, 7, 2, 6, 1, 3, 5, 6, 3,
         2, 1, 4, 3, 2, 3, 4],
        [2, 1, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2],
    ],
    'K7_7': [
        [6, 5, 4, 3, 3, 2, 1, 5, 1, 3, 2, 4, 7, 3, 5, 3, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 5,
         4, 3, 6, 5, 4, 5, 6],
        [2, 1, 6, 5, 4, 3, 2, 1, 1, 5, 4, 3, 1, 2, 7, 2, 3, 5, 5, 4, 3, 6, 5, 4, 5, 6],
        [8, 7, 7, 6, 5, 4, 3, 2, 1, 9, 3, 5, 8, 1, 7, 8, 5, 4, 3, 4, 5, 5, 4, 3, 2, 1, 6,
         5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6],
    ],
    'K8_20': [[4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 1, 7, 2, 4, 6, 1, 7, 1, 4, 3, 2, 5, 4, 3,
               4, 5, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6]],
    'K9_44': [
        [4, 3, 6, 5, 4, 3, 3, 2, 1, 4, 3, 2, 6, 1, 5, 2, 4, 7, 3, 6, 1, 5, 3, 6, 3, 2, 1,
         4, 3, 2, 3, 4],
        [4, 3, 6, 5, 4, 3, 3, 4, 3, 2, 1, 7, 6, 4, 1, 3, 5, 2, 4, 5, 2, 3, 5, 4, 3, 2, 1,
         6, 5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6],
        [4, 3, 6, 5, 4, 3, 3, 7, 3, 2, 1, 4, 3, 2, 6, 5, 4, 3, 7, 1, 6, 3, 5, 6, 3, 2, 1,
         4, 3, 2, 3, 4],
    ],
    'K9_45': [
        [4, 3, 8, 7, 7, 6, 5, 4, 3, 3, 2, 1, 7, 9, 4, 6, 1, 3, 7, 4, 5, 7, 6, 5, 4, 3, 2,
         1, 8, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
        [2, 1, 6, 5, 5, 4, 3, 2, 1, 1, 5, 2, 4, 7, 3, 1, 5, 3, 5, 4, 3, 2, 1, 6, 5, 4, 3,
         2, 5, 4, 3, 6, 5, 4, 5, 6],
        [4, 3, 3, 3, 2, 1, 5, 4, 3, 1, 4, 3, 4, 5, 3, 2, 1, 2, 3, 3, 2, 1, 4, 3, 2, 3, 4],
    ],
    'K9_47': [[2, 1, 6, 5, 8, 7, 6, 5, 5, 4, 3, 2, 1, 6, 9, 5, 4, 3, 8, 7, 1, 6, 9,
               3, 5, 7, 6, 7, 8, 3, 2, 1, 4, 3, 2, 3, 4]],
    'K10_140': [[4, 3, 6, 5, 4, 3, 3, 4, 3, 2, 1, 7, 4, 3, 2, 6, 1, 5, 2, 4, 1, 5, 2,
                 3, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6]],
    'K10_145': [[2, 1, 4, 3, 2, 1, 1, 5, 2, 4, 5, 2, 4, 1, 5, 4, 3, 2, 2, 3, 4]],
    'K10_161': [
        [6, 5, 4, 3, 8, 7, 6, 5, 4, 3, 3, 2, 1, 4, 3, 2, 9, 6, 8, 1, 5, 7, 9, 2, 4, 6, 8,
         6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 6, 5, 4, 7, 6, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 8, 7,
         6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
        [6, 5, 10, 9, 8, 7, 6, 5, 4, 3, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 13, 4, 6,
         10, 12, 1, 3, 5, 7, 9, 13, 10, 11, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10,
         9, 8, 7, 6, 5, 4, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3, 12, 11, 10, 9, 8, 7, 6, 5, 4,
         11, 10, 9, 8, 7, 6, 5, 12, 11, 10, 9, 8, 7, 6, 11, 10, 9, 8, 7, 12, 11, 10, 9, 8,
         11, 10, 9, 12, 11, 10, 11, 12],
    ],
    'K11n19': [[4, 3, 2, 1, 1, 3, 2, 5, 2, 1, 3, 2, 4, 3, 3, 2, 4]],
    'mK7_3': [
        [2, 1, 1, 1, 3, 1, 2, 2, 1, 3, 2, 2],
        [8, 7, 7, 7, 6, 5, 4, 3, 2, 1, 9, 1, 3, 5, 7, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4,
         3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8],
    ],
    'mK7_4': [[4, 3, 3, 3, 2, 1, 1, 5, 1, 3, 1, 3, 2, 1, 4, 3, 2, 3, 4]],
    'mK8_19': [[6, 5, 4, 3, 2, 1, 1, 3, 5, 7, 2, 4, 6, 6, 5, 4, 3, 2,
                5, 4, 3, 6, 5, 4, 5, 6]],
    'mK8_20': [[4, 3, 2, 1, 1, 3, 2, 5, 2, 1, 3, 2, 2, 3, 4]],
    'mK9_43': [[2, 1, 4, 3, 2, 1, 5, 4, 3, 1, 2, 3, 3, 2, 4, 3, 3, 2, 4]],
    'mK9_48': [[6, 5, 4, 3, 3, 3, 2, 1, 5, 4, 7, 1, 3, 4, 5, 3, 2, 1, 2, 3, 5, 4, 3,
                2, 1, 6, 5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6]],
    'mK9_49': [[6, 5, 4, 3, 3, 3, 2, 1, 5, 7, 1, 3, 2, 4, 5, 4, 3, 2,
                5, 4, 3, 6, 5, 4, 5, 6]],
    'mK10_124': [[8, 7, 6, 5, 4, 3, 2, 1, 1, 3, 5, 7, 9, 2, 4, 6, 8, 8, 7, 6, 5, 4, 3,
                  2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8]],
    'mK10_128': [[6, 5, 5, 4, 3, 3, 2, 1, 5, 4, 3, 2, 7, 2, 4, 1, 3, 5, 5, 4, 3, 2, 1,
                  6, 5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6]],
    'mK10_132': [
        [6, 5, 5, 7, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 2, 4, 6, 1, 3, 5, 7, 5, 4, 3, 2, 1, 6,
         5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6],
        [4, 3, 3, 5, 3, 2, 1, 4, 3, 2, 2, 4, 1, 3, 5, 2, 4, 4, 3, 2, 3, 4],
    ],
    'mK10_136': [[6, 5, 4, 3, 3, 5, 3, 2, 1, 4, 3, 2, 7, 2, 4, 1, 3, 5, 5, 4, 3, 2, 1,
                  6, 5, 4, 3, 2, 5, 4, 3, 6, 5, 4, 5, 6]],
    'mK10_139': [
        [6, 5, 4, 3, 3, 2, 1, 5, 7, 4, 6, 8, 3, 5, 7, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6,
         5, 8, 7, 6, 7, 8, 1, 2],
        [12, 11, 10, 9, 8, 7, 6, 5, 5, 7, 9, 11, 2, 4, 6, 8, 10, 13, 11, 10, 9, 8, 7, 6, 5,
         4, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3, 12, 11, 10, 9, 8, 7, 6, 5, 4, 11, 10, 9, 8,
         7, 6, 5, 12, 11, 10, 9, 8, 7, 6, 11, 10, 9, 8, 7, 12, 11, 10, 9, 8, 11, 10, 9, 12,
         11, 10, 11, 12],
    ],
    'mK10_142': [[6, 5, 4, 3, 3, 3, 2, 1, 5, 7, 6, 1, 3, 2, 4, 6, 5, 4, 3, 2,
                  5, 4, 3, 6, 5, 4, 5, 6]],
    'mK10_160': [[4, 3, 2, 1, 1, 3, 2, 2, 5, 1, 3, 2, 4, 2, 4, 3, 2, 3, 4]],
    'mK11n38': [[8, 7, 6, 5, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 9, 2, 4, 6, 1, 3, 5, 7,
                 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5,
                 4, 7, 6, 5, 8, 7, 6, 7, 8]],
    'mK11n95': [
        [6, 5, 4, 3, 3, 5, 4, 7, 2, 6, 4, 3, 5, 2, 6, 1, 5, 4, 3, 6, 5, 4, 5, 6, 1, 2],
        [8, 7, 6, 5, 5, 4, 3, 2, 1, 7, 6, 9, 3, 5, 8, 1, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6,
         5, 8, 7, 6, 7, 8, 1, 2],
    ],
    'mK11n118': [[2, 1, 6, 5, 8, 7, 6, 5, 5, 4, 3, 2, 1, 9, 6, 8, 1, 5, 7, 2, 4, 6, 9,
                  7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8]],
    'mK12n242': [
        [4, 3, 2, 1, 1, 3, 5, 2, 4, 3, 3, 2, 4, 1, 3, 5, 2, 4, 4, 3, 2, 3, 4],
        [12, 11, 10, 9, 8, 7, 6, 5, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12, 12, 11, 10, 9, 8,
         7, 6, 5, 4, 3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3, 12, 11, 10, 9, 8, 7, 6, 5, 4, 11,
         10, 9, 8, 7, 6, 5, 12, 11, 10, 9, 8, 7, 6, 11, 10, 9, 8, 7, 12, 11, 10, 9, 8, 11,
         10, 9, 12, 11, 10, 11, 12],
    ],
    'mK12n591': [[4, 3, 2, 1, 1, 3, 2, 5, 4, 2, 1, 4, 3, 5, 2, 4, 4, 3, 2, 3, 4]],
    'mK15n41185': [[8, 7, 6, 5, 4, 3, 2, 1, 1, 3, 5, 7, 9, 2, 4, 6, 8, 3, 5, 7, 7, 6, 5,
                    4, 3, 2, 8, 7, 6, 5, 4, 7, 6, 5, 8, 7, 6, 7, 8]],
}


# ============================================================
# Section 7: Constructions
# ============================================================

def _cable_parts(leg: Leg):
    """Shared braid ingredients for 2-cable constructions."""
    p = leg.num_cusps
    pp = [4 * i - 2 for i in range(1, p + 1)]
    dc = [x for gen in leg.braid for x in (2*gen, 2*gen - 1, 2*gen + 1, 2*gen)]
    return pp, dc


def whitehead_double(leg: Leg) -> Leg:
    """
    Legendrian Whitehead double of leg.
    Returns a new Leg whose braid encodes the Whitehead double plat closure.
    Requires leg to be a single-component knot.
    """
    if leg.num_components != 1:
        raise ValueError('whitehead_double requires a single-component knot')
    pp, dc = _cable_parts(leg)
    return Leg([2] + pp + dc + pp, name=f'WhiteheadDouble({leg.name})')


def twisted_2cable(leg: Leg) -> Leg:
    """
    Legendrian twisted 2-cable of leg.
    Returns a new Leg whose braid encodes the twisted 2-cable plat closure.
    Requires leg to be a single-component knot.
    """
    if leg.num_components != 1:
        raise ValueError('twisted_2cable requires a single-component knot')
    pp, dc = _cable_parts(leg)
    return Leg(pp + [1] + dc + pp, name=f'Twisted2Cable({leg.name})')


def two_copy(leg: Leg) -> Leg:
    """
    Legendrian 2-copy (push-off) of leg.
    Returns a 2-component link consisting of leg and its Legendrian push-off,
    with both components having the same Maslov potential (seed 0).
    Requires leg to be a single-component knot.
    The linking number between the two components equals tb(leg).
    """
    if leg.num_components != 1:
        raise ValueError('two_copy requires a single-component knot')
    pp, dc = _cable_parts(leg)
    return Leg(pp + dc + pp, maslov=[0, 0], name=f'TwoCopy({leg.name})')


def two_copy_shifted(leg: Leg) -> Leg:
    """
    Legendrian 2-copy of leg with shifted Maslov potential.
    Same as two_copy but the first component has Maslov seed 1 and the second
    has seed 0, shifting the grading of one copy by 1.
    Requires leg to be a single-component knot.
    """
    if leg.num_components != 1:
        raise ValueError('two_copy_shifted requires a single-component knot')
    pp, dc = _cable_parts(leg)
    return Leg(pp + dc + pp, maslov=[1, 0], name=f'TwoCopyShifted({leg.name})')


def split_augmentation(
    aug1: 'Augmentation',
    aug2: 'Augmentation',
    _tc_dga: Optional['DGA'] = None,
) -> 'Augmentation':
    """
    Construct the split augmentation of two_copy(K) from two Z/2 augmentations of K.

    Given Z/2 augmentations aug1, aug2 of a knot K, returns the induced augmentation
    of two_copy(K) where pure comp-1 generators receive aug1's values, pure comp-2
    generators receive aug2's values, and mixed generators map to 0.

    The generator correspondence (p = K.num_cusps, m = len(K.braid)):
      - K braid crossing g (1-indexed): comp-1 at index p + 4*(g-1) + 2,
        comp-2 at p + 4*(g-1) + 3 in two_copy(K)
      - K cusp j (0-indexed): comp-1 at 2*p + 4*m + 2*j + 1,
        comp-2 at 2*p + 4*m + 2*j + 2 in two_copy(K)

    Both augmentations must be Z/2 augmentations of the same single-component Leg,
    with the same grading_mod.

    _tc_dga: advanced use only — pass two_copy_shifted(K).dga() to target the shifted
    2-copy instead of two_copy(K).  The generator correspondence is identical since
    both constructions use the same braid word.
    """
    if aug1.dga.ring != GroundRing.Z2 or aug2.dga.ring != GroundRing.Z2:
        raise NotImplementedError('split_augmentation is only implemented over Z/2')
    if aug1.dga.leg is not aug2.dga.leg:
        raise ValueError('aug1 and aug2 must be augmentations of the same Leg')
    if aug1.grading_mod != aug2.grading_mod:
        raise ValueError('aug1 and aug2 must have the same grading_mod')
    K = aug1.dga.leg
    if K.num_components != 1:
        raise ValueError('split_augmentation requires a single-component knot')

    p = K.num_cusps
    m = len(K.braid)
    aug1_set = set(aug1.data)
    aug2_set = set(aug2.data)

    tc_dga = _tc_dga if _tc_dga is not None else two_copy(K).dga()

    split_gens = []
    for g in range(1, m + 1):
        base = p + 4 * (g - 1)
        if g in aug1_set:
            split_gens.append(base + 2)   # comp-1 pure copy of K crossing g
        if g in aug2_set:
            split_gens.append(base + 3)   # comp-2 pure copy of K crossing g
    for j in range(p):
        k_cusp = m + j + 1
        cusp_base = 2 * p + 4 * m + 2 * j
        if k_cusp in aug1_set:
            split_gens.append(cusp_base + 1)   # comp-1 cusp copy
        if k_cusp in aug2_set:
            split_gens.append(cusp_base + 2)   # comp-2 cusp copy

    return Augmentation(split_gens, tc_dga, aug1.grading_mod)
