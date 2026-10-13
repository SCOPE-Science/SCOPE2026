# Scientific review: exact ternary length-five deletion covering

## Correctness — PASS

The claim concerns the precise incidence relation between 243 possible length-five centers and 81 length-four targets, with repeated outcomes in a deletion shadow counted once. Seven explicit prototypes and their three global translations give 21 distinct centers. Their 27 normalized four-symbol descendant orbits are pairwise disjoint and exhaustive, so this is a partition rather than merely a covering. For the lower bound, ten disjoint symmetry orbits of the targets carry stated nonnegative integer weights totaling 468. The 25 orbits of centers have respective shadow-weight sums explicitly listed in the proof; their maximum is 23. The covering sum inequality therefore gives a lower bound of 21. A standard-library verifier reconstructs every orbit and checks all 243 center inequalities and 81 target coverage assertions. No floating-point solver output is needed for correctness.

## Originality — PASS, with residual risks

The exact statement and its implication from possible stronger earlier results were compared with Xie–Sun–Ge (2026, complete 14-page text), Lenz–Rashtchian–Siegel–Yaakobi (2019/2020, full article), Chee–Ge–Ling (2010, theorem scopes and relevant sections), and Afrati et al. (2014, definitions and pertinent constructions). Xie–Sun–Ge and Lenz et al. prove bounds/asymptotics, not the fixed exact value; Chee–Ge–Ling's main perfect-code spectra concern different lengths and deletion numbers; Afrati et al. reverse the insertion/deletion *naming convention* for the same direction of covering but give no exact 21-value certificate. The Houghten/Baker/Flack variable-length insertion-deletion *error-correcting* table tracks a different invariant. A relevant published finite deletion-correcting result for five symbols and length four has different parameters and optimizes packing, not this covering number. Results from alphabet-size three length-four *insertion* covering are not implied by, nor imply, the current ternary length-five deletion-covering problem. Residual risks include a historical unindexed finite table, an earlier equivalent perfect-code construction, and one old thesis whose indexed excerpt was accessible but whose full PDF was not; nonaccess is not treated as evidence of noncoverage.

## Value — PASS

This settles a canonical finite synchronization-error covering invariant for the first reasonably sized ternary length-five test case. The elementary shadow-size bound yields only 17 centers, versus the exact minimum 21. The upper construction is a complete partition of all 81 deletion descendants; the lower certificate is compact, integral, symmetry-reduced, and independently recheckable. Its exact value is useful as a benchmark for covering-dual relaxations and nonbinary finite code constructions, without requiring an unrelated general theorem. No claim is made about larger parameters.

## Sources, boundaries, and risks

Principal sources: https://arxiv.org/abs/2606.15379 (sections I, V); https://arxiv.org/abs/1911.09944 (definitions, lower/upper bounds, single-deletion construction); https://arxiv.org/abs/1008.1343 (perfect deletion-code spectra for other parameters); https://www.openproceedings.org/2014/conf/icdt/AfratiSRRSU14.pdf (terminology and general constructions); https://www.cosc.brocku.ca/~shoughten/insdel.html (variable-length minimum-distance table, distinct invariant). The possible existence of an earlier unindexed exact finite table is not excluded. The result has had no independent audit.

Self-review: passed. Independent audit: not yet performed.
