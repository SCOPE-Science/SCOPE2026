# Exact one-probe effective-dimension bias and a rank–regularization boundary layer

## Finding

Let \(A\) be a real symmetric positive-definite \(2\times2\) matrix with eigenvalues \(a\ge b>0\). For \(\zeta>0\) let \(f_\zeta(t)=t/(t+\zeta)\), and estimate the effective dimension \(d_\zeta(A)=\operatorname{tr}f_\zeta(A)\) by the **one-probe specialization of FlexTrace**, using a single \(\omega\sim\mathcal N(0,I_2)\):

\[
\widehat A=A\omega(\omega^{\mathsf T}A\omega)^{-1}\omega^{\mathsf T}A,
\qquad T_\zeta=\omega^{\mathsf T}f_\zeta(\widehat A)\omega.
\]

Define \(s=\sqrt{a(a+\zeta)}\) and \(t=\sqrt{b(b+\zeta)}\). Then, for every \(a\ge b>0\) and \(\zeta>0\), the **exact mean bias** is

\[
\boxed{B_\zeta(a,b):=d_\zeta(A)-\mathbb E T_\zeta
=\frac{ab(a-b)^2}{(a+\zeta)(b+\zeta)(s+t)^2}.}
\]

Consequently, \(B_\zeta(a,b)\ge0\), with equality exactly when \(a=b\). Its ratio to the weaker eigenvalue's contribution satisfies the **sharp uniform envelope**

\[
\boxed{0\le\frac{B_\zeta(a,b)}{b/(b+\zeta)}
=\frac{a(a-b)^2}{(a+\zeta)(s+t)^2}
\le\left(\frac{a-b}{a+\zeta}\right)^2<1.}
\]

Here the upper constant \(1\) cannot be decreased uniformly: after letting \(b\downarrow0\) with \(a,\zeta>0\) fixed, the bias-to-weak-contribution ratio tends to \((a/(a+\zeta))^2\), which approaches \(1\) as \(a/\zeta\to\infty\).

More importantly, for **each fixed \(a>0\)**, as \(b\downarrow0\) and \(\zeta\downarrow0\) jointly, along any path with \(b,\zeta>0\),

\[
\boxed{\frac{B_\zeta(a,b)}{b/(b+\zeta)}\longrightarrow1,
\qquad \mathbb E T_\zeta\longrightarrow1.}
\]

In particular, if \(\zeta=\gamma b\) with any fixed \(\gamma>0\), then

\[
\boxed{\lim_{b\downarrow0}B_{\gamma b}(a,b)=\frac{1}{1+\gamma},
\quad \lim_{b\downarrow0}d_{\gamma b}(A)=1+\frac{1}{1+\gamma},
\quad \lim_{b\downarrow0}\mathbb E T_{\gamma b}=1.}
\]

Thus the estimator asymptotically misses **all** of the nonvanishing effective-dimension contribution from a weak eigenvalue when the regularization tracks that eigenvalue. The two separate boundary limits do not commute:

\[
\boxed{
\lim_{b\downarrow0}\lim_{\zeta\downarrow0}B_\zeta(a,b)=1,
\qquad
\lim_{\zeta\downarrow0}\lim_{b\downarrow0}B_\zeta(a,b)=0.}
\]

## Assumptions and scope

The random vector has two independent standard real Gaussian components; exactly one sample is used both to construct the rank-one Nyström matrix and to probe its matrix function. The zero-column leave-one-out approximation in FlexTrace's defining equation is the zero matrix and \(f_\zeta(0)=0\), so the estimator above is literally its \(k=1\) case, not the different estimator \(\operatorname{tr} f_\zeta(\widehat A)\). All calculations concern exact arithmetic and finite, positive \(\zeta\), with \(\zeta=0\) invoked only as a one-sided limit. Orthogonal invariance reduces every real symmetric positive-definite \(2\times2\) input to \(A=\operatorname{diag}(a,b)\).

## Proof

