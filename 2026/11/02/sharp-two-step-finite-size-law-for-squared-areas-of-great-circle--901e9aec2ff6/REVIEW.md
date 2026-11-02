# Review of the finite-size spherical cell-area theorem

## Correctness — PASS

The exact three-probe Crofton identity reduces the squared area of a size-biased spherical cell to an integral over two auxiliary sphere points. Local exponential coordinates, the spherical cosine law, and a globally exponentially dominated remainder give a justified three-term expansion. The independent rational certificate re-evaluates all three planar triangle integrals (the normalizer, radial square, and area-over-opposite-side term) and establishes the constants \(4\pi^2/7\), \(32\pi^2/11\), \(8\pi^2/11\). The gamma radial moments give \(-10\) and \(65\), with the curvature term \(-28\pi^2/11\). The asymptotic proof is analytical; finite checks and optional quadrature alone are not used as an infinite proof.

## Originality — PASS (bounded prior-art scope)

The closest foundational source, Kabluchko–Thäle (arXiv:2005.01055v1, Sections 5.3–5.4), calculates first expected spherical intrinsic volumes of weighted cells and their large-\(n\) limits, not the square of random cell area. Hug–Schneider (arXiv:1508.07768, Theorem 8.1) proves second face-content moments for an **unweighted typical** Schläfli cell; a second moment of that cell corresponds to a *first* moment of the size-biased area, not its square. The new \(\mathbb E\sum_C\operatorname{area}(C)^3\) requires a third raw cell-area moment. Richey–Sarkar (arXiv:2006.01323) and the classical Goudsmit result provide planar moment background but not the finite spherical second correction. Actual database searches by source terminology, coefficient and equivalent cubic-area formulation returned no dominating record. Residual risk: Miles (1971) was accessible only through bibliographic information and later full-text citations; it was not fully inspected.

## Mathematical value — PASS

The squared area of an area-weighted cell measures the variability experienced by a random spherical location, rather than merely its mean. Its leading scaling connects to the planar Crofton cell; the correction \(-10/n\) measures finite binomial count effects, while the exact \(-28\pi^2/(11n^2)\) term isolates curvature. The observable requires a three-point joint no-cut integral and an exact two-dimensional triangle-moment evaluation, not a standard first-moment conversion or parameter substitution. The result concerns a motivated infinite family rather than an arbitrary single numeric slice.

## Limits and source coverage

The claim is asymptotic for isotropic independent cuts on the unit sphere. An exact fixed-\(n\) formula, nonisotropic extensions and higher-order corrections are not claimed. The 1971 Miles source remains a historical-priority risk; independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
