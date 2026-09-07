# First explicit quartic plane Cremona maps over F4: five PGL3(F4)-classes with composition-inverse certificates

## Context

The Noether–Castelnuovo generation theorem describes Bir(P^2) over algebraically
closed fields, and Hudson-type tables list homaloidal types in characteristic 0.
Concrete conjugacy tables over small finite fields, with Galois-orbit refinements
and explicit inverses, remain incomplete. Degree 4 over F4 is the smallest stratum
where both quartic homaloidal types coexist with non-trivial characteristic-2
Galois-orbit phenomena, where the even-permutation theorem for even q >= 4 can be
witnessed concretely, and where a closed machine-checkable table is directly
citable for finite-geometry catalogs and multivariate-birational benchmarks.

## Definitions

- F4 = {0,1,w,w^2}, w^2+w+1 = 0, written as integers 0,1,2,3 (2 = w, 3 = w^2);
  addition is XOR, multiplication is F2[t]/(t^2+t+1) arithmetic.
- F16 = F4[u]/(u^2+u+w); Frobenius over F4 is (a0+a1u) -> (a0+a1)+a1u, order 2.
- |P^2(F4)| = 21, |P^2(F16)| = 273, |PGL3(F4)| = 60480.
- Quartic monomial order (15): (4,0,0),(3,1,0),(3,0,1),(2,2,0),(2,1,1),(2,0,2),
  (1,3,0),(1,2,1),(1,1,2),(1,0,3),(0,4,0),(0,3,1),(0,2,2),(0,1,3),(0,0,4).
- A plane Cremona map of degree 4 over F4 is f = [f0:f1:f2] with ternary quartics
  over F4, no common factor, birational over the algebraic closure.
- Homaloidal types for d = 4 from sum m_i = 3(d-1) = 9 and sum m_i^2 = d^2-1 = 15
  are (4;3,1^6) (de Jonquieres) and (4;2^3,1^3) (symmetric).
- PGL3(F4)-conjugacy is g = A o f o A^{-1} with A in PGL3(F4).
- System multiplicity at a base point is the minimum order of the net after moving
  the point to [0:0:1]; it equals the minimum over basis members since combinations
  can only raise order by cancellation.

## Result

There are at least five distinct PGL3(F4)-conjugacy classes of plane Cremona maps
of degree 4 over F4, exhibited explicitly:

- **S1–S4 (symmetric, type (4;2^3,1^3))**: doubles [1:0:0],[0:1:0],[0:0:1] and
  singles S1 {[1:1:1],[1:1:w],[1:w:1]}, S2 {[1:1:1],[1:1:w],[1:w:w]},
  S3 {[1:1:1],[1:1:w],[1:w:w^2]}, S4 {[1:1:1],[1:w:w^2],[1:w^2:w]}.
  Each has an explicit quartic inverse over F4; both compositions equal the
  identity as rational maps with common degree-15 cofactor
  (S1 8/56, S2 7/40, S3 8/52, S4 4/24 monomials for g(f)/f(g)).
  F4-base = F16-base = exactly the six listed points; system multiplicities
  exactly 2,2,2,1,1,1; Noether sums 9/15 saturate.

- **DJ (de Jonquieres, type (4;3,1^6))**: triple [0:0:1], rational singles
  [0:1:0],[1:0:0],[1:1:0],[1:w:w], plus F16-pair P = [1:alpha:1],
  Q = [1:bar{alpha}:1] with alpha = 3u and bar{alpha} = 3+3u Frobenius conjugate.
  Directions from the centre are six distinct (four rational plus two conjugate
  non-rational); a fully rational (4;3,1^6) with no fixed line is impossible since
  six distinct directions are needed but P^1(F4) has five. Explicit quartic inverse
  over F4 with triple at [1:0:w]; g(f) cofactor 32 terms, f(g) 58 terms.
  F4-base exactly five rational points; F16-base exactly those five plus the pair.

Representative triples (w = 2, w^2 = 3; full coefficient vectors in
artifacts/representatives.json in the monomial order above):

- S1 f = (wX^2Y^2+wX^2YZ+X^2Z^2+XY^2Z, X^2Y^2+wX^2YZ+wX^2Z^2+XYZ^2,
  w^2X^2Y^2+X^2YZ+w^2X^2Z^2+Y^2Z^2).
- S4 f = (X^2Z^2+XY^2Z, X^2Y^2+XYZ^2, X^2YZ+Y^2Z^2) (sparsest).
- DJ f = (X^3Y+wX^3Z+XY^3, wX^3Y+wX^3Z+wX^2Y^2+XY^2Z,
  wX^3Y+w^2X^3Z+wX^2Y^2+wX^2YZ+Y^3Z).

