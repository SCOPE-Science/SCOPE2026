# Sharp one-sided weak-null norm profiles and extremizer rigidity in real \(L^4\)

## Finding
Let \((\Omega,\Sigma,\mu)\) be an atomless probability space and let \(X=L^4(\mu;\mathbb R)\). For \(x\in S_X\) and \(t>0\), set
\[
\Phi_x(t)=\sup\Big\{\limsup_{n\to\infty}\|x+t y_n\|_4:\ y_n\in S_X,\ y_n\rightharpoonup0\Big\}.
\]
There is a unique \(d=d(t)>0\) solving
\[
3d^2(d+1)(d+3)=4t^4.
\]
Set \(q=d(d+3)/2\). Then for every \(x\in S_X\),
\[
\boxed{\Phi_x(t)^4=F(t)^4=1+t^4+\frac{2}{d}(q^2+t^4).}
\]
Put \(a=(d+\sqrt{d^2+4q})/2\) and \(b=(\sqrt{d^2+4q}-d)/2\). Any weakly null sequence \(y_n\in S_X\) for which \(\|x+t y_n\|_4\to F(t)\) has measurable sets \(A_n\) such that
\[
\big\|t y_n-x(a\mathbf1_{A_n}-b\mathbf1_{A_n^c})\big\|_4\to0,
\qquad \int_{A_n}|x|^4\,d\mu\to\frac{b}{a+b}.
\]
For a maximizing limsup, this conclusion holds on a subsequence along which the norms converge to \(F(t)\). Sharp sequences attaining \(F(t)\) at **every** index exist for every unit \(x\).

## Assumptions and scope
All scalar functions are real, \(\mu\) is nonatomic and finite with total mass one, and weak convergence means \(\sigma(L^4,L^{4/3})\). The normalization of each perturbation is exactly \(\|y_n\|_4=1\). The supremum takes place over sequences, not nets. The result is a *one-sided supremum*, not the two-sided minimum or the modulus of weak almost squareness. No assertion is made here for atomic measures, complex functions, or exponents other than four. At \(t=0\), the continuous extension is \(F(0)=1\).

## Proof
**1. Algebraic envelope.** The function \(d\mapsto3d^2(d+1)(d+3)\) is continuous and strictly increasing from zero to infinity on positive arguments, proving the existence and uniqueness of \(d\). The defining equation and \(q=d(d+3)/2\) imply \(t^4=q(d^2+q)\). The numbers \(a,b\) are positive and satisfy \(a-b=d\), \(ab=q\). Expanding yields the exact scalar identity, valid for every real \(s,u\),
\[
\begin{aligned}
&\left(1+\frac{2q^2}{d}\right)s^4+(4+4q)s^3u
 +\left(1+\frac2d\right)u^4-(s+u)^4\\
&\qquad=\frac2d\,(u-as)^2(u+bs)^2\ge0.
\end{aligned}
\]
(The \(s^2u^2\) coefficient vanishes because \(q=d(d+3)/2\), and the \(su^3\) coefficient vanishes because \(a-b=d\).) Take \(s=x(\omega)\) and \(u=t y_n(\omega)\), integrate, and use \(\|x\|_4=\|y_n\|_4=1\). Since \(x^3\in L^{4/3}\), weak nullity gives \(\int x^3y_n\,d\mu\to0\). Therefore
\[
\limsup_n\|x+t y_n\|_4^4
\le 1+\frac{2q^2}{d}+\left(1+\frac2d\right)t^4
=F(t)^4.
\]

**2. Exact weakly null attainment.** The probability measure \(d\nu=|x|^4\,d\mu\) is atomless. Construct independent identically distributed random variables \(Z_n\) on \((\Omega,\Sigma,\nu)\) with
\[
\nu(Z_n=a)=\frac b{a+b},\qquad \nu(Z_n=-b)=\frac a{a+b}.
\]
Such a sequence exists on every atomless probability space by recursive subdivisions of measurable sets. We have \(\mathbb E_\nu Z_n=0\), and
\[
\mathbb E_\nu |Z_n|^4=ab(a^2-ab+b^2)=q(d^2+q)=t^4.
\]
Set \(y_n=xZ_n/t\), taking zero where \(x=0\). Then \(\|y_n\|_4=1\). The centered bounded independent variables \(Z_n\) are mutually orthogonal in \(L^2(\nu)\) and consequently converge weakly to zero there. Since they have a uniform essential bound, approximating arbitrary \(L^1(\nu)\) functions by \(L^2(\nu)\) functions proves \(\int h Z_n\,d\nu\to0\) for every \(h\in L^1(\nu)\). For arbitrary \(g\in L^{4/3}(\mu)\), \(gx\in L^1(\mu)\), so \(h=gx/|x|^4\) (zero on \(\{x=0\}\)) belongs to \(L^1(\nu)\), yielding
\[
\int g y_n\,d\mu=\frac1t\int hZ_n\,d\nu\to0.
\]
Hence \(y_n\rightharpoonup0\). Pointwise \(u=t y_n= xZ_n\) takes exactly the equality values \(ax\) and \(-bx\); the algebraic identity integrates with a zero remainder for every \(n\). Also \(\mathbb E_\nu(1+Z_n)^4=F(t)^4\). Thus \(\|x+t y_n\|_4=F(t)\) for every \(n\).

