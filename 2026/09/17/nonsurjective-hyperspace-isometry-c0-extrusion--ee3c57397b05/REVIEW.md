# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The central identity is the max-product Hausdorff formula
\[
d_H(A\times I,B\times J)=\max\{d_H(A,B),d_H(I,J)\}.
\]
It follows directly from the corresponding point-to-product distance
formula. The radius functional \(R(A)=d_H(A,\{0\})=\sup_{a\in A}\|a\|\)
is 1-Lipschitz, hence the interval-height contribution
\(|R(A)-R(B)|\) never exceeds the original Hausdorff distance. This proves
that radius extrusion preserves all Hausdorff distances exactly.

The singleton claim was checked separately: \(R(\{0\})=0\), whereas for
\(x\ne0\) the image of \(\{x\}\) has interval factor
\([-\|x\|,\|x\|]\) and is nondegenerate. Thus the map is proper and cannot
be induced pointwise by an underlying-space isometry.

The order statement follows in both directions by monotonicity of \(R\)
and projection onto the first coordinate. The outer-parallel-body formula
uses \(R(A\oplus tB_X)=R(A)+t\) and
\(B_{X\oplus_\infty\mathbb R}=B_X\times[-1,1]\). These identities remain
valid for closed Minkowski sums. The compact-convex restriction is valid
because products with compact intervals preserve compactness.

For \(c_0\), the coordinate map
\[
U(x,t)=(t,x_1,x_2,\ldots)
\]
is a surjective linear isometry from \(c_0\oplus_\infty\mathbb R\) onto
\(c_0\), so the general construction indeed becomes a self-embedding.

## Originality

Originality is assessed to the best of our knowledge.

The current full text of Cheng--He--Liu--Zheng, arXiv:2609.18252, was
inspected. Its main theorem assumes surjectivity and proves pointwise
affine representation for arbitrary real Banach spaces. Its proof
explicitly recovers outer parallel bodies and inclusion before using
surjectivity to pass from order minimality to singleton preservation.
No non-surjective infinite-dimensional counterexample of the present form
was found there.

The Gruber--Lettl 1980 Euclidean classification was checked at the
published abstract/metadata level. It gives the finite-dimensional form
\(C\mapsto i(C)+D\) with a fixed convex summand. This does not cover the
radius-dependent extrusion here; moreover, fixing the origin singleton
forces the fixed summand in their form to be a singleton.

Yu Zhou's 2022 paper on non-surjective ε-isometric embeddings is the
closest identified prior source. Its available abstract was inspected and
states support-space linearization results plus a pointwise
finite-dimensional conclusion under an additivity assumption. The full
article was not inspected, so it is the principal residual originality
risk. Searches for synonymous formulations involving non-surjective
Hausdorff isometries, convex hyperspaces, product/max norms, radius
thickening, singleton preservation, and \(c_0\) did not locate an
equivalent construction.

## Value

The result gives a sharp boundary for a very recent rigidity theorem:
surjectivity cannot be replaced merely by origin normalization, order
embedding, or exact preservation of outer parallel bodies. The example
also explains why the final minimal-element step in the surjective proof
has no direct nonsurjective analogue. The self-embedding on \(c_0\)
removes the possible objection that the failure is caused only by
enlarging the target dimension.

The same formula applies simultaneously to bounded closed convex sets and
compact convex sets, making the mechanism reusable across the two main
hyperspaces studied in the literature.

## Limitations

The result does not classify non-surjective hyperspace isometries. The
full text of Zhou (2022), DOI 10.1016/j.jmaa.2022.126282, was not
inspected, leaving a material but localized originality risk. Older
hyperspace literature could contain an equivalent product construction
under different terminology.

## Sources

- https://arxiv.org/abs/2609.18252
- https://doi.org/10.1112/blms/12.6.455
- https://doi.org/10.1016/j.jmaa.2022.126282
