# Scientific review

## Correctness — PASS

Every nonzero planar Kaczmarz projection lands on the line perpendicular to the chosen normalized row. The next residual power cancels its common amplitude, yielding an exact finite Markov kernel. Its symmetric edge weights give a reversible stationary distribution, so the finite-state additive ergodic theorem proves the almost-sure rate, including the periodic two-row case. A pairwise covariance formula proves the monotone power law and exact endpoints. The \(p=0\) iid kernel includes self-loops of zero logarithmic gain, producing the strict zero-power jump. Exact rational projection and stationary identities and independent seeded simulation checks were run from the supplied checker. Neither finite simulation nor code output replaces the analytical proof.

## Originality — PASS (best-knowledge, subject to independent verification)

The 2023 WRaSK source derives expected Bregman-distance bounds and studies monotonicity of a one-step bound. The 2020 Steinerberger paper gives a related expected-rate bound for residual-weighted ordinary Kaczmarz and discusses the large-power greedy limit. The 2019 adaptive sketch-and-project paper already notes that the last satisfied equation has zero residual; this is fully credited. None of their inspected theorems, proofs, discussion or appendices establishes the exact planar stationary edge law, strict pathwise exponent ordering, or universal long-time zero-power discontinuity. Searched published-finding corpus records on residual-based Kaczmarz, Markov row transitions, and equivalent angular formulas; the nearest records concern different finite-horizon cyclic, coherence and noisy-row claims. Semantic search coverage is incomplete; an unknown alternative derivation remains a residual novelty risk.

## Value — PASS

The exact pathwise rate is an evaluable, data-dependent alternative to general expected-error bounds, and the universal discontinuity reveals a singular parameter limit in an algorithm that is often described as smoothly interpolating uniform and greedy sampling. The angle-weighted stationary law and global monotonicity explain which row geometries govern long-run behavior and how small positive powers can change it. The claim holds for arbitrary finite row counts in the plane rather than an artificially selected small table. It is an exact benchmark for numerical row selection, not a universal recommendation for higher-dimensional applications.

## Closest literature and residual risks

Closest full-text sources: Zhang–Yuan–Wang–Zhang (2023), arXiv:2306.06813, sections 1, 3–4 and appendices as rendered; Steinerberger (2020), arXiv:2007.02910, sections 2–4; Gower–Molitor–Moorman–Needell (2019), arXiv:1909.03604, sections 1–2, 6–7 and the relevant exact-zero-residual argument. All use related sampling/conditioning concepts but neither their stated results nor their presented proofs imply the precise long-run edge-average identity. The theorem concerns exact arithmetic and almost-sure rather than expected-error behavior. Broad external search is not exhaustive; hidden prior equivalences are possible.

Self-review: passed. Independent audit: not yet performed.
