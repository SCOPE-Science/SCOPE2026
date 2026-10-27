# High-frequency ambiguity-zero strings for a mixed-polarity three-stage exponential pulse

## Finding

For any real rates \(a>b>0\), let
\[
\eta_a(t)=e^{-at}\mathbf1_{[0,\infty)}(t),\qquad
\check\eta_b(t)=e^{bt}\mathbf1_{(-\infty,0]}(t),\qquad
f_{a,b}=\eta_a*\eta_a*\check\eta_b.
\]
Define the symmetric self-ambiguity function, with Doppler frequency measured in cycles,
\[
A_{a,b}(T,\nu)=\int_{\mathbb R}
f_{a,b}(t+T/2)f_{a,b}(t-T/2)e^{-2\pi i\nu t}\,dt.
\]
Write \(d=a-b>0\), \(\lambda=a+b\), and let \(T_*>0\) be the **unique positive** solution of
\[
e^{dT_*}=1+\lambda T_*.
\]
Then there is an integer \(n_0=n_0(a,b)\) such that, for every integer \(n\ge n_0\), the ambiguity function has a zero at a positive delay \(T_n\) and a positive real Doppler frequency \(\nu_n\), with
\[
A_{a,b}(T_n,\nu_n)=0,\qquad
T_n=T_*+O_{a,b}(n^{-2}),\qquad
\nu_n=\frac{n+\frac12}{T_*}+O_{a,b}(n^{-1}).
\]
These zeros are distinct, and each is a simple zero in the complexified Doppler variable with delay held fixed. In particular, this explicitly given **threefold convolution of totally positive exponential factors has infinitely many genuine real delay–Doppler ambiguity zeros**. The constructed zero string has asymptotic Doppler spacing \(1/T_*\) and accumulates toward the finite-delay line \(T=T_*\) at unbounded Doppler frequency.

There is also a sharp boundary law. Keeping \(a>0\) fixed and letting \(b\uparrow a\),
\[
(a-b)T_*=\log\frac{a+b}{a-b}+
\log\log\frac{a+b}{a-b}+o(1).
\]
Thus the delay line supporting the high-frequency zeros escapes to infinity as the positive and negative exponential rates approach equality. The statement does **not** classify all ambiguity zeros at finite Doppler frequency or assert zero-freeness for \(b\ge a\).

## Assumptions and scope

All convolutions are ordinary convolutions on the real line, all rates are fixed positive real numbers, and \(a>b\) is essential to the theorem. The pulse is in \(L^1(\mathbb R)\cap L^2(\mathbb R)\), real-valued and nonnegative, but is not normalized to unit norm; multiplication by a positive constant changes no zero. The frequency \(\nu\) is in cycles per unit time; in the proof the variable \(w=\pi\nu\) is used. Only \(T>0\) and \(\nu>0\) are used to construct zeros. Every big-O assertion is for \(n\to\infty\) with \(a,b\) fixed. No uniformity as \(b\uparrow a\) is claimed for the sequence estimates.

A direct convolution gives the elementary pulse
\[
f_{a,b}(t)=\frac1{(a+b)^2}
\begin{cases}
e^{bt},&t<0,\\
e^{-at}(1+(a+b)t),&t\ge0.
\end{cases}
\]
Its asymmetry and the repeated positive-rate factor distinguish it from a two-factor exponential convolution and from all-forward three-factor convolutions.

## Proof

