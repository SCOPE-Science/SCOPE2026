# Cuspidal contact of the two Eckardt singular-locus curves at the Clebsch cubic
## Finding
Over \(\mathbb C\), consider the two rational curves \(C_{[3,2]}\) and \(C_{[4,1]}\) in the intersection of the two irreducible surfaces in the singular locus of the Eckardt hypersurface model described by Keneshlou. At their common point \(p_{\mathrm{Cl}}\) corresponding to the Clebsch cubic, both curve germs are cusps of type \(A_2\), and their local scheme-theoretic intersection has length \(3\).

More precisely, choose an affine representative of the five Sylvester coefficients near \([1:1:1:1:1]\) whose mean is \(1\), write the centered deviations as \(y_0,\ldots,y_4\) with \(\sum_i y_i=0\), and put \(u_j=e_j(y_0,\ldots,y_4)\) for \(2\le j\le5\). Since the standard four-dimensional representation of \(S_5\) is a reflection representation, \(\mathbb C[y_0,\ldots,y_4]^{S_5}/(\sum_i y_i)=\mathbb C[u_2,u_3,u_4,u_5]\). Thus \((u_2,u_3,u_4,u_5)\) are analytic coordinates on the local quotient, hence on the cubic-surface moduli chart at the Clebsch point.

In these coordinates,
\[
I_{[3,2]}=(15u_4-4u_2^2,\ 25u_5-12u_2u_3,\ 4u_2^3+135u_3^2)
\]
and
\[
I_{[4,1]}=(20u_4+3u_2^2,\ 50u_5+u_2u_3,\ 2u_2^3+5u_3^2).
\]
Hence each completed local ring is a plane cusp after eliminating \(u_4,u_5\), while
\[
I_{[3,2]}+I_{[4,1]}=(u_5,u_4,u_3^2,u_2u_3,u_2^2)
\]
up to replacing the displayed generators by a Gröbner basis. The quotient therefore has basis \(1,u_2,u_3\) and length \(3\).

## Assumptions and scope
The ground field is \(\mathbb C\). The statement is local at the Clebsch cubic and concerns the two specific curves \(C_{[3,2]}\) and \(C_{[4,1]}\) in Keneshlou's singular-locus decomposition. No assertion is made here about their local intersection at the Fermat cubic, nor about a complete local equation for either two-dimensional surface component.

The local quotient description uses the fact that the Clebsch point has all five Sylvester coefficients nonzero and equal, so one may normalize their mean to \(1\). Centering then identifies a neighborhood before quotienting with the standard \(S_5\)-representation \(\sum_i y_i=0\). The elementary symmetric functions of degrees \(2,3,4,5\) freely generate its invariant ring.

## Proof
Keneshlou identifies the two intersection curves by Sylvester multiplicity patterns \([3,2]\) and \([4,1]\). After the mean-one normalization and centering, a point of the first curve is represented, up to permutation, by
\[
(2t,2t,2t,-3t,-3t),
\]
while a point of the second is represented by
\[
(s,s,s,s,-4s).
\]
These vectors have coordinate sum zero, and every sufficiently near point of the respective curve germ has this form for a unique normalization parameter.

Taking elementary symmetric functions gives the exact quotient parametrizations
\[
C_{[3,2]}:\quad (u_2,u_3,u_4,u_5)=(-15t^2,-10t^3,60t^4,72t^5),
\]
\[
C_{[4,1]}:\quad (u_2,u_3,u_4,u_5)=(-10s^2,-20s^3,-15s^4,-4s^5).
\]
Eliminating \(t\) and \(s\), respectively, yields the two displayed prime ideals. In the first case, eliminating \(u_4,u_5\) leaves \(4u_2^3+135u_3^2=0\); in the second, it leaves \(2u_2^3+5u_3^2=0\). Over \(\mathbb C\), both are analytically equivalent to \(v^2+u^3=0\), so both germs are \(A_2\) cusps. Their reduced tangent cones are therefore the common line \(u_3=u_4=u_5=0\).

Combining the two ideals and row-reducing their Gröbner basis gives
\[
(u_5,u_4,u_3^2,u_2u_3,u_2^2).
\]
The local quotient has vector-space basis \(1,u_2,u_3\), proving that the scheme-theoretic intersection is isolated at the Clebsch point and has length \(3\).

## Verification
The bundled script `artifacts/verify.py` reconstructs both centered root patterns, computes all elementary symmetric functions, performs both eliminations, checks the two cusp equations, computes the sum ideal, and verifies the three standard monomials. Running it with Python and SymPy prints `VERIFY_OK`.

## Relationship to prior work
Keneshlou proves that the singular locus of the Eckardt hypersurface model has two rational surface components whose intersection consists of two rational curves \(C_{[3,2]}\) and \(C_{[4,1]}\), and states that these curves meet at the Clebsch and Fermat cubic surfaces. The paper also identifies their Sylvester multiplicity patterns. It does not give local equations for the curve germs at the Clebsch point, identify them as cusps, or compute the length of their local intersection scheme.

The patterns \([3,2]\) and \([4,1]\) are closely related to classical coincident-root or multiple-root loci of quintics. Chipalkatti and Kurmann describe singular loci and normalization behavior for general coincident-root loci, while Lee--Sturmfels give equations, parametrizations, and duality data for multiple-root loci including the degree-five partitions. Those results provide the appropriate broader comparison class, but the inspected statements do not identify the centered \(S_5\)-quotient curve germs occurring in cubic-surface moduli or imply the displayed pair of local quotient ideals and their length-three intersection without the additional quotient calculation above.

## Limitations
The finding is local at one of the two intersection points. The Fermat point is excluded because the birational moduli map has exceptional behavior there. The calculation does not determine the full completed local ring of the reducible two-dimensional singular-locus surface at the Clebsch point. The broader coincident-root literature is extensive, so an equivalent local calculation under different invariant coordinates remains a residual literature risk.

## References
H. Keneshlou, *Cubic surfaces on the singular locus of the Eckardt hypersurface*, arXiv:1909.05554; Le Matematiche 75 (2020), DOI:10.4418/2020.75.2.7.

H. Lee and B. Sturmfels, *Duality of Multiple Root Loci*, arXiv:1508.00202; Journal of Algebra 446 (2016), 499--526.

S. Kurmann, *Some remarks on equations defining coincident root loci*, arXiv:1108.4532; Journal of Algebra 352 (2012), 223--231.

J. Chipalkatti, *On equations defining Coincident Root loci*, Journal of Algebra 267 (2003), 246--271, DOI:10.1016/S0021-8693(03)00336-3.
