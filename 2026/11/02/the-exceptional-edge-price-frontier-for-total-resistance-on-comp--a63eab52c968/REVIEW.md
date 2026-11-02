# Scientific assessment: priced-edge resistance design on complete graphs

## Correctness — PASS
The weighted Laplacian spectrum follows by decomposing vectors into the distinguished-pair difference, remaining-vertex contrasts, and the between-block mode. The Kirchhoff index is \(n\) times the sum of inverse positive eigenvalues. Strict convexity of the inverse-trace objective and price-preserving symmetries force the unique unrestricted solution to have three edge classes. A sharp weighted Cauchy–Schwarz certificate gives the low-price allocation, and its feasibility is equivalent to \(\tau\le n/(n-2)\). At the threshold the exceptional edge vanishes. A cost-comparison/scaling argument proves that any positive use of that edge is strictly suboptimal at higher prices. Exact and numerical checks in the package independently test formulas, gradients and full matrices. Analytical quantifiers: every integer \(n\ge4\) and every \(B,\tau>0\).

## Originality — PASS, qualified
The 2006 and 2008 Ghosh–Boyd–Saberi primary texts contain general convexity/KKT and equal-price complete-graph results, but not the exceptional-price threshold or the three-class closed form. Bhoite and coauthors' 2026 primary text provides cost-sensitive optimization for a different base-network augmentation setting and general marginal-benefit conditions, not the exact present one-edge phase diagram. Search comparisons against mathematical research records and accessible earlier claims detected related graph optimization but no statement implying the present all-parameter result. Closest accessible related formulations do not dominate the new theorem. Remaining risk: an earlier specialized heterogeneous A-optimal design treatment may include this case, and search non-detection is not proof of uniqueness in the literature.

## Value — PASS
A dense complete network has redundant direct links, but it is not evident how much more expensive one link must become before deleting it is optimal when all other capacities may rebalance. The exact sharp price threshold \(1+2/(n-2)\) answers that design question for every network size, and shows that the price premium needed for deletion decays with size. The exact allocation, retained-edge positivity and quadratic transition provide more than a small finite calculation or a mere restatement of convexity.

## Scope and outstanding checks
Independent examination of the mathematical proof and a comprehensive historical priority audit remain unperformed. The result makes no claims about other objective functions or several price anomalies. Numerical comparisons corroborate but do not replace the proof.

Self-review: passed. Independent audit: not yet performed.
