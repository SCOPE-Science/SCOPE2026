# Sharp quadratic stability for four equicorrelated Gaussian fourth moments

## Finding
Let \((X_1,X_2,X_3,X_4)\) be a centered Gaussian vector with \(\mathbb E X_i^2=1\) and \(\mathbb E X_iX_j=\rho\) for distinct indices, where necessarily \(-1/3\le\rho\le1\). Set
\[
\Delta(\rho)=\mathbb E\!\left[\prod_{i=1}^{4}X_i^4\right]-\prod_{i=1}^{4}\mathbb E X_i^4.
\]
Define
\[
q(t)=284t^6-512t^5+440t^4-224t^3+85t^2-16t+3.
\]
The polynomial \(q\) has precisely one stationary point \(\tau\) in \([0,1/3]\), which is its strict minimum, with \(0.1655387<\tau<0.1655388\). The **sharp quadratic stability coefficient** for all admissible equicorrelations is
\[
C_* =1296q(\tau)=2510.51265\ldots,
\qquad\Delta(\rho)\ge C_*\rho^2.
\]
For \(\rho\ne0\), equality holds if and only if \(\rho=-\tau\); at \(\rho=0\), both sides vanish. Thus the weakest nontrivial normalized moment separation occurs at an *interior, negatively correlated* point rather than at the singular boundary \(\rho=-1/3\).

## Assumptions and scope
The Gaussian vector may have a singular covariance matrix. An equicorrelation matrix of order four has eigenvalues \(1-\rho\) (multiplicity three) and \(1+3\rho\) (multiplicity one), giving exactly the stated parameter interval. The result concerns fourth powers in four coordinates, with a coefficient sharp across this entire one-parameter family; it does not claim a universal quadratic coefficient over all covariance matrices or exponents. The negative range includes all unit-variance normalizations of uniform multinomial covariance matrices with four equal cell probabilities and an unobserved remainder cell.

## Proof
For nonnegative integers \(a_1,\ldots,a_4\) having even total, write \(M(a_1,\ldots,a_4)=\mathbb E\prod_i X_i^{a_i}\). The Gaussian integration-by-parts/Wick pairing recurrence, choosing any index \(i\) with \(a_i>0\), is
\[
M(a)=\sum_{j:a_j-\mathbf1_{j=i}>0}(a_j-\mathbf1_{j=i})R_{ij}\,M(a-e_i-e_j),
\quad R_{ii}=1,\quad R_{ij}=\rho\ (i\ne j),
\]
with \(M(0)=1\). This recurrence, applied exactly to \(a=(4,4,4,4)\), yields the explicit finite identity
\[
\Delta(\rho)=1296\rho^2\bigl(3+16\rho+85\rho^2+224\rho^3+440\rho^4+512\rho^5+284\rho^6\bigr).
\]
For \(\rho\ge0\), all coefficients after the leading constant are nonnegative; hence \(\Delta(\rho)/\rho^2\ge3888\) for \(\rho>0\). For negative \(\rho=-t\), \(0<t\le1/3\), the quotient equals \(1296q(t)\).

We prove \(q\) is strictly convex on \([0,1/3]\) without relying on root plots. Put \(u=3t\in[0,1]\). In the degree-four Bernstein basis \(\binom4k u^k(1-u)^{4-k}\), the coefficients of \(q''(u/3)\), indexed \(k=0,1,2,3,4\), are exactly
\[
170,\quad58,\quad394/9,\quad878/27,\quad934/27.
\]
All are strictly positive. Also \(q'(0)=-16<0\) and \(q'(1/3)=178/27>0\). By strict convexity, there is a unique zero \(\tau\) of \(q'\) in the open interval, which minimizes \(q\). Exact rational evaluation of \(q'\) at \(1655387/10^7\) and \(1655388/10^7\) gives opposite signs, proving the numerical enclosure. Because \(q(\tau)<q(0)=3\), the minimum on the negative interval is smaller than that on the nonnegative interval. The equality claims follow from strict convexity, strict inequality for positive \(\rho\), and the factor \(\rho^2\). The formula remains valid at singular covariance endpoints by Gaussian moment continuity.

## Verification
The standalone `verify.py` implements the Gaussian pairing recurrence over exact rational polynomial coefficients, checks the nine coefficients of the joint fourth moment independently against the stated identity, checks the full Bernstein coefficient vector using exact binomial transforms, the endpoint derivatives, rational isolating interval, and both endpoint identities. Run with `python3 verify.py` using only the Python standard library. All its assertions passed during preparation. These finite symbolic operations verify the exact polynomial identity and convexity certificate; the proof above supplies the universal parameter quantifiers.

## Relationship to prior work
Ouimet's *The Gaussian product inequality conjecture for multinomial covariances* (arXiv:2209.01505, first publicly posted 2022-09-03) studies the difficult negative-dependence multinomial covariance class through a finite combinatorial reformulation, without providing the present sharp fourth-moment quadratic coefficient. The later qualitative Gaussian product inequality is known for all equicorrelated vectors from Hirose (2026), and the stronger inequality for arbitrary centered Gaussian vectors and positive exponents is established by Ouimet and Greaves (2026). Those inequalities yield the sign \(\Delta\ge0\), but that sign alone does not determine the optimal positive coefficient or the interior worst-case correlation calculated here. Quantitative bivariate inequalities of Hu, Zhao and Zhou (2023) use only two Gaussian coordinates. No claim is made to solve the now-settled qualitative inequality.

## Limitations
The sharpness refers solely to the equicorrelated four-dimensional fourth-power setting. It does not transfer automatically to arbitrary correlation matrices, dimensions or mixed powers. The normal-form coefficient is obtained by an elementary but substantial finite Gaussian moment computation and not by a new general Gaussian inequality. Earlier publications may contain the same polynomial under another normalization; this remains a bibliographic priority risk. Independent expert validation has not been performed.

## References
- F. Ouimet, *The Gaussian product inequality conjecture for multinomial covariances*, arXiv:2209.01505 (2022, revised 2023), https://arxiv.org/abs/2209.01505 .
- K. Hirose, *The Gaussian product inequality for equicorrelated variables*, Journal of Mathematical Analysis and Applications 563 (2026), 130776, DOI:10.1016/j.jmaa.2026.130776 .
- F. Ouimet and D. Greaves, *A proof of the strong Gaussian product inequality conjecture*, arXiv:2609.20234 (2026), https://arxiv.org/abs/2609.20234 .
- Z.-C. Hu, H. Zhao and Q.-Q. Zhou, *Quantitative versions of the two-dimensional Gaussian product inequalities*, Journal of Inequalities and Applications 2023:2, DOI:10.1186/s13660-022-02906-w .
