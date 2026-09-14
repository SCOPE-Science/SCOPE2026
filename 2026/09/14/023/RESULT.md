# Realizability of the genus-0 degree-12 Belyi passport (4-2-2-1^4, 6-3-2-1, 6-4-2)

## Record statement
The genus-zero degree-12 Belyi passport
P2 = ([4,2,2,1,1,1,1], [6,3,2,1], [6,4,2]) over {0, 1, infinity} is realizable
over C by a connected cover f: P^1_C -> P^1_C of degree 12 branched only over
{0, 1, infinity} with exactly these ramification partitions.

## Context
The admitted target asked to decide the realizability of this fixed passport:
either exhibit an explicit transitive triple in S12 with the stated cycle types,
product 1, and transitive monodromy (with braid/Galois data), or give a rigorous
group-theoretic or arithmetic obstruction. The question is a Hurwitz-existence
instance: the Riemann-Hurwitz numerics are satisfied (7+4+3 = 14 parts;
deficits 5+8+9 = 22 = 2*12-2), but that condition is only necessary, so an
explicit witness or obstruction theorem is required.

## Definitions
A Belyi passport of degree n records the three ramification partitions above
0, 1, infinity. A transitive triple (t0, t1, tinf) in Sn with t0*t1*tinf = 1
and transitive subgroup H = <t0, t1, tinf> corresponds, by the Riemann existence
theorem, to a connected degree-n cover of P^1 branched only over {0,1,infinity}
with the matching ramification. Cycle type lists the orbit lengths including
fixed points. The monodromy group H is identified up to conjugacy in Sn.

## Result
P2 is realizable over C. An explicit transitive triple on {0,...,11}, written
as one-line images, is:

- t0 = (0,2,1,8,4,11,3,7,9,6,10,5), cycles (1 2)(3 8 9 6)(5 11),
  type (4,2,2,1,1,1,1), order 4;
- t1 = (9,0,8,2,3,4,6,5,7,1,11,10), cycles (0 9 1)(2 8 7 5 4 3)(10 11),
  type (6,3,2,1), order 6;
- tinf = (1,3,9,6,5,10,0,8,4,2,11,7), cycles (0 1 3 6)(2 9)(4 5 10 11 7 8),
  type (6,4,2), order 12.

The generated group H has order 12! = 479001600, is transitive and primitive,
hence H = S12. Signs are (-1,+1,-1), consistent with S12 and ruling out A12.
Census context: with the first generator fixed, exhaustive enumeration finds
532032 raw solutions (374784 transitive) in 831 simultaneous-conjugacy classes;
the full Hurwitz action gives 831 orbits of size 6 (the 3! branch permutations),
so each ordered-passport pure-braid orbit has length 1. The seed triple lies in
class 229 with monodromy S12; 488 of the 831 classes have H = S12. All three
branch classes are rational (power-conjugacy test), which is necessary but not
sufficient for field of moduli Q.

## Proof / evidence
Exact integer-arithmetic checks, independently re-executed by the auditor:
(1) cycle types equal the passport partitions exactly;
(2) t0*t1*tinf = identity under left-to-right map composition;
(3) BFS orbit of 0 under the generators and inverses is all 12 points;
(4) Riemann-Hurwitz deficits sum to 22, hence genus 0;
(5) Schreier-Sims (sympy) gives |H| = 479001600 with transitivity and
primitivity, so H = S12; a 12-cycle word in the generators was also found.
By the Riemann existence theorem this triple certifies a connected genus-0
degree-12 Belyi map with passport P2 over C; no group-theoretic obstruction
over C occurs. Census aggregates were cross-checked against stored arrays
(raw shape (532032,12), 831 class representatives, class-size distribution
{192:1, 384:275, 768:555}, 488 transitive representatives, matching
group-order table).

## Limitations
Existence is proved over C via Riemann existence only. No certified Q-model
(polynomials P, Q) is claimed: normalized numerical solves converged only to
fiber-collided degenerate configurations within budget. The field of moduli is
not determined (rational branch classes are necessary but not sufficient; the
Galois action on the 831 ordered classes was not computed), and the
descent/Brauer question is left open. Group-order computations for the full
census depend on sympy Schreier-Sims; all other headline checks are
dependency-free integer arithmetic.

## Reproducibility
Run `python3 output/artifacts/verify_certificate.py` (dependency-free): it
checks cycle types, product identity, transitivity, and genus from the three
one-line permutations. With sympy installed, the same file optionally checks
|H| = 479001600, transitivity, and primitivity. Original census scripts are
summarized, not copied in full, because the raw arrays exceed the public
package size limit.

## References
- J. Sijsling, On computing Belyi maps, Publ. Math. Besancon (2014).
- F. Pakovich, Hurwitz existence problem and fiber products, arXiv:2408.10874.
- N. M. Adrianov, Belyi functions of the special weighted trees of (2,3)-type,
  arXiv:2401.00183.
- LMFDB Belyi maps database (degrees 1-9 at time of audit).
