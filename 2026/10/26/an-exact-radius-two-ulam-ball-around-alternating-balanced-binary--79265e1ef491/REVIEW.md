# Scientific review: alternating binary Ulam radius-two ball

**Correctness: PASS.** The greedy embedding cost in a target alternating string depends exactly on word length, equal-adjacency count, and first bit. Necessity follows from the two-deletion equal-adjacency lower bound with a separate treatment of an initial run of ones; sufficiency follows from deleting letters inside equal-symbol runs. The balanced-run composition count simplifies to the claimed quartic. An independent dynamic-programming LCS verifier checks all binary words through length twelve, but it does not replace the general proof.

**Originality: PASS, with residual literature risk.** Fleischmann et al., arXiv:2610.17910v1, define jumbled neighborhoods and give a general cardinality bound; Kong and Hagiwara arXiv:1701.03896v1 and Kong arXiv:1712.03639v2 treat general-center radius one and sorted-center arbitrary-radius Ulam balls. Full original texts were examined, and their displayed claims do not determine the precise alternating-center radius-two ball. Relevant indexed searches for alternate terminology and exact tables found no stronger covering claim. A differently named unindexed result remains possible.

**Value: PASS.** A uniform exact radius-two size and an equally uniform run-statistic membership test for a natural balanced non-sorted center sharpen the finite-parameter understanding of multipermutation Ulam balls and two-jumble neighborhoods. They are applicable as an exact local ingredient in code-ball analyses. This is not a theorem on the extrema over all possible centers.

Scientific limits: fixed balanced alphabet content for the size formula; two allowed translocations; all centers, other alphabet sizes, radii above two and global optimality remain unproved.

Self-review: passed. Independent audit: not yet performed.