The four symmetric classes are pairwise non-conjugate (distinct base orbits under
the 54-element monomial stabilizer of the three doubles; the mult-2 locus is
exactly those three points so any conjugacy lies in the stabilizer). The DJ class
is not conjugate to any symmetric class (different homaloidal type). Hence at
least 4 symmetric and at least 1 de Jonquieres class (at least 5 total).

Configuration bounds: symmetric rational-single triples off the coordinate lines
(C(9,3) = 84) form exactly five stabilizer orbits (sizes 3,9,18,27,27); four
contain birational nets (S1–S4), the remaining orbit
{[1:1:1],[1:1:w],[1:1:w^2]} has fixed line X+Y=0 (2+3 = 5 > 4) and yields no
Cremona. De Jonquieres rational quadruples in distinct directions (1280 = 5*4^4)
form exactly three orbits under the 2880-element point stabilizer
(sizes 80,240,960); DJ is one realised orbit.

## Proof / evidence

(i) Claimed rational base points are common zeros with exact system
multiplicities (independently recomputed via affine-translation expansion,
matching replay matrix-substitution values); Noether sums are 9/15.
(ii) Enumeration of all 21 F4-points and 273 F16-points shows no further common
zeros (6 resp. 7). No F4-line is fixed (a line has 17 F16-points > 7).
Primitivity for higher-degree divisors is certified by explicit witness lines
with trivial homogeneous GCD: each f and g has 3–9 of 21 F4-lines whose three
binary-quartic restrictions share no common divisor of any degree >= 1 (all monic
linear/quadratic/cubic divisors plus t-divisibility and quartic proportionality
checked), so no common plane divisor exists; exact degree 4 follows.
(iii) Symbolic composition: with F^e = f0^e0 f1^e1 f2^e2 (deg 16),
g_j(f) = sum_e g_{j,e} F^e; Zg0(f)-Xg2(f) = 0 and Zg1(f)-Yg2(f) = 0
(degree-17 identities) and G0/X = G1/Y = G2/Z = phi != 0 (explicit degree-15
common factor), and symmetrically f(g) = psi·id; hence mutually inverse rational
maps, inverse degree 4, general member irreducible.
(iv) By (iii) the full base scheme satisfies Noether; exhibited proper points
already square-sum to 15, leaving no room for further proper (including F64
degree-3) or infinitely-near points; DJ pair multiplicities are forced to 1 each
by the same count.
(v) Type witnesses: symmetric have max multiplicity 2 (no triple, so not
Jonquieres); three doubles non-collinear and singles off coordinate lines, no
line meets the system in > 4. DJ has unique triple; pencil covariance verified on
all five F4-lines through [0:0:1]: four lines joining the centre to rational
singles contract, the free direction maps dominantly onto the line 2X+3Y+Z = 0
through [1:0:w]; i.e. f sends pencil([0:0:1]) to pencil([1:0:w]) (covariant form).

## Limitations

Full irredundant census number N (expected in the tens) is not determined.
Splitting of one net over target-coordinate changes, patterns with non-rational
doubles (quadratic/cubic double orbits), degree-3 (F64) single orbits, and
infinitely-near collisions are not exhausted. The 15360/122880 DJ raw counts are
searched/stable-family sizes with only the rational-quadruple quotient exactly
reduced. DJ witness is covariance p -> q, not strict invariance of one pencil.
F64 points are not enumerated (covered by saturation given verified inverses).

## Reproducibility

Run `python3 artifacts/replay.py` (pure stdlib, no CAS): rechecks P^2 counts,
|PGL3(F4)|, all base multiplicities and Noether sums, F4/F16 base counts, both
composition identities with common cofactors, and both orbit censuses in seconds
(degree-16 composition dominates). Representatives: artifacts/representatives.json.
Independent audit additionally verified multiplicities via affine translation and
primitivity via line-restriction GCD witnesses.

## References (gap context)

Hudson/Noether homaloidal tables (char 0, no finite-field Galois refinement);
Calabri–Nguyen fine classification of cubics arXiv:2002.11396 (closed field, no F4
quartics); Schneider generators over F2 arXiv:2008.07991; Asgarli–Lai–Nakahara–
Zimmermann bijective maps arXiv:1910.05302 and Genevois–Lonjou–Urech Neretin groups
arXiv:2110.14605 (parity/generation over finite fields, no degree-4 F4 normal
forms or inverses); Alberich-Carraminana LNM homaloidal-curves chapter
doi:10.1007/978-3-540-45538-7_6. None gives quartic F4 representatives, Galois
degree-multiplicity tables, or composition certificates.
