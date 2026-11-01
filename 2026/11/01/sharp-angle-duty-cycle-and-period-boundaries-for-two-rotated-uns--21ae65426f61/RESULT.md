# Sharp angle, duty-cycle and period boundaries for two rotated unstable saddle flows

## Finding

Two individually unstable planar linear saddle flows with the same spectrum can become exponentially stable under periodic switching. For the canonical pair of *symmetric*, equally damped, rotated saddles defined below, the stable region has a complete closed-form description. In particular, the stability boundary has a **single upper period cutoff**, rather than a disconnected antiresonance window: no switching rate can stabilize an unstable average within this family. There is an exact minimum rotation angle, an optimal equal-duty rule, and an explicit tolerance to duty-cycle imbalance. The cutoff diverges logarithmically when the two saddle axes become orthogonal; the duty-cycle tolerance closes with a square-root law at the cutoff.

Write \(c=\cos\theta\), \(s=\sin\theta\), \(T=u+v\), and \(\Delta=u-v\). The spectral radius of the one-period monodromy is exactly
\[
\rho(\Phi)=\exp\bigl(-aT+\operatorname{arcosh}S\bigr),\qquad
S=c^2\cosh(pT)+s^2\cosh(p\Delta).
\]
Therefore the system is exponentially asymptotically stable **if and only if**
\[
S<\cosh(aT).
\]

For fixed period \(T>0\), stable dwell times exist exactly when \(0\le c<a/p\) and, if \(c>0\), \(T<T_*(\theta)\), where \(T_*(\theta)>0\) is the unique solution of
\[
 c\sinh(pT_*/2)=\sinh(aT_*/2).
\]
At \(c=0\) set \(T_*=+\infty\). In the allowed region the complete, sharp duty-cycle condition is
\[
|\Delta|<\Delta_*(T,\theta),\qquad
\Delta_* =\frac1p\operatorname{arcosh}\!\left(
\frac{\cosh(aT)-c^2\cosh(pT)}{1-c^2}\right).
\]
In particular, \(\Delta_*<T\) for \(c>0\), and \(\Delta_*=(a/p)T\) for \(c=0\). Equal dwell times maximize the stability margin at every fixed period and angle. For \(0<c<a/p\), the **relative** tolerance \(\Delta_*(T,\theta)/T\) strictly decreases throughout \(0<T<T_*\), from the sharp rapid-switching limit
\[
\lim_{T\downarrow0}\frac{\Delta_*}{T}=\sqrt{\frac{(a/p)^2-c^2}{1-c^2}}
\]
to zero at the cutoff.

A complementary **fixed-duty classification** holds. Set \(m=|\Delta|/T\in[0,1)\). For \(c>0\), there is an exponentially stable switching period if and only if the *averaged* matrix is Hurwitz, equivalently
\[
 p\sqrt{c^2+(1-c^2)m^2}<a.
\]
When this strict inequality holds, exactly one positive transition period \(T_{\mathrm{crit}}(m,\theta)\) exists, determined by
\[
c^2\cosh(pT_{\mathrm{crit}})+(1-c^2)\cosh(pmT_{\mathrm{crit}})=\cosh(aT_{\mathrm{crit}}).
\]
Every \(0<T<T_{\mathrm{crit}}\) is stable, equality is neutral, and every larger period is unstable. An unstable or marginally stable averaged matrix cannot be rescued by finite-period switching in this symmetric family. In the orthogonal limit \(c=0\), all positive periods are stable exactly when \(pm<a\), and no positive period is stable when \(pm\ge a\).

