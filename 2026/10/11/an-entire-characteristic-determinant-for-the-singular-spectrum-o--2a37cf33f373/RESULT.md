# An entire characteristic determinant for the singular spectrum of the Hardy–Volterra commutator

## Finding
Let \(H=L^2((0,1);\mathbb R)\), and let \(J\), \(C\), and \(M\) respectively denote the integration operator, the Hardy–Cesàro averaging operator, and multiplication by the independent variable:
\[
(Jf)(x)=\int_0^x f(t)\,dt,\qquad
(Cf)(x)=\frac1x\int_0^x f(t)\,dt,\qquad
(Mf)(x)=xf(x).
\]
Consider the compact commutator \(T=MC-CM=CJ\), explicitly
\[
(Tf)(x)=\frac1x\int_0^x(x-t)f(t)\,dt.
\]
For each \(a\in\{2,3\}\), define the entire-in-\(z\) solution
\[
U_a(x,z)=\sum_{k=0}^{\infty}\frac{z^k x^{a+2k}}{D_{a,k}},\qquad
D_{a,0}=1,\qquad
D_{a,k}=\prod_{j=1}^k(a+2j)(a+2j-1)(a+2j-2)(a+2j-3).
\]
Set
\[
F(z)=U_2''(1,z)U_3'''(1,z)-U_3''(1,z)U_2'''(1,z).
\]
**Exact spectral characteristic theorem.** The zeros of \(F\) are all positive and real. A positive number \(s\) is a nonzero singular value of \(T\) if and only if \(F(s^{-2})=0\). At a root \(z\), the dimension of the corresponding singular eigenspace equals the nullity of the explicit matrix
\[
\begin{pmatrix}U_2''(1,z)&U_3''(1,z)\\U_2'''(1,z)&U_3'''(1,z)\end{pmatrix}.
\]
There are infinitely many such roots, with no finite accumulation point. The normalized entire characteristic function begins
\[
F(z)/12=1-z/6+z^2/480-z^3/181440+\cdots.
\]
Thus a convergent series and a two-by-two determinant, rather than spatial discretization, specify the entire singular spectrum.

## Assumptions and scope
All operators act on the real Hilbert space \(L^2(0,1)\), with Lebesgue measure and the unweighted Hilbert norm. Derivatives at \(x=1\) are ordinary derivatives of the displayed entire-in-\(x\) series. \(F\) is a scalar entire function of the complex parameter \(z\); the spectral assertion concerns its complete complex zero set, not merely real approximations. Singular-value multiplicity means multiplicity of the positive self-adjoint compact operator \(T^*T\), i.e. eigenspace dimension; it is not claimed without proof that the order of an analytic zero equals this dimension. Numerical roots quoted below are approximate only.

## Proof
**1. Compactness and injectivity.** The kernel of \(T\) is \(\mathbf 1_{0<t<x}(1-t/x)\). It is square integrable and
\[
\|T\|_{\mathrm{HS}}^2=\int_0^1\int_0^x(1-t/x)^2\,dt\,dx=1/6.
\]
Hence \(T\) is compact. If \(Tf=0\), then \(J^2f=xTf=0\), whence \(f=0\) almost everywhere. The range is infinite dimensional, so \(T^*T\) has infinitely many strictly positive eigenvalues tending to zero.

