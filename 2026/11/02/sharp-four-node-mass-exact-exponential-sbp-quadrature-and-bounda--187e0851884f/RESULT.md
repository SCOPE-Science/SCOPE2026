# Sharp four-node mass-exact exponential SBP quadrature and boundary-layer scaling

## Finding
For every real \(\lambda>0\), put \(\mathcal F_\lambda=\operatorname{span}\{1,e^{\lambda x},e^{-\lambda x}\}\) on \([-1,1]\). Require a *closed diagonal-norm function-space summation-by-parts operator* with positive diagonal \(H\), exact differentiation of \(\mathcal F_\lambda\), and the additional physical mass calibration \(\mathbf1^{\mathsf T}H\mathbf1=2\). Then **four nodes are necessary and sufficient**. The following rule is the unique reflection-symmetric four-node choice (nodes and diagonal weights) satisfying these conditions:

\[
\begin{gathered}
 c=\cosh\lambda,\quad m=\frac{\sinh\lambda}{\lambda},\quad
 v=\frac12+\frac{\sinh(2\lambda)}{4\lambda}-m^2,\quad d=c-m,\\
 t=m-\frac vd,\qquad a=\frac{\operatorname{arcosh}t}{\lambda},\\
 W=\frac{v}{d^2+v},\qquad w=\frac{d^2}{d^2+v},\\
 (x_1,x_2,x_3,x_4)=(-1,-a,a,1),\qquad
 H=\operatorname{diag}(W,w,w,W).
\end{gathered}
\]

All four weights are strictly positive and \(0<a<1\); the rule integrates exactly \(1,e^{\pm\lambda x},e^{\pm2\lambda x}\). It therefore supports a matrix \(D\) differentiating \(\mathcal F_\lambda\) exactly and satisfying \(HD+D^{\mathsf T}H=\operatorname{diag}(-1,0,0,1)\).

The sharp limiting laws are
\[
 \lim_{\lambda\downarrow0}a=\frac1{\sqrt5},\quad
 \lim_{\lambda\downarrow0}W=\frac16,\quad
 \lim_{\lambda\downarrow0}w=\frac56,
\]
\[
 \lim_{\lambda\to\infty}\big[\lambda(1-a)-\log(2\lambda)\big]=0,
 \qquad \lim_{\lambda\to\infty}\lambda W=\frac12.
\]
Thus the two free nodes enter logarithmic-width endpoint layers in the steep-exponential limit, while the endpoint quadrature weights decay like the reciprocal scale.

