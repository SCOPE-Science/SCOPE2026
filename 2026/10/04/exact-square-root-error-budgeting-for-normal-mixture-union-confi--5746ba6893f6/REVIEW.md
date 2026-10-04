# Same-model review
## Correctness
PASS. Writing \(s_i=\sqrt{{V_i+\eta^{{-2}}}}\) and \(z_i=a_i/s_i\) turns the total boundary into \(\sum_i s_i\phi(z_i)\) with \(\phi(z)=\sqrt{{\log(\eta^2/z^2)}}\) and weighted mean \(\sum_i s_i z_i/S=\alpha/S\). For \(\alpha<e^{{-1/2}}\), every feasible point lies where \(\phi''(z)>0\). Strict Jensen convexity therefore gives the unique allocation \(a_i=\alpha s_i/S\) and the exact minimized width. The union-bound validity statement uses fixed error levels only. The square-root-rate limit follows directly from the exact formula, and the entropy term follows from a first-order expansion in \(1/\log t\). The packaged checker independently replays the algebra numerically and catches indexing or sign errors.

## Originality
PASS. The motivating paper fixes both arm levels at \(\alpha/2\) in Theorem 4.9 and then studies the effect of clock imbalance on the width comparison in Proposition 4.12; its inspected full text contains no optimization of the arm-wise error allocation. The normal-mixture source literature develops the boundary itself rather than this heterogeneous union-budget design. Generic Bonferroni weighting explains why unequal fixed allocations can be valid but does not imply the closed-form square-root clock optimizer, the exact minimized normal-mixture width, or the entropy/KL second-order penalty. Candidate-specific semantic and web searches returned no equivalent result. A mathematically equivalent convex resource-allocation lemma may exist under different terminology; that remains a stated residual risk.

## Value
PASS. The source identifies arm imbalance as a regime where its union construction can be especially attractive, yet keeps the significance split equal. The result completely solves the natural design problem created by that observation: how to prespecify a fixed union-bound budget when the arms have unequal target variance clocks. It gives an exact finite-clock optimizer, a simple square-root-rate prescription for planned asymmetric experiments, and a quantitative penalty for equal splitting. The result also makes the important validity boundary explicit: target-based prespecification is covered, post-hoc allocation from observed plug-in clocks is not.

## Closest literature and limitations
The closest source is Lindon and Kallus, arXiv:2603.25971v2 / PMLR 306 (2026), especially Theorem 4.6, Theorem 4.9, and Proposition 4.12. Howard, Ramdas, McAuliffe, and Sekhon (2021) is the underlying normal-mixture confidence-sequence reference. The new statement is limited to deterministic fixed allocations and the stated convexity regime; it does not provide a data-adaptive error-spending rule or optimize the mixture parameter.

Same-model review: passed. Independent audit: not yet performed.