**1. Exact ambiguity expression.** Put \(w=\pi\nu\), \(u=a+iw\), and \(v=b-iw\). For \(\Re u,\Re v>0\), write \(\psi_u(T)=e^{-u|T|}\). Directly integrating each one-sided exponential's ambiguity function gives
\[
A(\eta_a,\eta_a)(T,\nu)=\frac{\psi_u(T)}{2u},\qquad
A(\check\eta_b,\check\eta_b)(T,\nu)=\frac{\psi_v(T)}{2v}.
\]
An elementary Fubini change of variables proves the convolution identity
\(A(g*h,g*h)(T,\nu)=(A(g,g)(\cdot,\nu)*A(h,h)(\cdot,\nu))(T)\)
for the integrable factors here. Hence
\[
A_{a,b}(T,\nu)=\frac{(\psi_u*\psi_u*\psi_v)(T)}{8u^2v}.
\]
For \(T\ge0\) and \(u^2\ne v^2\),
\[
(\psi_u*\psi_v)(T)=\frac{2(ue^{-vT}-ve^{-uT})}{u^2-v^2},\qquad
(\psi_u*\psi_u)(T)=\frac{e^{-uT}}u+Te^{-uT}.
\]
The second expression is \((\psi_u-u\partial_u\psi_u)/u\). Differentiating the first convolution identity with respect to \(u\), justified by exponential domination, gives
\[
(\psi_u*\psi_u*\psi_v)(T)
=\frac{2}{u(u^2-v^2)^2}
\left[2u^3e^{-vT}
-v\big(Tu(u^2-v^2)+3u^2-v^2\big)e^{-uT}\right].
\]
When \(a>b>0\) and \(w\in\mathbb R\), the factors \(u\), \(v\), and \(u^2-v^2\) are all nonzero. Therefore the real delay–Doppler zero equation is **exactly**
\[
e^{(u-v)T}=R(T,w),\qquad
R(T,w)=\frac{v}{2u^3}\big[T u(u^2-v^2)+3u^2-v^2\big]. \tag{1}
\]
Here \(u-v=d+2iw\). In particular, no cancellation or division by a zero has been introduced.

**2. Uniform large-Doppler expansion.** Rational expansion of the explicit right side of (1), uniform for \(T\) in compact sets, yields
\[
R(T,w)=-(1+\lambda T)-\frac{3i\lambda^2T}{2w}
+\frac{\lambda^2((4a+b)T-3)}{2w^2}+O_{a,b,T}(w^{-3}).\tag{2}
\]
The expansion and its first derivatives in \(T\) and \(1/w\) follow algebraically from a rational function, so are analytic around \(1/w=0\). Notice the **negative real** leading term; the phase of (1) at high positive Doppler is consequently near an odd multiple of \(\pi\).

**3. The unique positive limiting delay.** Let
\(F(T)=e^{dT}-1-\lambda T\) for \(T\ge0\). Then \(F(0)=0\), \(F'(0)=d-\lambda=-2b<0\), \(F''(T)=d^2e^{dT}>0\), and \(F(T)\to\infty\). Consequently \(F\) has exactly one positive zero \(T_*\), and \(F'(T_*)>0\). This nonzero derivative is critical for the next step.

