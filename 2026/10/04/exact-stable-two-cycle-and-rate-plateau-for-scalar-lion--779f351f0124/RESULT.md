# Exact stable two-cycle and rate plateau for scalar Lion
## Finding

Consider deterministic Lion on
\[
f(x)=\frac{a}{2}x^2,\qquad a>0,
\]
with
\[
u_t=\beta_1m_{t-1}+(1-\beta_1)a x_t,
\]
\[
m_t=\beta_2m_{t-1}+(1-\beta_2)a x_t,
\]
\[
x_{t+1}=(1-\eta\lambda)x_t-\eta\,\operatorname{sign}(u_t),
\]
where \(\eta,\lambda>0\), \(\beta_1,\beta_2\in[0,1)\), and \(\operatorname{sign}(0)=0\). Put
\[
q=\eta\lambda,\qquad \Delta=1+\beta_2-2\beta_1.
\]

For
\[
0<q<2,
\]
a nonzero period-two orbit exists if and only if
\[
\Delta>0.
\]
It is unique up to phase and is
\[
x_t=(-1)^t c,\qquad c=\frac{\eta}{2-q},
\]
with momentum amplitude
\[
m_t=(-1)^tM,\qquad
M=\frac{1-\beta_2}{1+\beta_2}\,a c.
\]

The orbit is locally exponentially stable. Its exact local one-step state factor is
\[
r_{\mathrm{loc}}=\max\{|1-q|,\beta_2\}.
\]
Hence the minimum local factor at fixed \(\beta_2\) is exactly \(\beta_2\), attained throughout
\[
1-\beta_2\le q\le1+\beta_2.
\]

The cycle satisfies the nominal Lion bound
\[
|x|\le\frac1\lambda
\]
if and only if
\[
q\le1.
\]
Thus for \(1<q<2\) the cycle is locally stable but lies outside that bound.

For the default Lion coefficients \(\beta_1=0.9\) and \(\beta_2=0.99\),
\[
\Delta=0.19>0,
\]
so this stable cycle exists for every \(0<\eta\lambda<2\).

## Assumptions and scope

The objective is a deterministic one-dimensional positive quadratic. The learning rate and decoupled weight decay are constant. The update ordering is the original Lion ordering: the sign readout mixes the current gradient with the previously stored momentum using \(\beta_1\), while the stored momentum is updated using \(\beta_2\).

This is a constant-step local dynamical result. It does not establish global attraction, stochastic convergence, or behavior for multidimensional or nonquadratic objectives. The singular boundaries \(q=2\) and \(\Delta=0\) are excluded from the nondegenerate classification.

## Proof

Write
\[
r=1-q.
\]
Let a nontrivial period-two orbit have consecutive states
\[
(x_+,m_-)\mapsto(x_-,m_+)\mapsto(x_+,m_-),
\]
with sign readouts \(\sigma_+\) and \(\sigma_-\). The position equations are
\[
x_-=r x_+-\eta\sigma_+,\qquad
x_+=r x_- -\eta\sigma_-.
\]

If \(\sigma_+=\sigma_-\), subtraction gives
\[
(1+r)(x_--x_+)=0.
\]
Since \(q\ne2\), \(1+r\ne0\), so the orbit would be trivial. Thus
\[
\sigma_-=-\sigma_+.
\]
Adding the two position equations and using \(q=1-r>0\) gives
\[
x_-=-x_+.
\]

The momentum equations then imply
\[
m_+=-m_-.
\]
Set \(x_+=c>0\), \(x_-=-c\), \(m_+=M\), \(m_-=-M\). Solving the momentum equation yields
\[
M=\frac{1-\beta_2}{1+\beta_2}\,a c.
\]
The positive-phase sign input is
\[
u_+=-\beta_1M+(1-\beta_1)a c
=\frac{a c}{1+\beta_2}\left(1+\beta_2-2\beta_1\right)
=\frac{a c}{1+\beta_2}\Delta.
\]
Therefore \(\sigma_+=\operatorname{sign}(\Delta)\). The position equation becomes
\[
(2-q)c=\eta\,\operatorname{sign}(\Delta).
\]
For \(0<q<2\), a positive \(c\) exists exactly when \(\Delta>0\), and then
\[
c=\frac{\eta}{2-q}.
\]
This also proves uniqueness up to phase.

When \(\Delta>0\), the sign input on the cycle has the strict margin
\[
\mu=\frac{a c\Delta}{1+\beta_2}>0.
\]
Hence a small enough perturbation preserves the alternating sign itinerary. On that neighborhood the one-step Jacobian in state \((x_t,m_{t-1})\) is
\[
J=
\begin{bmatrix}
1-q&0\\
(1-\beta_2)a&\beta_2
\end{bmatrix}.
\]
Its eigenvalues are \(1-q\) and \(\beta_2\), so the exact local one-step factor is
\[
\max\{|1-q|,\beta_2\}<1.
\]
The rate plateau follows from \(|1-q|\le\beta_2\).

Finally,
\[
\lambda c=\frac{q}{2-q},
\]
so \(c\le1/\lambda\) exactly when \(q\le1\).

## Verification

The accompanying `verify.py` checks exact rational instances of the two-cycle, random floating-point cases with \(\Delta>0\), the sign margin, the Jacobian factor, the rate plateau, and the exact crossing of the nominal bound at \(q=1\). It also performs bounded grid checks in representative \(\Delta<0\) cases.

Those finite checks are only algebra and transcription guards. The exhaustive period-two classification and stability statement are proved above.

## Relationship to prior work

The original Lion paper defines the two interpolation coefficients, sign readout, and decoupled weight decay, and explains the distinct roles of \(\beta_1\) and \(\beta_2\). The older Signum method also signs momentum but uses a different update rule.

A later Lion theory paper gives continuous- and discrete-time Lyapunov interpretations and connects weight decay with a bound-constrained problem. Its accessible primary abstract is highly relevant, but a complete full-text theorem comparison was unavailable during this review; this is the main originality risk.

The sign-training literature develops convergence-rate guarantees under smoothness or weak-smoothness assumptions. The inspected sources did not state the present constant-step scalar period-two criterion, closed-form amplitude, local rate plateau, or the exact \(q=1\) bound crossing.

## Limitations

The theorem is one-dimensional and deterministic. It does not cover stochastic gradients, minibatching, multidimensional coupling, nonquadratic objectives, or time-varying hyperparameters.

Local stability does not imply global attraction from arbitrary initial conditions.

The singular boundaries \(q=2\) and \(\Delta=0\) are not classified here.

A residual originality risk remains because the complete text of one directly relevant Lion Lyapunov paper could not be inspected.

## References

1. Jeremy Bernstein, Yu-Xiang Wang, Kamyar Azizzadenesheli, and Anima Anandkumar, “signSGD: Compressed Optimisation for Non-Convex Problems,” arXiv:1802.04434v1, 2018.
2. Xiangning Chen et al., “Symbolic Discovery of Optimization Algorithms,” arXiv:2302.06675v1, 2023.
3. Lizhang Chen, Bo Liu, Kaizhao Liang, and Qiang Liu, “Lion Secretly Solves Constrained Optimization: As Lyapunov Predicts,” arXiv:2310.05898v1, 2023.
4. Tao Sun, Congliang Chen, Peng Qiao, Li Shen, Xinwang Liu, and Dongsheng Li, “Rethinking SIGN Training: Provable Nonconvex Acceleration without First- and Second-Order Gradient Lipschitz,” arXiv:2310.14616v1, 2023.
