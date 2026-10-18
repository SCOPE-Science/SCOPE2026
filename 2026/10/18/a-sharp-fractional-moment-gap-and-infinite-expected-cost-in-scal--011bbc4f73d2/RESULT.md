# A sharp fractional-moment gap and infinite expected cost in scalar randomized model predictive control

## Finding

For a continuous-time scalar plant controlled by a freshly randomized finite-horizon optimal control every two time units, a completely explicit unbiased two-batch model produces *almost-sure exponential stabilization and decaying expected state magnitude*, but *exponentially increasing mean-square state and expected quadratic stage cost*. Moreover, its complete moment threshold lies strictly between orders one and two, and almost every realized infinite-horizon quadratic cost is finite even though its expectation is infinite. These are exact infinite-horizon assertions, not simulation extrapolations.

Specifically, let the true plant be \(\dot x=ax+u\), with \(a=147/145\). At times \(2n\), independently choose \(b_n=3/4\) or \(b_n=741/580\), each with probability \(1/2\). Compute the unique open-loop minimizer of \(\int_0^2 (x_b(t)^2+u(t)^2)\,dt\), where \(\dot x_b=b_n x_b+u\), initial state \(x_b(0)=X_n=x(2n)\), and no terminal cost. Apply that optimized time-dependent control to the *true* plant over the whole interval, then repeat. Define \(q_b=\sqrt{1+b^2}\), \(D_b=q_b\cosh(2q_b)-b\sinh(2q_b)\), and
\[
H(a,q)=\int_0^2 e^{as}\sinh(qs)\,ds=\frac12\left(\frac{e^{2(a+q)}-1}{a+q}-\frac{e^{2(a-q)}-1}{a-q}\right).
\]
The denominators are nonzero for both sampled models; the integral specifies the continuous extension otherwise. Put
\[
m_b=e^{2a}-\frac{H(a,q_b)}{D_b},\quad A=|m_{3/4}|,\quad B=|m_{741/580}|,\quad r_p=\frac{A^p+B^p}{2}.
\]
Then \(X_{n+1}=m_{b_n}X_n\) and, for every \(p>0\) and integer \(n\ge0\),
\[
\mathbb E|X_n|^p=|X_0|^p r_p^n.
\]
The exact constants satisfy \(1.38<m_{3/4}<1.40\), \(-0.50<m_{741/580}<-0.47\), \(r_1<1<r_2\), and \(AB<1\). There is therefore a **unique** \(p_*\in(1,2)\) such that \(r_{p_*}=1\). By continuity of the finite-horizon optimal-control transition, the strict inequalities persist on a nonempty open neighborhood of the two sampled drift coefficients and the horizon length, with the true drift always their mean. Moments of order \(0<p<p_*\) decay geometrically, those of order \(p=p_*\) remain constant, and those of order \(p>p_*\) increase geometrically for \(X_0\ne0\). Numerically \(p_*\approx1.601525123597\).

For every nonzero deterministic \(X_0\), \(X_n\to0\) exponentially almost surely, and the full continuous-time state has the same almost-sure stability property. Nevertheless, \(\mathbb E[X_n^2]=|X_0|^2r_2^n\to\infty\). If \(J_n=\int_{2n}^{2n+2}(x(t)^2+u(t)^2)\,dt\) denotes the **realized cost on the true plant**, then \(\sum_{n\ge0}J_n<\infty\) almost surely but \(\mathbb E\sum_{n\ge0}J_n=\infty\). In contrast, deterministic finite-horizon MPC built with the exact model \(b=a\) has multiplier strictly between \(0.39\) and \(0.40\), hence stable mean-square dynamics.

## Assumptions and scope

