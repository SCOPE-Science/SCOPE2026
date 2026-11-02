# Self-review

## Correctness

**PASS.** The proof reduces arbitrary nonempty binary ballots to singleton approvals without reducing attained utilities, balances the three possible minority types using an explicit two-case switch formula, and Pareto-completes the result. It checks all three possible coalition sizes against their exact floor quotas. Exact-integer direct coalition enumeration and independent utility-vector dynamic programming confirmed 31,464 unordered full-ballot round profiles through four rounds, 1,715 additional seven-type profiles through six rounds, and 900 seeded additional cases. Infinite-horizon validity is analytical; finite checks are not substituted for proof.

## Originality

**PASS under self-review, with stated priority risk.** Phillips et al. (2025), Section 6 and its appendix, introduce the same strong-core criterion and establish its general failure, but do not state the three-voter binary positive result. Their existence results for EJR+/FJR and their sFPJR serial dictatorship do not imply existence of the stronger sCore. Masařík et al. (2023) study broader feasibility constraints and distinct proportionality guarantees, not this strong temporal-core claim. Existing JR/PJR analyses are logically weaker. Actual targeted mathematical-record and literature searches found no equivalent all-horizon result; their failure to find a match is not proof of universal priority.

## Value

**PASS.** Strong temporal core stability is a motivated, usually unsatisfiable demand, and the result gives an exact positive structural domain with arbitrary time variation and a polynomial constructive algorithm. The substantive ingredient is simultaneous coverage of both single-voter and two-voter proportional quotas followed by Pareto completion, not a finite enumeration or a renaming of a known weaker axiom.

## Closest literature and limitations

- Phillips et al., *Strengthening Proportionality in Temporal Voting*, arXiv:2505.22513v1, Section 6, Definition 6.1, Proposition 6.2, and relevant appendix examples.
- Masařík et al., *A Generalised Theory of Proportionality in Collective Decision Making*, arXiv:2307.06077, introduction and public-decision model.
- Chandak et al., *Proportional Aggregation of Preferences for Sequential Decision Making*, arXiv:2306.14858, abstract and stated JR/PJR results.

The statement does not cover more than three voters, more than two alternatives, or empty approval ballots. Unindexed equivalent formulations are a residual priority risk; no independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