For \(0<c<a/p\), the geometric cutoff and tolerance obey
\[
 T_*(\theta)=\frac{2}{p-a}\log\frac1c+o(1)
\quad(c\downarrow0),
\]
and, with \(B(T)=[\cosh(aT)-c^2\cosh(pT)]/(1-c^2)\),
\[
\Delta_*(T,\theta)=
 \frac{\sqrt{-2B'(T_*)}}{p}\sqrt{T_*-T}
 +O\bigl((T_*-T)^{3/2}\bigr)
\quad(T\uparrow T_*),
\]
where \(B'(T_*)<0\). At the other angle boundary,
\[
T_*(\theta)\sim
\sqrt{\frac{24p(a/p-c)}{a(p^2-a^2)}}
\quad(c\uparrow a/p).
\]

## Assumptions and scope

Fix real parameters \(0<a<p\), \(\theta\in[0,\pi/2]\), and dwell times \(u,v>0\). With \(I\) the \(2\times2\) identity, put
\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\]
\[
A_1=-aI+pH,\qquad A_2=-aI+pR_\theta H R_\theta^{\mathsf T}.
\]
For each integer \(k\ge0\), solve \(\dot z=A_1z\) on \([kT,kT+u)\) and \(\dot z=A_2z\) on \([kT+u,(k+1)T)\), with continuous states at switches and \(T=u+v\). Both instantaneous matrices have exactly the same eigenvalues \(p-a>0\) and \(-p-a<0\). Stability refers to exponential convergence of **every** real initial state to zero as physical time tends to infinity. Neither matrix is required to be realizable as the companion matrix of a fixed-coordinate second-order mechanical oscillator.

At a nonorthogonal stability boundary the monodromy has one simple multiplier equal to \(1\) and a second multiplier \(e^{-2aT}<1\). A generic solution tends to a nonzero \(T\)-periodic solution, and zero is not asymptotically stable. In an unstable regime there is an expanding Floquet direction. No nonlinear or arbitrary-switching assertion is made.

## Proof

**1. Exact Floquet multipliers.** Set \(K=R_\theta H R_\theta^{\mathsf T}\). Since \(H^2=K^2=I\),
\[
 e^{uA_1}=e^{-au}\bigl(\cosh(pu)I+\sinh(pu)H\bigr),
\]
with the analogous formula replacing \(H,u\) by \(K,v\). Also \(\operatorname{tr}H=\operatorname{tr}K=0\) and \(\operatorname{tr}(KH)=2\cos(2\theta)\). Thus the undamped product has determinant \(1\) and half-trace
\[
\cosh(pu)\cosh(pv)+\cos(2\theta)\sinh(pu)\sinh(pv)
=c^2\cosh(pT)+s^2\cosh(p\Delta)=S.
\]
Here \(S\ge1\). The undamped product is a product of real symmetric positive-definite matrices and is similar to a symmetric positive-definite matrix, so its two eigenvalues are positive. Its characteristic polynomial gives \(e^{\pm\operatorname{arcosh}S}\). Multiplying by \(e^{-aT}\) gives precisely the claimed multipliers and stability criterion. The other multiplier is always positive and their product is \(e^{-2aT}\).

**2. Sharp angular and duty boundaries at fixed period.** For \(\theta>0\), the function \(S\) is strictly increasing with \(|\Delta|\ge0\). Its minimum at equal dwell times is
\[
S_0=c^2\cosh(pT)+s^2=1+2c^2\sinh^2(pT/2).
\]
The stable region can therefore be nonempty only if \(c\sinh(pT/2)<\sinh(aT/2)\). For \(0<c<a/p\), the ratio \(\sinh(aT/2)/\sinh(pT/2)\) decreases continuously and strictly from \(a/p\) to zero, giving the unique positive cutoff \(T_*\). Strict decrease follows by differentiating the logarithm and using the strict increase of \(x\mapsto x\coth x\) on \((0,\infty)\). If \(c\ge a/p\), the strict inequality fails for every \(T>0\); if \(c=0\), it holds for every \(T>0\). Solving the strict inequality \(S<\cosh(aT)\) for \(|\Delta|\) gives \(\Delta_*\). Since \(a<p\), the arcosh argument is strictly below \(\cosh(pT)\), so \(\Delta_*<T\) when \(c>0\). Equal dwell times are the unique stability-optimal choice for \(\theta>0\).

**3. Sharp *single-cutoff* law at every fixed duty fraction.** Fix \(m=|\Delta|/T<1\), and put \(w=c^2\in(0,1]\). The sign of the stability inequality is the sign of the entire function
\[
F(T)=w\cosh(pT)+(1-w)\cosh(pmT)-\cosh(aT)
=\sum_{k=1}^\infty
\frac{[p^{2k}(w+(1-w)m^{2k})-a^{2k}]T^{2k}}{(2k)!}.
\]
The matrix averaged over one period has eigenvalues
\[
-a\pm p\sqrt{w+(1-w)m^2};
\]
so it is Hurwitz exactly when the coefficient of \(T^2\) in \(F\) is negative. If that coefficient is nonnegative, *all* coefficients are nonnegative: by the monotonicity of weighted power means, the sequence \((w+(1-w)m^{2k})^{1/(2k)}\) is nondecreasing. Therefore \(F(T)>0\) for \(T>0\) (the case \(w=1\) is immediate). If the coefficient of \(T^2\) is negative and \(w>0\), the weighted power means increase towards \(1>a/p\); hence coefficients are initially negative, then positive, changing sign at most once. Let \(K\ge2\) be their first positive index. In the series for \(F(T)/T^{2K}\), every strictly negative lower-index term is an increasing function of \(T>0\), and every positive higher-index term is also increasing. This quotient is strictly increasing from \(-\infty\) near zero to \(+\infty\) as \(T\to\infty\), because \(F(T)\sim w e^{pT}/2\). Thus it has exactly one zero, with negative sign below and positive sign above. This proves the fixed-duty existence criterion and uniqueness of the transition. It also proves strict shrinkage of the **fractional** duty window with period: for \(0<T_1<T_2<T_*\), the fraction \(m=\Delta_*(T_2)/T_2\) is neutral at \(T_2\), hence strictly stable at \(T_1\) by the single-cutoff law, so \(\Delta_*(T_1)/T_1>m\). A quadratic expansion of \(S-\cosh(aT)\) gives the displayed sharp small-period limit. At \(w=0\), \(F(T)=\cosh(pmT)-\cosh(aT)\), giving the stated all-period orthogonal classification directly.

**4. Geometric boundary rates.** At the balanced cutoff, \(c\sinh(pT_*/2)=\sinh(aT_*/2)\). Letting \(c\downarrow0\) forces \(T_*\to\infty\). The large-argument formula for \(\sinh\) yields \(c e^{(p-a)T_*/2}\to1\), proving the logarithmic law. Expanding the same identity to cubic order in \(T_*\) as \(c\uparrow a/p\) yields \(T_*^2\sim24p(a/p-c)/[a(p^2-a^2)]\).

Finally, \(B(T_*)=1\) and
\[
B'(T_*)=\frac{a\sinh(aT_*)-pc^2\sinh(pT_*)}{1-c^2}<0.
\]
To see the sign, put \(t=T_*/2\) and use the root identity: its numerator equals \(2\sinh^2(at)[a\coth(at)-p\coth(pt)]<0\), again because \(x\mapsto x\coth x\) is strictly increasing. Taylor expansion of \(B\), followed by \(\operatorname{arcosh}(1+h)=\sqrt{2h}+O(h^{3/2})\), gives the square-root duty-tolerance law. This completes the classification including endpoint behavior.

## Verification

The standalone file `verify.py` computes the monodromy matrices directly using matrix exponentials and compares spectral radii against the closed formula at 525 parameter choices, including near-orthogonal and zero-angle limits. It also checks the exact example, strict stability on both sides of the predicted cutoff, the duty boundary, and representative fixed-duty and logarithmic regimes. Execute `python verify.py` with NumPy and SciPy installed. The analytical proof, not this finite test, establishes the quantified statements.

As a reproducible instance, set \(a=1\), \(p=2\), \(\theta=\arccos(1/3)\). Each mode has spectrum \(\{1,-3\}\). For equal dwell times, the sharp period boundary is
\[
T_*=2\operatorname{arcosh}(3/2)=1.924847300238\ldots.
\]
For \(0<T<T_*\), the full duty condition becomes
\[
\cosh(2\Delta)<\frac{9\cosh T-\cosh(2T)}8.
\]
At exactly orthogonal axes, by contrast, every \(T>0\) is stable whenever \(|\Delta|<T/2\), illustrating the singular disappearance of the finite-period cutoff.

## Relationship to prior work

Xiedeng, Celli, and Porfiri (2026) rigorously exhibit antiresonance windows for a modulated mechanical oscillator with a saddle and an unstable focus or node and emphasize the no-stabilization property for two saddles *in that oscillator's companion-matrix class*. Their physical state matrices have a common upper row and are not the arbitrary rotated symmetric saddle pair studied here. The present result therefore does **not** contradict their no-saddle-pair statement. It instead classifies a different canonical matrix geometry and proves exactly when fast switching stabilizes its two unstable saddles. Unlike their intermediate-frequency antiresonance, stabilization here requires a Hurwitz average and is lost at one upper period cutoff.

Gökçek (2004) supplies the general Floquet criterion and fast-switching sufficiency for Hurwitz averages. Hou, Wang, and Xie (2021) provide a hyperbolic-function instability threshold for a special cooperative pair whose individual modes are stable; their matrices, stability question, and switching normalization differ. Tripathi and Agarwal (2021) analyze dwell-time stability for two already Hurwitz matrices. The Araki–Lieb–Thirring matrix inequality gives general monotonicity comparisons for positive-definite matrix products, so absence of reentrant stable windows should not be credited as a general new principle. The proposed specific contribution is the **sharp joint angle/period/duty classification, with explicit quantitative tolerance and its singular boundary laws** for an unstable–unstable symmetric pair. No claim of universally new Floquet theory or of arbitrary-switching stability is made.

## Limitations

The modes are symmetric in the fixed Euclidean coordinate system and have identical opposing saddle exponents plus the same isotropic damping; this restrictions matters. The theorem does not extend to arbitrary nonsymmetric or companion-form oscillator matrices, where intermediate-frequency antiresonance and instability of the average can coexist with switched stability. The scheme is periodic two-mode switching, not adaptive, stochastic or irregular switching. This is an analytic self-reviewed result without an independent mathematical audit; historical priority may require additional specialized literature checking, particularly older matrix-analysis and switched-systems classifications. Numerical checks are illustrative and not infinite certificates.

## References

1. D. Xiedeng, P. Celli, and M. Porfiri, *Dynamic stabilization of a mechanical oscillator in the absence of any stable feature*, Nature Communications 17, 6024 (public March 10, 2026). DOI: 10.1038/s41467-026-70493-1. Open complete text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13346612/.
2. C. Gökçek, *Stability analysis of periodically switched linear systems using Floquet theory*, Mathematical Problems in Engineering (2004). DOI: 10.1155/S1024123X04401069.
3. T. Hou, Y. Wang, and X. Xie, *Instability and bifurcation of a cooperative system with periodic coefficients*, Electronic Research Archive 29 (2021), 3069–3079. DOI: 10.3934/era.2021026.
4. S. Tripathi and N. Agarwal, *Stability of bimodal planar linear switched systems*, arXiv:2109.04201 (2021).
5. K. M. R. Audenaert, *An Araki–Lieb–Thirring inequality for geometrically concave and geometrically convex functions*, arXiv:1204.3418 (2012).
