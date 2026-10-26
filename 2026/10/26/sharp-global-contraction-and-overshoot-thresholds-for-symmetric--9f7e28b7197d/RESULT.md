# Sharp global contraction and overshoot thresholds for symmetric MPRK22

## Finding

For the conservative-stage second-order modified Patankar--Runge--Kutta method \(\operatorname{MPRK22}(\alpha)\) at \(\alpha=1/2\), applied in exact arithmetic to symmetric two-species exchange, every strictly positive trajectory converges globally and geometrically to equilibrium at every finite positive step. Its *optimal global one-step contraction constant*, sharp overshoot boundary, and exceptional cubic-convergence step admit explicit formulas.

Write \(t=2\kappa h>0\), where \(\kappa>0\) is the exchange rate and \(h>0\) is the time step. For normalized signed error \(\delta=(y_1-y_2)/(y_1+y_2)\in(-1,1)\), a complete conservative MPRK22 step satisfies
\[
\delta^+=m_t(\delta^2)\delta,\qquad
m_t(D)=-\frac{4D+t^3+t^2-4t-4}{t^3+5t^2+8t+4-(2t^2+4t+4)D},\quad 0\le D\le1.
\]
The sharp uniform error contraction factor over all strictly positive initial states is
\[
q(t)=\sup_{-1<\delta<1}\frac{|\delta^+|}{|\delta|}
=\max\left\{\frac{2-t}{2+t},\ \frac{t^2+t-4}{t^2+3t+4}\right\}<1,
\]
with the ratio at \(\delta=0\) understood by continuous extension. The two displayed expressions are not individually nonnegative for all \(t\), but their maximum is the exact nonnegative operator bound. The unique minimizer \(t_*\approx1.7511007023760334\) is the positive root of
\[
t_*^3+2t_*^2-2t_*-8=0,\qquad q(t_*)\approx0.0663536698618376.
\]

The method never crosses the equilibrium, for *every* strictly positive initial state, precisely for
\[
0<t\le t_{\mathrm{no\text{-}cross}}=\frac{\sqrt{17}-1}{2}.
\]
Above this value there are strictly positive starts whose first update crosses the equilibrium; when \(t\ge2\), every non-equilibrium initial state crosses in each step. Exactly at \(t=2\),
\[
\delta^+=-\frac{\delta^3}{12-5\delta^2},\qquad
|\delta^+|\le\frac{|\delta|^3}{7},\qquad
\lim_{\delta\to0}\frac{\delta^+}{\delta^3}=-\frac1{12},
\]
so the equilibrium has exact cubic local convergence despite a nonzero sharp global contraction factor \(q(2)=1/7\).

## Assumptions and scope

Fix \(\kappa>0\), \(h>0\) and arbitrary \(y_1^0,y_2^0>0\). Consider the production--destruction system
\[
\frac{d}{ds}\binom{y_1}{y_2}=
\kappa\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\binom{y_1}{y_2}.
\]
Each step uses the original conservative-stage \(\operatorname{MPRK22}(1/2)\) scheme, not its nonconservative-stage variant, a multistep Patankar scheme, or a negative-Runge--Kutta-coefficient extension. With \(M=y_1+y_2>0\), put \(x=y_1/M\) and \(v=y_1^{(2)}/M\). Its stage and final linear solves reduce exactly to
\[
v=\frac{2x+t/2}{t+2},\qquad
u=\frac{x}{v},\qquad w=\frac{1-x}{1-v},\qquad
x^+=\frac{x+(t/2)w}{1+(t/2)(u+w)}.
\]
Here \(0<x,v<1\). The complementary new component is \(1-x^+\). At each step \(M\) is unchanged. Convergence is measured in the signed species difference \(\delta=2x-1\); its absolute value equals the normalized \(\ell_1\) distance to the equilibrium vector.

## Proof

**Exact update and positivity.** The underlying Runge--Kutta coefficients at \(\alpha=1/2\) satisfy \(b_1=0\), \(b_2=1\). The conservative Patankar stage solves \(y^{(2)}=(I-(h\kappa/2)B)^{-1}y\), where \(B=\bigl(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\bigr)\). In the final Patankar linear solve the denominator for component \(j\) is \((y_j^{(2)})^2/y_j\), so its rate coefficient is \(y_j/y_j^{(2)}\). Dividing by total mass produces the equations in the preceding section. Both \(u,w\) are strictly positive; the numerator of \(x^+\) is positive and the difference between its denominator and numerator is \((1-x)+(t/2)u>0\). Therefore \(0<x^+<1\) for every positive \(t\) and \(x\), while the paired flux equations conserve \(M\).

