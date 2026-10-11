# Scientific review: exact local Bergman-pole spectrum

**Correctness — PASS.** The monomial norm calculation fixes the normalization, while the Poisson-kernel identity computes every Hessian Fourier eigenvalue as a strictly positive integral. Convexity in the discrete Fourier index locates the extremal modes; the digamma recurrence and dominated convergence establish the stated formulas and asymptotics. A standard-library numerical checker compares three separate finite calculations, but the proof is analytic for every integer \(N\ge2\).

**Originality — PASS within the inspected record.** Abakumov–Borichev–Fedorovskiy (arXiv:2009.01898v1, Lemma 12) establish positive curvature and global equispaced minimization, not its exact \(N\)-by-\(N\) Hessian eigenvalues. Corbett (arXiv:2609.21121v1, Section 2.3) proves Hessian positivity and global minimization, but no spectral diagonalization, extremal modes, or sharp quadratic coefficient. Bezrukov (arXiv:2609.03134v1) gives a broader global inequality, not this local spectrum. Targeted searches found no statement implying the full result; this is not a proof of absence from all literature.

**Value — PASS.** The question is the quantitative rigidity of the canonical minimizer in Chui's weighted Bergman problem. Unlike qualitative uniqueness, the precise Fourier spectrum identifies the most and least costly perturbations and proves that the angular condition number approaches the sharp limit \(2\). The result supplies a reusable stability benchmark for near-regular pole configurations.

**Limits and risks.** The theorem concerns only the indicated critical Bergman weight and local angle variations. Unindexed equivalent spectral calculations remain possible. Finite numerical tests do not certify the all-integer theorem; the analytic proof supplies that step.

Same-model review: passed. Independent audit: not yet performed.
