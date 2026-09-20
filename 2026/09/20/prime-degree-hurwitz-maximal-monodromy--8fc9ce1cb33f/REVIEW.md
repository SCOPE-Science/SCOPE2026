# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The local lemma is exact. If a partition contains one part q and no other part divisible by q, raising a permutation of that type to the least common multiple of the other parts fixes every other cycle and leaves a q-cycle. Conversely, if a power is exactly one q-cycle, the cycle-power decomposition forces the supporting original cycle to have length q exactly once, while every other cycle length divides the exponent; because the q-cycle remains nontrivial, that exponent is not divisible by q, so no other part is divisible by q.

For a connected degree-p realization, monodromy is transitive and hence primitive because p is prime. Jordan's theorem then applies to the q-cycle with q<=p-3 and gives A_p<=G<=S_p. The sign identity sgn(sigma)=(-1)^{p-l(Λ)} makes the A_p/S_p dichotomy intrinsic to the passport. These arguments apply to every connected realization, not only to the realization furnished by the existence theorem.

The deck-group claim follows from the standard quotient description by a point stabilizer H in the Galois closure: N_G(H)=H in the natural A_p or S_p action because H has a unique fixed letter. The Galois-closure genus formula is the standard Riemann--Hurwitz formula with inertia order lcm(Λ_i).

Both displayed degree-seven examples were recomputed directly. For (3,2,2)^3, total defect is 12, G=A_7, inertia orders are 6,6,6, and the closure genus is 631. For ((5,2),(5,2),(3,1,1,1,1)), the defects are 5,5,2, G=S_7, inertia orders are 10,10,3, and the closure genus is 1177.

## Originality

**PASS, to the best of our knowledge.**

Song--Wen--Zhang, arXiv:2609.20572v1, was inspected directly. Their Theorem 1.1 proves realization of every compatible prime-degree branch datum, and their Section 2 records the transitive monodromy criterion. The accessible text does not state a Jordan-cycle criterion, an A_p/S_p passport dichotomy, trivial deck groups on such a locus, or a normal-closure genus refinement; searches within the paper for “Jordan”, “alternating”, “symmetric”, “Galois closure”, and “automorphism” returned no occurrences.

The Jordan step itself is classical and is not claimed as new. Neumann (1975) is a standard reference for primitive groups containing prime-power cycles. Cadoret (2005) provides an important prior-context check: in a Hurwitz-space construction, she explicitly uses that a transitive group of prime degree is primitive and that the presence of a 3-cycle forces alternating monodromy. This shows that the group-theoretic method in a Hurwitz setting is established prior art.

Broader searches covered prime-degree branched covers, passports and branch cycles, Jordan's theorem in monodromy arguments, full alternating/symmetric monodromy, and ramification-profile formulations. They located classical and modern applications of Jordan's theorem, but no statement combining the 2026 universal realizability theorem with the exact local partition criterion q occurs once and no other part is divisible by q, nor the resulting forced-monodromy theorem for every connected realization.

No inaccessible paper was identified as specifically likely to contain the exact new combination. Neumann's original article was bibliographically located but its full text was not required for novelty because Jordan's theorem is treated here as prior work. The principal residual risk is the recency of the Song--Wen--Zhang preprint: a later revision or an unindexed parallel observation could add the same corollary.

## Value

**PASS.**

The result upgrades a broad existence theorem into an explicit Galois-group rigidity theorem on a readily checkable passport locus. It determines the monodromy of every connected realization from the partition data alone, not merely of one constructed cover. This immediately fixes the Galois-closure degree and genus, removes deck stabilizers, and specializes to explicit A_p and S_p Belyi passports.

The local criterion is reusable and exact at the cyclic-inertia level: it characterizes precisely when a prescribed ramification profile itself contains a small prime cycle after taking a power. This creates a clean bridge from partition combinatorics to global monodromy through primitivity and Jordan's theorem.

## Limitations

- The Jordan-visible condition is sufficient but not necessary for maximal monodromy.
- The result does not classify passports whose monodromy is a smaller transitive subgroup of prime degree.
- The normal-closure genus calculation is standard once G is known.
- Jordan's theorem and earlier Hurwitz-space applications of it are prior work.
- The source existence theorem is a very recent preprint, leaving residual revision and parallel-work risk.
- Independent audit has not been performed.
