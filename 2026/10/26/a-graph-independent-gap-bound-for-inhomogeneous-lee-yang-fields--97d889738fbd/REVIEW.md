# Review

### Correctness

**PASS.** The uniform-field proof's zero-free polynomial is still zero-free on the unit polydisc. With \(h_* = \min_i h_i\), the physical vector \(y^*_{i,m}=e^{-2\epsilon h_i}\) obeys \(|\lambda y^*_{i,m}|\le e^{-\epsilon h_*}\) on \(|\lambda|=e^{\epsilon h_*}\). This preserves the logarithmic bound and the exponential correlation rate. The Trotter comparison uses \(\Gamma=3W+\sum_i h_i\), and the field term commutes with the diagonal insertions. The low-energy spectral argument then gives the stated \(h_*/4\) gap. No numerical evidence is used as proof.

### Originality

**PASS, within the inspected literature.** The closest direct source, Rayudu–Takahashi (arXiv:2607.10765), states the result for a uniform longitudinal field. Its proof is inspected in the full HTML text, including the correlation-decay and spectral-gap arguments. The field-profile extension requires controlling a nonconstant evaluation vector coordinatewise. Searches of an indexed mathematical-findings corpus for the exact claim and its aliases returned no matching finding. Wong et al. (arXiv:2602.03605) discuss Lee–Yang radii and EPR-like Hamiltonians, while Björnberg–Ueltschi study transverse fields; neither inspected statement covers this claim. Residual risk: an unindexed source may already contain the same extension, or the extension may be regarded as a short corollary of the 2026 proof.

### Value

**PASS.** The theorem removes the uniformity restriction on the external field and covers arbitrary positive spatial profiles, including inhomogeneous or disordered fields, while keeping a lower bound independent of graph size and interaction strength. The dependence on \(h_*\) is explicit and identifies exactly how the guarantee degrades as the weakest field approaches zero.

### Closest literature and limitations

- Rayudu and Takahashi, “Spectral gap of Lee-Yang Hamiltonians,” arXiv:2607.10765v1 (2026): uniform-field theorem and proof method.
- Wong, Bravyi, Gosset, and Liu, “Lee-Yang tensors and Hamiltonian complexity,” arXiv:2602.03605v1 (2026): Lee–Yang tensor radii and EPR-like Hamiltonian gap questions, not a positive site-dependent longitudinal-field bound.
- Björnberg and Ueltschi, “Decay of transverse correlations in quantum Heisenberg models,” *J. Math. Phys.* 56 (2015), 043303: transverse-field correlation decay, a different direction and observable class.

The result is finite-volume, assumes every field is strictly positive, and does not establish optimality of the constant.

Self-review: passed. Independent audit: not yet performed.