This is an exactly solved scalar, unconstrained continuous-time linear-quadratic example: input matrix, state weight, and control weight equal one; prediction and application horizons both equal two; terminal penalty zero; exact arithmetic; and independent, equally likely new batches at each horizon. The batch is constant throughout each two-unit prediction horizon (one time subinterval per horizon). It is **unbiased in the random-batch decomposition sense**, because \(A_1=3/8\), \(A_2=741/1160\), \(A_1+A_2=147/145\), and selecting either singleton with probability \(1/2\), followed by probability rescaling, gives model drift \(2A_1=3/4\) or \(2A_2=741/580\). Both the plant and every sampled model are stabilizable and detectable with unit input/state weighting. This scalar test case is a stability benchmark, **not** a computational acceleration claim.

## Proof

For any fixed model drift \(b\) and initial state \(X\), the strict convexity of the objective in \(u\) implies a unique optimizer. The first-order optimality conditions, with half-scaled adjoint \(p\), are
\[
\dot x_b=b x_b-p,\qquad \dot p=-x_b-bp,\qquad x_b(0)=X,\quad p(2)=0,\quad u=-p.
\]
Because \(q_b=\sqrt{1+b^2}>b\), the positive denominator \(D_b=q_b\cosh(2q_b)-b\sinh(2q_b)>0\). Solving the boundary-value system yields
\[
p(t)=\frac{X\sinh(q_b(2-t))}{D_b},\qquad u_b(t)=-\frac{X\sinh(q_b(2-t))}{D_b}.
\]
Indeed \(x_b(t)=-\dot p(t)-bp(t)\), giving \(x_b(0)=X\) and \(\dot x_b=b x_b-p\) since \(q_b^2=1+b^2\). The Euler–Lagrange conditions suffice by strict convexity. Applying \(u_b\) instead to the true drift \(a\), the variation-of-constants formula gives
\[
X_{n+1}=e^{2a}X_n-\frac{X_n}{D_b}\int_0^2e^{a(2-t)}\sinh(q_b(2-t))\,dt=m_bX_n.
\]
Fresh-batch independence gives the exact moment product formula for all real \(p>0\).

