# Tight Fuss parallelotopes have an exact ellipsoid-controlled volume spectrum
## Finding
Let
\[
n\ge2,
\]
let \(A\) be a positive definite symmetric linear map on \(\mathbb R^n\), and assume the higher-dimensional Fuss condition
\[
\operatorname{tr}(A^2)=1.
\tag{1}
\]
Take
\[
E_{\mathrm{out}}=\mathbb S^{n-1},
\qquad
E_{\mathrm{in}}=A\mathbb S^{n-1}.
\tag{2}
\]

Gibson, Saldanha, and Tomei prove that the labeled centrally symmetric parallelotopes simultaneously inscribed in \(E_{\mathrm{out}}\) and circumscribed about \(E_{\mathrm{in}}\) are parametrized by \(O(n)\).

For an orthonormal frame
\[
Q=(q_1,\ldots,q_n)\in O(n),
\]
the corresponding tight parallelotope has half-edge vectors
\[
\ell_k q_k,
\qquad
\ell_k=\|Aq_k\|.
\tag{3}
\]
Therefore
\[
\boxed{
\operatorname{Vol}(P_Q)
=
2^n\prod_{k=1}^n\|Aq_k\|.
}
\tag{4}
\]

As \(Q\) ranges over \(O(n)\), these volumes fill exactly the closed interval
\[
\boxed{
\left[
2^n\det A,\;
2^n n^{-n/2}
\right].
}
\tag{5}
\]

The lower endpoint is attained exactly when the frame diagonalizes \(A\):
\[
\boxed{
\operatorname{Vol}(P_Q)=2^n\det A
\iff
Q^{\mathsf T}AQ\text{ is diagonal}.
}
\tag{6}
\]

The upper endpoint is attained exactly when
\[
\boxed{
\|Aq_1\|
=
\cdots
=
\|Aq_n\|
=
\frac1{\sqrt n}.
}
\tag{7}
\]
An orthonormal frame satisfying (7) exists for every \(A\) obeying (1). Hence every admissible inner ellipsoid has a tight regular cube:
\[
\boxed{
\text{there is a cube of side length }\frac2{\sqrt n}
\text{ inscribed in }\mathbb S^{n-1}
\text{ and circumscribed about }A\mathbb S^{n-1}.
}
\tag{8}
\]

There is a dual volume statement. The polar of \(P_Q\) is
\[
C_Q
=
P_Q^\circ
=
\operatorname{conv}
\left\{
\pm\frac{q_k}{\|Aq_k\|}:1\le k\le n
\right\},
\tag{9}
\]
a tight cross polytope circumscribed about the unit sphere and inscribed in
\[
A^{-1}\mathbb S^{n-1}.
\]
Its volume spectrum is exactly
\[
\boxed{
\left[
\frac{2^n n^{n/2}}{n!},\;
\frac{2^n}{n!\det A}
\right].
}
\tag{10}
\]
For corresponding polar pairs,
\[
\boxed{
\operatorname{Vol}(P_Q)\operatorname{Vol}(C_Q)
=
\frac{4^n}{n!}.
}
\tag{11}
\]

Thus the entire tight Fuss family has a complete Euclidean volume profile. Principal-axis parallelotopes minimize volume, while a regular cube always maximizes it.

## Assumptions and scope
The ellipsoids are centered and use the normalization of the source: the outer ellipsoid is the Euclidean unit sphere, while the inner ellipsoid is its image under the positive symmetric map \(A\).

For \(n\ge2\), condition (1) implies every eigenvalue of \(A\) is strictly less than \(1\), so the inner ellipsoid lies strictly inside the unit ball.

A tight parallelotope means a centrally symmetric parallelotope whose vertices lie on the unit sphere and whose facets are tangent to the inner ellipsoid. The source proves that every such parallelotope is orthogonal and that all labeled tight parallelotopes are parametrized by \(O(n)\).

The statement concerns ordinary Euclidean \(n\)-volume in this normalized realization. Under an invertible linear transformation sending a general outer ellipsoid to the unit sphere, Euclidean volume scales by the determinant of that transformation.

## Proof
The source proves that a tight parallelotope associated with
\[
Q=(q_1,\ldots,q_n)\in O(n)
\]
has vertices
\[
\pm\ell_1q_1\pm\cdots\pm\ell_nq_n
\]
with
\[
\ell_k=\|Aq_k\|.
\tag{12}
\]
Because the \(q_k\) are orthonormal, its edge vectors have lengths
\[
2\ell_1,\ldots,2\ell_n
\]
in mutually orthogonal directions. Hence
\[
\operatorname{Vol}(P_Q)
=
2^n\prod_{k=1}^n\ell_k,
\]
which is (4).

Set
\[
B=A^2.
\]
Then
\[
d_k
=
\ell_k^2
=
q_k^{\mathsf T}Bq_k,
\tag{13}
\]
and
\[
\sum_{k=1}^n d_k
=
\operatorname{tr}(B)
=
1.
\tag{14}
\]

For the lower bound, write \(B\) in the orthonormal basis \(Q\). Hadamard's determinant inequality gives
\[
\det B
\le
\prod_{k=1}^n d_k.
\tag{15}
\]
Since \(A\) is positive definite,
\[
\sqrt{\det B}=\det A.
\]
Taking square roots in (15) and using (4) yields
\[
\operatorname{Vol}(P_Q)
\ge
2^n\det A.
\tag{16}
\]
Equality in Hadamard's inequality holds exactly when the matrix of \(B\) in the frame \(Q\) is diagonal. Because \(A\) is positive definite, \(A\) and \(A^2\) have the same eigenspaces. This proves (6).

