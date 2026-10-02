# Independent Audit — Global quadratic Hausdorff stability for the planar fractional-perimeter comparison

**Audit date:** 2026-10-01 (UTC) (UTC)  
**Disposition:** passed

## Correctness — PASS

The quantitative tangent-angle argument has a uniform quadratic Jensen gap on a central chord interval. After integration, its Fourier spectral gap controls the nonconstant tangent-angle defect. For normalized outer parallel bodies, the curvature-radius primitive scales with the needed power of \((1+r)^{-1}\); the source’s first-variation identity then transfers the positive fractional-Willmore gap to a chord-functional and hence fractional-perimeter deficit. Writing the curvature radius as \(\rho=h+h\), the resulting \(\dot H^{-1}\) defect is a weighted Fourier norm of the support function after translation modes \(k=\pm1\) are removed, and it dominates the \(H^1\) norm, hence the support-function sup norm equal to Hausdorff distance. Smooth convex approximation preserves perimeter, chord functional, and Hausdorff distance. The perturbation \(h=1+\varepsilon\cos 2\theta\) has Hausdorff distance of order \(|\varepsilon|\) and perimeter deficit of order \(\varepsilon^2\), proving local optimality of exponent two.

## Originality — PASS

The full primary source arXiv:2609.19052v2 proves the sharp qualitative fixed-perimeter comparison and provides the geometric identities, but contains no quantitative deficit theorem. The closest prior stability work for two fractional perimeters is local and has upper order \(t<1\), while the older nested-convex nonlocal-perimeter Hausdorff estimate addresses monotonicity under set inclusion rather than the fixed-perimeter disk deficit. A curvature-radius stability record published later on 2026-09-19 is not prior art for this record: the Hausdorff record entered the repository at 04:21:52 UTC, whereas the curvature-radius record entered at 19:21:08 UTC.

## Scientific value — PASS

The theorem upgrades a newly sharp extremal comparison to a global coercive geometric estimate and identifies the locally optimal Hausdorff power. The proof also links tangent-angle convexity, outer-parallel variation, curvature-radius control, and support-function geometry in a reusable way.

## Source inspections

- arXiv:2609.19052v2 full HTML inspected through Theorem 1.1, proof strategy, support-function lemmas, smooth approximation, and chord continuity.
- Resultary results and the later curvature-radius published record were inspected and commit timestamps compared.
- Giannetti–Stefani abstract was inspected for its nested-set hypothesis.

## Residual risks

- Very recent unindexed stability work remains possible.
