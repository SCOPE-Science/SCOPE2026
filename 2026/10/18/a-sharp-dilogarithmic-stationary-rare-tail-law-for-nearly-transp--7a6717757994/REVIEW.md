# Scientific assessment: a sharp stationary rare-tail law

## Correctness — PASS

The claim is restricted to fixed \(y>0\), \(c\uparrow1\), and the stationary one-time law of rate-one Brownian partial resetting. Its proof constructs the established independent-Laplace stationary series, expands the **exact** logarithmic moment generating function to order one (not just the large-deviation rate), and demonstrates a uniform tilted density local central limit theorem by a Fourier-integrable product bound. Direct exponential-tilt inversion yields the stated \(\sqrt\delta\) prefactor and the discrete Euler–Maclaurin boundary correction \(\exp(B(t_y))\). The Laplace-transform, stationary-generator, Fourier-factor and order-one correction assertions are separately checked by a standalone exact-rational/numerical program. Finite checks are supplementary; the limit and relative error follow from the written analytic estimates. Boundary regimes with varying \(y\) are expressly excluded.

## Originality — PASS, with literature risk

The existing stationary-product formula is fully credited to Di Bello et al. (2023), Grzywny et al. (2024), and Kolb–Wübker (2026). The logarithmic large-deviation rate is **covered at the general weighted-sum level** by Najim (2002) and Vysotsky (2021, Theorem 6.1); it is not being proposed as a new standalone result. The full texts of these sources were compared to the final claim. The assessed addition is the **model-specific sharp relative-error rare-tail probability**, with its exact order-one correction and prefactor, not the already known exponential rate. The closest sharp-distribution primary text inspected, van Leeuwaarden–Temme (2011), treats finite polynomially weighted sums of positive exponentials, whereas the present invariant is an infinite geometric sum of symmetric Laplace variables. General saddlepoint or precise-deviation theorems may conceivably subsume this calculation after verification of model-specific hypotheses and boundary terms; this is a genuine residual priority risk. No assertion of globally proved novelty or independent validation is made.

## Value — PASS

For near-transparent resetting, exponentially small stationary displacements of order \((1-c^2)^{-1}\) arise naturally from a process whose ordinary fluctuations are much smaller. The logarithmic rate cannot estimate these tail probabilities to relative precision and cannot distinguish the actual geometric contraction grid from its continuous approximation: its missing correction is a nonconstant function of the threshold. The proved result supplies the correct absolute normalization and an explicit threshold-dependent factor, addressing a concrete precision gap with a nontrivial tilted local-limit argument. No extension to more general resets, multidimensional motions, or uniform thresholds is claimed.

## Closest literature and limitations

Assefa–Keller-Ressel–Palmowski (2026), arXiv:2610.01363v1: new model-level motivation and polynomial moments, not a sharp stationary tail. Di Bello et al. (2023), arXiv:2305.13722: known stationary density and transform. Grzywny et al. (2024), arXiv:2412.15626: stationary densities and long-time transition asymptotics. Kolb–Wübker (2026), doi:10.1112/blms.70314: stationary series and conditioned process. Vysotsky (2021), doi:10.30757/ALEA.v18-42, and Najim (2002): prior general kernel-weighted logarithmic LDP. van Leeuwaarden–Temme (2011), doi:10.1016/j.spl.2011.05.013: sharp asymptotics for a different finite power-weighted positive-exponential family. The sharp displayed asymptotic holds at fixed \(y>0\) only. Priority risk from more general sharp weighted-array deviation formulae is not excluded.

Self-review: passed. Independent audit: not yet performed.
