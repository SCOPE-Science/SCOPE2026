# Isomorphism census of clean degree-8 dessins with passport black 2^4 and white 3^2 2^1, with cartographic certificate and verified Belyi witness

## Context

Grothendieck's correspondence identifies connected clean dessins d'enfants
with transitive permutation triples up to simultaneous conjugacy and with
Belyi maps up to isomorphism. General algorithms and uniform-passport or
uniquely-determined-tree theorems do not publish fixed-passport tables for
non-uniform low-degree strata. This record closes the clean degree-8 stratum
with black profile 2^4 and white profile 3^2 2^1 (non-uniform, non-star,
mixed genus), giving explicit triples, genera, automorphism sizes,
centralizer orbits, empty face types, and one exact rational Belyi witness,
all replayable in under a second with stdlib Python.

## Definitions

Fix n = 8. Composition convention: (pq)(x) = p(q(x)).
A clean dessin of the stated passport is encoded by a triple
(s0, s1, sInf) in S8^3 with:
- s0 of cycle type 2^4 (four black vertices of valency 2),
- s1 of cycle type 3^2 2^1 (three white vertices of valencies 3, 3, 2),
- s0 s1 sInf = 1, i.e. sInf = (s0 s1)^{-1},
- <s0, s1> transitive on {1,..,8} (connectedness),
up to simultaneous conjugacy in S8 (isomorphism).
Faces correspond to cycles of sInf; if sInf has cycle type lambda with
F = |lambda| parts, put V = 4+3 = 7, E = 8, chi = V - E + F = F - 1,
g = (2 - chi)/2. Automorphism size is |C_{S8}(s0, s1)|.
Fix s0^can = (1 2)(3 4)(5 6)(7 8), 0-indexed imagelist [1,0,3,2,5,4,7,6].
Let C = C_{S8}(s0^can), |C| = 2^4 * 4! = 384 (wreath C2 wr S4).

## Result

The stratum black 2^4 / white 3^2 2^1 contains exactly 4 connected classes
up to isomorphism: three of genus 0 with face types (6,1,1), (5,2,1),
(3,3,2), and one of genus 1 unicellular with face type (8,), with
automorphism sizes 2, 1, 2, 2 respectively. Face types (4,3,1) and (4,2,2)
are empty in this stratum.

Representatives with s0^can fixed (1-indexed cycles; 0-indexed imagelists
in parentheses):

- Class A: s1 = (1 2 3)(4 5)(6 7 8) ([1,2,0,4,3,6,7,5]),
  sInf = (2 3 5 8 6 4) ([0,2,4,1,7,3,6,5]), face (6,1,1), g = 0, |Aut| = 2, orbit 192.
- Class B: s1 = (1 2 3)(4 5 7)(6 8) ([1,2,0,4,6,7,3,5]),
  sInf = (2 3 7 6 4)(5 8) ([0,2,6,1,7,3,5,4]), face (5,2,1), g = 0, |Aut| = 1, orbit 384.
- Class C: s1 = (1 3)(2 5 8)(4 7 6) ([2,4,0,6,7,3,5,1]),
  sInf = (1 8 4)(2 3 6)(5 7) ([7,2,5,0,6,1,4,3]), face (3,3,2), g = 0, |Aut| = 2, orbit 192.
- Class D: s1 = (1 3 5)(2 4 7)(6 8) ([2,3,4,6,0,7,1,5]),
  sInf = (1 7 6 3 2 5 8 4) ([6,4,1,0,7,2,5,3]), face (8,), g = 1, |Aut| = 2, orbit 192.

Each satisfies s0 s1 sInf = id. The 960 transitive s1 with s0^can fixed
partition into centralizer orbits of sizes 192 + 384 + 192 + 192 = 960;
globally 100800 of 117600 = 105 x 1120 pairs are transitive (105 x 960).

The class (6,1,1) carries the explicit Belyi map over Q:

  f(x) = -(x^4 - 12x^2 + 24)^2 / (64 (x^2 - 9)),
  f(x) - 1 = -x^2 (x^2 - 8)^3 / (64 (x^2 - 9)),

of degree 8 with ramification 2^4 over 0, 3^2 2^1 over 1, (6,1,1) over
infinity.

## Proof / Evidence

