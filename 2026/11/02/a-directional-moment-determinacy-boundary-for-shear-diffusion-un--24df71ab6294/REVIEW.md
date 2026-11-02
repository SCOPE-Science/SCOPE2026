# Scientific review: directional moment-determinacy boundary in sheared reset diffusion

## Correctness — PASS

The result applies to stationary planar Brownian diffusion with *simultaneous full Poisson resetting to the origin*. Stochastic Fubini gives the variance polynomial \(V(t)=2D[t+\gamma uv\,t^2+\gamma^2u^2t^3/3]\) for a unit projection. The last-reset age is exponential and independent of the path, so the stated positive normalized mixture is exact. For nonzero effective shear, its cubic variance term leads to the unique saddle \(t=\ell\sqrt{|z|}\), action \(4r\ell\sqrt{|z|}/3\), and a computable finite subleading action shift \(rv/(\gamma u)\). The Gaussian-mixture prefactor gives the exact \(|z|^{-1/2}\) density factor. Standard Laplace-method domination beyond the saddle and the explicitly stated change of scale justify passage to the full improper integral.

All polynomial moments follow by exponential age mixing; nonzero exponential moments diverge for a nonzero cubic term. The explicit tail makes the Hamburger Krein logarithmic integral finite, so the projection is moment-indeterminate by the established criterion; the exceptional zero-effective-shear case is exactly Laplace and moment-determinate. None of these conclusions is inferred merely from a finite computation. The standalone checker passed 31 finite diagnostics and is provided with source code.

## Originality — PASS, with stated residual risk

The primary paper, Abdoli–Olsen–Löwen, arXiv:2410.10333v1, already derives the model's transient Gaussian propagator, exact renewal representation, and finite moments; they are not claimed as new. Its last section discusses heavy tails for the *partial-reset nonstationary* process, not the exact directional tail of the *full-reset stationary* process. The distinct diffusing-diffusivity reset process of Santra–Basu–Sabhapandit, arXiv:2205.00549v1, already has a square-root stretched-exponential tail with a power prefactor; neither the general half-power motif nor Laplace's method is claimed new. Its stochastic diffusivity dynamics do not imply the present shear-specific exponent coefficient, direction-dependent prefactor, or exceptional transverse axis. Lin's moment-problem survey and Lin–Stoyanov product theory supply general criteria and related examples, but not this all-direction sheared Brownian stationary classification. The closest related earlier work in this research history concerns conditional mean and variance given the transverse coordinate, not tail or moment determinacy of every projection.

Targeted literature searches and claim-level comparisons found no checked explicit statement covering the complete theorem. This is evidence for originality, not proof of worldwide publication priority. Broad Gaussian-mixture and random-time-asymptotic theorems may give shorter derivations, and unexamined recent literature remains a risk.

## Mathematical value — PASS

The distributional distinction concerns the ability to reconstruct a physically observable stationary displacement from *all* its moments. It is not inferred from low-order kurtosis: even an infinite sequence of correctly computed shear-sensitive moments fails to determine the marginal law, while a transverse observation remains uniquely determined. The exact direction-dependent tail constant quantifies rare strong-flow excursions; its angular prefactor and rate constant vary across nontransverse projections even though the square-root exponent is fixed. This clarifies why perturbative stationary density expansions around zero shear are nonuniform in far tails and identifies a natural geometric boundary, rather than an arbitrary parameter slice. The result closes a concrete distributional gap beyond the source paper's moment calculations, with plausible relevance to directional rare-event measurement and inference.

## Limitations and further verification

The statement uses isotropic independent Brownian noise, linear shear, fixed origin and full homogeneous Poisson resetting. Tail asymptotics are pointwise in each fixed nonzero effective shear; no uniform angular/small-shear limit, partial-reset analogue, or joint bivariate moment classification is proved. Independent publication-priority verification is not performed.

Self-review: passed. Independent audit: not yet performed.
