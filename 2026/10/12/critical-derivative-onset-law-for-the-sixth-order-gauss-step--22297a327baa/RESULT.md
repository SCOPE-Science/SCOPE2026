# Critical derivative-onset law for the sixth-order Gauss step

## Finding
Let
\[
R(z)=\frac{1+z/2+z^2/10+z^3/120}{1-z/2+z^2/10-z^3/120}
\]
be the sixth-order three-stage Gauss--Legendre stability function. Let \(\rho\) denote the positive root of \(s^3+6s^2-40=0\), so that \(\rho\approx2.207606805471073\). The equality of \(\rho\) with the absolute-monotonicity radius of \(R\) was established by Lóczi and Ketcheson [1], Theorem 4.1; it is **prior work**.

For every real \(s>\rho\), define the first negative derivative index
\[
k_*(s)=\min\{k\in\mathbb Z:\ k\ge1,\ R^{(k)}(-s)<0\}.
\]
This index is finite. The new quantitative finding is
\[
\boxed{\displaystyle\lim_{s\downarrow\rho}(s-\rho)k_*(s)=C=3.809808603810598\ldots.}
\]
An exact expression for \(C\) is provided below. The law quantifies the growing derivative order required to expose failure of positivity immediately beyond the known radius. It also constructs corresponding finite absorbing-chain counterexamples, without asserting minimal dimension among all chains.

## Assumptions and scope
Write \(p(z)=z^3-12z^2+60z-120\). Its unique real root \(a\in(9/2,5)\) and conjugate pair \(b,\overline b\), \(\operatorname{Im}b>0\), are the simple poles of \(R\). Put \(\alpha=\operatorname{Re}b=(12-a)/2\) and
\[
A(z)=-8\frac{z^2+10}{z^2-8z+20},\quad U=|A(a)|,\quad W=2|A(b)|,\quad\theta=\arg(b+\rho).
\]
The numerator and denominator have no common root, and \(U>W>0\). The sharp constant is
\[
\boxed{C=\frac{(a+\rho)^2}{a-\alpha}\log\left(\frac UW\right).}
\]
The asymptotic concerns real steps \(s>\rho\) approaching \(\rho\) from above; neither nonlinear SSP preservation nor positivity of internal Runge--Kutta stages is asserted.

## Proof
**1. Pole geometry and domination.** The derivative of \(p\) is \(3((z-4)^2+4)\) on the real axis, so \(p\) has one real root \(a\in(9/2,5)\). Its remaining roots are \(b=\alpha+i\beta\) and \(\overline b\), with
\[
\alpha=\frac{12-a}{2},\quad |b|^2=a^2-12a+60,\quad\beta^2=\frac34(a^2-8a+32).
\]
The residue of \(R\) at each pole is \(A(z)\) evaluated at that pole, and the partial fraction expansion is
\[
R(z)=-1-\frac{A(a)}{a-z}-\frac{A(b)}{b-z}-\frac{\overline{A(b)}}{\overline b-z}.
\]
Direct algebra shows \(|a+s|=|b+s|\) precisely when \(s=4(5-a)/(a-4)=\rho\); substituting \(a=4(s+5)/(s+4)\) in \(p(a)=0\) gives \(s^3+6s^2-40=0\). Consequently \(a+s>|b+s|\) for \(s>\rho\). The strict residue inequality \(U>W\) follows by squaring positive quantities. With \(d=a^2-8a+20\), \(m=a^2-12a+60\) and \(\alpha=(12-a)/2\), set
\[
N=m^2-20m+40\alpha^2+100,\quad
D=m^2-16m\alpha+80\alpha^2+24m-320\alpha+400.
\]
One has \(D=d(a^2-8a+32)>0\), \(|A(b)|^2=64N/D\), and \(U^2=64(a^2+10)^2/d^2\). Polynomial reduction modulo \(p(a)=0\) yields
\[
(a^2+10)^2D-4d^2N=480(27a^2-125a+20)>0.
\]
The right-hand side is positive because \(a>9/2\), the quadratic is increasing there, and its value at \(9/2\) is \(17/4\).

