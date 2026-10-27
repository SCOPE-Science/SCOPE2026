# Self-review

## Correctness — PASS

The claim is restricted to unweighted approval elections with candidate supporter size at most the unrounded Hare quota. The integral-core implication follows from a tight double count of approval incidences over any blocking coalition. The stronger core+ implication uses an explicit uniform positive payment and reserve certificate satisfying every constraint of Becker–Greger–Peters Theorem 3.3, including strict reserve deficiency at each losing candidate. For each positive integral quota, the three-candidate sharpness construction has a direct proof of integral-core membership and an exact feasible fractional core+ block. Cases with nonintegral quota, no supporters, and quota one are covered. The accompanying standalone program checks 10,893 eligible profile-and-committee-size configurations, 37,417 committees, and exact witnesses for quota 1 through 50. The finite checks are not the infinite proof.

## Originality — PASS (qualified)

The 2026 motivating paper proves existence of core committees in unrestricted profiles and establishes the general core+ payment criterion. It does not state the all-committees JR/core/core+ equivalence on the candidate support cap, the greedy characterization, or the one-over-quota fractional-integral separation. Published work on Lindahl priceability proves a distinct and often stronger constraint, while sparse-disapproval existence results bound the opposite side of the approval incidence graph. Searches of relevant papers and indexed research summaries yielded no implication-equivalent result. Nevertheless the positive direction has a short derivation from the 2026 payment certificate, and pre-existing variants under sparse hypergraph terminology remain a historical-priority risk; novelty is not certified independently.

## Mathematical value — PASS

The Hare quota is the natural threshold for cohesive voter groups and simultaneously bounds candidate incidence capacity. At that exact threshold, a generally LP-defined, stronger fractional fairness property collapses to a basic combinatorial JR test **for every committee**, supplying a simple exact recognition and construction algorithm. The separation from the integral core with only one above-quota candidate, three candidates total, and every integral quota establishes a sharp boundary rather than a cosmetic increment. This informs when the fractional fairness hierarchy has substantive content.

## Limits and comparisons

Only the explicitly stated quota-capped election domain is characterized. Above it, the witness refutes uniform collapse but does not imply that core+ is absent. The payment-system equivalence is a cited prior theorem. Complete historic priority and external mathematical auditing are outstanding. Main comparisons: Becker–Greger–Peters (arXiv:2609.11912), *On the Edge of Core (Non-)Emptiness* (arXiv:2512.16895), *Sparse Disapproval Guarantees a Nonempty Hare Core* (arXiv:2609.04537), and *Justified Representation: From Hare to Droop* (arXiv:2508.00811).

Self-review: passed. Independent audit: not yet performed.
