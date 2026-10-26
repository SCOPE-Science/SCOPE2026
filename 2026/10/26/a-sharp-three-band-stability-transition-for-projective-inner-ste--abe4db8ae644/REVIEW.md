# Self-review

**Correctness — PASS.** The published PISV tableau was reconstructed into the exact scalar cubic. Factoring \(R+1\) and \(R-1\) yields two quadratics whose discriminants both switch sign at \(\lambda=1/9\). Their exact roots, signs, the global endpoint \(2/\lambda\), and stiff-limit expansions prove the full negative-real-axis classification; finite checks are supplemental only. At the critical ratio two interior modes are neutral, not convergent.

**Originality — PASS, with residual priority risk.** Koellermeier and Samaey (arXiv:2210.08302v2, Eq. (96), §6.2, Fig. 9(c)) supply the PISV method and qualitative stability-region plots. The new contribution assessed here is the precise three-band to one-band transition, the closed-form boundaries and the two critical neutral points, not the already-specified numerical method or the general Runge--Kutta stability test. Comparisons with relevant projective-integration literature and available mathematical findings did not identify exact covering statements. The search is not an exhaustive priority guarantee.

**Value — PASS.** The classification solves a motivated spectral-gap design problem for projective integration, revealing that a sufficiently large outer/inner ratio necessarily leaves two intervals of inner-Euler-stable modes that are unstable after a full PISV update. The sharp threshold and exact interval widths are useful benchmarks for choosing macro/micro steps in stiff systems.

**Limitations.** The result concerns the three-stage PISV, scalar real nonpositive eigenvalues and \(0<\lambda\le1/2\). It makes no claims of complex-plane, nonlinear, nonnormal or positivity stability. Some weakly stable modes fail to decay. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