**2. Exact high-order coefficient formula.** For integer \(k\ge1\), Taylor coefficients at \(-s\) are
\[
c_k(s)=\frac{R^{(k)}(-s)}{k!}=\frac{U}{(a+s)^{k+1}}+2\operatorname{Re}\frac{-A(b)}{(b+s)^{k+1}}.
\]
Writing \(\lambda(s)=\log((a+s)/|b+s|)\), and absorbing the constant residue phase into \(\varphi\), the sign of \(c_k(s)\) is that of
\[
U-W e^{(k+1)\lambda(s)}\cos((k+1)\theta(s)+\varphi),
\]
where \(\theta(s)=\arg(b+s)\) and the precise choice of \(\varphi\) does not affect the argument. At the critical radius, \(\lambda(\rho)=0\), while differentiation gives
\[
\lambda'(\rho)=\frac1{a+\rho}-\frac{\alpha+\rho}{|b+\rho|^2}
=\frac{a-\alpha}{(a+\rho)^2}>0.
\]
Thus \(\lambda(\rho+\delta)=\lambda'(\rho)\delta+O(\delta^2)\).

**3. Irrational critical pole angle.** Let \(t=2\cos(2\theta)\). Since \(|b+\rho|=a+\rho\),
\[
t=2-\frac{4\beta^2}{(a+\rho)^2}
=-\frac{a^4-16a^3+128a^2-512a+736}{(a^2-8a+20)^2}.
\]
Eliminating \(a\) using \(p(a)=0\) gives
\[
25t^3-195t^2+534t-353=0.
\]
This primitive polynomial is irreducible over \(\mathbb Q\): modulo two it becomes \(t^3+t^2+1\), which has no root in \(\mathbb F_2\). Its leading coefficient is \(25\), so \(t\) is not an algebraic integer. If \(\theta/\pi\in\mathbb Q\), then \(e^{2i\theta}\) is a root of unity, making \(t=e^{2i\theta}+e^{-2i\theta}\) an algebraic integer, a contradiction. Hence \(\theta/\pi\notin\mathbb Q\).

**4. Lower and upper onset bounds.** Write \(L=\log(U/W)>0\) and \(C=L/\lambda'(\rho)\). For any fixed \(\varepsilon\in(0,1)\), uniformly over integers \(1\le k\le(1-\varepsilon)C/\delta\), sufficiently small \(\delta>0\) gives \((k+1)\lambda(\rho+\delta)<L\). Therefore \(c_k(\rho+\delta)>0\), and
\[
\liminf_{\delta\downarrow0}\delta k_*(\rho+\delta)\ge C.
\]
For the converse, choose \(k_0=\lceil(1+\varepsilon)C/\delta\rceil\). For small \(\delta\), all \(k\ge k_0\) satisfy
\[
Ue^{-(k+1)\lambda(\rho+\delta)}/W < e^{-\varepsilon L/2}<1.
\]
Because \(\theta/\pi\) is irrational, every orbit of rotation by \(\theta\) on the circle meets the open arc where \(\cos\xi>e^{-\varepsilon L/2}\). Compactness of the circle supplies a **finite** integer \(M(\varepsilon)\) such that every orbit meets the arc within the first \(M(\varepsilon)\) consecutive rotations. By continuity the same assertion, with a slightly smaller positive margin, holds uniformly for all \(\theta(\rho+\delta)\) near \(\theta\). For some \(k\in[k_0,k_0+M(\varepsilon)]\), the cosine term therefore exceeds the required threshold and \(c_k(\rho+\delta)<0\). Hence
\[
\limsup_{\delta\downarrow0}\delta k_*(\rho+\delta)\le(1+\varepsilon)C.
\]
Letting \(\varepsilon\downarrow0\) proves the stated limit. The same dominant-complex-pole argument (using that the angle remains strictly between zero and \(\pi\)) shows \(k_*(s)<\infty\) for every \(s>\rho\).

**5. Finite Markov witness.** Let \(k=k_*(s)\). On the \((k+2)\)-state pure-birth chain, take unit jump rates from each state to the next and make the last state absorbing. The transient block is \(-I+N\), where \(N\) is the \((k+1)\)-dimensional nilpotent superdiagonal shift. Matrix analytic calculus gives
\[
[R(sG)]_{0,k}=\frac{s^k}{k!}R^{(k)}(-s)<0.
\]
The rational step is well defined since all poles of \(R\) have positive real part. Thus this explicit finite chain reveals non-stochasticity. No optimality of the chain's state count over other generators is asserted.

## Verification
The self-contained script `verify_gauss3_boundary.py` checks the pole-distance substitution, the exact residue-dominance reduction, the irreducible angle polynomial by elimination, and the exact rational fact \(R^{(13)}(-3)/13!<0\). High-precision examples sample the onset order at six values above the critical radius; these are numerical checks, not proof of the asymptotic. The analytic argument above proves the limit for all sufficiently small positive distances and gives a finite witness for every \(s>\rho\).

## Relationship to prior work
Lóczi and Ketcheson [1], Theorem 4.1, already establish **the exact radius** \(\rho\), the three poles, and residue domination. Their theorem determines where some derivative eventually becomes negative; it does **not** give a quantitative asymptotic for the index of the first such derivative as the radius is approached. The new finding adds the \(1/(s-\rho)\) onset law with its exact coefficient and proves pole-angle irrationality to control the oscillatory sign. The general link between absolute-monotonicity radii and linear end-step positivity is classical [2]. The known zero full-method SSP radius of three-stage Gauss concerns stage-level/nonlinear conditions and is not the positive linear-end-step radius [3]. Existing \([2/2]\) Padé positivity obstructions concern a different stability function [4].

## Limitations
The first negative derivative index is **not** asserted to equal the smallest number of states among all Markov generators that can yield a negative end-step entry. Finite tests are not exhaustive and do not establish the asymptotic. This result does not replace the established 2013 determination of the absolute-monotonicity radius; it quantifies near-critical onset beyond that boundary. The analysis is for the fixed sixth-order Gauss stability function, exact arithmetic, and real positive step parameters.

## References
1. L. Lóczi and D. I. Ketcheson, "Rational functions with maximal radius of absolute monotonicity," *LMS Journal of Computation and Mathematics* 17 (2014), 159–205, Theorem 4.1, originally arXiv:1303.6651 (first public submission 2013-03-26), https://arxiv.org/abs/1303.6651 , https://doi.org/10.1112/S1461157013000326 .
2. D. I. Ketcheson, "Highly Efficient Strong Stability-Preserving Runge–Kutta Methods with Low-Storage Implementations," *SIAM Journal on Scientific Computing* 30 (2008), 2113–2136, §2 and Theorem 1, https://doi.org/10.1137/07070485X .
3. D. I. Ketcheson, C. B. Macdonald and S. Gottlieb, "Optimal implicit strong stability preserving Runge–Kutta methods," *Applied Numerical Mathematics* 59 (2009), 373–392, §2.5, https://doi.org/10.1016/j.apnum.2008.03.034 .
4. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, "Essentially negative news about positive systems," *Linear Algebra and its Applications* 436 (2012), 3425–3442, https://doi.org/10.1016/j.laa.2011.12.021 .