## Assumptions and scope
The parameter is any fixed real \(\lambda>0\); arithmetic and identities are exact. A closed node set means distinct nodes \(-1=x_1<x_2<\cdots<x_n=1\). A diagonal-norm SBP operator is a pair of real matrices \((H,D)\) with \(H=\operatorname{diag}(h_1,\ldots,h_n)\), all \(h_i>0\), and \(HD+D^{\mathsf T}H=\operatorname{diag}(-1,0,\ldots,0,1)\), such that \(D(f(x_i))_i=(f'(x_i))_i\) for all \(f\in\mathcal F_\lambda\). *Mass-exact* means \(\sum_i h_i=\int_{-1}^1 1\,dx=2\). This is an **additional** requirement, not part of the general definition of an FSBP operator.

The minimality assertion is over all closed node sets (not only symmetric ones), with positive diagonal norm and the same mass calibration. Uniqueness is asserted **only for reflection-symmetric four-node quadrature nodes and weights**; no uniqueness of arbitrary nonsymmetric constructions or differentiation-matrix implementation is claimed.

## Proof
**1. Necessary moment conditions.** For all \(f,g\in\mathcal F_\lambda\), exact differentiation and the SBP identity imply
\[
 \sum_i h_i(fg)'(x_i)=[fg]_{-1}^{1}=\int_{-1}^1(fg)'(x)\,dx.
\]
Directly multiplying the basis functions shows
\[
 (\mathcal F_\lambda\mathcal F_\lambda)'=\operatorname{span}\{e^{\lambda x},e^{-\lambda x},e^{2\lambda x},e^{-2\lambda x}\}.
\]
Together with the mass constraint, the positive quadrature must be exact on the five-dimensional space \(\mathcal Q_\lambda=\operatorname{span}\{1,e^{\pm\lambda x},e^{\pm2\lambda x}\}\).

**2. Universal obstruction at three or fewer closed nodes.** For hypothetical three nodes \(-1,\xi,1\), let \(y=e^{\lambda x}\), \(u=e^{-\lambda}\), \(v_0=e^{\lambda}\), and \(r=e^{\lambda\xi}\). Then
\[
 q_\xi(x)=y^{-2}(y-u)(v_0-y)(y-r)^2
\]
belongs to \(\mathcal Q_\lambda\) because it is a quartic in \(y\), divided by \(y^2\). It is nonnegative throughout \([-1,1]\), positive except at finitely many points, and vanishes at all three nodes. Its integral is therefore strictly positive, whereas every rule on those nodes returns zero. The same witness excludes two closed nodes by choosing an arbitrary \(\xi\in(-1,1)\). Thus no mass-exact closed FSBP rule has fewer than four nodes, regardless of weight signs.

**3. Explicit four-node construction.** Let \(X\) be uniform on \([-1,1]\), and set \(Z=\cosh(\lambda X)\). Its range is \([1,c]\), first moment is \(m\), second moment is \(m^2+v\), with \(m\in(1,c)\) and \(v>0\). Moreover
\[
 (m-1)(c-m)-v=\mathbb E[(Z-1)(c-Z)]>0,
\]
since \(1<Z<c\) with positive probability. Consequently \(1<t=m-v/(c-m)<m<c\), so \(a=\operatorname{arcosh}(t)/\lambda\in(0,1)\). The proposed symmetric four-node rule has normalized mass \(W+w=1\), and its induced distribution for \(Z\) places probability \(W\) at \(c\) and probability \(w\) at \(t\). The identities
\[
 Wc+wt=m,\qquad Wc^2+wt^2=m^2+v
\]
follow by substitution. Odd hyperbolic sines integrate to zero, and \(\cosh(2z)=2\cosh^2z-1\). Hence the rule integrates exactly the constant and both signs of the first and second exponential frequencies. Positivity is immediate from \(v>0\), \(d>0\). Any symmetric four-node rule satisfying these moment equations must reproduce the same two-point distribution of \(Z\): variance forces \(v=(c-m)(m-t)\), and the mean then forces \(W=v/(d^2+v)\). This proves the claimed symmetric uniqueness.

**4. Actual SBP differentiation operator.** Let \(V\) be the \(4\times3\) matrix of sampled basis functions \((1,e^{\lambda x},e^{-\lambda x})\), and \(V'\) the sampled derivatives. The columns of \(V\) are linearly independent: multiplying a nonzero linear combination by \(e^{\lambda x}\) produces a quadratic in \(e^{\lambda x}\), which cannot vanish at three distinct nodes. Set \(B=\operatorname{diag}(-1,0,0,1)\) and \(K=HV'-BV/2\). Product-derivative exactness yields \(V^{\mathsf T}K+K^{\mathsf T}V=0\). Define
\[
 U=V(V^{\mathsf T}V)^{-1/2},\quad A=K(V^{\mathsf T}V)^{-1/2},\quad
 S=AU^{\mathsf T}-UA^{\mathsf T}-U(U^{\mathsf T}A)U^{\mathsf T}.
\]
Because \(U^{\mathsf T}U=I\) and \(U^{\mathsf T}A\) is skew-symmetric, \(S^{\mathsf T}=-S\) and \(SU=A\). Therefore \(SV=K\). Taking \(D=H^{-1}(B/2+S)\) gives \(DV=V'\) and the SBP identity. This proves sufficiency without assuming any unverified matrix-compatibility theorem.

**5. Sharp parameter limits.** Taylor series at zero give
\[
 c-m=\frac{\lambda^2}{3}+O(\lambda^4),\quad
 m=1+\frac{\lambda^2}{6}+O(\lambda^4),\quad
 v=\frac{\lambda^4}{45}+O(\lambda^6).
\]
Hence \(t=1+\lambda^2/10+O(\lambda^4)\), yielding the stated classical four-node Gauss–Lobatto limit. As \(\lambda\to\infty\), direct expansion of the displayed hyperbolic moments gives
\[
 c-m\sim\frac{e^\lambda}{2},\quad
 v\sim\frac{e^{2\lambda}}{8\lambda},\quad
 t\sim\frac{e^\lambda}{4\lambda}.
\]
Thus \(W\sim1/(2\lambda)\) and \(\operatorname{arcosh}(t)=\log(2t)+o(1)=\lambda-\log(2\lambda)+o(1)\), establishing the asserted logarithmic node layer.

**6. Why calibration genuinely costs a node.** On the symmetric three-node grid \((-1,0,1)\) a positive quadrature exact for \((\mathcal F_\lambda\mathcal F_\lambda)'\) exists, with endpoint weights \(A_3=\sinh\lambda/[\lambda(2\cosh\lambda+1)]\) and middle weight \(B_3=2\sinh\lambda(\cosh\lambda+1)/[\lambda(2\cosh\lambda+1)]\). Its total mass is
\[
 M_3=\frac{2\sinh\lambda(\cosh\lambda+2)}{\lambda(2\cosh\lambda+1)}>2,
 \qquad M_3-2=\frac{2\lambda^4}{45}+O(\lambda^6).
\]
The inequality follows because the numerator excess, after removing a positive factor, equals \(F(\lambda)=\sinh\lambda(\cosh\lambda+2)-\lambda(2\cosh\lambda+1)\), for which \(F(0)=0\) and \(F'(\lambda)=2\sinh\lambda(\sinh\lambda-\lambda)>0\). Thus no conclusion that *all* three-node FSBP operators are impossible is intended: the sharp obstruction is precisely to simultaneously enforcing exact physical mass.

## Verification
The standalone `verify.py` uses Python's high-precision `decimal` arithmetic and checks nine positive parameter values for exactness of all five exponential moments, positivity, and a freshly reconstructed skew-symmetric differentiation matrix solving \(SV=K\). It then checks the finite-scale three-node mass defect and the approach toward both asymptotic laws on four larger parameters. It does not replace the universal proof. Run `python verify.py` from the extracted package; it needs only the Python standard library. Double-precision evaluation should not be used blindly near \(\lambda=0\), where cancellations can be severe, or at large \(\lambda\), where exponentials grow rapidly.

## Relationship to prior work
Haase, Winters, and Glaubitz (arXiv:2610.30272v1, first public 21 October 2026) prove entropy-stable flux differencing for general FSBP and state the precise positive-quadrature criterion on \((\mathcal F\mathcal F)'\). Their examples use polynomial-enriched one-sided exponential spaces and do not state the mass-calibrated symmetric opposite-exponential formulas here. Hale, Harley, Nchupang, and Nordström (arXiv:2604.23306v1) give the broad generalized Gauss–Lobatto principle. Bercik, Patrascu, and Zingg (arXiv:2607.08934v1) and Glaubitz, Haase, Öffner, and Stafforst (arXiv:2607.13224v1) develop general minimal-node algorithms and related exponential examples. These are foundational prior results: generic existence of positive quadratures or FSBP matrices is not claimed as new. When generalized Chebyshev moment theory is applied directly to the augmented five-function space, it also predicts the abstract four-node minimum; that abstract cutoff is therefore not itself claimed as historically novel. The targeted additional results are the explicit hyperbolic solution, analytical comparison to the uncalibrated three-node rule, and sharp limiting logarithmic layer. A broad exponential-fitting literature exists, and historical priority for an algebraically equivalent explicit rule has not been independently resolved.

## Limitations
The theorem is restricted to one-dimensional first-derivative SBP on \([-1,1]\), one real positive frequency, closed nodes, and the stated extra mass-exactness condition. Symmetric four-node *quadrature* uniqueness does not entail unique general non-symmetric quadrature. The matrices are mathematical exact-arithmetic constructions; no numerical-conditioning guarantee at extreme frequencies, PDE stability experiment, convergence theorem, or assertion of independent validation is made. The asymptotic formula is pointwise in the parameter, not a uniform finite-precision stability claim.

## References
- H. M. Haase, A. R. Winters, J. Glaubitz, *Summation-by-parts operators for general function spaces: Flux differencing, entropy stability, and accuracy*, arXiv:2610.30272v1 (21 October 2026), https://arxiv.org/html/2610.30272v1.
- N. Hale, C. Harley, P. Nchupang, J. Nordström, *Summation-by-parts operators for general function spaces: optimal nodes*, arXiv:2604.23306v1 (25 April 2026), https://arxiv.org/html/2604.23306v1.
- A. Bercik, L. Patrascu, D. W. Zingg, *Construction and Optimization of Summation-by-Parts Operators for General Function Spaces Using an Improved Generalized Gaussian Quadrature Algorithm*, arXiv:2607.08934v1 (9 July 2026), https://arxiv.org/abs/2607.08934.
- J. Glaubitz, H. Haase, P. Öffner, F. Stafforst, *Gaussian FSBP operators: Comparison and application to numerical methods for hyperbolic conservation laws*, arXiv:2607.13224v1 (14 July 2026), https://arxiv.org/abs/2607.13224.
- G. Vanden Berghe, M. Van Daele, H. Vande Vyver, *Exponentially-fitted algorithms: fixed or frequency dependent knot points?*, Applied Numerical Analysis and Computational Mathematics 1 (2004), 49–65, https://doi.org/10.1002/anac.200310005 (abstract examined as historical adjacent work).
