# Exact dyadic joint valuation law for two binomial factors

## Finding

For each integer \(L\geq0\), let \(n\) range uniformly over \(\{0,1,\ldots,2^L-1\}\) and put
\[
X(n)=\nu_2\!\left(\binom{2n}{n}\right),\qquad
Y(n)=\nu_2\!\left(\binom{3n}{n}\right).
\]
Define the **joint enumerator**
\[
P_L(u,v)=\sum_{0\leq n<2^L}u^{X(n)}v^{Y(n)}.
\]
With formal indeterminates \(z,u,v\), its complete length-generating function is
\[
\boxed{\sum_{L\geq0}P_L(u,v)z^L=\frac{N(u,v,z)}{D(u,v,z)}}
\]
where
\[
\begin{aligned}
N={}&1+uz-uvz+u^2v^2z^2-u^2vz^2-uv^2z^2,\\
D={}&1-z-uvz-uz^2+uvz^2-uv^2z^2+u^2vz^3+uv^2z^3.
\end{aligned}
\]
In particular, the exact mixed valuation covariance is, for every \(L\geq0\),
\[
\boxed{\operatorname{Cov}(X,Y)=\frac{5L}{12}-\frac49+
\frac{9+7(-1)^L}{36\,2^L}.}
\]
The individual and mixed means are
\[
\begin{aligned}
\mathbb E[X]&=\frac L2,\\
\mathbb E[Y]&=\frac L2-\frac23+\frac{3+(-1)^L}{6\,2^L},\\
\mathbb E[XY]&=\frac{L^2}{4}+\frac L{12}-\frac49+
\frac{(9L+9)+(3L+7)(-1)^L}{36\,2^L}.
\end{aligned}
\]
Thus \(\operatorname{Cov}(X,Y)/L\to5/12\) as \(L\to\infty\). The full rational enumerator determines all finite-length joint probabilities, not only these moments.

## Assumptions and scope

The valuation \(\nu_2(m)\) is the exponent of \(2\) in a positive integer \(m\); the binomial coefficient \(\binom00\) is \(1\), so the case \(n=0\) has \(X=Y=0\). All statements apply to every integer \(L\geq0\), with no limiting or primality hypothesis. The generating-function equality is in \(\mathbb Z[u,v][[z]]\); its denominator has constant term \(1\). Every expectation refers to the uniform distribution on the stated \(2^L\) integers.

## Proof

**1. Carry model.** Kummer's theorem implies \(X(n)=s_2(n)\), the binary digit sum. Also \(Y(n)\) counts carries in the binary addition \(n+2n=3n\). Write \(n=\sum_{j=0}^{L-1}b_j2^j\), with \(b_j\in\{0,1\}\), \(b_{-1}=0\), and \(b_j=0\) for \(j\geq L\). Start with \(c_0=0\) and define
\[
c_{j+1}=\left\lfloor\frac{b_j+b_{j-1}+c_j}{2}\right\rfloor
\qquad(0\leq j<L).
\]
At the first zero-padded position \(j=L\), the final carry is \(c_{L+1}=\lfloor(b_{L-1}+c_L)/2\rfloor\); no carry can occur beyond this position. Hence
\[
X=\sum_{j=0}^{L-1}b_j,\qquad Y=\sum_{j=0}^{L}c_{j+1}.
\]

**2. Transfer matrix and exact rational form.** Use states \((b_{j-1},c_j)\) ordered as \((0,0),(0,1),(1,0),(1,1)\). Reading bit \(b_j\) creates weight \(u^{b_j}v^{c_{j+1}}\) and moves to \((b_j,c_{j+1})\). Thus the weighted transition matrix and terminal carry vector are
\[
M=\begin{pmatrix}
1&0&u&0\\
1&0&0&uv\\
1&0&0&uv\\
0&v&0&uv
\end{pmatrix},\qquad
f=\begin{pmatrix}1\\1\\1\\v\end{pmatrix}.
\]
For the row vector \(e=(1,0,0,0)\), bijection between length-\(L\) bit strings and integers in the stated interval gives the **exact identity**
\[
P_L(u,v)=eM^Lf.
\]
Summing the geometric matrix series yields \(\sum_{L\geq0}z^LP_L=e(I-zM)^{-1}f\). Direct determinant computation gives
\[
\det(I-zM)=D(u,v,z),\qquad
\det((I-zM)_{\mathrm{col}\,1\gets f})=N(u,v,z).
\]
Here the latter matrix is obtained by replacing its first column by \(f\). Cramer's rule proves the displayed exact generating function. The standalone checker independently verifies both multivariate determinant identities coefficient by coefficient over the integers, without numerical substitution.

