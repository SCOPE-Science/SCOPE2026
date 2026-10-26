# A sharp mean-square stability island for fourth-order two-derivative Runge–Kutta under symmetric curvature perturbations

## Finding

The two-stage fourth-order two-derivative Runge–Kutta update of Gottlieb, Grant, and Herrera (their TDRK2s4p1e, equation (5.4)) has an **exact, bounded-away-from-zero interval of mean-square stable step sizes** on the planar harmonic oscillator if both second-derivative evaluations in one step share an independent, symmetric, multiplicative perturbation.

Put \(\vartheta=h\omega>0\), and let \(0\le\epsilon<1\) be the relative perturbation amplitude. Let \(s_c\) be the unique positive zero of
\[
1+2s-23s^2-12s^3=0,\qquad
s_c=0.239035648791400\ldots,
\]
so that \(\epsilon_c=\sqrt{s_c}=0.488912721036588\ldots\). For \(0<\epsilon<\epsilon_c\), define
\[
\vartheta_\pm^2=
\frac{4\bigl(1+7\epsilon^2\pm\sqrt{1+2\epsilon^2-23\epsilon^4-12\epsilon^6}\bigr)}{1+6\epsilon^2+\epsilon^4}.
\]
Then **the iterates converge to zero in mean square from every deterministic initial vector if and only if**
\[
\boxed{\vartheta_-<\vartheta<\vartheta_+.}
\]
If \(\epsilon=0\), this criterion becomes \(0<\vartheta<2\sqrt2\). At \(\epsilon=\epsilon_c\) there is exactly one positive neutral step \(\vartheta_c=2.071725470840522\ldots\) and no mean-square stable positive step; all other positive steps grow in mean-square energy. If \(\epsilon>\epsilon_c\), every positive step grows in mean-square energy. In particular, **arbitrarily small nonzero curvature perturbations destroy mean-square stability for all sufficiently small positive steps, even though intermediate steps remain stable**.

## Assumptions and scope

Fix real \(\omega>0\) and \(h>0\), and put
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad \dot u=\omega Ju,\qquad u_0\in\mathbb R^2.
\]
The exact first derivative is \(F(v)=\omega Jv\) and the exact second total derivative is \(G(v)=-\omega^2v\). At every integer step \(k\), independently draw \(\xi_k\in\{-1,1\}\) with equal probabilities and set \(q_k=1+\epsilon\xi_k\). The **same** \(q_k\) is reused for both evaluations of the second derivative *within* step \(k\); successive steps use independent draws. Define the perturbed curvature oracle \(G_{q_k}(v)=-q_k\omega^2v\) and the numerical step
\[
Y_k=u_k+\tfrac h2F(u_k)+\tfrac{h^2}{8}G_{q_k}(u_k),
\qquad
u_{k+1}=u_k+hF(u_k)+\tfrac{h^2}{6}\bigl(G_{q_k}(u_k)+2G_{q_k}(Y_k)\bigr).
\]
This is an explicitly specified *two-point, time-independent-law multiplicative curvature-perturbation model*. It is **not** asserted to reproduce actual floating-point rounding, independent errors between stage evaluations, or randomization of the time nodes. "Mean-square asymptotic stability" means \(\lim_{n\to\infty}\mathbb E\|u_n\|_2^2=0\) for every deterministic initial state; a unit expected squared-norm multiplier is neutral, not stable.

## Proof

**Step 1: exact pathwise multiplier.** Write \(z=h\lambda\) for a scalar test eigenvalue and \(G_q(v)=q\lambda^2v\). Substituting the stage equation into the endpoint equation gives
\[
R_q(z)=1+z+\frac q2z^2+\frac q6z^3+\frac{q^2}{24}z^4.
\]
For the oscillator, the one-step real matrix is \(a_qI+b_qJ\), where, with \(\vartheta=h\omega\),
\[
a_q=1-\frac q2\vartheta^2+\frac{q^2}{24}\vartheta^4,
\qquad
b_q=\vartheta\left(1-\frac q6\vartheta^2\right).
\]
Because \(J^\mathsf TJ=I\) and \(J^\mathsf T=-J\), the update satisfies, *pathwise for every input vector*,
\[
\|u_{k+1}\|_2^2=(a_{q_k}^2+b_{q_k}^2)\|u_k\|_2^2.
\]
Independence across steps therefore yields the exact identity
\[
\mathbb E\|u_n\|_2^2=m_\epsilon(\vartheta)^n\|u_0\|_2^2,
\qquad
m_\epsilon(\vartheta)=\tfrac12\sum_{\xi=\pm1}\bigl(a_{1+\epsilon\xi}^2+b_{1+\epsilon\xi}^2\bigr).
\]
No appeal to finite-time experiments is needed for the all-iteration identity.

**Step 2: polynomial sign.** Expanding a single multiplier in \(x=\vartheta^2\),
\[
a_q^2+b_q^2-1=(1-q)x+\frac{q(q-1)}3x^2+\frac{q^2(2-3q)}{72}x^3+\frac{q^4}{576}x^4.
\]
Taking the equally weighted average at \(q=1\pm\epsilon\) (and writing \(s=\epsilon^2\)) cancels the linear term and gives
\[
\boxed{m_\epsilon(\vartheta)-1
=\frac{x^2}{576}\bigl[(1+6s+s^2)x^2-(8+56s)x+192s\bigr].}
\]
For \(x>0\), strict mean-square stability is equivalent to negativity of the displayed quadratic, denoted \(Q_s(x)\).

