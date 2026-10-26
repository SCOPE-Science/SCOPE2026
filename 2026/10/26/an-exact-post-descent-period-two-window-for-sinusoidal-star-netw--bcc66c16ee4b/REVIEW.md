# Self-review

## Correctness
**PASS.** In the edge-difference formulation of the unit-weight star, the incidence Gram matrix is \(K=I+\mathbf1\mathbf1^{\mathsf T}\). The diagonal circle reduces to \(t\mapsto t+\kappa\sin t\). An exact two-step interchange gives \(\kappa=2\delta/\sin\delta\), strictly monotone for \(\delta\in(0,\pi)\). At both orbit points the derivative is the same matrix \(I-h\cos\delta\,K\), whose entire spectrum yields the cutoff \(\kappa=\pi\). The local implicit-function argument ensures robust weighted persistence only inside the strictly attracting window. Fifteen numerical matrix/transition examples were replayed. Finite checks supplement, not replace, the analytic proof.

## Originality
**PASS (best-knowledge, with residual priority risk).** The full 2026 primary source arXiv:2610.10993v1 gives the same star model and a sharp lower step bound but no period-two formula beyond descent. Earlier local flip analysis for a tridiagonal path is not a global stability classification for this rank-one-coupled star. Searches for Huygens star two-cycles, sinusoidal discrete Kuramoto period doubling and equivalent sine-map formulations found nearby but non-covering triangle, all-to-all and classical continuous-time results. Scalar orbit existence is a reduction, but it does not on its own prove full transverse attraction. Older papers accessible only through abstracts remain an acknowledged risk.

## Mathematical value
**PASS.** At the very threshold where strict descent ceases, a stable oscillation is born in the physical multi-oscillator model and persists up to the exact second boundary \(\pi/(n+1)\), regardless of the number of leaves after rescaling. The full Floquet spectrum and positive-weight robustness identify a tangible open family of discrete oscillatory attractors, without claiming an unsupported global portrait.

## Closest literature and limitations
The closest source is Buescu–D'Aniello–Oliveira (2026), arXiv:2610.10993v1, §§3–5; prior path-family local flip results have a different Gram matrix. At \(\kappa=\pi\) only linear neutral behavior is proved. No all-periodic-orbit classification, full basin measure, or statement on global Morse–Smale transversality follows. Exhaustive independent priority review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
