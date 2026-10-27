# A sign-cell bound for norm attainment on odd-exponent Banach planes

## Finding
For every odd integer \(p\ge3\) and every real linear operator \(T:\ell_p^2\to\ell_p^2\) that is not a scalar multiple of an isometry, define
\[
M_T=\{x\in S_{\ell_p^2}:\|Tx\|_p=\|T\|\}.
\]
Then
\[
|M_T|\le 4(p-1).
\]
In particular, for \(p=3\), a non-isometric operator on the real cubic plane has at most eight norm-attaining unit vectors.

## Assumptions and scope
The scalar field is \(\mathbb R\), the domain and range are both the two-dimensional sequence space \(\ell_p^2\), and \(p\) is an odd integer at least three. The operator is linear and is not a scalar multiple of an isometry. No optimality of the bound is claimed.

## Proof
Write \(T(x,y)=(a_1x+b_1y,a_2x+b_2y)\), and put \(M=\|T\|^p>0\). The function
\[
G(x,y)=|a_1x+b_1y|^p+|a_2x+b_2y|^p-M(|x|^p+|y|^p)
\]
is everywhere nonpositive and is continuously differentiable away from the origin. Its zero directions are exactly the projective directions represented by norm-attaining unit vectors.

Mark the two coordinate-axis directions and the kernels of the nonzero rows of \(T\). There are at most four marked directions, so they divide the real projective line into at most four open arcs. On any such arc the signs of both input coordinates and of each nonzero output coordinate are fixed. With \(u=|x|>0\) and \(v=|y|>0\), the restriction of \(G\) to the arc is represented by a homogeneous polynomial
\[
P(u,v)=\delta_1(\alpha_1u+\beta_1v)^p+\delta_2(\alpha_2u+\beta_2v)^p-M(u^p+v^p),
\]
where \(\delta_i\in\{-1,1\}\) is the fixed sign of the corresponding output and \(\alpha_i,\beta_i\) are the matrix entries after the fixed input sign changes. These coefficients need not be nonnegative.

The polynomial \(P\) cannot be identically zero. Indeed, if it were, the coefficients of \(u^{p-1}v\) and \(uv^{p-1}\) would give
\[
\delta_1\alpha_1^{p-1}\beta_1+\delta_2\alpha_2^{p-1}\beta_2=0,
\qquad
\delta_1\alpha_1\beta_1^{p-1}+\delta_2\alpha_2\beta_2^{p-1}=0.
\]
If all four coefficients are nonzero, division of these equations yields
\((\alpha_1/\beta_1)^{p-2}=(\alpha_2/\beta_2)^{p-2}\). Since \(p-2\) is odd, the two ratios are equal, so the rows are proportional; the first equation then makes their signed \(p\)-th powers cancel, contradicting \(M(u^p+v^p)>0\). If any coefficient is zero, the same two equations force each row to be supported on at most one coordinate. If either row is zero, or if both rows occupy the same coordinate, one of the pure-power coefficients vanishes, contradicting the identity with \(M>0\). Hence the rows occupy different coordinates, and comparison of the two pure-power coefficients gives equal absolute values \(M^{1/p}\) for their nonzero entries. In that case \(T\) is a scalar multiple of a signed permutation, hence a scalar multiple of an isometry, also a contradiction.

Now consider a maximizing direction in the closure of one of the arcs. It is a zero of the corresponding polynomial, and its derivative in a local projective coordinate is zero because \(G\le0\) and \(G\) is continuously differentiable. Thus the zero has multiplicity at least two. A nonzero polynomial of degree at most \(p\) has at most \(\lfloor p/2\rfloor\) distinct roots of multiplicity at least two. Each arc closure therefore contains at most \(\lfloor p/2\rfloor\) maximizing directions. Since there are at most four arcs, the number of maximizing projective directions is at most \(4\lfloor p/2\rfloor=2(p-1)\). Each such direction corresponds to exactly two antipodal unit vectors, giving \(|M_T|\le4(p-1)\), as claimed.

## Verification
The argument is symbolic: it uses the degree of a piecewise polynomial, differentiability of \(|t|^p\) for \(p>1\), and root multiplicity at a global maximum. No numerical enumeration is used as a substitute for the universal proof. For \(p=3\), each sign-sector polynomial is cubic and can contain at most one distinct double root. The estimate is an upper bound only; equality is not asserted.

## Relationship to prior work
Debmalya Sain's paper proves \(|M_T|\le2(8p-5)\) for every integer \(p\ge2\) when \(T\) is not a scalar multiple of an isometry on \(\ell_p^2\), and explicitly leaves the optimal bound open. For odd \(p\ge3\), the present estimate \(4(p-1)\) is strictly smaller than \(2(8p-5)\). The claim is a sharper bound on the same norm-attainment set, not a solution of the optimal-bound problem.

## Limitations
The bound is not claimed to be sharp, and the exact maximum cardinality remains unresolved here. The proof applies only to real two-dimensional \(\ell_p\) spaces for odd integer \(p\ge3\); it does not address noninteger exponents, higher dimensions, complex scalars, or the isometry case.

## References
1. D. Sain, “On the norm attainment set of a bounded linear operator,” arXiv:1608.00755 (first submitted 2016-08-02), especially Theorem 2.7 and the discussion of the optimal-bound question. https://arxiv.org/abs/1608.00755
