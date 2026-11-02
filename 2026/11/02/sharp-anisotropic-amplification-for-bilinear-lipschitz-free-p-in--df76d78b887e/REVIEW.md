# Scientific review: anisotropic bilinear interpolation

## Correctness — PASS
The domain, map and target norm are explicit. A cycle-flow elimination argument reduces the finite \(p\)-free norm to the sixteen spanning trees, and an optimal three-edge \(p=1\) transport decomposition yields the uniform factor \(3^{1/p-1}\). The derivative at the center of increasingly elongated rectangles has weighted source norm one; its tree costs tend to three equal loads. The two bounds coincide. The finite checker tests individual cases but is not used as an infinite proof. Boundaries \(p=1\), positive side lengths and axis exchange are addressed.

## Originality — PASS (qualified)
Bíma's 2023 study treats coordinatewise-affine interpolation over equal-side-length cubes, not rectangular aspect-ratio asymptotics. The closest indexed later result gives the exact *square* value \((2+2^p)^{1/p}/4\), which is strictly below the present sharp rectangular-family supremum when \(p<1\). Semantic database and literature searches covering anisotropic, weighted-rectangle and equivalent interpolation formulations found no dominating claim. The exact square result's underlying text was not accessible; its documented mathematical statement is narrower. An unindexed general rectangular result remains a bibliographic risk.

## Value — PASS
The distortion of barycentric maps into \(p\)-Banach envelopes depends on shape, not just dimension. Determining the best possible constant uniformly over all four-vertex Manhattan rectangles distinguishes the equal-side-length model from the singular anisotropic limit. The bound is attained asymptotically by three balanced transport loads, giving an interpretable sharp benchmark for anisotropic cell interpolation. The claim does not merely reparametrize the known square formula.

## Limits
No exact formula at finite unequal aspect ratio is asserted, and independence from unindexed literature is not certified. The field is real and the target is the four-vertex free \(p\)-space.

Self-review: passed. Independent audit: not yet performed.
