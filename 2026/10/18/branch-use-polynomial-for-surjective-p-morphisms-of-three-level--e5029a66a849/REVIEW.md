# Self-review

## Correctness — PASS

The theorem fixes finite labeled rooted tree posets with three levels and positive branch sizes, and specifies the order-preserving back condition as equality of principal upsets. The proof forces source root and leaf images, excludes a source middle vertex mapping to the target root, and exhausts the two legal local branch behaviors. Surjective leaf maps above a chosen target middle vertex are counted by the inclusion–exclusion Stirling expression. Choices on distinct source branches are independent; root back-surjectivity holds precisely when all target middle vertices are used. This bijection proves the polynomial coefficient and global inclusion–exclusion formulas with explicit quantifiers. `verify.py` directly enumerates maps for 50 small cases and separately checks a subset DP on 13,260 cases. No finite calculation is presented as a proof of the infinite family.

## Originality — PASS

De Jongh and Yang (2011, Definition 1.1, Section 3) supply the classical frame semantics and Jankov context, not the stated count. Rzążewski and Stronkowski (2025, Section 5, Theorem 5.1 and Lemma 5.4) solve the stronger *decision* problem for all source tree posets; accordingly the existence test here is not counted as original. Their proof/algorithm do not state the numeric number or the multivariate fiber distribution. Benjamins, Bezhanishvili and Moraschini (2026, Section 2.3) give a general quotient-kernel equivalence but not a closed enumeration for source and target branch profiles. Search terms checked included `surjective bounded morphisms height three rooted tree Kripke frames exact counting Stirling numbers inclusion exclusion`, `number of p morphisms finite rooted posets finite trees rank 2 counting`, `"number of surjective p-morphisms" finite`, and `"p-morphisms" "Stirling" posets`, plus equivalence- and branch-profile-related variants. No exact published numeric coefficient enumerator was found; equivalent unindexed prior work remains a residual risk.

## Mathematical value — PASS

The count is an exact natural invariant of a finite Kripke-frame quotient problem, whose qualitative existence is prominent in decision algorithms and Jankov semantics. It covers all irregular positive branch profiles at the first depth with two independent kinds of branch images and records a meaningful distribution absent from yes/no algorithms: how many source centers collapse to target leaves and how many cover each target center. This yields exact multiplicity information relevant to finite Heyting-algebra embeddings and p-morphism quotient counts; the theorem does not require a conjectured downstream application or a paper-sized contribution. The easy existing sorted-size feasibility condition is explicitly not marketed as the finding.

## Sources and limitations

Read: the author manuscript of de Jongh–Yang (definition and Jankov sections); Rzążewski–Stronkowski's arXiv primary full text, especially Theorem 5.1, Lemma 5.4, algorithm and references; Benjamins–Bezhanishvili–Moraschini's manuscript (finite duality and E-partition theorem). Closest prior science makes Boolean existence efficient for trees, and the general partition characterization supplies conceptual background; neither implies a displayed exact numerical formula without further counting arguments. The result is restricted to labeled three-level rooted trees, and unindexed equivalents may exist. Independent verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
