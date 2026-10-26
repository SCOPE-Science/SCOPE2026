# Fourth Spectral Moment of the Uniform Correlation-Matrix Prior

## Finding

Let \(R\) be uniformly distributed, with respect to Lebesgue measure on its free off-diagonal entries, over the set of positive-definite real correlation matrices of size \(p\times p\), where \(p\ge2\). Set \(A=R-I_p\). Then

\[
\mathbb E\!\left[\operatorname{tr}(A^4)\right]
=\frac{p(p-1)(p-2)(p-3)}{(p+1)^3}
+\frac{2p(p-1)(p-2)}{(p+1)^2}
+\frac{3p(p-1)}{(p+1)(p+3)}.
\]

Equivalently,

\[
\mathbb E\!\left[\operatorname{tr}(A^4)\right]
=\frac{p(p-1)(3p^3+5p^2-13p+9)}{(p+1)^3(p+3)}
=3p-16+\frac{42}{p}+O(p^{-2})
\quad (p\to\infty).
\]

The three summands respectively count four-distinct-index cycles, one repeated opposite-index pair, and a repeated edge in the trace expansion.

## Assumptions and scope

The law is the uniform correlation-matrix law, equivalently the LKJ distribution with shape parameter \(\eta=1\). The formula is asserted only for this uniform case. It is an expectation identity for the fourth spectral moment of \(R-I_p\); it does not claim a variance formula, a concentration bound, or a formula for general \(\eta\).

The uniform law has a Gram representation: take independent random vectors \(U_1,\ldots,U_p\), each uniform on the unit sphere in \(\mathbb R^{p+1}\), and set \(R_{ij}=U_i\cdot U_j\). The Gram matrix is positive definite almost surely and has constant density on the correlation-matrix domain.

## Proof

Write \(d=p+1\). For independent uniform unit vectors in \(\mathbb R^d\), rotational symmetry gives

\[
\mathbb E[(U_i\cdot U_j)^2]=\frac1d,
\qquad
\mathbb E[(U_i\cdot U_j)^4]=\frac{3}{d(d+2)}.
\]

The second identity follows from the standard spherical-coordinate moments: if \(V\) is uniform on the unit sphere, symmetry and \((\sum_{a=1}^d V_a^2)^2=1\) give \(\mathbb E[V_1^4]=3/[d(d+2)]\). Also, for four distinct indices, successive conditioning on one vector at a time yields

\[
\mathbb E[(U_i\cdot U_j)(U_j\cdot U_k)(U_k\cdot U_\ell)(U_\ell\cdot U_i)]=d^{-3}.
\]

Because \(A_{ii}=0\),

\[
\operatorname{tr}(A^4)=\sum_{i,j,k,\ell=1}^{p} A_{ij}A_{jk}A_{k\ell}A_{\ell i}
\]

has no contribution when adjacent indices coincide. The remaining ordered quadruples split into three disjoint cases:

1. **All four indices distinct.** There are \(p(p-1)(p-2)(p-3)\) choices, each with expectation \(d^{-3}\).
2. **Exactly one opposite pair is equal:** \(i=k\) or \(j=\ell\), but not both. There are \(2p(p-1)(p-2)\) choices. The product is a product of two squared inner products sharing one vector; conditional independence given that vector gives expectation \(d^{-2}\).
3. **Both opposite pairs are equal:** \(i=k\) and \(j=\ell\). There are \(p(p-1)\) choices, each contributing \(\mathbb E[(U_i\cdot U_j)^4]=3/[d(d+2)]\).

Summing these contributions and substituting \(d=p+1\) gives the first displayed formula. Algebraic simplification gives the rational expression in the second display. Expanding that rational function at infinity gives \(3p-16+42/p+O(p^{-2})\).

## Verification

The included standard-library script `verify.py` performs exact rational checks of the trace-index case count for every \(p\) from 2 through 12 and checks the rational simplification for every \(p\) from 2 through 40. These finite checks supplement the general proof; they are not used as a substitute for it. The moment identities used in the proof follow from rotational symmetry and the uniform-sphere coordinate moments derived above.

## Relationship to prior work

Wang, Wu, and Chu establish the equivalence between the LKJ correlation-matrix law and a restricted Wishart construction, and identify the uniform case when the Wishart degrees of freedom equal the matrix dimension plus one. That representation supplies the spherical Gram model used here. Their inspected paper does not state the explicit fourth spectral moment above. The present result is a moment calculation for the uniform case, not a new characterization of the LKJ distribution.

## Limitations

The calculation applies to \(\eta=1\) only. No formula for \(\eta\ne1\), no fluctuation law for \(\operatorname{tr}(A^4)\), and no claim about absolute publication priority is made. The literature comparison is targeted rather than exhaustive, and independent audit has not been performed.

## References

Wang, Z., Wu, Y., and Chu, H. (2018). *On equivalence of the LKJ distribution and the restricted Wishart distribution*. arXiv:1809.04746v1. https://arxiv.org/abs/1809.04746
