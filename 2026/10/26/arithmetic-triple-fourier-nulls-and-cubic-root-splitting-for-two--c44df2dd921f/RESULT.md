# Arithmetic triple Fourier nulls and cubic-root splitting for two concentric spherical shells

## Finding
Let \(\sigma_a\) be uniform **probability** surface measure on the sphere of radius \(a\) in \(\mathbb R^3\), and fix \(0<r<1\). For the positive probability measure \(\mu_r=(\sigma_1+\sigma_r)/2\), adopt \(\widehat\mu_r(\xi)=\int e^{-i\xi\cdot x}\,d\mu_r(x)\). Its radial Fourier profile, an entire function of the complex variable \(t\), is
\[
\Phi_r(t)=\frac12\left(\frac{\sin t}{t}+\frac{\sin(rt)}{rt}\right),\qquad \Phi_r(0)=1.
\]
Every positive **real** zero is simple except in the following precisely classified case. Write \(r=p/q\) in lowest positive terms if it is rational. If \(p+q\) is odd, its positive triple zeros are exactly
\[
 t_j=(2j+1)q\pi,\qquad j=0,1,2,\ldots.
\]
These are all multiple positive real zeros, and every one has multiplicity **exactly three**. For irrational \(r\), or rational \(r\) with \(p+q\) even, all positive real zeros are simple. In particular, the number of triple zeros in \((0,R]\) equals \(R/(2q\pi)+O(1)\) in the resonant case and zero otherwise. If \(Z_{\rm mult}(R)\) and \(Z_{\rm distinct}(R)\) count respectively all positive real zeros with and without their analytic multiplicities, their exact difference is twice the number of triple zeros, thus
\[
Z_{\rm mult}(R)-Z_{\rm distinct}(R)=\frac{R}{q\pi}+O(1)
\]
in the resonant case, and exactly zero otherwise. No asymptotic formula for either *individual* count is asserted.

The triple roots have a universal local **cubic-root unfolding** in the radius ratio. For \(r_0=p/q\) resonant and any fixed \(j\ge0\), put \(t_0=(2j+1)q\pi\), let \(\delta=r-r_0\in\mathbb R\), and define the nonzero real constant
\[
C=\sqrt[3]{\frac{6t_0}{r_0(r_0^2-1)}}.
\]
For sufficiently small nonzero real \(\delta\), the three complex-frequency zeros near \(t_0\), counted with multiplicity, are simple and satisfy
\[
t_k(\delta)=t_0+\omega_k C\sqrt[3]{\delta}+O_{r_0,t_0}(|\delta|^{2/3}),\quad
\omega_k=e^{2\pi i k/3},\quad k=0,1,2,
\]
where \(\sqrt[3]{\cdot}\) denotes the real cube root for real arguments. Exactly one of these zeros remains real; the other two are nonreal complex conjugates. This statement is local around each fixed triple root, not uniform over arbitrarily high frequencies or over ratios approaching one.

## Assumptions and scope
The ambient space is \(\mathbb R^3\); shell measures are normalized to have **equal total mass** rather than equal area density. The Fourier convention has no \(2\pi\) in the exponent. The radius ratio satisfies the strict inequalities \(0<r<1\), and the assertions about multiplicity classification concern real nonzero radial frequencies. For the unfolding, the spectral parameter \(t\) is complexified while \(r\) varies over nearby real values.

## Proof
**Spherical Fourier transform.** On the sphere of radius \(a\), with \(\xi\) aligned with the north pole, the latitude coordinate \(u=\cos\theta\) has uniform probability density \(1/2\) on \([-1,1]\). Consequently,
\[
\widehat\sigma_a(\xi)=\frac12\int_{-1}^1e^{-ia|\xi|u}\,du=\frac{\sin(a|\xi|)}{a|\xi|}.
\]
This also proves that \(\Phi_r\) is entire by removability at the origin, and \(\Phi_r(0)=1\). For \(t\ne0\), \(\Phi_r(t)=H(t,r)/(2t)\), with
\[
H(t,r)=\sin t+r^{-1}\sin(rt),\quad H_t(t,r)=\cos t+\cos(rt).
\]
The analytic multiplicities of \(H\) and \(\Phi_r\) coincide at every nonzero zero.

**Complete repeated-root exclusion.** Factor the derivative as
\[
H_t(t,r)=2\cos\left(\frac{(1+r)t}{2}\right)\cos\left(\frac{(1-r)t}{2}\right).
\]
Suppose \(t>0\) and \(H(t,r)=H_t(t,r)=0\). If the first cosine factor vanishes, the sine-addition identities imply \(\sin t=\sin(rt)\); hence \(0=H(t,r)=(1+r^{-1})\sin t\). If the second cosine factor vanishes, they imply \(\sin t=-\sin(rt)\); hence \(0=H(t,r)=(1-r^{-1})\sin t\). Because \(0<r<1\), both coefficients are nonzero. In either case \(\sin t=\sin(rt)=0\). Therefore \(t=m\pi\), \(rt=n\pi\) for positive integers \(m,n\), and \(r=n/m\) must be rational.

