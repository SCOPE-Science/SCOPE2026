# Labelled mutation data is not a Hamiltonian-isotopy invariant on Bl_2 CP^2

## Context

Let X = Bl_2 CP^2 with its monotone symplectic form and the toric Lagrangian
seed of Pascaleff-Tonkonog Table 1: W(x,y) = x + y + x^{-1} + y^{-1} + (xy)^{-1}
with support {(1,0),(0,1),(-1,0),(0,-1),(-1,-1)} and disk directions
V = {(1,-1),(-1,1),(-1,0),(0,-1),(1,1)}. Finite iterated
Pascaleff-Tonkonog mutations carry the disks along (Shende-Treumann-Williams,
Theorem 4.24). The admitted target question: if two mutation words give
Hamiltonian-isotopic monotone tori, must their labelled seeds (W_w,V_w) be
equivalent under one joint A in SL(2,Z)?

## Definitions

A labelled LG seed is S = (W,V) with W a Laurent polynomial and V a multiset
of integral directions. Mutation mu_v acts on W by the wall-crossing pullback
x^u -> x^u(1+m)^{-(u.v)} (with m = x^{v_2}y^{-v_1}) followed by exact division,
and on V by the tropical rule mu_v(u) = u + max(0, u_1 v_2 - u_2 v_1) v with
negation at the mutated slot. Joint SL(2,Z)-equivalence means one matrix
carries W-exponents (with coefficients) and all of V simultaneously.

## Result

The target statement is FALSE. The empty word w = () and the reverse
double-mutation word w' = (2,2) (mutate along v_2 = (-1,0), then back along
the mutated disk (1,0) at the same slot) give Hamiltonian-isotopic tori
L_w, L_w' in X, but SL(2,Z)-inequivalent labelled seeds. Explicitly,
W_1 = x + xy + y + (xy)^{-1} + y^{-1},
V_1 = {(1,-1),(-2,1),(1,0),(0,-1),(0,1)},
W_2 = xy + y + (xy)^{-1} + (xy^2)^{-1} + y^{-1}
with support {(1,1),(0,1),(-1,-1),(-1,-2),(0,-1)},
V_2 = {(2,-1),(-2,1),(-1,0),(1,-1),(0,1)}.
The invariant n(S) = |V cap supp(W)| gives n(S_0) = 2 versus n(S_2) = 1, so
no lattice bijection, hence no SL(2,Z) matrix, carries both parts at once.
Exhaustive enumeration confirms the unique W-only SL map ((1,0),(1,1))
fails on V.

## Proof / evidence

Isotopy: Pascaleff-Tonkonog Lemma 4.19 (reverse mutation) states two
consecutive mutations along D then the mutated disk D' return a Hamiltonian-
isotopic configuration; both steps here stay Laurent, hence admissible by
Theorems 4.6/4.8/4.24. Wall-crossing: along (-1,0) with m = y, dots give
N = x(1+y)^2 + y(1+y) + x^{-1} + y^{-1}(1+y) + (xy)^{-1}, exactly divisible
once by (1+y) to yield W_1; along (1,0) with m = y^{-1},
N = (xy)^{-1}(1+y^{-1})^2 + y^{-1}(1+y^{-1}) + y(1+y^{-1}) + x + xy, exactly
divisible once by (1+y^{-1}) to yield W_2. Tropical updates are hand-checked
and match generic code mut2.py (validated on Example 4.11) via
verify_counterexample.py. Inequivalence is the counting invariant plus the
column-constrained exhaustive SL search.

## Limitations

The disproof cites Pascaleff-Tonkonog Lemma 4.19 and Theorems 4.8/4.20/4.24
for mutation legitimacy and does not re-prove those Floer-theoretic results.
It concerns labelled (W,V) data, not W alone: potentials still return up to
GL(2,Z) per Remark 4.4.

## Reproducibility

Run output/artifacts/verify_counterexample.py with output/artifacts/mut2.py
in the same directory; it asserts hand-vs-code agreement, the 2-vs-1
invariant, and absence of any simultaneous SL(2,Z) map.

## References

J. Pascaleff and D. Tonkonog, The wall-crossing formula and Lagrangian
mutations, Adv. Math. (arXiv:1711.03209): Definitions 4.1-4.5, Theorems
4.6/4.8/4.20/4.24, Lemma 4.19, Table 1, Example 4.11, Remark 4.4.
