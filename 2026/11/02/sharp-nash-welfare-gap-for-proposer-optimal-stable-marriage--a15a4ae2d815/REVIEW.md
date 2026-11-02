# Scientific review

## Correctness — PASS

The claim is for every integer \(n\ge2\), every strict complete balanced preference profile, and exactly the positive utilities \(n-r\). Men-proposing Gale--Shapley is man-optimal among stable matchings, so each changed man's ratio is at most \((n-1)/n\), while each changed woman's is at most \(n\); bijections make the numbers of changed men and women identical. The product bound follows with equality conditions tracked factor by factor for \(n\ge3\). A cyclic construction attains the upper bound for every \(n\). First/second and first/last ranks characterize equality and identify both relevant matchings uniquely; derangement enumeration counts each labeled extremal profile once. Positive utilities avoid zero denominators. Independent blocking-pair enumeration confirms all \(46{,}656\) labeled \(3\times3\) profiles, with 12 extremizers, and all 16 two-pair profiles. The analytic proof, not the finite program, covers all \(n\).

## Originality — PASS, with residual risks

The original full-text preprint by Desai et al. [1], including its main formal results, algorithms, computational evaluation, conclusion and relevant appendix material, was examined. It establishes maximization of NSW *within* stable matchings, not a tight universal performance ratio for the specific men-proposing Gale--Shapley baseline. Jain--Vaish [2] concerns different two-sided matching optimization without the same stability constraint. Published small-market stable-marriage census and fairness-conflict results concern other invariants and objectives. A comparison of Nash-product maximizers against minimum-regret stable matchings concerns a different objective from the DA approximation ratio. No inspected primary statement implies the combination of the all-size factor, equality classification and exact labeled count. Relevant unindexed work and full texts of some related database records remain possible novelty risks; searches alone do not certify universal absence.

## Value — PASS

The motivating work makes rank-derived Nash welfare an explicit stable-matching objective and provides an optimal algorithm. Quantifying how much NSW that standard men-optimal DA algorithm can lose is a natural algorithm-comparison question, with the exact multiplicative gap growing as \(\sqrt{n-1}\). The construction establishes unavoidable loss, while the necessity theorem and profile count locate all worst cases and their rarity under impartial culture; this is a structural benchmark, not an arbitrary small invariant or purely computational census.

## Closest literature and limitations

[1] P. Desai et al., *Fair Stable Matching: A Nash Social Welfare Approach*, arXiv:2609.02354v1 (2026-09-02). [2] P. Jain and R. Vaish, *Maximizing Nash Social Welfare under Two-Sided Preferences*, arXiv:2312.09167 (2023), AAAI 2024. Two closest published published-finding corpus records are the three-by-three stable-marriage full-symmetry census and the rank-maximal/sex-equal conflict census. Only complete strict balanced preferences and utility \(n-r\) are covered. Exhaustive tests stop at \(n=3\), despite the general analytic proof. The absence of an independent audit must not be confused with a certification of priority.

Self-review: passed. Independent audit: not yet performed.