**1. Reduction to one Gaussian ratio.** Set \(y=A\omega\) and \(q=\omega^{\mathsf T}A\omega>0\) almost surely. The rank-one matrix \(\widehat A=yy^{\mathsf T}/q\) has nonzero eigenvalue \(\lambda=y^{\mathsf T}y/q\). Since \(f_\zeta(0)=0\),

\[
f_\zeta(\widehat A)=\frac{\widehat A}{\lambda+\zeta},
\qquad T_\zeta=\frac{(\omega^{\mathsf T}y)^2}{y^{\mathsf T}y+\zeta q}
=\frac{(a\omega_1^2+b\omega_2^2)^2}
{a(a+\zeta)\omega_1^2+b(b+\zeta)\omega_2^2}.
\]

This identity is valid for every nonzero probe. In polar coordinates, write \(\omega_1=\sqrt R\cos\theta\), \(\omega_2=\sqrt R\sin\theta\), with independent uniform \(\theta\in[0,2\pi)\) and \(R\sim\chi_2^2\), so \(\mathbb ER=2\). Put \(c=\cos\theta\), \(u=\sin\theta\), and \(D=s^2c^2+t^2u^2\); then

\[
\mathbb ET_\zeta=2\mathbb E_\theta\left[\frac{(ac^2+bu^2)^2}{D}\right].
\]

**2. Exact angular integration.** Substitution \(v=\tan\theta\) gives

\[
\mathbb E_\theta(D^{-1})
=\frac2\pi\int_0^\infty\frac{dv}{s^2+t^2v^2}
=\frac1{st}.
\]

Together with \(c^2+u^2=1\) and \(s^2c^2+t^2u^2=D\), this implies

\[
\mathbb E_\theta\frac{c^2}{D}=\frac1{s(s+t)},
\quad \mathbb E_\theta\frac{u^2}{D}=\frac1{t(s+t)}.
\]

Applying \(c^4+c^2u^2=c^2\) and \(s^2c^4+t^2c^2u^2=c^2D\), and their swapped counterparts, yields

\[
\mathbb E_\theta\frac{c^2u^2}{D}=\frac1{2(s+t)^2},\quad
\mathbb E_\theta\frac{c^4}{D}=\frac{s+2t}{2s(s+t)^2},\quad
\mathbb E_\theta\frac{u^4}{D}=\frac{t+2s}{2t(s+t)^2}.
\]

All displayed identities include \(s=t\) by continuity. Substituting them into the polar expression gives

\[
\mathbb ET_\zeta=
\frac{a^2(1+2t/s)+2ab+b^2(1+2s/t)}{(s+t)^2}.
\]

**3. Exact bias and sign.** Since \(d_\zeta(A)=a^2/s^2+b^2/t^2\), subtracting the previous expression produces a perfect square:

\[
\begin{aligned}
(s+t)^2B_\zeta(a,b)
&=\frac{a^2t^2}{s^2}+\frac{b^2s^2}{t^2}-2ab\\
&=\left(\frac{at}{s}-\frac{bs}{t}\right)^2
=\frac{a^2b^2(a-b)^2}{s^2t^2}.
\end{aligned}
\]

Using \(s^2=a(a+\zeta)\) and \(t^2=b(b+\zeta)\) proves the boxed formula and its equality condition.

**4. Sharp weak-mode comparison.** Division by \(f_\zeta(b)=b/(b+\zeta)\) gives the exact ratio above. Because \(s+t>s\),

\[
\frac{a(a-b)^2}{(a+\zeta)(s+t)^2}
\le\frac{a(a-b)^2}{(a+\zeta)s^2}
=\left(\frac{a-b}{a+\zeta}\right)^2<1
\]

with strictness in the first inequality when \(a>b\); for \(a=b\), both sides of the first comparison vanish and the last \(<1\) still holds. With \(b\downarrow0\) at fixed \(a,\zeta>0\), the exact ratio tends to \((a/(a+\zeta))^2\), establishing uniform sharpness of the constant \(1\) through the subsequent \(a/\zeta\to\infty\) limit.

