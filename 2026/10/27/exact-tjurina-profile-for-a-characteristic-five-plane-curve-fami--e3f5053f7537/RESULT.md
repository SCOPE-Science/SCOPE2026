# Exact Tjurina profile for a characteristic-five plane-curve family \(f_k\)

## Finding
Let \(K\) be an algebraically closed field of characteristic \(5\), let \(k\ge14\) be an integer, and put \(f_k=x^3+xy^{13}+y^k\in K[[x,y]]\). Its Tjurina number is exactly
\[
\tau(f_k)=\dim_K K[[x,y]]/(f_k,\partial_xf_k,\partial_yf_k)
=\min\{k+12+3\mathbf{1}_{k\equiv2\pmod5},37\}.
\]
In particular, the value stabilizes at \(37\) for every \(k\ge25\); the residue class \(k\equiv2\pmod5\) produces an earlier jump at \(k=17\), and the value reaches \(37\) already at \(k=22\).

## Assumptions and scope
The coefficient field is algebraically closed of characteristic exactly \(5\), and the exponent is an integer \(k\ge14\). The Tjurina number is the length of the completed local algebra defined above. No assertion is made for other characteristics, for \(k<14\), or about modality beyond what follows from independently established results.

## Proof
Write \(R=K[[x,y]]\) and \(I_k=(f_k,\partial_xf_k,\partial_yf_k)\). Since \(13=3\) in characteristic \(5\), multiplying the derivative generators by units and reducing \(f_k\) modulo \(\partial_xf_k\) gives
\[
I_k=(x^2+2y^{13},\;xy^{12}+2k y^{k-1},\;y^k-xy^{13}).
\]

First suppose \(k\not\equiv2\pmod5\). From \(xy^{12}=-2k y^{k-1}\) we obtain \(xy^{13}=-2k y^k\), so the third generator is \((1+2k)y^k\). Its coefficient is nonzero, hence \(y^k\in I_k\) and \(xy^{13}=0\) in the quotient. The S-polynomial of \(x^2+2y^{13}\) and \(xy^{12}+2k y^{k-1}\) is \(2y^{25}-2kxy^{k-1}\); the second term vanishes because \(k\ge14\) and \(xy^{13}=0\). Thus \(y^{25}\in I_k\). Consequently
\[
I_k=(x^2+2y^{13},\;xy^{12}+2k y^{k-1},\;y^r),\qquad r=\min(k,25).
\]
With lexicographic order \(x>y\), these generators form a Gröbner basis: their leading monomials are \(x^2,xy^{12},y^r\), and the S-polynomials reduce using \(y^r=0\) and \(k\ge14\). A basis of the quotient is therefore \(1,y,\ldots,y^{r-1},x,xy,\ldots,xy^{11}\), so \(\tau(f_k)=r+12=\min(k+12,37)\).

Now suppose \(k\equiv2\pmod5\). Then \(2k=4\) in \(K\), so the second generator becomes \(xy^{12}-y^{k-1}\), and the third generator is redundant because \(xy^{13}=y^k\). Hence
\[
I_k=(x^2+2y^{13},\;xy^{12}-y^{k-1}).
\]
The S-polynomial of these two generators is \(2y^{25}+xy^{k-1}=2y^{25}+y^{2k-14}\). The exponent \(2k-14\) is never \(25\) for an integer \(k\equiv2\pmod5\). Factoring out the smaller power of \(y\) leaves a power series with nonzero constant term, hence a unit in \(R\). Therefore \(y^r\in I_k\), where \(r=\min(25,2k-14)\), and
\[
I_k=(x^2+2y^{13},\;xy^{12}-y^{k-1},\;y^r).
\]
Again the leading monomials are \(x^2,xy^{12},y^r\); the S-polynomials reduce by these generators. The same monomial basis has length \(r+12\), giving \(\tau(f_k)=\min(2k-2,37)\). Since the allowed exponents in this residue class begin with \(17\) and then \(22\), this equals \(\min(k+15,37)\) on the specified range. Combining the two cases proves the formula.

The finite length in both cases also verifies that the germ is isolated. The proof is an exact local-algebra argument; no finite experiment is used as a substitute for the all-\(k\) statement.

## Verification
The proof reduces the Tjurina ideal in the completed local ring to a three-generator monomial-leading ideal in each residue case. The unit-factor step in the exceptional residue class is valid in \(K[[x,y]]\), not merely in the polynomial ring. The standard monomials are exactly \(y^j\) for \(0\le j<r\) and \(xy^j\) for \(0\le j<12\), yielding length \(r+12\). The resulting formula agrees with the published sample values \(\tau(f_{16})=28\), \(\tau(f_{17})=32\), and \(\tau(f_{18})=30\). No independent audit has been performed.

## Relationship to prior work
Ma, Ying, and Zuo study Tjurina-number jumps in positive characteristic and explicitly record the characteristic-five example \(\tau(f_{17})=32\), while the neighboring values at \(k=16\) and \(k=18\) agree with the characteristic-zero expression \(k+12\). The result here gives a uniform exact profile for every integer \(k\ge14\), including stabilization at \(37\); it does not claim a new general theorem about modality or replace their classification results.

## Limitations
The statement is restricted to characteristic \(5\) and the displayed family. The complete primary preprint could not be retrieved during this inspection; the accessible arXiv record and the inspected text excerpt establish the motivating example but do not provide a full-text search of every later section. Thus the mathematical proof is self-contained, while literature-overlap risk remains for an uninspected portion of the same preprint. No claim is made about other characteristics or about modality for every member of the family.

## References
Hongrui Ma, Aoyu Ying, and Huaiqing Zuo, “Tjurina Number Jumps and Unimodal Hypersurface Singularities in Positive Characteristic,” arXiv:2510.02619v1, first submitted 2025-10-02. The source records the characteristic-zero formula \(\tau(f_k)=k+12\) and the characteristic-five values at \(k=16,17,18\).
