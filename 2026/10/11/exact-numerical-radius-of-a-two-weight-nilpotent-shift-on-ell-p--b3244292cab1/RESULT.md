# Exact numerical radius of a two-weight nilpotent shift on \(\ell_p^3\)

## Finding
Let \(1<p<\infty\) and \(a,b>0\). On either the real or complex three-dimensional sequence space \(\ell_p^3\), consider the nilpotent weighted shift
\[
T_{a,b}(z_1,z_2,z_3)=(a z_2,b z_3,0).
\]
Set \(r=b/a\), and let \(u>0\) be the **unique positive solution** of
\[
u^{p-1}+(p-1)^{(p-2)/(p-1)}r^{p/(p-1)}u=p-1. \tag{1}
\]
Then the **exact spatial numerical radius** is
\[
\boxed{v_p(T_{a,b})=\frac{p-1}{p}\,a\,u^{-(p-1)/p}.} \tag{2}
\]
Define
\[
A=u^{(p-1)/p},\qquad
C=\left(\frac{bA}{(p-1)a}\right)^{1/(p-1)},\qquad
D=(A^p+1+C^p)^{1/p}. \tag{3}
\]
The magnitudes of every maximizing unit vector are uniquely determined: they are \((A,1,C)/D\). Over the complex scalars, **all** maximizing vectors are
\[
\frac{e^{i\alpha}}D\bigl(A,e^{i\theta},Ce^{2i\theta}\bigr),
\qquad \alpha,\theta\in\mathbb R, \tag{4}
\]
with phases read modulo \(2\pi\). Over the real scalars, (4) holds with \(e^{i\alpha},e^{i\theta}\in\{+1,-1\}\). In particular the same radius holds for both scalar fields.

For \(p=2\), (2) becomes the Hilbert-space value \(\sqrt{a^2+b^2}/2\). For the unit two-weight shift at \(p=4\), equation (1) gives
\[
v_4(T_{1,1})=0.759077552014653123713117078359\ldots,
\]
strictly greater than its Hilbert value \(1/\sqrt 2\). As \(b\downarrow0\), the value tends to the known rank-one constant \(a(p-1)^{(p-1)/p}/p\).

## Assumptions and scope
The exponent lies strictly between \(1\) and \(\infty\), the two weights are strictly positive real numbers, and the scalar field is either \(\mathbb R\) or \(\mathbb C\). For a bounded operator \(T\) on a Banach space \(X\), the spatial numerical radius is
\[
v(T)=\sup\{|x^*(Tx)|:x\in X,\ \|x\|=1,\ x^*\in X^*,\ \|x^*\|=1,\ x^*(x)=1\}.
\]
For \(X=\ell_p^3\), the norming functional is unique and has coordinates \(\overline{x_j}|x_j|^{p-2}\), interpreted as \(0\) when \(x_j=0\). It gives the exact variational expression
\[
v_p(T_{a,b})=\max_{\sum_{j=1}^3|x_j|^p=1}
\left|a\overline{x_1}|x_1|^{p-2}x_2+b\overline{x_2}|x_2|^{p-2}x_3\right|. \tag{5}
\]
The three-dimensional shift has two interacting links, unlike the rank-one shift in two coordinates.

## Proof
**Reduction to positive magnitudes.** Write \(A=|x_1|\), \(B=|x_2|\), \(C=|x_3|\). The triangle inequality applied to (5) yields
\[
\left|a\overline{x_1}|x_1|^{p-2}x_2+b\overline{x_2}|x_2|^{p-2}x_3\right|
\le aA^{p-1}B+bB^{p-1}C.
\]
Equality is achieved by taking nonnegative real coordinates. By homogeneity, the desired maximum therefore equals
\[
\max_{A,B,C\ge0,\ (A,B,C)\ne(0,0,0)}
\frac{aA^{p-1}B+bB^{p-1}C}{A^p+B^p+C^p}. \tag{6}
\]
This quotient is continuous on the compact positive part of the \(\ell_p^3\) sphere and is strictly positive somewhere, so its maximum exists and is positive.

**No boundary maximizer.** If \(B=0\), the numerator of (6) is zero. If \(A=0\) and \(B>0\), replacing \(A\) by \(\varepsilon>0\) increases the numerator by \(a\varepsilon^{p-1}B\), while the denominator increases only by \(\varepsilon^p\). The resulting quotient strictly increases for all sufficiently small \(\varepsilon\). Likewise, if \(C=0\) and \(B>0\), replacing \(C\) by \(\varepsilon\) increases the numerator by \(bB^{p-1}\varepsilon\), while the denominator increases by \(\varepsilon^p\); this too is an improvement. Thus every maximum has \(A,B,C>0\), for every \(p>1\).

**Stationary equations.** Use scale invariance to set \(B=1\), and let \(\lambda>0\) be the maximizing quotient. Maximizing the homogeneous degree-\(p\) numerator subject to \(A^p+B^p+C^p=1\) gives the Lagrange equations; Euler's identity ensures the multiplier equals the quotient \(\lambda\). The derivatives in the first, third, and second coordinates, respectively, yield
\[
\lambda=\frac{(p-1)a}{pA},\qquad
C^{p-1}=\frac{bA}{(p-1)a},\qquad
 aA^p+(p-1)bAC=(p-1)a. \tag{7}
\]
In the last equality we have substituted the first formula into the middle-coordinate stationarity equation and multiplied by \(A\).