**4. Real analytic implicit-function construction.** For an integer \(n\ge0\), set \(k=n+\tfrac12\) and introduce a real phase correction \(\theta\) by
\[
w=\frac{\pi k+\theta/2}{T}.
\]
Then \(e^{2iwT}=-e^{i\theta}\), so equation (1) is equivalent to the complex equation in two real unknowns
\[
H_k(T,\theta)=e^{dT+i\theta}+R\left(T,\frac{\pi k+\theta/2}{T}\right)=0.\tag{3}
\]
Put \(\varepsilon=1/k\). Because
\[
\frac1w=\frac{\varepsilon T}{\pi+\varepsilon\theta/2},
\]
expression (3) has a real analytic extension at \(\varepsilon=0\) for \(T\) near \(T_*>0\), \(\theta\) near zero. By (2),
\[
H_\infty(T,\theta)=e^{dT+i\theta}-(1+\lambda T).
\]
At \((T_*,0)\), its Jacobian for the map \((T,\theta)\mapsto(\Re H,\Im H)\) has columns
\( (F'(T_*),0)\) and \((0,e^{dT_*})\); its determinant \(F'(T_*)e^{dT_*}\) is strictly positive. The ordinary real analytic implicit-function theorem therefore supplies unique real solutions \((T_n,\theta_n)\) in a fixed neighborhood for all sufficiently large \(n\), with \(T_n\to T_*\), \(\theta_n\to0\), and positive \(w_n\). Substitution into (1) proves \(A_{a,b}(T_n,\nu_n)=0\) with \(\nu_n=w_n/\pi\).

At a solution, the imaginary part of (3) and the first correction in (2) show \(\theta_n=O(k^{-1})\). The first correction to (2) is purely imaginary. Thus the real part of (3) gives \(F(T_n)=O(k^{-2})\); because \(F'(T_*)>0\), it follows that \(T_n-T_*=O(k^{-2})\). Finally,
\[
\nu_n=\frac{k}{T_n}+\frac{\theta_n}{2\pi T_n}=
\frac{k}{T_*}+O(k^{-1}),
\]
proving the two asserted asymptotic laws. Consecutive frequencies differ by \(1/T_*+O(n^{-1})\), hence are eventually strictly increasing.

For the claimed Doppler simplicity, differentiate the left side minus the right side of (1) with respect to \(w\) at a constructed zero, with \(T=T_n\) held fixed. The derivative is
\[
2iT_ne^{(d+2iw_n)T_n}-\partial_w R(T_n,w_n)
=-2iT_*e^{dT_*}+o(1)\ne0,
\]
since \(\partial_wR=O(w^{-2})\). All prefactors relating (1) to the ambiguity function are nonvanishing in the stated domain. Hence each sufficiently distant constructed zero is simple as a zero in complex Doppler frequency at its fixed delay.

**5. Boundary-law derivation.** Write \(h=d/\lambda\in(0,1)\). Rearranging \(e^{dT_*}=1+\lambda T_*\) gives the explicit real Lambert-W representation
\[
T_*=-\frac1d W_{-1}(-h e^{-h})-\frac1\lambda,
\]
where \(W_{-1}\) is the real lower branch; the principal branch corresponds to the trivial zero delay. As \(h\downarrow0\), the standard inverse relation \(y-\log y=\log(1/h)+o(1)\), for \(y=dT_*\to\infty\), yields
\(y=\log(1/h)+\log\log(1/h)+o(1)\). This is exactly the displayed close-rate delay law.

## Verification

The companion `verify.py` requires the packages listed in `requirements.txt`. Execute `python verify.py` from the same directory. The supplied `verification_output.txt` records a successful run. The checker symbolically verifies the triple-convolution identity and the large-frequency expansion, independently integrates the original ambiguity definition at nine moderate-frequency test points, and numerically solves the two real zero equations for nine high-precision positive-frequency roots across three rate pairs. These finite calculations corroborate the exact identities and the predicted root geometry; the unbounded zero-string claim is proved by the analytic implicit-function argument, **not** by enumeration or floating-point sampling.

## Relationship to prior work

Jaming (2006) establishes moment-based **local** zero-free regions for radar ambiguity functions (including MSC 42B10); its estimates do not classify real zeros of specific threefold exponential convolutions. Kloos and Stöckler (2013) study totally positive functions and exponential splines primarily through Zak transforms and Gabor frames, rather than the present ambiguity-zero location problem. Gröchenig, Jaming and Malinnikova (2018), especially their Example 3 and Lemma 3.1, establish zero-freeness for **two-factor** exponential convolutions including one reversed factor. Their Theorem 4.2 treats repeated one-sided factors and their discussion flags more complex higher convolutions for further investigation. These results neither assert nor logically imply the mixed-polarity three-factor zero-string phenomenon proved here.

The present window has three exponential factors, two with rate \(a\) on the positive half-line and one with rate \(b<a\) on the negative half-line; it does not fall within the cited two-factor formula or the same-sign repeated-factor theorem. An equivalent result expressed in rational-filter terminology, exponential-spline geometry, or elsewhere in the ambiguity literature remains a publication-priority risk.

## Limitations

The theorem proves existence of an explicit cofinite string of genuine ambiguity zeros in the parameter region \(a>b>0\), not a classification of **all** zeros, a global zero count, or a converse for \(b\ge a\). Estimates for fixed rates are not uniform near \(a=b\). The constructed zeros have unbounded Doppler coordinate but converge in delay; this is not an accumulation of zeros at a finite point of the delay–Doppler plane. The source comparisons are substantial but cannot guarantee global publication novelty.

## References

1. P. Jaming, *Zero-free regions of radar ambiguity functions and moments*, arXiv:math/0606397v1 (first public version 2006-06-16), especially Theorem 3.1. https://arxiv.org/abs/math/0606397
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1 (2013-11-28). https://arxiv.org/abs/1311.7359
3. K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner distribution and the short-time Fourier transform*, arXiv:1811.03937v1 (2018-11-09), Sections 3–4, Lemma 3.1, Theorem 4.2. https://arxiv.org/abs/1811.03937
