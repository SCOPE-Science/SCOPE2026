# Scientific review: Universal first period response on a quadratic chameleon Hopf sheet

## Correctness — PASS

The equilibrium Jacobian factors exactly as \((\lambda+b)(\lambda^2-\alpha\lambda/b+1)\); transversality is \(1/(2b)>0\). With the normalized critical eigenvectors, the only contributing quadratic Hopf term produces \(G_{21}=5i/(b+2i)\) and \(\ell_1=5/(b^2+4)>0\), proving a subcritical branch for each fixed \(b>0\). A separate Poincaré–Lindstedt expansion proves both solvability equations, \(R^2=2(b^2+4)/(5b)\), and \(\omega_2=1/4\). Standard analytic nondegenerate Hopf theory upgrades the formal leading expansion to the genuine local periodic family. The included symbolic checker validates the critical identities; six periodic shooting runs corroborate the physical period and amplitude. It would be incorrect to regard these six runs as an infinite proof.

## Originality — PASS within inspected evidence

The defining Zhang et al. paper's full author-uploaded text was inspected in its dynamical equations, Sections 2–4, numerical damping studies, and Theorem 4.2. It proves subcritical Hopf specifically for \(\mu(z)=\alpha-z\), equivalent to \(b=1\), but neither evaluates the full damping-dependent \(\ell_1(b)\) nor states the universal period slope or physical amplitude law. The later Liu et al. chameleon analysis was inspected; it concerns a different vector field with different quadratic couplings, so its Hopf statements cannot imply the present formulas. Searches for general parameter, same polynomial terms, equivalent normal forms, period responses and published mathematical research findings did not identify a covering result. The closest indexed research on Sprott F/S and cubic jerk Hopf bifurcations concerns different equations and offers no direct corollary. A failed search does not establish absolute novelty; hidden/unindexed material and the undated August 2023 preprint label remain priority risks.

## Value — PASS

The damping parameter appears in the original model's numerical studies but not in its analytically solved Hopf sheet. Determining the general first focal coefficient proves nondegeneracy at every positive damping value and reveals how the repelling local cycle varies with damping; in contrast, the **first physical period correction is exactly independent of damping**. This gives a substantive quantitative calibration of the unstable periodic orbits near a stable equilibrium, which can organize the local basin geometry relevant to the defining study's hidden dynamics. The finding does not assert a global hidden-attractor theorem or a new general Hopf method.

## Closest literature and limits

Zhang et al. (2023), *Mathematical Modelling and Control*, DOI 10.3934/mmc.2023032, Section 4, Theorem 4.2: b=1 subcritical Hopf, credited; the whole preprint was accessible via its author upload. Liu et al. (2025), *AIMS Mathematics*, DOI 10.3934/math.2025225: different quadratic flow. Kuznetsov (2004): general calculation only. This local theorem requires a fixed \(b>0\) and small \(\alpha\); there is no claim of uniformity at the damping endpoints, no global attractor census, and no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
