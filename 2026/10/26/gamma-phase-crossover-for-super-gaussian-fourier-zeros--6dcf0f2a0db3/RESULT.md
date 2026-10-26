# Gamma-phase crossover for super-Gaussian Fourier zeros

## Finding
For real \(p>0\), define the even Fourier transform, with angular-frequency normalization,
\[
F_p(x)=\int_{\mathbb R}e^{-|t|^p}e^{-ixt}\,dt=2\int_0^\infty e^{-t^p}\cos(xt)\,dt.
\]
There is an explicit universal crossover governing the first linearly many positive real zeros as \(p\to\infty\). Let \(\Phi:[0,\infty)\to\mathbb R\) be the continuous unwrapped argument of \(\Gamma(1+is)\), normalized by \(\Phi(0)=0\). Put
\[
R(s)=\operatorname{Re}\!\left(\frac{\Gamma''(1+is)}{\Gamma(1+is)}\right),\qquad s_k=\frac{k\pi}{p}.
\]
For every fixed \(C>0\), there is \(p_C\) such that, for each real \(p\ge p_C\), the first \(\lfloor Cp/\pi\rfloor\) positive real zeros of \(F_p\) exist and are simple. They are uniquely indexed \(x_{p,1}<x_{p,2}<\cdots\) from the origin, with no intervening positive zeros, and uniformly for \(1\le k\le\lfloor Cp/\pi\rfloor\),
\[
\boxed{x_{p,k}=k\pi-\Phi(s_k)+\frac{\Phi(s_k)\Phi'(s_k)-\frac12s_k R(s_k)}p+O_C(p^{-2}).}
\]
There is a unique \(s_*>0\) satisfying \(\Phi(s_*)=0\), numerically \(s_*=1.8055470716051069\ldots\). If \(k=k(p)\) and \(k\pi/p\to s\in(0,\infty)\setminus\{s_*\}\), then \(x_{p,k}-k\pi\to-\Phi(s)\). In particular the zeros sit to the *right* of the ideal top-hat/sinc zeros when \(0<s<s_*\), and to the *left* when \(s>s_*\). The change of sign occurs on the nontrivial mesoscopic scale \(k\asymp p\).

For each fixed positive integer \(k\), a sharper central-moment formula holds:
\[
\boxed{x_{p,k}=\frac{k\pi}{\Gamma(1+1/p)}-\frac{\zeta(3)(k\pi)^3}{3p^3}+O_k(p^{-4}).}
\]
The correction after rescaling by the Weibull mean is negative and governed by the third logarithmic cumulant. These are asymptotics for a growing zero window, not a claim about the entire unbounded Fourier zero set at any fixed \(p\).

## Assumptions and scope
The parameter \(p\) is arbitrary real, not necessarily integer or even. The theorem considers positive *real* Fourier zeros and the limit \(p\to+\infty\); all constants in \(O_C(\cdot)\) may depend on fixed \(C\), but not on \(p\) or the zero index in the displayed range. \(\Phi\) is the unique continuous lift of the gamma argument beginning at zero; replacing it by a principal argument generally makes the theorem false. No claim of uniformity in \(C\to\infty\) is made.

## Proof
**1. Exact Weibull reduction.** For \(x>0\), integration by parts, with vanishing boundary term at infinity, gives
\[
\frac{xF_p(x)}2=\int_0^\infty pt^{p-1}e^{-t^p}\sin(xt)\,dt
=\int_0^\infty e^{-u}\sin(xu^{1/p})\,du.
\]
Let \(U\) have the unit-exponential distribution, \(L=\log U\), and \(X_p=e^{L/p}\). Thus \(xF_p(x)/2=\mathbb E\sin(xX_p)\). Writing
\[
Q_p(x)=\mathbb E e^{ix(X_p-1)},\qquad
\frac{xF_p(x)}2=\operatorname{Im}\big(e^{ix}Q_p(x)\big),
\]
converts zeros into a phase-crossing problem. Since \(\mathbb E e^{isL}=\Gamma(1+is)\), the limiting phase factor is explicit.

**2. Uniform gamma approximation and first correction.** For fixed \(C>0\) and \(0\le s\le C\), Taylor's theorem for \(e^{L/p}\) and \(e^{iz}\), together with
\(\mathbb E[|L|^j e^{4|L|/p}]<M_j\) for sufficiently large \(p\), yield uniformly
\[
Q_p(ps)=\Gamma(1+is)+\frac{is}{2p}\Gamma''(1+is)+O_C(p^{-2}).
\]
The moment bound follows directly from integrability of \(u^{\pm4/p}|\log u|^j e^{-u}\) near zero and infinity. Differentiation of the original expectation additionally gives
\[
\sup_{x\ge0}|Q'_p(x)|\le\mathbb E|X_p-1|=O(p^{-1}).
\]
The gamma function has no zeros, so \(\min_{0\le s\le C}|\Gamma(1+is)|>0\). Consequently \(Q_p\) is nonzero throughout \([0,Cp]\) for large \(p\). Let \(\theta_p(x)\) be its continuous argument with \(\theta_p(0)=0\). Taking the imaginary part of the logarithm of the preceding expansion gives
\[
\theta_p(ps)=\Phi(s)+\frac{s}{2p}R(s)+O_C(p^{-2}),\qquad
\sup_{0\le x\le Cp}|\theta'_p(x)|=O_C(p^{-1}).
\]
The sign of the \(R\)-term here is **positive**, because the first correction to \(Q_p\) is \(+is\Gamma''/(2p)\).

**3. Exhaustive, simple zeros on linearly expanding intervals.** The function \(h_p(x)=x+\theta_p(x)\) satisfies \(h_p(0)=0\) and \(h'_p(x)>0\) on \([0,(C+1)p]\) for all sufficiently large \(p\). Moreover \(h_p((C+1)p)>Cp\). The identity
\[
\frac{xF_p(x)}2=|Q_p(x)|\sin h_p(x)
\]
therefore gives exactly one simple positive zero for each integer \(1\le k\le\lfloor Cp/\pi\rfloor\), namely the solution of \(h_p(x_{p,k})=k\pi\). Monotonicity proves that these are the *first* such zeros, with no extra zeros between. The derivative at any such zero is \((-1)^k|Q_p|h'_p\ne0\). Boundedness of \(\theta_p\) implies \(x_{p,k}-k\pi=O_C(1)\). Inserting this estimate into the uniform phase expansion, Taylor-expanding at \(s_k=k\pi/p\), and comparing coefficients establishes the boxed \(O_C(p^{-2})\) formula.

**4. Exactly one phase-sign crossover.** The classical digamma series gives
\[
\Phi'(s)=\operatorname{Re}\psi(1+is)
=-\gamma+\sum_{n=1}^\infty\frac{s^2}{n(n^2+s^2)},
\qquad
\Phi''(s)=\sum_{n=1}^\infty\frac{2sn}{(n^2+s^2)^2}>0\quad(s>0).
\]
Here \(\psi=\Gamma'/\Gamma\) and \(\gamma\) is Euler's constant. The first derivative starts at \(-\gamma\) and diverges to \(+\infty\), since summing over \(1\le n\le s\) gives a divergent harmonic lower bound. Strict convexity and \(\Phi(0)=0\) prove exactly one further positive zero \(s_*\), with the asserted sign pattern. The zero expansion proves the crossover in the positions of the Fourier zeros.

**5. Fixed-index skewness correction.** Let \(m_p=\mathbb E X_p=\Gamma(1+1/p)\) and \(Y_p=X_p-m_p\). Since \(pY_p\to L-\mathbb E L\) in every fixed moment, and the third cumulant of \(L\) is \(\psi''(1)=-2\zeta(3)\),
\[
\mathbb E Y_p^3=-\frac{2\zeta(3)}{p^3}+O(p^{-4}),\quad
\mathbb E|Y_p|^j=O(p^{-j})\quad(j=2,4,5).
\]
At \(x_0=k\pi/m_p\), use the exact identity
\[
\mathbb E\sin(xX_p)=\sin(xm_p)\mathbb E\cos(xY_p)
+\cos(xm_p)\mathbb E\sin(xY_p).
\]
Taylor's theorem gives \(\mathbb E\sin(x_0Y_p)=-x_0^3\mathbb E Y_p^3/6+O_k(p^{-5})\). The derivative with respect to \(x\) at \(x_0\) is \((-1)^k(m_p+O_k(p^{-2}))\). The unique nearby zero therefore lies at
\(x_0-\zeta(3)(k\pi)^3/(3p^3)+O_k(p^{-4})\), as claimed.

## Verification
Run `python verification/check.py` using `verification/requirements.txt` to reproduce direct numerical Fourier integral evaluations, the exact Weibull identity, root localization at increasing shape parameters, and convergence of the first- and second-order phase predictions. The checker is supplementary numerical evidence: all uniformity, uniqueness, simplicity, and the existence of the crossover follow analytically above.

## Relationship to prior work
The real zeros of Fourier integrals with fixed even super-Gaussian exponent were studied by Senouf (1995 preprint; 1996 journal paper) and by Paris (2012), using large-frequency steepest descents and Wright-function asymptotics. The present problem is a *different simultaneous limit*: the exponent diverges while the zero index grows proportionally to the exponent. In this scaling the Weibull boundary law and the nonvanishing complex gamma characteristic function yield a bounded phase shift, a second-order uniform correction, and its unique sign reversal. The inspected fixed-exponent expansions do not state these results; older unindexed sources could conceivably contain an equivalent uniform limit. The full text of Ki and Kim (2007) was not obtained, so no whole-document exclusion claim is made about it.

## Limitations
The conclusion controls the first \(O(p)\) positive real zeros for any fixed implicit constant; it does not classify farther zeros or all complex zeros. The numerical value of \(s_*\) is an approximation to the uniquely defined gamma-phase root. The originality comparison is literature-based and is not independent priority certification.

## References
- D. Senouf, *Asymptotic and Numerical Approximations of the Zeros of Fourier Integrals*, UCLA CAM Report 95-12 (March 1995), https://ww3.math.ucla.edu/camreport/95-12.pdf ; SIAM J. Math. Anal. 27 (1996), 1102–1128, doi:10.1137/S0036141094272216.
- R. B. Paris, *On the Asymptotics and Zeros of a Class of Fourier Integrals*, European Journal of Pure and Applied Mathematics 5 (2012), 260–281, https://www.ejpam.com/ejpam/article/view/1206/264 (public page dated 2012-07-31).
- H. Ki and Y.-O. Kim, *The Zero-Distribution and the Asymptotic Behavior of a Fourier Integral*, J. Korean Math. Soc. 44 (2007), 455–466, doi:10.4134/JKMS.2007.44.2.455 (abstract consulted; full text not verified).
- NIST Digital Library of Mathematical Functions, Chapter 5 (Gamma and digamma functions), https://dlmf.nist.gov/5.
