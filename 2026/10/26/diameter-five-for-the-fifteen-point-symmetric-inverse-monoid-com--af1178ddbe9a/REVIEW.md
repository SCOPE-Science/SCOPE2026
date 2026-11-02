# Independent mathematical audit

## correctness

PASS

Verified the claimed alpha and beta are actual 15-cycles. For every nonidentity power pair (alpha^i,beta^j) with 1<=i,j<=14 (196 cases), independently propagated every one of 15 candidate basepoint images through the pair and their inverses. In each case the joint action reaches all 15 points and the only globally consistent injective equivariant image is 0->0, so the common full-permutation centralizer is trivial. A partial bijection commuting with an n-cycle is a power of that cycle, so any path from the two full cycles with <=4 edges would need a noncentral common partial-bijection neighbor of an alpha power and beta power. The transitive pair action forces any nonzero common partial bijection to be a full permutation, contradicted by the centralizer enumeration. Checked the explicit path alpha -> alpha^5 -> id_{0,5,10} -> id_{2,3,9} -> beta^5 -> beta: disjoint supports and preserved orbit sets imply all five commuting adjacencies; no node equals 0 or 1. Proposition 6.13(2) of the 2012 source supplies upper bound 5. The 196 finite tests are exhaustive for degree 15, not a claim about all odd composite degrees.

## originality

PASS

Qualified PASS: Araújo–Bentz–Konieczny Proposition 6.13(2) proves only diameter in {4,5} for odd composite n; Theorem 6.16 proves 5 for odd prime powers and explicitly leaves distinct-prime odd composites open. n=15 is not a prime power. Group-only commuting-graph theorems are not lower bounds for an inverse monoid, since partial bijections create additional paths. East–Gould–Miller–Quinn-Gregson–Ruškuc 2024 investigate *right-congruence diameter* of infinite semigroups, a distinct invariant. No inspected exact degree-15 centralizer witness or equivalent theorem was found; targeted later specialized treatments remain a priority risk.

## value

PASS

The degree 15 case is the smallest natural odd composite degree with two distinct prime factors left explicitly open by the main 2012 inverse-monoid paper. An explicit five-edge geodesic and fully exhaustive centralizer obstruction settle a nontrivial finite boundary case; no paper-sized generalization is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
