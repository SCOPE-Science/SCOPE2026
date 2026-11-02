# Self-review

**Claim.** Complete EJR-1 spectra and a sharp cost-premium boundary in symmetric participatory budgets. The theorem gives exact cost-EJR-1 and cardinality-EJR-1 characterizations for all feasible outcomes in a natural two-tier approval-budget family, then an exact compatibility threshold and sharp private-bundle deficit.

## Correctness — PASS

The proof explicitly fixes the integer domain, budget, approval sets, strict hypothetical-augmentation convention and the non-exhaustiveness allowance. The full voter group and all common projects force cost-fair outcomes to fund all or all but one common project; converse coalition checks cover singletons and every multi-voter group. Cardinal fairness reduces to singleton private-bundle quotas and the worst group of each size, which is represented by ordered satisfaction scores. Feasibility yields the sharp premium threshold. An independent direct-quantifier enumeration with `verify_ejr1.py` checked 63,191 feasible outcomes across 13 parameter pairs; all characterizations, counts, compatibility results, and deficit extrema agreed. The infinite-family claim rests on the provided proof rather than these tests.

## Originality — PASS (best-knowledge, with residual priority risk)

Brill et al., arXiv:2302.03672, Proposition 3.6 already prove qualitative incompatibility using the special case with two voters and premium five. This precedent is openly credited, and the incompatibility phenomenon itself is not claimed as new. Its inspected statement and proof do not provide the complete outcome criteria, exact cost-fair count, all-size sharp premium threshold, or optimum singleton shortfall. Peters, Pierczyński and Skowron, arXiv:2008.13276, establish single-satisfaction proportionality guarantees, not simultaneous-fairness classification. Searches for synonymous formulations and dominating results in published mathematical records did not identify equivalent coverage. Abstract-only later sources remain residual priority risks, and a negative search is not proof of novelty.

## Mathematical value — PASS

The problem is motivated by an explicit published conflict between two natural proportionality measures; the symmetric family models a choice between common capital-intensive projects and locally approved inexpensive projects. The complete classification identifies exactly when strong fairness objectives can agree, gives a sharp premium-to-electorate ratio rather than one numerical counterexample, and quantifies the unavoidable loss if the cost-based requirement is prioritized. The sorted-score test also turns an exponential coalitional axiom into a direct finite check for this family. These are natural structural consequences and a meaningful compatibility boundary, not merely recomputation of the published example.

## Closest literature and limitations

- Brill et al. (2023), Proposition 3.6: a single two-voter, five-premium incompatibility witness; subsumed by the present family, but no exact parameter phase diagram in the inspected proof.
- Peters et al. (2020/2021): existence and algorithmic guarantees for one satisfaction measure; the present theorem compares two measures on the same outcome.
- Baharav et al. (2026), arXiv:2609.02030, and Skowron (2026), arXiv:2610.15516: related recent proportionality work inspected at abstract level only, so substantive uninspected priority risk remains.
- Applicability is restricted to the indicated symmetric family and the exact EJR-1 convention; no general-purpose social-choice rule or independent external verification is claimed.

Self-review: passed. Independent audit: not yet performed.