Write \(r=p/q\) in lowest terms; then \(m=kq\), \(n=kp\) with \(k\) a positive integer. The remaining derivative condition is
\[
H_t(t,r)=(-1)^{kq}+(-1)^{kp}=0,
\]
which is equivalent to \(p+q\) odd and \(k\) odd. In particular, **no double zeros** arise away from this list. Differentiating further,
\[
H_{tt}=-\sin t-r\sin(rt),\qquad H_{ttt}=-\cos t-r^2\cos(rt).
\]
At a listed point, \(H_{tt}=0\) and
\[
H_{ttt}(t,r)=(-1)^{kq}(r^2-1)\ne0.
\]
Thus every multiple zero has order exactly three. The positive triple-zero set is exactly the arithmetic progression stated in the finding. Counting odd \(k\) with \(kq\pi\le R\) proves the triple-zero count and the multiplicity-minus-distinct counting identity.

**Unfolding.** Fix a listed \((t_0,r_0)\) and put \(s=t-t_0\), \(\delta=r-r_0\). Set \(A=\cos(t_0)\in\{\pm1\}\); then \(\cos(r_0t_0)=-A\). Exact differentiation gives
\[
H_r(t_0,r_0)=-\frac{At_0}{r_0},\qquad
H_{ttt}(t_0,r_0)=A(r_0^2-1).
\]
The first two \(t\)-derivatives vanish at \((t_0,r_0)\). Analytic Taylor expansion therefore yields
\[
H(t_0+s,r_0+\delta)=A\left(\frac{r_0^2-1}{6}s^3-\frac{t_0}{r_0}\delta\right)
+O(|s|^4+|s\delta|+|\delta|^2).
\]
Let \(u=\sqrt[3]{\delta}\), with the real cube root when \(\delta\) is real, and set \(s=uw\). Dividing by \(u^3\) gives a holomorphic family in \((w,u)\) near each of the three distinct simple roots of
\[
\frac{r_0^2-1}{6}w^3-\frac{t_0}{r_0}=0.
\]
The complex analytic implicit-function theorem yields three branches \(w_k(u)=\omega_kC+O(u)\), and hence the displayed expansions. A small disk enclosing \(t_0\) has exactly three zeros counted with multiplicity for all sufficiently small \(\delta\), by Rouché's theorem (or the Weierstrass preparation theorem). Distinct leading constants make all three perturbed zeros simple. Reality of coefficients and the three leading cube-root directions imply precisely one real branch and one conjugate nonreal pair for every sufficiently small nonzero real \(\delta\). This completes the proof.

## Verification
Run `python check.py` with `mpmath` installed as in `requirements.txt`. The self-contained checker directly integrates the latitude Fourier formula in high precision at twelve parameter/frequency choices, verifies exact predicted resonance derivatives numerically at twenty-five cases, tests twelve same-parity shared roots, and follows all three local complex zeros for four signed perturbations. Its recorded output is in `check_output.txt`. The all-frequency and all-parameter assertions are proved above; finite numerical tests are supplemental only.

## Relationship to prior work
Bezubik and Strasburger's 2006 account derives spherical surface-measure Fourier formulas and Bessel-function expansions, so the individual-shell \(\operatorname{sinc}\) transform is classical rather than a novelty claim. González Vieli's 2011 article (published in 2012) characterizes spherical Fourier restriction uniqueness in terms of Bessel zeros; it concerns a **single supporting sphere and arbitrary densities**, not the exact repeated-real-zero set of an equal-mass two-radius positive measure. Logan's 1983 work studies maximal zero counts of the wider class of positive-definite bandlimited functions; an upper bound for counted multiplicities does not imply the present radius-parity classification, exact triple-zero locations, or cubic-root splitting. These comparisons are not a guarantee of worldwide publication priority.

## Limitations
The theorem does not claim anything about multiple **nonreal** zeros away from local resonant neighborhoods, unequal shell masses, dimensions other than three, or more than two radii. No quantitative uniformity as \(t_0\to\infty\) or \(r_0\uparrow1\) is established. Published sources may contain equivalent formulations under the two-centered-uniform-mixture or exponential-sum terminology; those aliases remain a priority risk. No independent mathematical validation has been performed.

## References
- A. Bezubik and A. Strasburger, *A New Form of the Spherical Expansion of Zonal Functions and Fourier Transforms of SO(d)-Finite Functions*, first public 2006-03-03, arXiv:math-ph/0603011, https://arxiv.org/abs/math-ph/0603011.
- F. J. González Vieli, *A uniqueness result for the Fourier transform of measures on the sphere*, first online 2011-12-08, Bull. Aust. Math. Soc. 86 (2012), 78–82, https://doi.org/10.1017/S0004972711002942.
- B. F. Logan, *Extremal Problems for Positive-Definite Bandlimited Functions. III. The Maximum Number of Zeros in an Interval*, SIAM J. Math. Anal. 14 (1983), 258–268, https://doi.org/10.1137/0514024.