**5. Regularization–rank boundary layer.** Fix \(a>0\) and let \(b,\zeta\downarrow0\) jointly. Then \(s\to a\), \(t\to0\), and the exact ratio in Step 4 tends to \(1\). Also \(a/(a+\zeta)\to1\), so \(\mathbb ET_\zeta=d_\zeta(A)-B_\zeta(a,b)\to1\). Along \(\zeta=\gamma b\), the weak contribution \(b/(b+\zeta)\) is identically \(1/(1+\gamma)\), giving the boundary-layer formula. For fixed \(b>0\), putting \(\zeta\downarrow0\) in the exact bias yields \((a-b)^2/(a+b)^2\), and then \(b\downarrow0\) gives \(1\). Conversely, with fixed \(\zeta>0\), taking \(b\downarrow0\) gives zero bias, and the following \(\zeta\downarrow0\) limit is zero. This proves the noncommuting iterated limits.

## Verification

The companion `verify.py` uses Python's standard library. It verifies 84 exact-rational closed-bias identities using eigenvalue pairs whose square-root parameters are rational, reconstructs 756 Nyström quadratic forms independently as literal \(2\times2\) matrices, compares the expectation with eight independent high-resolution angular quadratures, and tests 15 small-eigenvalue/regularization matched-scale cases. Run `python3 verify.py` in the directory containing the file. The expected success message begins `VERIFY_OK`. The exact integrals and all limiting statements are proved above; finite tests do not certify them by enumeration.

## Relationship to prior work

Madhavan, Alexanderian, and Saibaba (2026, arXiv:2603.05721v1) introduce FlexTrace in their Eq. (3.2) and include \(f_\zeta\) as the effective-dimension example in Table 1. Their Theorems 3.3 and 3.5 and Section 5 give general bias and mean-squared-error bounds; the published spectral tail bias bound in Theorem 3.3 assumes at least four probes. Those statements do not give the present **exact** one-probe, two-eigenvalue nonlinear bias, the sharp weak-mode ratio, or the noncommuting boundary limits. The estimator itself and general nonnegative-bias perspective are fully credited, not claimed new.

Persson and Kressner (arXiv:2209.11023v3, particularly Section 5) analyze approximating matrix functions through Nyström sketches and estimating traces of the approximations. Their basic trace-of-sketch estimator is not the same random quantity as a probe reused to evaluate the sketched function. Epperly, Tropp, and Webber (arXiv:2301.07825v2, XNysTrace) prove unbiasedness for the **linear** trace-estimation problem; linear unbiasedness neither states nor implies this nonlinear effective-dimension bias profile.

The three primary sources compared here and published-index searches do not establish that every equivalent calculation is absent from older literature. General work on ratios of Gaussian quadratic forms could contain an algebraically equivalent integral under different terminology.

## Limitations

Only the one-probe specialization, two real positive eigenvalues, Gaussian sampling, and \(f_\zeta(t)=t/(t+\zeta)\) are covered. The limiting operation \(\zeta\downarrow0\) does not assert that the source's estimator is defined at \(\zeta=0\). No bound on the variance, mean-squared error, higher-dimensional error, larger sketch budgets, or finite-precision behavior follows from this theorem. At exactly rank one with fixed \(\zeta>0\), the single probe gives an unbiased estimate; the claimed loss pertains to the joint approach to the rank and regularization boundaries. The source comparisons do not exhaust older literature on Gaussian quadratic-form ratios.

## References

1. M. Madhavan, A. Alexanderian, and A. K. Saibaba, *FlexTrace: Exchangeable Randomized Trace Estimation for Matrix Functions*, arXiv:2603.05721v1, 2026-03-05. https://arxiv.org/html/2603.05721v1
2. D. Persson and D. Kressner, *Randomized Low-Rank Approximation of Monotone Matrix Functions*, arXiv:2209.11023v3. https://arxiv.org/html/2209.11023v3
3. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, arXiv:2301.07825v2. https://arxiv.org/html/2301.07825v2