Substitute the second identity of (7) into the last one, divide by \(a\), and put \(u=A^{p/(p-1)}\). Since \(A^p=u^{p-1}\) and \(AC=u\bigl(b/((p-1)a)\bigr)^{1/(p-1)}\), we obtain exactly equation (1). Its left-hand side is continuous, strictly increasing from \(0\) to \(\infty\) on \(u>0\), so (1) has a unique positive solution. Hence (7) has one positive magnitude triple, up to common scaling. Since a positive interior maximum must exist, this unique stationary triple is necessarily that global maximum. The first identity in (7) now proves (2), and normalization proves (3).

**Phases and completeness.** Because all three maximizing magnitudes are positive and both weights are positive, equality in the complex triangle inequality is equivalent to the two adjacent phase increments being equal: \(\arg(x_2)-\arg(x_1)\equiv\arg(x_3)-\arg(x_2)\pmod{2\pi}\). This gives (4) and exhausts the complex maximizers. The real sign patterns are the corresponding restrictions. There are no other magnitude patterns, by the uniqueness of the positive stationary point. The proof is complete.

## Verification
The enclosed standalone `CHECK.py` evaluates the unique root by monotone log-domain bisection and compares its predicted radius against 60,000 direct samples of the original three-coordinate quotient. It also checks the Hilbert formula for three pairs of weights and the \(p\)-versus-Hölder-dual numerical-radius identity for 15 exponent/weight cases. All checks completed. These are finite diagnostics; global optimality and uniqueness are established by the boundary and stationarity argument above, not by sampling.

Direct high-precision evaluation of equation (1) yields \(v_4(T_{1,1})=0.759077552014653123713117078359\ldots\), \(v_3(T_{2,1})=1.18991135047126493822554748338\ldots\), and \(v_2(T_{1,1})=1/\sqrt2\).

## Relationship to prior work
Martín, Merí, and Popov (2010 preprint, subsequently *Journal of Functional Analysis*) define numerical radius on \(L_p\) spaces, identify the two-coordinate **rank-one** shift radius \(\kappa_p=(p-1)^{(p-1)/p}/p\), and derive general lower bounds for positive operators. Their relevant definitions and rank-one calculation are in the openly available preprint, page 2; its theorems do not supply the present two-link, three-coordinate weighted radius or its maximizer classification.

Undrakh, Nakazato, Vandanjav, and Chien (*Electronic Journal of Linear Algebra*, 2015) analyze weighted shifts on a **Hilbert** \(\ell_2\) space using the Hermitian-part spectrum and a tridiagonal recurrence. Their finite-dimensional formulas recover the \(p=2\) case, but those spectral arguments do not imply the general non-Hilbert \(1<p<\infty\) statement. Earlier weighted-shift numerical-radius work by Chang and Wang (2012) likewise explicitly assumes a complex Hilbert space. Related papers on numerical ranges in weighted Hardy spaces and semi-inner-product spaces address different operator families and general properties rather than equation (1).

The exact root and classification above apply to an arbitrary pair of positive link weights and to both scalar fields, thereby exhibiting a genuinely interacting finite-shift calculation beyond the established rank-one and Hilbert formulas within the literature examined.

## Limitations
The theorem concerns only this positive two-link nilpotent shift in dimension three; it is not a closed formula for arbitrary \(3\times3\) operators, general finite path lengths, or the numerical index of \(\ell_p^3\). The endpoint exponents \(p=1\) and \(p=\infty\) are excluded. The root equation is implicit for general real \(p\), though it is unambiguous and numerically stable via monotonicity. An incomplete or unindexed historical literature record could contain an equivalent formulation; the available comparisons do not constitute a proof of universal bibliographic novelty. The full text of the 2012 Hilbert shift-permutation article was not inspected, although its accessible abstract explicitly fixes a Hilbert-space setting.

## References
1. M. Martín, J. Merí, M. Popov, “On the numerical radius of operators in Lebesgue spaces,” arXiv:1011.4785, publicly posted 22 November 2010; *Journal of Functional Analysis* 261 (2011), 149–168, DOI 10.1016/j.jfa.2011.03.007. Open preprint: https://www.ugr.es/~mmartins/Curriculum/Papers/pre-MarMerPop(2).pdf.
2. B. Undrakh, H. Nakazato, A. Vandanjav, M.-T. Chien, “The numerical radius of a weighted shift operator,” *Electronic Journal of Linear Algebra* 30 (2015), 944–963, DOI 10.13001/1081-3810.2821. Open PDF: https://journals.uwyo.edu/index.php/ela/article/download/1617/1617.
3. C.-T. Chang, K.-Z. Wang, “Maximizing numerical radii of weighted shifts under weight permutations,” *Journal of Mathematical Analysis and Applications* 394 (2012), 592–602, DOI 10.1016/j.jmaa.2012.04.039.
4. A. Abdollahi, M. T. Heydari, “Spatial Numerical Range of Operators on Weighted Hardy Spaces,” *International Journal of Mathematics and Mathematical Sciences* (2011), article 812680, DOI 10.1155/2011/812680.
5. D. R. Sahu, J. Nahak, S. Nanda, “Numerical Range of Two Operators in Semi-Inner Product Spaces,” *Abstract and Applied Analysis* (2012), article 846396, DOI 10.1155/2012/846396.