**3. Rigidity.** Suppose \(y_n\rightharpoonup0\), \(\|y_n\|_4=1\), and \(\|x+t y_n\|_4\to F(t)\). Integrating the identity and using the vanishing linear term forces
\[
\int (t y_n-a x)^2(t y_n+b x)^2\,d\mu\to0.
\]
Choose \(A_n\) pointwise where \(|t y_n-a x|\le|t y_n+b x|\), and choose the other level on its complement. Since \(\min\{|u-as|,|u+bs|\}^4\le(u-as)^2(u+bs)^2\), the stated \(L^4\) approximation follows. Pair the approximation with \(x^3\in L^{4/3}\). Weak nullity implies
\[
0=\lim_n\int x^3(t y_n)\,d\mu
=\lim_n\left((a+b)\int_{A_n}|x|^4\,d\mu-b\right),
\]
which gives the unique asymptotic weighted mass. For sequences maximizing only a limsup, take a subsequence along which the norm tends to the sharp upper bound and apply the same argument.

## Verification
The scalar polynomial identity can be checked by expanding both sides and comparing the five coefficients in \(s^{4-j}u^j\), \(j=0,\ldots,4\). The crucial cancellations use \(a-b=d\), \(ab=q\), and \(2q=d(d+3)\). The probabilistic construction is exact and does not rely on a finite enumeration. For \(t=1\), direct numerical solution gives \(d\approx0.5031886736133\), \(q\approx0.8813824310463\), and \(F(1)\approx1.735040526220\). A symmetric Rademacher multiplier instead gives \(8^{1/4}\approx1.681792830507\): the skew two-level law is genuinely necessary for maximizing the one-sided norm.

## Relationship to prior work
Rodríguez and Rueda Zoca (2023, arXiv:2301.07943, especially Section 2) use Rademacher-type weakly null multipliers to prove weak almost squareness for nonatomic \(L^1\) and Bochner variants. This motivates the weak-null construction, but their result concerns the **simultaneous smallness** of plus and minus norms at exponent one, rather than the maximal one-sided quartic growth studied here. Related work on weak-null *symmetric minimum* perturbation radii in real \(L_p\) for \(p\ge2\) gives the smaller \((1+t^p)^{1/p}\); its optimization direction and quantifiers are different. Pearson-type skewness–kurtosis inequalities are antecedents to optimizing moments of a two-point law, but a moment inequality alone neither provides a weakly null maximizing sequence for every basepoint nor classifies near-maximizers in \(L^4\).

## Limitations
The proof is restricted to real atomless \(L^4\). A one-sided result does not imply any two-sided weak almost squareness property. Uniqueness of the asymptotic *two levels* means uniqueness in \(L^4\) proximity, not convergence of the level sets themselves. The comparison with related unpublished or inaccessible full texts is not exhaustive; independent originality assessment has not been performed.

## References
1. J. Rodríguez and A. Rueda Zoca, *On weakly almost square Banach spaces*, arXiv:2301.07943 (first public version 2023-01-19), Section 2. https://arxiv.org/abs/2301.07943
2. *Sharp weak-null symmetric perturbation profiles in real \(L_p\) spaces*, published-finding corpus record 2026/10/11/SCOPE-sharp-weak-null-symmetric-perturbation-profiles-in-real-l-p-spac--1c76df9d726f. Available summary distinguishes a symmetric minimization from the one-sided supremum here.
3. Classical Pearson skewness–kurtosis inequality, a related moment-optimization principle; no novelty of the general moment inequality is claimed.
