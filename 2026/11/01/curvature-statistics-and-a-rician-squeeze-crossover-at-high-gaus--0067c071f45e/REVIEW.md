# Scientific review of the Gaussian spectrogram peak-curvature theorem

## Correctness (C) — PASS

The definition of a peak is a strict positive-height local maximum of the field \(H_b\). The Gaussian entire function has independent circular Gaussian Taylor jets at a translated critical point. The Chern-derivative zero constraint sets \(a_1=0\), and the relevant Kac–Rice Jacobian is exactly \(2|a_2|^2-|a_0|^2\). The weighted maximum ensemble therefore has joint density \(3(s-2t)e^{-s-t}\) on \(s>2t>0\). This density integrates to one; the associated mean maximum intensity is \(1/(3\pi)\), agreeing with Abreu's established result.

The Hessian expansion and the transformation under \(S_b=\operatorname{diag}(e^b,e^{-b})\) yield the displayed real symmetric two-by-two matrix. Integration of the exact Palm density gives the finite-height eccentricity tail. Conditional \(T\mid S=s\) tends to a unit exponential law, and under \(S\ge h\) one has \(S/h\to1\). The high-peak jet is consequently a standard planar real Gaussian after scaling. Eigenvalue perturbation gives the noncentral Rayleigh (Rician) crossover and, for fixed nonzero squeeze, the normal limit about \(e^{4|b|}\). These deductions use distributional convergence, not simulated evidence. Degenerate maxima have zero intensity and do not contribute.

A standalone standard-library checker passed 79 supplementary exact, quadrature, and finite-sample assertions. It checks normalization, tails and the scaled Hessian ratio independently of the symbolic limiting arguments. Reproducible checks strengthen confidence but do not certify a limit theorem.

## Originality (O) — PASS, with residual historical-priority risk

Abreu's 2022 open-access full article gives the number and height of spectrogram critical points, including the same Chern/Gaussian jet setup, and is the closest indispensable scientific antecedent. The article's statements and proofs on first intensities and height densities do not give the ratio of principal real Hessian curvatures, its exact Palm tail, or the novel joint high-height/squeeze scaling. A derivation from its premises still requires a new marked Palm integration, Hessian eigenvalue law and a varying-window limit.

Haimi–Koliander–Romero's 2022 full article treats signed indices/critical counts of Gaussian Weyl–Heisenberg zeros; the signature of a Hessian does not determine the continuously valued curvature ratio. Haimi–Odelius–Romero's 2025 full arXiv text gives spatial pair correlations of GEF zeros/critical points, not a one-point marked Hessian distribution. The 2026 hyperuniformity article likewise concerns number variance and critical-point indices, not this shape mark. Relevant semantic research-record comparisons concerning Gaussian anisotropy and discrete cyclic Gabor spectrogram Hessians involve different objects and cannot imply this continuous Gaussian random peak-shape law. No equivalent or stronger covering result was found in the checked material; that negative search is not proof of global novelty.

The strongest residual risk is an unlocated general marked-Kac–Rice theorem that specializes to the same exact curvature tail or double-scaling Rice law, possibly in older random-landscape or Gaussian random-section literature. Priority remains provisional pending independent literature verification.

## Mathematical value (V) — PASS

Curvature anisotropy of a spectrogram maximum is a natural geometric statistic of the local time-frequency concentration landscape, distinct from maxima counts and ordinates. The exact unsqueezed law has a nontrivial \(r^{-2}\) tail, so the second moment of the condition number diverges even though the mean is finite. The high-peak law shows that unusually high noise peaks become asymptotically circular at rate \(h^{-1/2}\); infinitesimal window squeezing competes with random curvature at precisely the same scale, producing a noncentral Rician transition, whereas fixed squeezing leads to Gaussian fluctuations around deterministic eccentricity. This is a structural phase-boundary calculation, rather than a reparameterization of the already-known peak-height density.

## Closest prior literature and limits

- Luís Daniel Abreu, *Local Maxima of White Noise Spectrograms and Gaussian Entire Functions*, arXiv:2210.06721 (first posted 2022-10-13), especially Sections 2.2, 3 and 4.2–4.3, DOI 10.1007/s00041-022-09979-7. Essential Gaussian-jet, average-count and height formulas, but not the marked curvature crossover.
- Antti Haimi, Günther Koliander, José Luis Romero, *Zeros of Gaussian Weyl–Heisenberg Functions and Hyperuniformity of Charge* (2022), DOI 10.1007/s10955-022-02917-3, especially first-intensity and Section 6.8 index/critical-point statements; not an eigenvalue-ratio distribution.
- Antti Haimi, Lukas Odelius, José Luis Romero, *Local repulsion between zeros and critical points of the Gaussian Entire Function*, arXiv:2510.06821 (2025), Theorem 1.1; concerns two-point local repulsion rather than one-point Hessian marks.

Only Gaussian-window complex white noise in one time-frequency dimension and the stated Palm selection convention are treated. No global-maximum, non-Gaussian or arbitrary-window claim is made. The numerical checker is not an infinite-dimensional validation. An independent historical-priority audit is not supplied.

Self-review: passed. Independent audit: not yet performed.
