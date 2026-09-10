# Braid-orbit component census for the (2,3,7) Nielsen classes of PSL(2,7) and PSL(2,8)

## Context

For a finite group G and conjugacy classes C=(C1,...,Cr), the Nielsen class
N(G,C) is the set of generating tuples with product 1 and entries in the
given classes. The Artin braid group acts by Hurwitz moves; its orbits are
the connected components of the corresponding Hurwitz space, equivalently
Galois orbits of the associated regular dessins / covers. For the
(2,3,7) triangle type the quotients PSL(2,7) (order 168, Klein quartic,
genus 3) and PSL(2,8) (order 504, Fricke–Macbeath curve, genus 7) are the
two smallest Hurwitz groups PSL(2,q) by order — a closed initial segment.
Macbeath's classification settles existence of (2,3,7) generation for
these groups but not the number or degrees of Hurwitz-space components.

## Definitions

- G1 = PSL(2,7), |G1|=168, realized as 2x2 determinant-1 matrices over F7
  modulo scalars (168 projective elements).
- G2 = PSL(2,8), |G2|=504, realized as 2x2 determinant-1 matrices over
  F8 = F2[t]/(t^3+t+1) (bit representation 0..7, modulus 0xB).
- Ordered (2,3,7) Nielsen class: N(G) = {(x,y) : o(x)=2, o(y)=3,
  o(xy)=7}, identified with triples (x,y,z), xyz=1, of exact orders
  (2,3,7) via z=(xy)^{-1}.
- Pattern union: U(G) = {(x,y,z) : xyz=1, {o(x),o(y),o(z)}={2,3,7}}
  (6 position patterns).
- Hurwitz moves: s1:(x,y,z)->(xyx^{-1},x,z),
  s2:(x,y,z)->(x,yzy^{-1},y) plus inverses; pure-braid generators
  a=s1^2, b=s2^2 (preserve the ordered (2,3,7) pattern).
- Inn(G)-classes: orbits under simultaneous conjugation.

## Result

- N1 = 336 = 2*|G1|, split 168 + 168 by the class of xy (two order-7
  classes 7A/7B, each exactly 168 pairs).
- N2 = 1512 = 3*|G2|, split 504 + 504 + 504 by the class of xy (three
  order-7 classes 7A/7B/7C, each exactly 504 pairs).
- Generation: every such pair generates (all 336 close to G1; all 1512
  close to G2), by exhaustive subgroup-closure computation and
  independently by Dickson maximal-subgroup Lagrange exclusion
  (G1 maximals S4 order 24, F21 order 21: 7∤24 excludes S4, 2∤21
  excludes F21; G2 maximals D18 order 18, D14 order 14, F56 order 56:
  7∤18 excludes D18, 3∤14 excludes D14, 3∤56 excludes F56).
- Pure-braid orbits: b1 = 2 orbits of 168 (G1); b2 = 3 orbits of 504
  (G2). Each pure orbit is exactly one z=xy class fiber.
- Full-braid orbits on U: |U1|=2016 in 2 orbits of 1008 (G1);
  |U2|=9072 in 3 orbits of 3024 (G2).
- Modulo Inn(G): ordered class has 2 Inn-classes of 168 (G1) and 3 of
  504 (G2), one per pure-braid orbit with trivial stabilizer
  (168=|G1|/1, 504=|G2|/1); each full-braid orbit contains 6
  Inn-classes (one per position pattern).
- Separation: the conjugacy class of z=xy is constant on each pure
  orbit and distinct across orbits (verified computationally; braid
  moves preserve it on the ordered pattern). Over F8 the
  commutator-trace tr([x,y]) takes distinct values 2, 6, 4 on the
  three G2 pure orbits (defining-characteristic separator). For G1
  the SL(2,7)-lift commutator trace is 3 on both orbits, so
  separation there rests on the 7A/7B label.
- Joining data: every orbit member carries an explicit word in pure
  generators {a,A,b,B} joining the orbit representative to it;
  full-braid moves joining the six position patterns are exhibited.
- Geometric reading (standard framework): the (2,3,7) Hurwitz space
  of PSL(2,7) has 2 components (degrees 168/168, reduced degree 2)
  and that of PSL(2,8) has 3 components (degrees 504/504/504,
  reduced degree 3).

## Proof / evidence

Computational certification, not an abstract proof. Group tables
(168x168, 504x504) with inverses, orders, classes, and matrix lifts
are stored; auditor spot-checked inverses, 2000-sample
associativity, order relations, and F8 matrix-multiplication
consistency (all pass). Order-filtered pair search over at most
|G|^2 pairs (28224; 254016) yields N1=336, N2=1512 with the stated
z-class fibers. Pure- and full-braid BFS with xyz=1 and closure
asserts yields the stated orbit sizes; Inn-reduction by conjugation
over all g in G yields the stated class counts. Exhaustive
subgroup-closure generation re-run for ALL pairs: 0 failures.
F8 commutator traces recomputed from stored lifts: 2/6/4 match.
Replay script `output/artifacts/verify.py` re-enumerates N,
re-checks generation, re-runs pure-braid BFS, and checks
z-class constancy/separation.

## Limitations

- Counts are for the full union over all order-7 classes; per-type
  refinements coincide here since each pure orbit is a single
  z-class fiber.
- The braid-orbit = Hurwitz-component = Galois-orbit identification
  is the standard framework (background), not re-proved; the
  computation certifies the braid-orbit side.
- Generation via Dickson cites ATLAS maximal lists plus Lagrange
  divisibility; the independent exhaustive closure check covers
  every pair without assuming list completeness.
- No claim about higher genus or other ramification types.

## Reproducibility

Artifacts: `output/artifacts/G1.pkl`, `G2.pkl` (multiplication
tables, inverses, orders, classes, lifts), `nielsen_counts.json`,
`nielsen_G1.json` (336 pairs), `nielsen_G2.json` (1512 pairs),
`braid_census.json` (orbit sizes, reps, joining words, Inn counts,
commutator traces), `verify.py` (independent replay).

## References

- ATLAS of Finite Group Representations: L3(2)=L2(7);
  L2(8) — standard generators, maximals, classes.
  https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L27/
  https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L28/
- Macbeath Hurwitz-group classification; Singerman full regularity
  (background, e.g. arXiv:2505.02089).
- Salih, Hurwitz components of groups with socle PSL(3,q) —
  adjacent-socle precedent. https://doi.org/10.17398/2605-5686.36.1.51
- Shiina, Rigid braid orbits related to PSL2(p^2). TMJ.
  https://doi.org/10.2748/tmj/1113246941
- Jones/Zvonkin, Hurwitz groups as monodromy groups of dessins;
  MathWorld Hurwitz Bound (Klein/Fricke–Macbeath context).
