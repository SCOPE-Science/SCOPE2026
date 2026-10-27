# Self-review

**Correctness: PASS.** From the rate-one renewal mixture and the exact Gaussian covariance, the exponent reduces uniformly on compact positive reset-age scales to \(LF_c(s)\). Small-age and large-age integrals are exponentially dominated by choosing proper cutoffs, so standard Laplace expansion applies at every nondegenerate global saddle. Factoring the derivative gives exactly the young and old branches; eliminating the two stationarity equations and equality of costs proves the sole crossover \(c_*=\sqrt3/24\). Direct differentiation and Gaussian prefactors yield the strict rate corner and two-atom conditional age law. The symbolic and numerical checker, replayed from the package, separately corroborates key identities. No finite experiment is treated as a proof of an infinite assertion.

**Originality: PASS (best-knowledge, with priority risk).** The motivating 2024 shear-resetting source [1] was inspected in its full publicly available HTML text, including appendices. It gives the free Gaussian propagator, stationary reset-age mixture, moments and distributional analysis, but no displayed comparison of two competing conditional ages on parabolic far-tail rays or universal sharp two-age caustic. Searches for equivalent integral-mixture saddle laws, anisotropic tail rate functions, dominant age branches, and exact constants in the accessible research database and primary literature did not reveal an implying result. General renewal/resetting references [2,3] give the mixture starting point, not the claimed sharp minimizer phase diagram. Prior work may implicitly contain the optimization; independent priority audit has not occurred.

**Scientific value: PASS.** A measurable far-displacement event selects either a recent extreme excursion or an older gentler shear excursion. Their coexistence at one exact threshold, together with a nonanalytic spatial rare-event rate and a calculable bimodal age posterior, characterizes physical history selection not visible from stationary moments or the exact mixture formula alone. Universality in added longitudinal diffusivity is a useful robustness result. The exact nontrivial minimizer exchange and conditional age distribution supply benchmarks for rare-event sampling of sheared resetting systems.

**Scope and risks.** The far-tail parameter and finite diffusivity remain fixed, no critical finite-size window is analyzed, and the source's stationary mixture could allow an equivalent calculation in uninspected asymptotics literature. The computation cannot substitute for external validation or a priority review.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Abdoli, Olsen, and Löwen, *Shear-Driven Diffusion with Stochastic Resetting*, arXiv:2410.10333v1 (2024-10-14), https://arxiv.org/html/2410.10333v1 .

[2] Evans, Majumdar, and Schehr, *Stochastic resetting and applications*, arXiv:1910.07993.

[3] Eule and Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting* (2016).
