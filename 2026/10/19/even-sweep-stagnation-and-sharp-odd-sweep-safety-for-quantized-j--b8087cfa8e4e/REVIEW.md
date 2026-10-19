# Mathematical review

**Correctness — PASS.** The correction polynomial is reconstructed directly from the zero-start inner recurrence. Symmetry reduces every error mode to a real scalar. A discrete convexity/chord inequality establishes the uniform sharp norm bound for odd sweep counts, and the endpoint eigenvectors establish both sharpness and failure at the longer-sweep threshold. The binary midpoint calculation is exact. The included rational checker independently multiplies actual small graph matrices; finite tests are only supporting evidence. No extrapolation from sampling is used.

**Originality — PASS on the inspected record, with bounded residual risk.** The 2026 matrix-splitting paper provides the algorithm and a restart equivalence for the unperturbed splitting, not the quantized-operator odd/even phase result. Earlier multigrid work explicitly recognizes loss of definiteness under storage quantization, and classical Neumann iterations give the truncated polynomial, so neither ingredient is new. The combined quantified Perron-mode annihilation, sharp uniform odd-sweep safety inequality, power-of-two-degree binary realization, and bipartite convergence boundary were not located in inspected primary texts or semantic research-record searches. A possible older specialization in polynomial preconditioning remains a limitation; novelty is not inferred from search silence alone.

**Value — PASS.** The result explains a real design decision in restarted low-precision stationary correction: longer inner runs can completely remove the useful correction in a graph Perron mode despite exact residual refreshing. It gives a sharp safe inner-sweep policy for a natural family of SPD sparse systems and quantifies both rate preservation and instability boundaries. The result is structural, not an arbitrary small numerical example.

**Closest literature.** Lindquist et al. (arXiv:2610.06414, Section 2.1), Tamstorf et al. (arXiv:2007.06628, Sections 1 and 4), Suzuki and Iwashita (arXiv:2505.20719, Sections 3–4), and Zhang and Trogdon (arXiv:1909.07506, Sections 1–3). Standard Neumann and spectral-theorem components are acknowledged explicitly in RESULT.md.

**Limitations and residual risk.** The exact-arithmetic-after-storage idealization does not certify an IEEE hardware run with additional operation rounding. The source quantization boundary entails large condition numbers; no universal well-conditioned failure is claimed. Independent bibliographic and mathematical audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
