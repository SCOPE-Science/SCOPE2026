# Review of nearest-neighbor delegation loss

## Correctness
**PASS.** The claimed optimum follows from an exact orbit-length identity, explicit component formulas for one- and two-vertex directed cycles on a path, endpoint minimization of sums of decreasing nonnegative terms, and subadditivity that merges all components. Every assumption is stated, including permissible self-delegation and exchangeability without independence. Separate finite computational enumeration of all delegation profiles and fixed-count exchangeable laws on paths of 2–9 voters agrees; exact turnout-subset enumeration agrees for paths of 2–6 voters. The infinite-domain result is established analytically, not by these enumerations. Strictness for i.i.d. \(0<q<1\) is from strictly decreasing orbit-failure probabilities.

## Originality
**PASS, subject to residual publication-priority risks.** The closest explicit predecessor is Brill et al., arXiv:2607.12610, Appendix B.4, Proposition 19, which gives an unrestricted Hamiltonian-cycle optimum for independent participation; that optimum is usually infeasible on a path. Their 2025 COMSOC paper and the expanded paper were inspected. Grossi and Nitsche, arXiv:2506.09789, analyze decay of expected influence down delegated paths but do not prove this social-path optimization or arbitrary exchangeable-turnout law. Other sources concern ranked backups, centrality, or epistemic correctness, not this exact loss-minimization problem. published-finding corpus searches and available prior claims did not reveal an equivalent or stronger theorem, but search noncoverage is not proof of priority; a related 2026 centrality paper was accessible only in summary and remains a risk.

## Value
**PASS.** Proposition 19's all-voter cyclic optimum requires unrestricted delegation. Restricting delegation to trusted immediate neighbors on a social line is a natural, qualitatively different design constraint. The exact optimal loss, sharp placement rule, and full correlation robustness quantify the representation price of locality, including the nonzero large-electorate absolute penalty under independent participation. This informs network-design tradeoffs; it is not merely a renamed fixed numeric example.

## Limits
The finding measures unrepresented voting weight, not strategic equilibrium, proportional representation, accuracy, or concentration of influence. The order-invariant turnout hypothesis is essential to the placement theorem; heterogenous independent turnout can make an interior reciprocal pair preferable. Arbitrarily correlated **exchangeable** turnout is covered. No external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