Census (exhaustive computation, replayable): all s0 of type 2^4 are
conjugate, so every simultaneous class meets s0 = s0^can, and two pairs
(s0^can, s1), (s0^can, s1') are simultaneously conjugate iff
s1' = c s1 c^{-1} for c in C. Hence classes are exactly C-orbits on
transitive s1. Counts 1120 = 8!/(3^2 2! 2) and 105 = 8!/(2^4 4!) confirmed
by filtering all 40320 permutations; |C| = 384 by commutation filter.
Transitivity by BFS. Program finds 960 transitive s1 with s0^can fixed,
partitioned into 4 C-orbits of sizes 192, 384, 192, 192; stabilizer sizes
2, 1, 2, 2 satisfy orbit x stab = 384; stabilizer in C equals C(s0^can, s1),
the dessin automorphism group. Per orbit, sInf = (s0 s1)^{-1} computed,
s0 s1 sInf = 1 asserted, cycle type by visited-set inspection, F/chi/g as
above. Only the four listed face types occur; (4,3,1), (4,2,2) absent.
Independent global loop over all 117600 pairs finds 100800 = 105 x 960
transitive pairs, consistent with the reduction.

Belyi witness (hand-checkable algebra + integer-arithmetic script): with
B = x^4 - 12x^2 + 24, D = x^2 - 9, W = x^2 (x^2 - 8)^3, e = -64, c = -1/64:
B^2 - W = -64(x^2 - 9) by expansion (R = [576, 0, -64] low-to-high);
deg f = max(8,2) = 8. B has 4 distinct roots (y = x^2, y^2 - 12y + 24,
disc 48 != 0, roots 6 +/- 2 sqrt3 > 0 distinct nonzero); B(0) = 24,
B|_{y=6} = -12 so B, B' coprime. Coprimality: B(+/-3) = -3 so gcd(B,D) = 1;
B(0) = 24, B|_{x^2=8} = -8 so gcd(B,W) = 1; disc(D) = 36, 3^2 - 8 = 1 so
gcd(D,W) = 1. White divisor W: 0 double, +/-2 sqrt2 triple, profile 3^2 2^1.
Derivative: B' = 4x^3 - 24x, D' = 2x,
H := 2B'D - BD' = 6x^5 - 96x^3 + 384x = 6x(x^2 - 8)^2 exactly, so
f' = c B H / D^2. Finite critical points are B = 0 (four simple zeros of f',
double zeros of f) and H = 0 (0 simple, +/-2 sqrt2 double, matching f - 1
multiplicities 2, 3, 3); deg H = 5 fully factored so no others. Simple poles
+/-3 unramified; infinity a pole of order 8 - 2 = 6. Riemann-Hurwitz:
4x1 + (1+2+2) + 5 = 14 = 2x8 - 2. Faces of orders 1, 1, 6 give type (6,1,1),
F = 3, chi = 2, g = 0. Since the census shows a unique class with face type
(6,1,1), and P1 minus a finite set is connected (so the unramified cover is
connected, monodromy transitive), f witnesses class A.

## Limitations

Closed-form Belyi maps for the (5,2,1), (3,3,2), (8,) classes are not
constructed. Monodromy identification of the witness uses passport
uniqueness from the census plus the connected-cover argument, not an
explicit loop-lifting isomorphism to the listed triple. Field-of-definition
statements beyond the Q-coefficients of f are not proved. Census
correctness relies on replay of the two short stdlib scripts.

## Reproducibility

No network, single core, stdlib Python 3 only:

  python3 artifacts/census.py       # -> 4 classes, counts, orbits (~0.3 s)
  python3 artifacts/belyi_verify.py # -> Belyi identities (<0.1 s)

Artifacts: artifacts/census.py, artifacts/belyi_verify.py,
artifacts/triples.json (machine-readable class table).

## References

- Hidalgo, Bipartite graphs and their dessins d'enfants, arXiv:1611.02901:
  general embedding algorithm; does not fix (2^4; 3^2 2^1) nor give this table.
- Uniform-passport regularity theorems, arXiv:2602.11867: white profile 3^2 2^1
  is non-uniform, outside scope.
- Pairs of tree dessins and Shabat polynomials, arXiv:2510.10192; Shabat
  polynomials and monodromy groups of trees uniquely determined by passport,
  arXiv:1805.07530 (Cameron et al.): uniquely determined trees/tree pairs;
  here four classes across g = 0, 1, non-unique.
- Adrianov-Shabat Belyi functions of genus-2 dessins with 4 edges: disjoint
  degree/genus/passport.