The rational-interval certificate in `verify.py`, using 65-term rational Taylor partial sums with a rigorously bounded exponential remainder, proves
\[
1.38<m_{3/4}<1.40,\quad -0.50<m_{741/580}<-0.47,\quad 0.39<m_a<0.40,
\]
\[
0<r_1<1<r_2,\qquad 0<AB<1.
\]
Because both the optimized input and the true-plant transition depend continuously on the two sampled drifts and positive horizon, the strict multiplier, moment, and product inequalities hold under sufficiently small parameter perturbations preserving unbiased sampling. In particular \(q_{3/4}=5/4\), \(q_{741/580}=941/580\), and \(q_a=\sqrt{42634}/145\); the last radical receives an exact rational-square enclosure. Let \(g(p)=r_p-1\) for \(p\ge0\). Then \(g(0)=0\), \(g''(p)=(A^p(\log A)^2+B^p(\log B)^2)/2>0\), \(g'(0)=\log(AB)/2<0\), and \(g(p)\to\infty\). Strict convexity and these signs give exactly one positive zero; since \(g(1)<0<g(2)\), it lies in \((1,2)\). At that zero the product identity makes the moment independent of the number of steps.

Because neither multiplier vanishes, the strong law of large numbers applies to their bounded logarithms: for \(X_0\ne0\),
\[
\lim_{n\to\infty}\frac{\log|X_n/X_0|}{n}=\frac12\log(AB)<0\qquad\text{almost surely}.
\]
On each interval the true state and applied control are \(X_n\) times one of two continuous deterministic functions, uniformly bounded on \([0,2]\). Thus the sample-time exponential rate implies almost-sure exponential decay throughout continuous time; the same uniform bound and \(r_1<1\) give exponentially decaying expected magnitude at every time.

For the realized true-plant interval cost, define \(\phi_b(t)\) as the true-state response starting from one under the displayed sampled-model control and \(\psi_b(t)=-\sinh(q_b(2-t))/D_b\). Then
\[
c_b=\int_0^2(\phi_b(t)^2+\psi_b(t)^2)\,dt\in(0,\infty),\quad J_n=c_{b_n}X_n^2.
\]
Positivity follows from \(\phi_b(0)=1\) and continuity; finiteness follows from finite-horizon continuity. Independence of \(b_n\) from \(X_n\) yields
\[
\mathbb E J_n=\frac{c_{3/4}+c_{741/580}}2\,|X_0|^2r_2^n.
\]
Its sum diverges by \(r_2>1\) and Tonelli's theorem. On almost every path, however, \(\sum_n X_n^2<\infty\) by the negative log growth and \(J_n\le (\max_b c_b)X_n^2\), proving finite realized total cost.

## Verification

Run `python3 verify.py` in the directory containing this document. It uses only the Python standard library. Its interval class represents lower/upper bounds as `fractions.Fraction`; it encloses the exponential at rational arguments by a Taylor polynomial of degree 65 and a positive geometric majorant for the remaining tail. Negative arguments use reciprocal enclosures. The derived hyperbolic-function bounds propagate through the exact optimal-control formula, certify both sign-separated multipliers, and verify the strict first/second moment, product, and deterministic nominal inequalities. A separate fourth-order Runge–Kutta integration checks the controlled-plant endpoint transitions numerically; that approximation is corroborative, not the proof. The numerical value quoted for the unique threshold comes from bisection, not from a formal transcendental root certificate.

## Relationship to prior work

Veldman, Borkowski and Zuazua (2022/2024), `arXiv:2211.05463`, introduce and analyze exactly the randomized-model MPC mechanism based on unbiased batches and establish sufficient exponential stability of **expected absolute state** (Theorem 1, Section IV). Their result does not assert mean-square stability or a finite expected infinite-horizon quadratic performance index whenever expected state magnitude decreases; nor does it calculate the present explicit two-batch scalar multipliers or their sharp fractional-moment threshold. The example does not contradict their sufficient hypotheses, and it makes no claim that their rate applies at these parameters. Veldman and Zuazua (2021/2022), `arXiv:2109.13798`, analyze finite-horizon optimal-control approximation through randomized time-splitting and explicitly describe fair two-singleton batches (Example 1); the material examined there does not state the repeated-receding-horizon risk dichotomy. The general product-moment criterion for scalar iid random multipliers, strict convexity, and the logarithmic strong law are standard tools, **not** claimed new. The contribution is their exact instantiation in a finite-horizon optimal-control mechanism with independently certified, competing stability notions and opposite conclusions for the same quadratic performance metric.

## Limitations

This is an explicitly motivated one-dimensional large-batch-interval boundary example, not a uniform guarantee or an impossibility statement for all random-batch MPC choices. No benefit in computational complexity arises in this dimension. It does not cover process noise, inequality constraints, intermediate within-prediction random switching, feedback recomputation within each interval, or different terminal penalties. The moment critical exponent is specified exactly as a unique transcendental root; its decimal approximation is not asserted exact. Overlapping formulations in older random-switching/multiplicative-control literature remain a priority risk. No independent validation has been performed.

## References

1. D. W. M. Veldman, A. Borkowski and E. Zuazua, *Stability and Convergence of a Randomized Model Predictive Control Strategy*, first arXiv publication 2022-11-10, `arXiv:2211.05463`, Section II, Theorem 1 and Section V. https://arxiv.org/html/2211.05463v3
2. D. W. M. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, first arXiv publication 2021-09-28, `arXiv:2109.13798`, Example 1 and Sections 2–3; open-access *Numerische Mathematik* 151 (2022), 495–549. https://link.springer.com/article/10.1007/s00211-022-01290-3
3. C. Liu, S. Shi and B. De Schutter, *Stability and Performance Analysis of Model Predictive Control of Uncertain Linear Systems*, first arXiv publication 2024-05-24, `arXiv:2405.15552`; bibliographic/abstract comparison only; complete text was not accessible in this comparison. https://arxiv.org/abs/2405.15552
