# Scientific review: two-tap delay restabilization

## Correctness — PASS

The characteristic equation, the exhaustive trigonometric imaginary-root factorization, the crossing-direction calculation, and the ordering of the first three critical times were reconstructed from the specified scalar retarded equation. The uniform bound \(|s|^2\le a+b\) on right-half-plane roots rules out loss of root count at infinity; the small-delay expansion \(s'(0)=-3b/4\) supplies the initial stable state. All three crossings are simple and transverse, so a \(+2,-2,+2\) right-half-plane root count proves the two stable windows and the intervening instability. The Dirac comparison follows from the full odd/even crossing sequences and \(b/a>5/13\). The 2026 source's actual equilibrium and linearized coefficients were substituted, not merely inferred from an analogy. Reproducible numerical residual checks passed for five pairs, plus numerical root searches for a representative case; such tests are not substituted for the universal proof.

## Originality — PASS, with material priority risk

Bîrdac–Fikl–Kaslik–Mureşan (2026), arXiv:2607.17645v1, derives the exact second-order characteristic equation for the macroscopic type-2 state and treats Dirac and Gamma kernels. Its Section 5.5 and Remark 5.13 give the single-delay \(13b=5a\) boundary but not an equal two-point-delay kernel. The new kernel has real-frequency transform zeros, violating the paper's phase-regular hypothesis, and its stabilizing middle crossing is exactly at such a zero. The inspected 2026 main text and Appendix A do not establish the new universal window or the contrast at equal mean delay. A semantic published-record search for aliases including bimodal, two-tap, two commensurate delays, and second-order characteristic equations did not identify the exact claim.

A **substantial unresolved priority risk** is Cahlon–Schmidt (2024), *On Asymptotic Stability of Second Order Differential Equations with Two Commensurate Delays*, which studies a larger equation class containing this one. Only its abstract and opening page were accessible; its unseen theorems cannot be certified as noncovering, and further human comparison is warranted. Hata–Matsunaga (2022) studies a first-order two-delay equation, not the second-order characteristic equation here. General frequency-sweeping theory of Gu–Niculescu–Chen (2005) provides methodology, not by itself the displayed exact three-window theorem. No general claim that multi-delay stability switching is new is made.

## Mathematical value — PASS

The formula resolves a sharply motivated missing kernel case in a contemporary macroscopic neuron model: neither the single Dirac nor the phase-regular Gamma examples exhibit this universal two-window law across every \(0<b<a\). The second window is explained by perfect Fourier cancellation between two equal synaptic-delay pathways, while in a substantial open parameter wedge a single delay of the same mean never restabilizes. The exact three thresholds and the explicit physical parameter example make a testable dynamical distinction rather than an arbitrary numerical slice. The result is narrow by design; no nonlinear Hopf type, all-delay classification, or full-population attraction is asserted.

## Closest literature and remaining limitations

Primary source: https://arxiv.org/abs/2607.17645 (Sections 2, 3, 5, 8, and Appendix A). Earlier same-class article: https://online.watsci.org/abstract_pdf/2024v31/v31n4a-pdf/1.pdf (first page only). General two-delay methodology: https://doi.org/10.1016/j.jmaa.2005.02.034 ; related first-order comparison: https://doi.org/10.7494/OpMath.2022.42.5.673 . The priority risk of the inaccessible full Cahlon–Schmidt paper is specifically retained. No independent scientific review is represented.

Self-review: passed. Independent audit: not yet performed.
