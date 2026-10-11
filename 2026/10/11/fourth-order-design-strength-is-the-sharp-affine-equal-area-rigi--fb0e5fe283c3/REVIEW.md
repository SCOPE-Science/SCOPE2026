# Same-model review

## Correctness

PASS. The source's exact affine Jacobian says that the \(j\)-th facet area is multiplied by
\[
|\det A|\,|A^{-T}x_j|.
\]
Thus equal transformed areas mean that the positive quadratic form
\[
Q=A^{-1}A^{-T}
\]
has one constant value on every design node. For a spherical \(4\)-design, the square of the resulting quadratic defect is a degree-four polynomial integrated exactly by the nodes. Its node average is zero, so its spherical integral is zero; nonnegativity forces the defect to vanish identically and hence \(Q\) is scalar. The explicit six-node example is checked directly to be a spherical \(3\)-design and to have constant transformed facet multiplier under the displayed nonsimilarity.

## Originality

PASS. The primary paper gives both ingredients separately and remarks only that affine maps generally introduce unequal weights. Its inspected full text does not classify exceptional maps preserving equal facet areas and does not state a strength-four threshold or a strength-three counterexample. Searches in Minkowski-polytope, spherical-design, projective-design, and unit-norm-frame terminology found no covering statement.

Residual risk: the quadratic-form lemma may exist in abstract finite-frame language without the geometric formulation surfaced by the searches.

## Value

PASS. The affine-covariance section of the source makes preservation of equal facet weights a natural structural question. Fourth-order design exactness is precisely the first moment level that can test the square of an anisotropic quadratic defect, and the explicit \(3\)-design example proves that this is a real threshold. The result therefore supplies a sharp rigidity boundary rather than a routine corollary.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Congpei An, arXiv:2608.11570v1, especially Corollary 4.3 and Proposition 8.1. Broader projective-design and unit-norm-frame literature was checked for equivalent equal-norm linear-map formulations.

The theorem is exact, three-dimensional, and concerns facet-area preservation only. No quantitative near-rigidity or higher-dimensional sharpness theorem is asserted.