**2. The singular eigenproblem.** Write \(u=J^2f=\int_0^x(x-t)f(t)\,dt\) for any nonzero \(f\) obeying \(T^*Tf=\sigma^2 f\). Then \(u''=f\), \(u(0)=u'(0)=0\), and \(Tf=u/x\). The adjoint is
\[
(T^*g)(t)=\int_t^1(1-t/x)g(x)\,dx.
\]
Thus \(h=T^*Tf\) satisfies \(h(1)=h'(1)=0\) and \(h''(x)=u(x)/x^2\) for positive \(x\). From \(h=\sigma^2u''\) we obtain, with \(\lambda=\sigma^{-2}\),
\[
u^{(4)}(x)=\lambda\frac{u(x)}{x^2},\qquad
u(0)=u'(0)=u''(1)=u'''(1)=0.\tag{1}
\]
The endpoint at zero is singular, so admissible solutions of (1) must additionally obey \(u''\in L^2(0,1)\); that condition will be automatic for the series solutions.

**3. Rigorous regularity at the singular endpoint.** Cauchy–Schwarz gives
\[
|u(x)|\le\bigl(\int_0^x(x-t)^2dt\bigr)^{1/2}\|f\|_2
\le x^{3/2}\|f\|_2/\sqrt3.
\]
Consequently \(u(x)/x^2=O(x^{-1/2})\in L^1(0,1)\). Because \(h''=u/x^2\) and \(h=\sigma^2 f\), the eigenfunction \(f\) has absolutely continuous first derivative and finite endpoint values \(f(0),f'(0)\). Thus \(u''(0)\) and \(u'''(0)\) exist. Four integrations of (1) give the Volterra equation
\[
u(x)=a x^2+b x^3+\frac{\lambda}{6}\int_0^x(x-t)^3\frac{u(t)}{t^2}\,dt,
\quad a=u''(0)/2,\quad b=u'''(0)/6.\tag{2}
\]
On the weighted space with norm \(\sup_{0<x\le\delta}|u(x)|/x^2\), the integral term in (2) has operator norm at most \(|\lambda|\delta^2/24\). Local contraction followed by ordinary Volterra continuation proves uniqueness for each pair \((a,b)\). The series for \(U_2\), \(U_3\) solve (2), as the displayed denominator satisfies
\[
D_{a,k}/D_{a,k-1}=(a+2k)(a+2k-1)(a+2k-2)(a+2k-3).
\]
The factors grow quartically, so the series and all derivatives converge locally uniformly in \((x,z)\). Each admissible solution is therefore \(aU_2+bU_3\), and both basis solutions have square-integrable second derivative on the closed interval.

**4. Characteristic equivalence, including the converse.** The right endpoint conditions in (1) are precisely
\[
\begin{pmatrix}U_2''(1,\lambda)&U_3''(1,\lambda)\\U_2'''(1,\lambda)&U_3'''(1,\lambda)\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=0.
\]
A nontrivial admissible solution exists exactly when \(F(\lambda)=0\). Conversely, let \(F(\lambda)=0\) and choose a nonzero coefficient pair in that kernel. Put \(f=u''\), and note \(u=J^2f\). For \(h=T^*Tf\), the functions \(h\) and \(\lambda^{-1}u''\) have identical second derivatives and both vanish together with their first derivatives at \(x=1\); hence \(T^*Tf=\lambda^{-1}f\). The case \(\lambda=0\) is excluded because \(F(0)=12\). The self-adjoint positivity of \(T^*T\) therefore forces every root \(\lambda\) to be positive real. Conversely every positive eigenvalue gives a root. Injectivity of \(u\mapsto u''\) on the zero-left-boundary subspace proves the eigenspace-nullity statement. Compactness supplies the infinitude and discreteness.

**5. Coefficients and an independent trace check.** Recurrence expansion gives \(F(z)=12-2z+z^2/40-z^3/15120+\cdots\). Independently, the kernel of \(TT^*\) is
\[
K(x,y)=\frac{\min(x,y)}2-\frac{\min(x,y)^2}{6\max(x,y)},\quad x,y>0.
\]
Its diagonal integral equals \(1/6\), and direct integration of its squared kernel gives \(17/720\), supplying exact trace checks for the normalization and the first two determinant coefficients. No Fredholm-determinant identity is assumed in proving the characteristic theorem.

## Verification
The standalone `verify.py` computes the first four coefficients of \(F\) with exact rational arithmetic, verifies the two trace identities, calculates four zeros of \(F\) at elevated precision, and compares their inverse square roots with a Nyström discretization of the **independently derived** symmetric kernel of \(TT^*\). The first four approximations are
\[
0.3915493382518084,\quad0.1005754215648547,\quad
0.0448912903665687,\quad0.0252869731426519.
\]
Run `python verify.py` with the dependencies listed in `requirements.txt`. The analytic argument above, not finite computation, establishes the infinite-dimensional characterization.

## Relationship to prior work
Chuong–Hung (arXiv:1208.5242v1, 26 August 2012) develops weighted Hardy–Cesàro operators and commutators; its general commutator (1.5) specializes to the present operator, but its focus is weighted boundedness rather than this spectrum. Hofmann–von Wolfersdorf (2009) studies singular-value behavior of **outer-weighted first integration** and exact Bessel problems, rather than the present \(x^{-1}J^2\) map. Ramlau–Koutschan–Hofmann (arXiv:1811.11642v1) derives characteristic equations for **unweighted** \(J^n\), whose fourth-order coefficient is constant at \(n=2\). Deng–Fischer–Hofmann (arXiv:2401.11411v1) studies exactly \(T=CJ\), proves \(\sigma_n(T)\asymp n^{-2}\), and explicitly notes the difficulty of solving its eigenproblem; that manuscript does not display this entire characteristic determinant or exact root characterization. Distinguishing an exact transcendental equation from elementary closed-form roots is essential.

## Limitations
The theorem gives an implicit exact description, not elementary formulas for individual singular values, not certified enclosing intervals for the numerical approximations, and not a proved sharp asymptotic constant or a simplicity theorem for all zeros. It does not claim that \(F/12\) is a Fredholm determinant, nor that the order of every zero equals its eigenspace dimension. Historical equivalence through general weighted fourth-order spectral theorems remains a bibliographic risk; independent external review has not been performed.

## References
1. B. Hofmann and L. von Wolfersdorf, *A new result on the singular value asymptotics of integration operators with weights*, Journal of Integral Equations and Applications 21 (2009), 281–295, DOI: 10.1216/JIE-2009-21-2-281. Earliest verified publication: 2009-07-17.
2. N. M. Chuong and H. D. Hung, *A generalized weighted Hardy–Cesàro operator, and its commutator on weighted \(L^p\) and BMO spaces*, arXiv:1208.5242v1 (2012-08-26).
3. R. Ramlau, C. Koutschan, and B. Hofmann, *On the singular value decomposition of n-fold integration operators*, arXiv:1811.11642v1 (2018-11-28).
4. Y. Deng, H.-J. Fischer, and B. Hofmann, *The degree of ill-posedness for some composition governed by the Cesàro operator*, arXiv:2401.11411v1 (2024-01-21).