**Step 3: sharp global classification.** Its leading coefficient \(A_s=1+6s+s^2\) is positive. Its discriminant is
\[
(8+56s)^2-4(1+6s+s^2)\,192s
=64(1+2s-23s^2-12s^3)=64f(s).
\]
The cubic \(12s^3+23s^2-2s-1\) has exactly one positive root by Descartes' rule of signs (and existence by continuity). Thus \(f\) is positive on \([0,s_c)\), zero at \(s_c\), and negative above it. For \(0<s<s_c\), the quadratic has two distinct strictly positive roots because their sum \((8+56s)/A_s\) and product \(192s/A_s\) are both positive. The quadratic is strictly negative exactly between those roots, which equal the squares of \(\vartheta_-\) and \(\vartheta_+\) stated above. For \(s=s_c\), its single minimum touches zero at
\[
x_c=\frac{4(1+7s_c)}{1+6s_c+s_c^2};
\]
thus \(m=1\) there and \(m>1\) at all other positive steps. For \(s>s_c\), \(Q_s\) is strictly positive for every real \(x\), giving universal mean-square growth. For \(s=0\), \(Q_0(x)=x(x-8)\), so the stable interval is precisely \(0<\vartheta<2\sqrt2\).

**Step 4: the small-step paradox and sharp asymptotics.** For every fixed \(\epsilon>0\), the leading contribution is
\[
m_\epsilon(\vartheta)-1=\frac{\epsilon^2}{3}\vartheta^4+O(\vartheta^6),
\qquad\vartheta\downarrow0,
\]
which is strictly positive at sufficiently small positive step sizes. For \(\epsilon\downarrow0\), Vieta's formulas give
\[
\vartheta_-(\epsilon)=2\sqrt6\,\epsilon+O(\epsilon^3),
\qquad
\vartheta_+(\epsilon)=2\sqrt2\,(1-\epsilon^2+O(\epsilon^4)).
\]
These expansions demonstrate why the stable band is separated from zero as soon as the curvature error is nonzero.

As an exact-rational illustration at \(\epsilon=1/5\), \(m_\epsilon(\vartheta)-1\) takes the values \(6497/11520000>0\) at \(\vartheta=1/2\), \(-103/45000<0\) at \(\vartheta=1\), \(-2096/5625<0\) at \(\vartheta=2\), and \(11313/5000>0\) at \(\vartheta=3\). This gives loss–gain–loss of mean-square stability as a single step length increases.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only Python's standard library, direct \(2\times2\) matrix updates and exact rational arithmetic. Running \(\texttt{python3 verify.py}\) returned \(\texttt{VERIFY_OK 10007}\); checks include 6,171 rational coefficient/sign cases, 2,520 real-matrix versus complex-amplifier comparisons, and finite-path enumeration up to eight independent draws. It also checks numerical values of the coalescence threshold. These checks support the algebra and reproducibility; **they are not substituted for the all-parameter, all-iteration proof above**.

## Relationship to prior work

Gottlieb, Grant, and Herrera [1] introduced a mixed-precision framework for two-derivative Runge–Kutta methods, including exactly the two-stage fourth-order update (their equation (5.4)). Their section 5.2 and Figure 3 analyze perturbation order and display numerically perturbed deterministic linear-stability regions. Those finite-time/pointwise stability results do not determine the expectation of a product of independent, stepwise random energy multipliers under the correlated two-evaluation perturbation law specified here. The present theorem gives an exact moment-based phase diagram and a sharp noise-amplitude threshold for that law.

Bochacik, Goćwin, Morkisz, and Przybyłowicz [2] studied randomized first-derivative Runge–Kutta algorithms, explicitly distinguishing mean-square, almost-sure, and in-probability stability regions. Their randomized stage-point method is not the fourth-order two-derivative scheme, and its scalar amplification law is not the polynomial \(R_q\) proved here. Bochacik and Przybyłowicz [3] studied a randomized implicit two-stage method, likewise distinct from the shared-curvature model. The standard classical fourth-order stability interval appears as the \(\epsilon=0\) limit of the theorem; it does not imply the nonzero-noise classification.

## Limitations

The theorem concerns only a linear planar skew-rotation, one specific explicit two-derivative scheme, one shared symmetric multiplicative perturbation per step, and **mean-square energy**. The values of \(\epsilon\) are relative oracle errors, not calibrated machine precisions. Stagewise-independent errors, nonzero-mean errors, state-dependent rounding, general matrices, nonlinear dynamics, almost-sure stability, and finite-horizon accuracy may exhibit different thresholds. The published figures in [1] motivate the question, but this analysis does not reinterpret their plotted data as a stochastic ensemble or claim a result for actual hardware. Although targeted published-literature comparisons did not identify an exact equivalent of the threshold, historical priority has not been independently established.

## References

[1] S. Gottlieb, Z. J. Grant, and C. Herrera, *Mixed Precision and Mixed Accuracy Explicit Two-Derivative Runge–Kutta Methods*, arXiv:2602.14369v1, publicly posted 2026-02-16; especially equation (5.4), section 5.2 and Figure 3. https://arxiv.org/html/2602.14369v1

[2] T. Bochacik, M. Goćwin, P. M. Morkisz, and P. Przybyłowicz, *Randomized Runge–Kutta method — stability and convergence under inexact information*, arXiv:2006.12131, first posted 2020-06-22; especially section 5. https://arxiv.org/abs/2006.12131

[3] T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059, first posted 2024-04-29. https://arxiv.org/abs/2404.19059