For the upper bound, the arithmetic-geometric mean inequality and (14) give
\[
\prod_{k=1}^n d_k
\le
\left(\frac1n\right)^n.
\tag{17}
\]
Therefore
\[
\operatorname{Vol}(P_Q)
\le
2^n n^{-n/2}.
\tag{18}
\]
Equality in (17) holds exactly when
\[
d_1=\cdots=d_n=\frac1n,
\]
which is precisely (7).

It remains to show that equality in the upper bound is always attainable. We use an elementary constant-diagonal lemma.

**Lemma.** If \(B\) is symmetric on an \(m\)-dimensional Euclidean space and
\[
\operatorname{tr}(B)=mc,
\]
then there is an orthonormal basis
\[
u_1,\ldots,u_m
\]
with
\[
u_j^{\mathsf T}Bu_j=c
\qquad
(1\le j\le m).
\]

**Proof of the lemma.** The average eigenvalue is \(c\), so the minimum and maximum eigenvalues straddle \(c\). By continuity of the Rayleigh quotient on the unit sphere, there is a unit vector \(u_1\) with
\[
u_1^{\mathsf T}Bu_1=c.
\]
Compress \(B\) to \(u_1^\perp\). Its trace is
\[
mc-c=(m-1)c.
\]
Apply the same argument inductively to the compression. This constructs the required orthonormal basis. \(\square\)

Applying the lemma to \(B=A^2\) with
\[
c=\frac1n
\]
produces a frame satisfying (7). For this frame all half-edge lengths equal \(1/\sqrt n\), so \(P_Q\) is a regular cube. This proves (8).

To see that every intermediate volume is attained, note that the volume in (4) is a continuous function of \(Q\). For \(n\ge2\), \(SO(n)\) is connected. Multiplying one column of \(Q\) by \(-1\) changes the component of \(O(n)\) but leaves every value \(\|Aq_k\|\), and hence the volume, unchanged. Thus the full volume image is a connected compact subset of \(\mathbb R\) containing both endpoints in (5); it is exactly the interval (5).

For the polar statement, an orthogonal parallelotope
\[
P_Q
=
\sum_{k=1}^n[-\ell_kq_k,\ell_kq_k]
\]
has polar
\[
P_Q^\circ
=
\operatorname{conv}
\left\{
\pm\frac{q_k}{\ell_k}:1\le k\le n
\right\}.
\tag{19}
\]
The standard cross-polytope determinant formula gives
\[
\operatorname{Vol}(C_Q)
=
\frac{2^n}{n!\prod_{k=1}^n\ell_k}.
\tag{20}
\]
Combining (20) with (4) proves (11), while inversion of the interval (5) gives (10). The same continuity argument shows that every volume in (10) occurs.

## Verification
The proof is symbolic and covers every \(n\ge2\).

The source-dependent step was checked directly in the open-access full text. The paper proves that tight centrally symmetric parallelotopes exist exactly when
\[
\operatorname{tr}(A^2)=1,
\]
that each tight parallelotope is orthogonal, and that for frame \(Q=(q_k)\) its half-edge lengths are
\[
\ell_k=\|Aq_k\|.
\]
The paper also states the polar cross-polytope correspondence.

The accompanying `verify.py` independently checks deterministic anisotropic positive matrices in dimensions \(2\) through \(7\). It reconstructs constant-diagonal orthonormal frames recursively, verifies the lower and upper volume equalities, samples additional orthogonal frames to check both bounds, and checks the constant polar volume product (11). These finite computations are corroborative only.

## Relationship to prior work
Gibson, Saldanha, and Tomei prove the higher-dimensional Fuss existence theorem and the \(O(n)\)-parametrization of tight parallelotopes. Their paper does not discuss the volume of these parallelotopes; direct full-text searches for “volume”, “determinant”, and “Hadamard” return no occurrence relevant to such a spectrum.

The present result uses their exact half-edge formula and asks how the determinant-like product varies over the full orthogonal parameter space. Hadamard's inequality gives the principal-axis minimum, while the trace constraint gives a universal arithmetic-geometric mean maximum. The constant-diagonal lemma supplies the non-obvious equality realization and shows that every admissible ellipsoid has a tight regular cube.

The dual cross-polytope spectrum is not a separate optimization: polarity turns the parallelotope volume product into its reciprocal, with the exact constant product (11).

Targeted searches under “higher dimensional Euler Fuss”, “Poncelet parallelotope”, “tight parallelotope”, “ellipsoid”, “volume spectrum”, “determinant”, and the dual cross-polytope formulation did not locate a statement implying (5), (8), or (10).

## Limitations
The theorem applies to the centered ellipsoid pair in the source's Fuss regime
\[
\operatorname{tr}(A^2)=1.
\]
It does not address nonconcentric ellipsoids, non-centrally-symmetric cubical polytopes, or volume optimization for the source's tight simplex family.

The upper volume is universal after unit-sphere normalization, but the lower volume depends on
\[
\det A.
\]
No stability estimate is claimed for frames whose volumes are close to either endpoint.

The exact interval statement uses connectedness of the orthogonal parameter family and therefore concerns the complete source family of labeled tight parallelotopes, not an arbitrary restricted subfamily.

## References
1. Peter Gibson, Nicolau Saldanha, and Carlos Tomei, *Higher dimensional versions of theorems of Euler and Fuss*, arXiv:2210.17350, first public version 2022-10-31; *Arnold Mathematical Journal* 10 (2024), 409--421, DOI 10.1007/s40598-023-00243-4.
