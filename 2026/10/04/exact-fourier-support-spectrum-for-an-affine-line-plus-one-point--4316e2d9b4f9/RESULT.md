# Exact Fourier-support spectrum for an affine line plus one point over \(\mathbb F_3\)
## Finding
Let \(d\ge2\), let \(u,v\in\mathbb F_3^d\) be linearly independent, and suppose \(f:\mathbb F_3^d\to\mathbb C\) is supported exactly on
\[
x+\{0,u,2u,v\},
\]
with all four values on that support nonzero. Then
\[
|\operatorname{supp}\widehat f|\in\{6,7,8,9\}3^{d-2},
\]
and every one of these four sizes occurs on every support of this affine type.

Equivalently, after affine normalization, a polynomial
\[
P(X,Y)=a+bX+cX^2+eY,
\qquad abce\ne0,
\]
on \(\mu_3^2\) has exactly \(0,1,2\), or \(3\) zeros. In particular, a four-point support containing a full affine line cannot produce a Fourier support smaller than \(6\cdot3^{d-2}\).

## Assumptions and scope
The Fourier transform is taken with respect to the standard additive characters of \(\mathbb F_3^d\); normalization does not affect support. The support geometry is a full affine line of three points together with one point outside that line. The claim is about exact attainable support cardinalities, not coefficient magnitudes or extremizer uniqueness.

## Proof
Translation and an invertible linear change of coordinates reduce the support to
\[
\{0,e_1,2e_1,e_2\}.
\]
Writing the four nonzero values of \(f\) as \(a,b,c,e\), the Fourier transform, up to a nonzero phase, is the evaluation of
\[
P(X,Y)=a+bX+cX^2+eY
\]
at \((X,Y)\in\mu_3^2\). Each pair \((X,Y)\) occurs exactly \(3^{d-2}\) times as the frequency varies, because \(e_1,e_2\) are independent.

For fixed \(X\in\mu_3\), the expression \(P(X,Y)\) is affine-linear in \(Y\) with nonzero coefficient \(e\). Therefore it can vanish for at most one of the three values \(Y\in\mu_3\). There are only three choices of \(X\), so \(P\) has at most three zeros on \(\mu_3^2\). Hence the local Fourier support has size at least \(6\).

It remains to realize each zero count. Put \(\omega=e^{2\pi i/3}\).

For zero zeros, take
\[
(a,b,c,e)=(1,1,1,1).
\]
Then \(1+X+X^2\) equals \(3\) at \(X=1\) and \(0\) at the other two cube roots, so no value of \(P\) vanishes.

For one zero, take
\[
(a,b,c,e)=(1,1,1,-3).
\]
The only zero is \((X,Y)=(1,1)\).

For two zeros, take
\[
(a,b,c,e)=\left(\frac13,\frac{4\omega}{3},\frac{4\omega^2}{3},1\right).
\]
If \(A(X)=a+bX+cX^2\), then
\[
A(1)=A(\omega)=-1,
\qquad
A(\omega^2)=3,
\]
so the zeros are exactly \((1,1)\) and \((\omega,1)\).

For three zeros, take
\[
(a,b,c,e)=\left(\frac{-2-\omega}{3},\frac{1+2\omega}{3},\frac{-2-\omega}{3},1\right).
\]
Here
\[
A(1)=A(\omega)=-1,
\qquad
A(\omega^2)=-\omega,
\]
so the zeros are exactly \((1,1)\), \((\omega,1)\), and \((\omega^2,\omega)\). All four coefficients in every displayed witness are nonzero. Thus the local support sizes are exactly \(9,8,7,6\), and multiplying by \(3^{d-2}\) proves the claim.

## Verification
The proof is analytic and valid in every dimension \(d\ge2\). The accompanying exact verifier represents \(\mathbb Q(\omega)\) as pairs \(r+s\omega\) with \(\omega^2+\omega+1=0\), evaluates all nine local Fourier values for the four displayed witnesses, and checks zero counts \(0,1,2,3\). It also checks the row-pigeonhole obstruction showing that any set of four local zeros would contain two points with the same \(X\), which would force the nonzero coefficient of \(Y\) to vanish. The computation is corroborative only.

## Relationship to prior work
Bonami and Ghobber study \(\mathbb Z_p\times\mathbb Z_p\) and characterize equality cases for cardinality-based uncertainty minima. Their full text explains that the earlier rank-deficient-Fourier-matrix literature determines Meshulam-type minimum functions and partial equality information. Those results concern the minimum spectrum size as support cardinality varies; the inspected material does not give the complete set of attainable Fourier-support sizes for a prescribed four-point affine line-plus-one geometry.

This distinction matters here: cardinality alone does not record the support geometry. The result identifies an exact geometry-dependent gap and all attainable values above it for this affine orbit.

## Limitations
The theorem is specific to the line-plus-one affine support type over \(\mathbb F_3\). It does not classify arbitrary four-point supports over larger fields or all coefficient orbits. A residual literature risk is that a detailed rank-deficient-submatrix table for \(F_3\otimes F_3\) could encode some of these fixed-support facts implicitly; the inspected uncertainty-principle source presents those tables as minimum/rank information rather than this complete fixed-support spectrum.

## References
1. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, first publicly posted 2010-03-26.
2. S. Delvaux and M. Van Barel, *Rank-deficient Submatrices of Fourier Matrices*, Linear Algebra and its Applications 429 (2008), 16–34.
