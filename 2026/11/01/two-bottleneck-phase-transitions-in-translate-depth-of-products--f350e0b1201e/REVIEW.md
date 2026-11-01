# Scientific review: product-simplex translate-depth phase law

## Correctness — PASS

The claim is a statement about a common dilation of a Cartesian product of nondegenerate simplices, with normalized product-volume measure, and the supremum over all translates excluding a query point. The key overlap identity is proved by barycentric inequalities, including empty intersections and boundary limits. The optimization of a missing translate is an infimum of a positive-part sum; the explicit limiting threshold construction proves attainability in the supremum sense. Product factorization handles the union of exclusion events without assuming that the same translate optimizes every factor. The maximizer is reduced to the product centroid, then to a finite dimension envelope. The function \(x\log(x/(x+1))\) has strictly positive second derivative \(1/[x(x+1)^2]\), proving that only the smallest and largest factor dimensions can control the maximum. All boundary scales, including \(t=T_q\), \(t=t_*\), and \(t=1\), are included correctly. The median sets follow by saturating the same inequalities. The accompanying executable checker passed 434 exact rational assertions, including independently clipped interval and triangle volumes; finite tests support but do not replace the proof.

## Originality — PASS with residual priority risk

The October 19, 2026 depth paper supplies general definitions, depth-region erosions, covariogram considerations, and tangent-cone dilation limits. An existing exact result for a single simplex already provides the one-factor special case, and the present paper does not claim it. The new assertion is the exact **coupled** maximum for products with unequal factor dimensions: a strict-convexity reduction to only the extreme dimensions, the explicit internal crossing \(t_*\), and an exact classification of the median set. For a triangular prism, the unique median appears only at the isolated scale \(8/9\) between line-segment and triangular median loci. These conclusions are not stated or directly determined by the previously inspected single-simplex or general erosion results without the new product-minimax and extreme-dimension arguments. A search of the available mathematical records and literature did not identify a covering theorem, but this is not a guarantee of priority. The 1999 homothetic-simplex intersection paper was accessible via its abstract and excerpt rather than a verified full reading, creating a limited residual literature risk.

## Value — PASS

Translate-based depth is a natural convex-geometric centrality functional whose behavior for nonsmooth testing bodies differs sharply from classical halfspace depth. The entire maximum-depth and median-geometry classification of products of simplices supplies explicit benchmark examples for genuinely high-dimensional non-simplex polytopes. The phenomenon is not merely an added parameter: a single uniform triangular prism displays three exact corners in the maximum-depth curve, exchange of the dimension controlling the optimum, and a change in the topology and dimension of the median set from a segment through a singleton to a triangle. The formulas make the role of extreme factor dimensions transparent for arbitrary products.

## Scope and limitations

This review verifies one complete theorem with its consequences, not independent priority or an independent proof audit. The theorem is restricted to a fixed Cartesian product, uniform measure, and a single common dilation. Testing bodies with independently varied factor scales, rotations or more general distributions are outside the claim. Historical-priority uncertainty is explicitly retained.

Self-review: passed. Independent audit: not yet performed.
