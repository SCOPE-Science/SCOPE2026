# Self-review

## Correctness — PASS

The stochastic normalization \(\sqrt2\) makes the generator \(f''-n(x-P_ax)f'\), with invariant density proportional to \(e^{-n\operatorname{dist}^2/2}\). The conjugated Schrödinger potential is coercive; one-dimensional Sturm oscillation gives discrete simple eigenvalues indexed by zeros. The exterior square-integrable solution is \(e^{z^2/4}D_\nu(z)\). Its derivative at zero gives the explicit gamma quotient. Matching value and derivative against trigonometric solutions inside the interval yields an exact low-mode phase equation. A uniform Taylor expansion of the gamma quotient for bounded positive mode number produces the square-root effective half-width and a mode-fourth-power \(n^{-3/2}\) correction. The bound \(O_{a,j}(n^{-5/2})\) follows from the remainder in the arctangent and implicit-function inversion, retaining the effective half-width in the denominators. The checker passes 378 numerical assertions, including an independent finite-difference eigensystem. Infinite-dimensional claims use analysis, not numerical enumeration.

## Originality — PASS (best-knowledge assessment)

The strongest relevant primary source, Mane (arXiv:2512.00386, 2025), analyzes invariant-measure Wasserstein convergence and Euler discretization for penalized reflected diffusion; its inspected discussion does not state the gamma-ratio spectral equation or fixed-mode asymptotic coefficient. Darapaneni (arXiv:2610.35145, 2026) describes the same quadratic projection potential and general mixing rates, but its inspected introductory main results do not supply the exact interval eigenvalue expansion. The earlier Gürbüzbalaban–Hu–Zhu sampling work supplies convergence and complexity guarantees rather than an inspected explicit spectrum. Classical parabolic-cylinder formulas alone do not imply the implicit-root expansion without the domain matching and spectral indexing. Targeted searches, including semantic published-finding searches, found no equivalent statement, but a differently indexed piecewise-OU spectral formula remains a genuine priority risk. No uniqueness certification is claimed.

## Mathematical value — PASS

Penalization converts reflected constrained sampling into unconstrained diffusion, but the effect of finite penalty on relaxation eigenvalues matters separately from convergence of invariant measures. The result provides a complete fixed-mode asymptotic comparison with reflecting Brownian motion, a universal thermal boundary width, and the first nontrivial *dispersive* departure from pure length renormalization. The last coefficient depends on the fourth power of the spectral mode and has a strict sign, so it captures a dynamical effect that cannot be obtained by simply replacing the interval length. Its benchmark value is limited to a solvable one-dimensional model.

## Closest literature and residual risks

The directly relevant papers are Mane (2025, arXiv:2512.00386), Gürbüzbalaban–Hu–Zhu (2024, arXiv:2212.00570), and Darapaneni (2026, arXiv:2610.35145). Only the first and third were materially read in mathematical detail for this assessment; the 2024 paper was compared from its author/publisher summary and is not certified absent of a specialized appendix. Some special-function and piecewise-Ornstein–Uhlenbeck spectral literature may contain an equivalent formula under a different model name. The result is not independently validated.

Self-review: passed. Independent audit: not yet performed.
