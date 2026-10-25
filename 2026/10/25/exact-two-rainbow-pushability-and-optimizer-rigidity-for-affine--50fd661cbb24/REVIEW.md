# Scientific review: exact two-rainbow pushability of affine-regular hexagons

## Correctness — PASS

For a canonical six-vertex affine-regular hexagon, the exact integer identity
\[
6A_{jk}=3+x_jx_k+3y_jy_k-(-1)^{j+k}
\]
correctly represents the common-edge indicator for all 36 ordered vertex pairs. Summing against independent vertex laws and imposing their combined zero expectation yields
\[
\frac23-S=\frac{X^2+3Y^2+1+ab}{6}\ge0.
\]
Here \(a,b\in[-1,1]\); hence all three terms after regrouping are nonnegative. Equality forces opposite pure parity supports and zero centroid on each of the two alternating triangles. Three independent affine equations uniquely give uniform weights \(1/3\) on each triangle. The exact verifier checks the kernel identities, equality witness, and uniqueness determinants. It does not substitute finite sampling for the general probability-law argument. The proof also explicitly preserves the origin and incidence under invertible linear maps.

## Originality — PASS, subject to literature uncertainty

The primary paper of Martínez-Sandoval and Olvera-Sampieri, arXiv:2610.17157v1, introduces the invariant in Section 3.1, states a facet-depth upper bound in Section 4.1, computes cubes in Section 4.2, and asks for further exact computations in Section 7. The source's centrally symmetric bound specializes to the trivial upper estimate \(1\) on a hexagon at \(r=2\); its square/cube computation concerns a different face-incidence structure. No hexagonal calculation occurs in the inspected relevant source sections. Indexed records about affinely regular hexagonal norms, Minkowski asymmetry and translative covering ratios involve other invariants and do not logically imply a common-edge probability conditioned on collective balancing. Accessible historical results concerning cross-polytopes have square, not hexagonal, two-dimensional face incidence. Searches did not locate an equivalent exact statement or optimizer classification. An unindexed or independently rediscovered identity remains a priority risk; absence in searches is not a uniqueness proof.

## Value — PASS

This is an exact answer to the recent paper's explicit problem of calculating rainbow pushability for additional centered polytopes. The affinely regular hexagon is a natural first planar case beyond the parallelogram. The sharp value \(2/3\) is strictly less than one even for two colors, whereas the cited universal facet-depth bound fails to give any strict improvement. Moreover, the pointwise parity–quadratic certificate classifies both and only the maximizing distributions; it explains the obstruction geometrically as complementary centered alternating triangles. The value \(\pi_2<1\) triggers the source's two-color pushed Carathéodory/KKMS conclusions for this polygon. No claim is made for other polygons or higher rainbow numbers.

## Closest literature and limitations

Primary: L. Martínez-Sandoval and A. Olvera-Sampieri, *Pushed Colorful Polytopal KKMS Theorem and Orthogonal Star Transversals*, arXiv:2610.17157v1, initially public October 12, 2026; https://arxiv.org/html/2610.17157v1. Relevant text read: Sections 3.1–3.3, 4.1–4.2 and 7. Related polyhedral and hexagonal publications located by scientific searches concern different invariants; their uninspected portions remain a limited priority risk. The exact defect identity is specific to affine-regular six-vertex incidence and does not establish a value for arbitrary centrally symmetric hexagons. The embedded test verifies finite identities only; the argument for all real distributions is analytic.

Self-review: passed. Independent audit: not yet performed.