**3. Moments.** Differentiate the rational identity in \(u\) and \(v\), then set \(u=v=1\). The three resulting ordinary length-generating functions are
\[
\begin{aligned}
\sum_{L\geq0}z^L\sum_n X(n)
 &=\frac{z}{(1-2z)^2},\\
\sum_{L\geq0}z^L\sum_n Y(n)
 &=\frac{z^2(z-2)}{(z-1)(z+1)(1-2z)^2},\\
\sum_{L\geq0}z^L\sum_n X(n)Y(n)
 &=\frac{z^2(2z^4-2z^3-2z^2+7z-4)}{(z-1)^2(z+1)^2(2z-1)^3}.
\end{aligned}
\]
The last two rational functions have the explicit partial-fraction forms
\[
\begin{aligned}
\sum_{L\geq0}z^L\sum_nY(n)
={}&\frac{z}{(1-2z)^2}-\frac{2}{3(1-2z)}+\frac{1}{2(1-z)}+\frac{1}{6(1+z)},\\
\sum_{L\geq0}z^L\sum_nX(n)Y(n)
={}&\frac{z(1+2z)}{2(1-2z)^3}+\frac{z}{6(1-2z)^2}-\frac{4}{9(1-2z)}\\
&+\frac{1}{4(1-z)^2}+\frac{7}{36(1+z)}-\frac{z}{12(1+z)^2}.
\end{aligned}
\]
All inner sums run over \(0\leq n<2^L\). Their coefficient expansions use only \([z^L](1-az)^{-1}=a^L\), \([z^L](1-az)^{-2}=(L+1)a^L\), and \([z^L](1-az)^{-3}=\binom{L+2}{2}a^L\), with \(a\in\{2,1,-1\}\). Partial fractions yield the explicit means above, after division by \(2^L\). Subtracting \(\mathbb E[X]\mathbb E[Y]\) from \(\mathbb E[XY]\) produces exactly the covariance formula. Every step is a formal rational-function identity, valid simultaneously for all \(L\).

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3.8 or later; no external packages are needed. The program performs independent integer-polynomial determinant computations for the numerator and denominator, formally checks the three derivative rational identities by polynomial cross multiplication, enumerates all \(2^L\) inputs for \(0\leq L\leq9\), checks valuations against direct binomial coefficients when \(L\leq8\), and checks the exact moment formulas using rational arithmetic. Successful execution prints a single line beginning with \(\texttt{VERIFY\_OK}\). Finite checks are supporting evidence: the transfer-matrix proof establishes the identities for all lengths.

## Relationship to prior work

Kummer's classical carry theorem supplies the valuation model. Barat and Grabner (2001) develop matrix and block-digit methods for binomial valuations over Pascal's triangle; their results explain the general method but do not state this specific joint enumerator or covariance. Spiegelhofer and Wallner (2016) give explicit generating functions for counts of entries with a fixed valuation within a row of Pascal's triangle, a different family of distributions. Wan and Zudilin's 2011 Table 1 records the product \(\binom{2n}{n}\binom{3n}{n}\) as Zagier's hypergeometric Apéry-like example \(\mathrm{(B)}\), explaining why the joint valuation of these two factors is natural; their generating functions concern Legendre polynomial weights, not simultaneous \(2\)-adic valuations. On specializing \(u=1\), the present bivariate enumerator recovers the previously recorded univariate dyadic enumerator for \(\nu_2(\binom{3n}{n})\); the additional variable \(u\) and mixed covariance are the new assertions. Broad transfer-matrix tools could independently be specialized to derive this result; such methodological antecedents are acknowledged rather than described as absent.

## Limitations

The theorem concerns only the prime \(2\), the two specified binomial factors, and complete dyadic intervals of indices; it gives no claims about odd primes, arbitrary interval endpoints, or new divisibility congruences for the product itself. The reported originality is relative to inspected primary publications, mathematical-record searches, and accessible earlier statements; an unlocated equivalent specialization or stronger joint distribution theorem remains possible. The mathematical proof and symbolic checks are supplied, but independent verification and priority assessment have not been performed.

## References

1. E. E. Kummer (1852), *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, Journal für die reine und angewandte Mathematik **44**, 93–146 (carry theorem).
2. G. Barat and P. J. Grabner (2001), *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society **64**, 523–547. DOI: 10.1112/S0024610701002630. Author manuscript: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf.
3. J. Wan and W. Zudilin (2011), *Generating functions of Legendre polynomials: a tribute to Fred Brafman*, Max Planck Institute for Mathematics preprint 2011/37. https://archive.mpim-bonn.mpg.de/973/1/preprint_2011_37.pdf.
4. L. Spiegelhofer and M. Wallner (2016), *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089. https://arxiv.org/abs/1604.07089.
