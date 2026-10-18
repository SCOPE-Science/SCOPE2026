# Self-review

**Correctness — PASS.** The stated domain guarantees a valid conditional Bernoulli model. Conditioning on latent vectors identifies the diagonal triangle moment and only nonzero cross terms (pairs sharing an edge). The spherical second- and third-moment identities determine each term exactly. Independent finite rational enumeration over a moment-matching signed-coordinate latent law checks the first and second moments for three and four vertices; arithmetic checks establish the explicit six-to-seven sign boundary. The infinite family is proved algebraically, not inferred from the finite checks.

**Originality — PASS, qualified.** Huang–Li (arXiv:2610.12765v1) and Mao–Wu–Xu (arXiv:2602.14998v1) provide the model, signed-triangle constructions, and general variance upper bounds, including overlap decomposition, but neither inspected result states the exact affine-link variance or all-sample sign reversal. Specific published-finding corpus and literature searches for the affine kernel, signed triangles, exact variance, and spherical random graph threshold found no covering claim. This is a finite-sample refinement of established methodology; an unlocated broad exact overlap identity could subsume it.

**Value — PASS.** The complete variance-ordering classification makes the relationship between geometric dependence and centered triangle noise mathematically precise, including a counterexample to monotonic variance inflation at fixed marginal edge density and a sharp natural integer boundary. This informs small-sample calibration of the signed-triangle detection statistic; it is not merely a restatement of a variance upper bound or an arbitrarily chosen parameter census.

Independent scientific review, including a priority audit, remains unperformed. Only the affine-link variance claim is assessed; no asymptotic detection theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