**Scalar error identity.** Substitute \(x=(1+\delta)/2\) and \(v=(1+\delta/(1+t/2))/2\) into the final fraction. Clearing the positive denominators gives the displayed rational multiplier \(m_t(D)\) with \(D=\delta^2\). Set
\[
K=t^3+5t^2+8t+4,\quad H=2t^2+4t+4.
\]
For \(0\le D\le1\), \(K-HD\ge K-H=t(t^2+3t+4)>0\). Direct differentiation yields
\[
\frac{\partial m_t}{\partial D}=-\frac{2t^3(t+1)(t+2)}{(K-HD)^2}<0.
\]
Its endpoints are therefore the exact extremal values:
\[
c(t):=m_t(0)=\frac{2-t}{2+t},\qquad
b(t):=m_t(1)=\frac{4-t-t^2}{t^2+3t+4},
\]
and
\[
c(t)-b(t)=\frac{2t^2}{(t+2)(t^2+3t+4)}>0.
\]
For all finite \(t>0\), \(-1<b(t)<c(t)<1\): the lower inequality follows from \(b(t)+1=(2t+8)/(t^2+3t+4)>0\); the upper from \(c(t)<1\). Hence \(\max_{D\in[0,1]}|m_t(D)|=\max\{c(t),-b(t)\}<1\), proving unconditional global geometric error contraction and convergence to \(y_1=y_2=M/2\). The bound is sharp as a supremum since values \(D\to0\) and \(D\to1^-\) can be approached by strictly positive states; at \(D=0\) the ratio is interpreted by continuity.

**Unique optimal step.** Both \(c(t)\) and \(b(t)\) strictly decrease, since
\[
c'(t)=-\frac4{(t+2)^2},\qquad
b'(t)=-\frac{2(t^2+8t+8)}{(t^2+3t+4)^2}.
\]
As \(t\) runs from zero to infinity, \(c(t)\) decreases from \(1\) to \(-1\) and \(-b(t)\) increases from \(-1\) to \(1\); their single crossing uniquely minimizes their maximum. Clearing denominators in \(c(t)=-b(t)\) gives \(t^3+2t^2-2t-8=0\); this crossing is its unique positive root. Exact rational signs at \(1751100/10^6\) and \(1751101/10^6\) isolate the root.

**Sharp sign boundary and cubic step.** Since \(m_t\) decreases in \(D\), a step is non-crossing for all strictly positive states if and only if \(b(t)\ge0\), which is equivalent to \(t^2+t-4\le0\). Above that root, values \(D<1\) close enough to \(1\) yield \(m_t(D)<0\) and a genuine crossing. For \(t\ge2\), \(c(t)\le0\) and strict monotonicity makes \(m_t(D)<0\) whenever \(D>0\). Substitution of \(t=2\) produces \(m_2(D)=-D/(12-5D)\), and \(12-5D\ge7\) establishes the global cubic inequality. The denominator tends to \(12\) as \(D\to0\), proving the exact cubic local coefficient.

## Verification

The accompanying standalone `verify.py` executes exact-rational stage/final solves and compares them to the closed error multiplier over a deterministic rational parameter grid. It also checks algebraic derivative difference identities, contraction inequalities, sign boundaries, the optimal-root bracket and cubic-step identity. Run with `python3 verify.py` from the directory containing this result and that file. The finite tests check the implementation and algebra at test points; the universally quantified statements follow from the preceding analytic proof, not enumeration.

## Relationship to prior work

Kopecz and Meister (arXiv:1702.04589v1, first public 2017-02-15) developed second-order modified Patankar--Runge--Kutta families and established their order, positivity and conservation; those are not claimed here. Izgin, Kopecz and Meister (arXiv:2202.01099v1, 2022) established local Lyapunov stability for MPRK22 and give the very same two-state exchange as a numerical example, but their general positive-two-way analysis does not provide this sharp global nonlinear contraction, its optimal step, or a universal non-overshoot boundary. Their one-way pure-decay case has a global result, but it does not imply the symmetric two-way theorem. Izgin, Kopecz, Meister and Schilling (arXiv:2309.01562v1, 2023) showed that some negative-coefficient MPRK schemes exhibit local but not global stability and discussed global stability with nonnegative coefficients as a conjectural phenomenon. The present theorem establishes a specific positive-coefficient symmetric test case and resolves a quantitative benchmark, not their entire conjecture.

## Limitations

The theorem concerns strictly positive initial states, exact arithmetic, a symmetric two-state conservative linear exchange and one specific positive-coefficient MPRK22 member. It neither proves the analogous result for unequal exchange rates, more components, other Patankar variants, or nonautonomous systems, nor guarantees floating-point robustness. A publication-priority risk remains for equivalent specialized analyses outside the material inspected; the result has not undergone independent audit.

## References

1. S. Kopecz and A. Meister, *On Order Conditions for modified Patankar-Runge-Kutta schemes*, arXiv:1702.04589v1 (2017), https://arxiv.org/abs/1702.04589.
2. T. Izgin, S. Kopecz and A. Meister, *On Lyapunov Stability of Positive and Conservative Time Integrators and Application to Second Order Modified Patankar--Runge--Kutta Schemes*, arXiv:2202.01099v1 (2022), https://arxiv.org/abs/2202.01099.
3. T. Izgin, S. Kopecz and A. Meister, *On the Stability of Unconditionally Positive and Linear Invariants Preserving Time Integration Schemes*, arXiv:2202.11649v1 (2022), https://arxiv.org/abs/2202.11649.
4. T. Izgin, S. Kopecz, A. Meister and A. Schilling, *On the non-global linear stability and spurious fixed points of MPRK schemes with negative RK parameters*, arXiv:2309.01562v1 (2023), https://arxiv.org/abs/2309.01562.
