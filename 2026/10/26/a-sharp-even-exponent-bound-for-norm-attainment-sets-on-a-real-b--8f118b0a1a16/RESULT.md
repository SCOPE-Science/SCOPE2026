# A sharp even-exponent bound for norm-attainment sets on a real Banach plane

## Finding

For every even integer \(p\ge 2\), every real linear operator \(T:\ell_p^2\to\ell_p^2\) that is not a scalar multiple of an isometry has at most \(p\) norm-attaining unit vectors. The bound is sharp at \(p=4\): the operator \(T(x,y)=(x+y,x-y)\) attains its norm at exactly

\[
M_T=\left\{(\varepsilon 2^{-1/4},\delta 2^{-1/4}):\varepsilon,\delta\in\{-1,1\}\right\}.
\]

## Assumptions and scope

All spaces and operators are real. The exponent \(p\) is an even integer with \(p\ge2\). The norm is \(\|(x,y)\|_p=(|x|^p+|y|^p)^{1/p}\), and

\[
M_T=\{z\in\mathbb R^2:\|z\|_p=1,\ \|Tz\|_p=\|T\|\}.
\]

The zero operator is excluded because it is a scalar multiple of an isometry. No claim is made here for odd exponents, complex spaces, or dimensions greater than two. The upper bound for even \(p\ge6\) is not claimed to be optimal.

## Proof

Write \(T(x,y)=(ax+by,cx+dy)\), with real coefficients. Since \(p\) is even, define the homogeneous polynomial of degree \(p\)

\[
Q(x,y)=\|T\|^p(x^p+y^p)-\big((ax+by)^p+(cx+dy)^p\big).
\]

The operator-norm inequality \(\|T(x,y)\|_p\le\|T\|\|(x,y)\|_p\) gives \(Q(x,y)\ge0\) for every real pair \((x,y)\). If \(Q\) were identically zero, then \(\|Tz\|_p=\|T\|\|z\|_p\) for every \(z\), so the nonzero operator \(T/\|T\|\) would be an isometry. Thus \(Q\) is not the zero polynomial.

Every norm-attaining unit vector is a zero of \(Q\). Regard its zero set as directions in the real projective line: a direction is the class of all nonzero scalar multiples of a vector. At any real projective zero, use a local affine coordinate (and the reciprocal coordinate for the direction at infinity). The resulting one-variable polynomial is nonnegative on a neighbourhood of the zero, so its zero has even multiplicity. A nonzero homogeneous polynomial of degree \(p\) has at most \(p\) projective zeros counted with multiplicity. Hence \(Q\) has at most \(p/2\) distinct real projective zero directions. Each direction corresponds to exactly two antipodal points on the unit sphere, so \(|M_T|\le p\).

To show sharpness at \(p=4\), take \(T(x,y)=(x+y,x-y)\). Then

\[
\|T(x,y)\|_4^4=(x+y)^4+(x-y)^4=2(x^4+y^4)+12x^2y^2.
\]

On the unit sphere, \(x^4+y^4=1\), and \(x^2y^2\le (x^4+y^4)/2=1/2\). Thus \(\|T(x,y)\|_4^4\le8\), with equality exactly when \(x^2=y^2\). The unit-sphere constraint then forces \(|x|=|y|=2^{-1/4}\), giving precisely the four points displayed above. Finally, \(T\) is not a scalar multiple of an isometry: the unit vectors \((1,0)\) and \((2^{-1/4},2^{-1/4})\) have different image norms, since their fourth-power image norms are respectively \(2\) and \(8\).

## Verification

The bound follows from an exact polynomial argument; no numerical experiment is used as proof. The only multiplicity fact needed is that a real zero of a nonnegative one-variable polynomial has even multiplicity. The direction at infinity is covered by changing projective coordinate. The example is verified by the exact expansion and the equality condition in \(x^2y^2\le1/2\). The result establishes a general upper bound for even exponents and an optimal count for \(p=4\), but does not determine the optimal count for every even exponent.

## Relationship to prior work

Debmalya Sain's 2016 preprint, *On the norm attainment set of a bounded linear operator*, proves \(|M_T|\le2(8p-5)\) for real \(\ell_p^2\) when \(T\) is not a scalar multiple of an isometry and explicitly asks for an optimal bound. The argument above uses the additional nonnegativity and even-degree structure of a binary form, yielding \(|M_T|\le p\) for even \(p\) and an exact sharp answer at \(p=4\).

Sain's later work on extreme contractions characterizes norm attainment in Hilbert spaces, which covers the Hilbert exponent but not the non-Hilbert \(\ell_4^2\) case. His semi-inner-product characterization gives a general criterion for norm attainment, but does not give this cardinality bound. No exact prior statement for the even-exponent count or the four-point extremizer was located in the literature searches recorded with this result.

## Limitations

The proof is specific to two real dimensions, where a homogeneous polynomial has finitely many projective zero directions. It does not extend by the same root-count argument to dimensions greater than two. The bound \(|M_T|\le p\) is not claimed sharp for even \(p\ge6\), and the optimal bound for odd \(p\) remains unresolved here. The literature search is not a proof that no independent treatment exists.

## References

1. D. Sain, “On the norm attainment set of a bounded linear operator,” arXiv:1608.00755, first public version 2016-08-02; *Journal of Mathematical Analysis and Applications* 457 (2018), 67–76. DOI: 10.1016/j.jmaa.2017.07.070.
2. D. Sain, “On extreme contractions and the norm attainment set of a bounded linear operator,” arXiv:1708.07333; *Annales of Functional Analysis* 10 (2019), 135–143. DOI: 10.1215/20088752-2018-0014.
3. D. Sain, “On the norm attainment set of a bounded linear operator and semi-inner-products in normed spaces,” arXiv:1802.10439; *Indian Journal of Pure and Applied Mathematics* 51 (2020), 179–186.
