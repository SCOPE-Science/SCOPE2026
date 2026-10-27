# Self-review

## Correctness — PASS

The theorem uses the exact reflecting mean-field equation of Cao and Gong for every integer \(k\ge1\). The proof separately verifies that the cumulative-coordinate system is cooperative, that reflection forces the mean to remain nonpositive, and that the initially nonpositive distribution is dominated by its unbiased reflecting counterpart. The neutral chain's explicit first eigenfunction has a strictly positive projection from every permitted nontrivial initial distribution, giving eventual strict stochastic domination by the uniform equilibrium. An all-\(k\) discrete-parabola subsolution then prevents that domination from collapsing. The exact positive-coefficient polynomial in the geometric frozen-chain comparison excludes any negative limiting mean other than \(-k\). This is an analytic proof; the independent verification script checks finite instances but is not used to infer the infinite statement.

## Originality — PASS, provisional historical priority

Cao and Gong (arXiv:2605.28984v1, May 27, 2026) explicitly pose the proved one-sided-support conclusion as an expectation requiring proof, while their stated attraction theorem requires an initial mean close to an extreme. The present conclusion covers all distributions supported on one side of zero, including those with average arbitrarily close to zero. Discrete Incremental Voting (arXiv:2606.06381) uses direction-of-difference interactions instead of probability-biased steps, and the earlier Cao–Reed persuasion/repulsion paper has different update rules. Earlier related statements about local uniform-state eigenvalues or relaxation *conditional on a selected extreme* do not imply which extreme is selected. A search of mathematical records and relevant literature revealed no equivalent or dominating basin theorem. This search does not prove uniqueness; monotone mean-field birth–death comparison results elsewhere remain a priority risk.

## Mathematical value — PASS

The result resolves a specific, explicitly proposed conjecture on basin selection in a new opinion-dynamics system, for an infinite sequence of opinion-space sizes and an infinite-dimensional family of initial distributions across them. It replaces a near-extreme mean threshold with a sharp qualitative initial-support criterion, distinguishes exactly the exceptional all-zero initial datum, and provides an all-\(k\) method using order, spectral positivity, and a strictly improving frozen-chain stationary mean. The full mixed-sign initial-data basin remains outside the claim.

## Sources and limitations

Primary inspected source: Cao and Gong, arXiv:2605.28984v1, equations (1.1), (2.1), Section 3.2 and Section 4. Related complete accessible model description: Berenbrink et al., arXiv:2606.06381, introduction and formal protocol. Cao and Reed, doi:10.1137/24M1700661, abstract and MSC classification were accessible, but the publisher's full text was restricted. The verification script checks exact identities for finitely many \(k\) and illustrative numerical trajectories; it does not replace the general proof. Historical priority and proof are not independently audited.

Self-review: passed. Independent audit: not yet performed.
