# Genus-one refined floor-diagram ledger for Hirzebruch bidegree (3,4), with lambda-class series check

## Context
Bousseau's program interprets refined (Block-Göttsche) floor diagrams on
P^2 and Hirzebruch surfaces as generating series of higher-genus relative
Gromov-Witten invariants with a lambda-class insertion, after q = e^{iu}.
Concrete genus-1 evaluations at fixed bidegree are scarce. Bidegree (3,4)
on F0 is the minimal scope where a genuine cycle appears while the
combinatorics stays bounded, testing the elliptic refined-weight rule and
supplying genus-1 log-GW calibration data.

## Definitions and fixed data
Let X = F0 = P^1 x P^1, beta = 3 D0 + 4 F (bidegree (h,d) = (3,4)).
The h-transverse datum has height h = 3, d_b = 4 incoming and d_t = 4
outgoing unbounded edges of weight 1, v_l = (-1,0)^3, v_r = (1,0)^3,
so |Delta| = 2h + d_b + d_t = 14.
Point count n = 14: g_{Delta,n} = n + 1 - |Delta| = 1, bounded edges 3.
A (Delta,14)-floor diagram: weighted oriented graph with 3 vertices, 3
bounded edges, 8 unbounded weight-1 edges, acyclic with first Betti
number 1, divergence in_bounded - out_bounded = b_V - a_V =: d_V at each
vertex, sum a_V = sum b_V = 4, sum d_V = 0.
Refined multiplicity: m_BG(D;q) = prod_{bounded E} [w_E]_q^2,
[m]_q = (q^{m/2}-q^{-m/2})/(q^{1/2}-q^{-1/2}).
Marking: increasing bijection {1..14} -> V union E with A < e < B for
bounded e:A->B, e < V incoming, V < e outgoing; count per class =
#LE(rep)/|Aut(rep)|. Ledger G(q) = sum over marked iso classes of m_BG.
Any vertically stretched configuration may be used (Brugallé-Mikhalkin
independence); the census enumerates all marked diagrams.

## Result
Theorem. For the above (3,4) data with n = 14:
(a) Exactly 105 isomorphism classes of marked elliptic floor diagrams
(listed in artifacts/ledger.json with orientation, bounded weights,
(a_V),(b_V), linear-extension count, |Aut|, marking count, per-class
refined polynomial).
(b) G(q) = 6q^-5 + 96q^-4 + 798q^-3 + 4416q^-2 + 17274q^-1 + 42432
+ 17274q + 4416q^2 + 798q^3 + 96q^4 + 6q^5; G(q) = G(q^-1), G(1) = 87612.
(c) G(1) = 87612 equals the unrefined genus-1 sum over D of prod_E w_E^2.
(d) Under Bousseau Thm 5.12 with g = 1, d_b+d_t = 8, |Delta| = 14:
sum_{g>=1} N_{g,rel}^{Delta,14} u^{2g+6} = u^-6 G(e^{iu}) (2 sin(u/2))^14;
H(u) = u^-6 G(e^{iu})(2 sin(u/2))^14 = u^8(N_1+N_2 u^2+...):
N_1 = 87612, N_2 = -94913, N_3 = 3306499/60,
N_4 = -8097139/360, N_5 = 308342441/43200.

## Proof / evidence
Exact parametric census (stdlib-only census.py): 30 labeled acyclic
connected 3-edge orientations; 61 divergence triples from compositions of
4 into 3 parts; per (orientation,d) exact incidence solve Aw = d via
rational particular solution plus primitive integer null vector, merged
congruences, finite positivity interval (every 3-edge connected null
vector here mixed-sign, asserted); S3 quotient with canonical
parallel-edge weight sorting -> 105 classes; max bounded weight 4 (no
truncation). Markings via 2^14 subset-DP linear extensions divided by
full Aut order (vertex x parallel-edge x unbounded-leg permutations),
integrality asserted per class. Per-class prod [w]_q^2 summed to G(q);
symmetry asserted and verified. Independently rechecked by exhaustive
weights-1..6 brute force (separate code) reproducing 105 classes and
87612, and by auditor brute-force replay. Series via stdlib Fraction
E(u)*T(u) expansion (series.py) plus sympy cross-check; auditor
independently recomputed N_1..N_5 exactly. Part (d) cites the general
Bousseau correspondence proof; the audit contribution is the new exact
(3,4) ledger and its exact coefficient consequences.

## Limitations
- Lambda reading (d) depends on cited Bousseau Theorem 5.12 (not
reproved); comparison is at relative-with-lambda level, not absolute
log-GW numbers.
- F0 (k = 0) specialization only; F_k k > 0 not treated.
- Ledger is tied to the stated refined-weight/marking convention.

## Reproducibility
python3 output/artifacts/census.py  # -> ledger.json; prints G table; expects G(1)=87612, nclasses 105
python3 output/artifacts/series.py  # -> series.txt; exact rational N_1..N_6
Both stdlib-only.

## References
- P. Bousseau, Refined floor diagrams from higher genera and lambda
classes, arXiv:1904.10311 / Selecta 2021 (correspondence Thm 5.12).
- F. Block, q-Floor Diagrams computing Refined Severi Degrees.
- T. Blomme, G. Mével, Asymptotic computations of tropical refined
invariants in genus 0 and 1.
- Y. Ding, J. Hu, Refined floor diagrams relative to a conic and
Caporaso-Harris-type recursion.
- T. Blomme, Floor diagrams and enumerative invariants of line bundles
over an elliptic curve.
