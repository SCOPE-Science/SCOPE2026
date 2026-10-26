# A sharp positivity resonance and logarithmically delayed sign loss in damped two-step Chebyshev integration

## Finding
For the explicit two-stage, second-order, damped two-step Runge–Kutta–Chebyshev realization specified below, the scalar decay equation \(y'=-\lambda y\), \(\lambda>0\), has the full strict absolute-stability interval \(-9/2<z=-\lambda h<0\). With exact positive startup \(y_0=1\), \(y_1=e^z\), there is a unique \(z_*=-3.762080033887951242488\ldots\) such that **every endpoint iterate is strictly positive if and only if \(z\in[z_*,0)\)**. For every \(z\in(-9/2,z_*)\), the endpoint sequence is eventually strictly negative and has exactly one sign transition. At the threshold, the method is unexpectedly **exact on the entire scalar exponential orbit**: \(y_n=e^{nz_*}\) for every integer \(n\geq0\). As \(z\uparrow z_*\) from below, the first negative index diverges logarithmically, with the explicit coefficient in the proof.

## Assumptions and scope
Take fixed \(h>0\) and an autonomous differential equation \(y'=f(y)\). The explicit two-step method, for \(n\geq1\), is
\[
\begin{aligned}
v_0&=\tfrac{16}{9}y_n-\tfrac79y_{n-1},\\
v_1&=v_0+\tfrac49 h f(v_0),\\
v_2&=\tfrac74v_1-\tfrac34v_0+\tfrac79h f(v_1),\\
y_{n+1}&=\tfrac47y_n+\tfrac37v_2.
\end{aligned}
\]
For nonautonomous equations, the stage evaluation times are \(t_n+7h/9\) and \(t_n+11h/9\), respectively. These exact coefficients are the \(s=2\), \(\eta=1/2\) specialization of the damped Chebyshev construction of Moisa and Faleichik (2023): its parameters are \(\alpha=4/7\), \(\omega=\sqrt{7/6}\), and \(\beta=16\omega/9\), satisfying the paper's order conditions. The present result concerns **endpoint iterates only**, with **exact startup** and **exact arithmetic**, on a strictly positive scalar exponential solution. It makes no assertion about positivity of the internal stages, other startup rules, general vector fields, or adaptive steps.

Define
\[
\begin{aligned}
T(z)&=\tfrac43+\tfrac{56}{27}z+\tfrac{112}{243}z^2
=\tfrac73\left(1+\tfrac49z\right)^2-1,\\
A(z)&=\tfrac47(1+T(z)),\qquad B(z)=-\tfrac14T(z).
\end{aligned}
\]
For \(0<T<4/3\), set
\[
\lambda_\pm(T)=\frac{4(1+T)\pm\sqrt{16-17T+16T^2}}{14},
\]
with \(0<\lambda_-(T)<\lambda_+(T)<1\), and put
\[
z_L=-\tfrac94\left(1+\sqrt{3/7}\right),\qquad z_R=-\tfrac94\left(1-\sqrt{3/7}\right).
\]
There is a unique \(z_*\in(-9/2,z_L)\) solving
\[
\lambda_-(T(z_*))=e^{z_*}.
\]
This equation, rather than its displayed numerical approximation, is the exact definition of the threshold.

## Proof
**Method and order.** Substitution of \(f(y)=\lambda y\), \(z=h\lambda\), into the four stage equations gives
\[
y_{n+1}=A(z)y_n+B(z)y_{n-1},\qquad
A(z)=\tfrac43+\tfrac{32}{27}z+\tfrac{64}{243}z^2,\quad
B(z)=-\tfrac13-\tfrac{14}{27}z-\tfrac{28}{243}z^2.
\]
The nonautonomous stage abscissae above and direct Taylor expansion give the endpoint coefficients \(1\), \(1\), and \(1/2\) through order two for an exact input pair. In particular, for the exponential test, \(e^{2z}-A(z)e^z-B(z)=\tfrac{62}{243}z^3+O(z^4)\). Hence this is a genuine second-order two-stage realization, not an arbitrarily chosen recurrence.

**Sharp absolute-stability interval.** The characteristic polynomial is \(r^2-A(z)r-B(z)\). Its strict Schur/Jury inequalities become
\[
1-A-B=\tfrac{12-9T}{28}>0,\qquad
1+A-B=\tfrac{44+23T}{28}>0,\qquad
1+B=1-\tfrac T4>0.
\]
Because \(T(z)\geq-1\), these hold precisely when \(T(z)<4/3\), equivalently \(-9/2<z<0\). In this interval both characteristic roots have modulus below one. Thus loss of positivity below cannot be attributed to ordinary linear instability.

**Spectral sign criterion.** Whenever \(T>0\), the discriminant \((16-17T+16T^2)/49\) is strictly positive. The two real roots are positive, and \(\lambda_-(T)\) increases strictly from \(0\) to \(1/3\) as \(T\) ranges from \(0\) to \(4/3\). To see monotonicity, implicit differentiation of \(r^2-\tfrac47(1+T)r+T/4=0\) yields
\[
\frac{d\lambda_-}{dT}
=\frac{\tfrac47\lambda_--\tfrac14}{2\lambda_--\tfrac47(1+T)}>0;
\]
the numerator and denominator are both negative, because \(\lambda_-\leq1/3<7/16\). Write \(E=e^z\). Exact startup produces, for all integers \(n\geq0\),
\[
y_n=\frac{(E-\lambda_-)\lambda_+^n+(\lambda_+-E)\lambda_-^n}{\lambda_+-\lambda_-}.
\]
Since \(\lambda_+>\lambda_->0\) and \(E>0\), this sequence is strictly positive for every \(n\) **exactly when \(E\geq\lambda_-\)**. When \(E<\lambda_-\), the coefficient of the dominating positive root is negative; the ratio of the smaller-root term to the larger-root term decreases strictly, so there is one crossing from positive to negative, and no later return. At \(E=\lambda_-\) the larger-root component vanishes and \(y_n=E^n\) exactly.

If \(-1\leq T\leq0\), both \(A(z)\) and \(B(z)\) are nonnegative, with \(A+B>0\); positive initial terms therefore generate positive endpoints at all subsequent times. The only possible negative endpoints thus lie in the two intervals where \(T>0\): \((-9/2,z_L)\) and \((z_R,0)\).

**Uniqueness and global sharpness.** On \((-9/2,z_L)\), \(T(z)\) decreases strictly from \(4/3\) to \(0\), so \(\lambda_-(T(z))\) strictly decreases from \(1/3\) to \(0\), while \(e^z\) strictly increases. Since \(e^{-9/2}<1/3\), exactly one crossing \(z_*\) occurs. On \((z_R,0)\), \(\lambda_-\leq1/3\), but \(e^z>e^{z_R}>e^{-1}>1/3\) (using \(z_R>-1\) and \(e<3\)). There can be no crossing on this second interval. Combining both regions with the nonnegative-coefficient middle proves the stated if-and-only-if positivity law on the whole stability interval.

**First-negative index and delay.** For \(-9/2<z<z_*\), define \(E=e^z\), \(L=\lambda_+(T(z))\), \(l=\lambda_-(T(z))\), so \(0<E<l<L<1\). The unique real crossing index is
\[
\nu(z)=\frac{\log\left((L-E)/(l-E)\right)}{\log(L/l)},
\qquad N_-(z)=1+\lfloor\nu(z)\rfloor.
\]
The formula for \(N_-\) counts a zero at an integer crossing as nonnegative: the next iterate is the first strictly negative one. Set \(K=e^{z_*}-\left.\tfrac{d}{dz}\lambda_-(T(z))\right|_{z=z_*}>0\), and let \(L_*=\lambda_+(T(z_*))\), \(l_*=e^{z_*}\). Taylor expansion gives \(l-E=K(z_*-z)+O((z_*-z)^2)\), hence
\[
N_-(z)=\frac{\log(1/(z_*-z))}{\log(L_*/l_*)}+O(1)
\qquad(z\uparrow z_*).
\]
Numerically \(\log(L_*/l_*)=3.2155242642\ldots\). The divergence is logarithmic, not a numerical failure to detect the sign change.

## Verification
The included standalone `verification/check.py` (Python standard library only) exactly reconstructs the stage recurrence and order-two identities using rational arithmetic. It then numerically brackets the unique transcendental root, checks the analytic spectral predictions on 600 sampled stable steps, checks the first-negative index, and tests logarithmic delay. Its actual replay produced `VERIFY_OK 2229` and \(z_*=-3.76208003388795124248878373658024979994\ldots\). The infinite-iteration assertions and uniqueness come from the proof, not the finite checks.

## Relationship to prior work
Moisa and Faleichik (2023), arXiv:2303.16267v1, supply the explicit damped two-step Chebyshev construction, order conditions, and negative-real-axis stability design. The method coefficients used here are an exact rational specialization of that established scheme. The new assertion is not the recurrence or the stability polynomial: it is the global, exact-startup **endpoint-positivity threshold**, its coincident nonzero exponential exactness resonance, and the logarithmic first-negative law. Moisa (2024) studies a later related family, but its full text was inaccessible for this comparison; unknown stronger coverage remains a scientific risk. Faleichik and Moisa (2025), arXiv:2504.00323v1, design a **one-step** method with a positive monotone stability polynomial, rather than classifying endpoint signs for the present damped two-step recurrence. Published positivity-onset results for BDF2 concern a distinct recurrence and do not imply this formula.

## Limitations
The result is exact arithmetic, fixed-step, scalar autonomous linear decay with a specially calibrated, but directly source-derived, two-stage parameter choice. It does not establish positivity of internal stage vectors or general semidiscrete parabolic systems, and it does not imply nonlinear monotonicity or SSP properties. The transcendental threshold has no claimed elementary closed form. Its numerical decimal is descriptive, not a replacement for the defining equation. No claim of independent scientific validation or exhaustive literature uniqueness is made.

## References
1. A. Moisa and B. Faleichik, *Second order stabilized two-step Runge-Kutta methods*, arXiv:2303.16267v1 (first public 2023-03-28), especially equations (9)–(10), (21), (24). https://arxiv.org/html/2303.16267v1
2. A. Moisa, *A family of two-step second order Runge–Kutta–Chebyshev methods*, Journal of Computational and Applied Mathematics 446 (2024), 115868, DOI: 10.1016/j.cam.2024.115868 (full text not inspected).
3. B. Faleichik and A. Moisa, *Explicit Runge-Kutta-Chebyshev methods of second order with monotonic stability polynomial*, arXiv:2504.00323v1 (2025), introductory motivation and one-step construction. https://arxiv.org/abs/2504.00323
