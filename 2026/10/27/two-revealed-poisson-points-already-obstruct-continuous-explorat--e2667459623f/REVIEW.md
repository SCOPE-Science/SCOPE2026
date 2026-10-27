# Scientific review

**Correctness: PASS.** The eight-word cylinder property, together with first-point prefixes, proves the full stopping property for arbitrary locally finite configurations. Diffuse Poisson simplicity and the count table imply at most two exposed points. On the positive-probability empty configuration the target occupies exactly two specified cells; intensity continuity forces any attempted exploration to start by visiting one of them. A positive-probability contrasting configuration agrees on the initially explored region but requires completely omitting that cell. Observed-history stopping-time adaptivity then contradicts equality even modulo intensity. The accompanying finite-state checker was run and passed; the continuum conclusion relies on the explicit analytical proof.

**Originality: PASS, with residual risk.** Khezeli's one-point attainment theorem is directly relevant and does not claim a two-point extension. Last–Peccati–Yogeshwaran Appendix B already demonstrates nonattainability, but its explicit three-cell example can reveal unboundedly many Poisson points and chiefly addresses ultimate-union attainment. The present construction imposes a two-point bound and proves nonattainment even at an observed-history stopping time. Targeted record and literature searches did not identify a dominating bound of this form; a logically equivalent unindexed example would defeat originality.

**Value: PASS.** The construction settles the first missing cardinality case and establishes that the attainable one-point regime has the optimal revealed-point bound. The failure persists under compactness, diffuseness, three cells and positive-probability finite realizations. This is a structural boundary of a recent theorem, not a routine numerical alteration.

**Closest prior literature:** Ali Khezeli, arXiv:2610.22011v1 (2026-10-15), Theorem 1.3 and Definition 4.1; Last, Peccati and Yogeshwaran, arXiv:2101.07180v3, Appendix B. The older Appendix B construction is nonattainable without a two-point bound and requires care when comparing ultimate unions with stopped equality.

**Limitations and risks:** No independent assessment has occurred; the search cannot guarantee that no equivalent construction is contained in all other point-process literature. No non-continuous exploration claim. Finite code checks do not establish the infinite-dimensional impossibility.

Self-review: passed. Independent audit: not yet performed.
