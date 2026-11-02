# Scientific review: joint first-passage exposure law

## Correctness (C): PASS

The claimed domain is \(D,r,a>0\), arbitrary \(s,u,v\ge0\), Brownian generator \(D\partial_{xx}\), a killing boundary at zero, and independent Poisson resetting to the starting point. The point-local-time normalization is an occupation **density**, yielding the interface jump \(D[f'(a+)-f'(a-)]=uf(a)\). Solving the left and right constant-coefficient backward equations uniquely produces the full joint Laplace transform, not just a moment expansion. Setting two transform arguments to zero reproduces three source marginals. The Lévy representation is verified by integrating a positive Lévy measure with finite \(\int(1\wedge t)\Pi(dt)\). Differentiation yields the exact conditional mean, conditional variance and correlation. Independent finite-difference discretizations and symbolic calculations were run; their role is corroboration only. The proof and the limits stated in the result are consistent.

## Originality (O): PASS with substantial residual risk

Four scientific comparisons were made against accessible full text and mathematical search records. Singh–Pal (2022) provides separate Laplace transforms and a general Feynman–Kac approach, but not a complete evaluated transform for \((T,L,R)\) or this joint coupling; separate marginals do not determine a joint distribution. Colantoni–D'Ovidio–Pagnini (2025), Theorem 6, **already gives the same subordinator exponent and Lévy measure** for reflected resetting Brownian motion. That ingredient is expressly excluded from the novelty claim. The present contribution is the three-way absorbing first-passage coupling, the independent exponential stopping representation, and the resulting exact monotonic exposure correlation. The 2019 local-time work concerns primarily fixed-horizon local-time statistics; the 2023 OU paper studies separate first-passage functionals in a different model. No evaluated stronger statement was identified in the inspected material or index results. A sufficiently general excursion-process theorem may subsume the specialization after reductions; this remains a material priority risk and is not disguised as established independence from prior mathematical theory.

## Value (V): PASS

The originating first-passage literature identifies three physically natural, separately calculated quantities: time until successful capture, local exposure at the reset/catalytic site, and duration of spatial residence above that site. Their simultaneous law is needed for joint trajectory constraints and dependence questions; independent marginal formulas cannot answer those questions. The transform supplies all mixed moments and a concrete conditional stochastic representation, while the exact correlation interpolates monotonically between weak and strong resetting. This is a complete natural joint classification with a structural interpretation, not an arbitrary finite parameter slice or a tiny numerical improvement. It does not imply an unproved application to other reset processes or any experimental guarantee.

## Closest sources and remaining limitations

- P. Singh and A. Pal, arXiv:2202.02715 (2022), equations 9, 20, 28, and 67: source model, method, marginal laws; no evaluated three-variable law in inspected text.
- F. Colantoni, M. D'Ovidio, G. Pagnini, DOI 10.1007/s10955-025-03527-5 (2025), Section 6, Theorem 6: reflected-process subordinator exponent exactly matches an ingredient under compatible normalization.
- A. Pal et al., arXiv:1902.00907 (2019), Sections III–V: local-time methodology for resetting diffusion, not the same stopped three-way joint observable.
- A. Dubey and A. Pal, arXiv:2304.05226 (2023), Sections 3–4: OU-reset residence and local-time calculations, distinct generator and separate observables.

Unresolved publication-priority risk from broad excursion/subordinator theory is expressly retained. The scientific theorem, not a claim about publication history, passed the self-review. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
