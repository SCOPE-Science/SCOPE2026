# AdaLoss has an exact target-error phase transition on strongly convex quadratics
## Finding

The loss-value accumulator of AdaLoss has two qualitatively different asymptotic regimes, distinguished solely by whether its supplied target equals the attained minimum. A fixed nonzero target error changes geometric convergence into a sharp stretched-exponential law with an explicit power prefactor, even though the gradient field and Hessian remain unchanged.

Let
\[
F(x)=\ell_\star+\frac12 x^\top Hx,\qquad H=H^\top\succ0,\quad \ell_\star>0,
\]
with \(x\in\mathbb R^d\), and let \(L=\lambda_{\max}(H)\). Fix
\[
\eta>0,\quad \alpha>0,\quad c>0,\quad b_0>\eta L,\quad x_0\ne0.
\]
The deterministic one-sample specialization of Algorithm 1 in the defining AdaLoss paper is
\[
\boxed{\begin{aligned}
b_{t+1}^2&=b_t^2+\alpha|F(x_t)-c|,\\
x_{t+1}&=x_t-\frac{\eta}{b_{t+1}}Hx_t,
\end{aligned}}\qquad t=0,1,2,\ldots.
\]
Here \(c\) is the proposed surrogate for the optimum loss value.

**Exact target.** If \(c=\ell_\star\), the accumulator converges to a finite \(b_\infty>\eta L\). For every eigenvalue \(\lambda\) whose eigenspace is present in the initial error, the corresponding nonzero spectral component converges geometrically with ratio
\[
\boxed{q_\lambda=1-\frac{\eta\lambda}{b_\infty}\in(0,1).}
\]
More precisely, for each active coordinate \(z_{i,t}\) in an orthonormal Hessian eigenbasis, there is a nonzero constant \(C_i\) such that
\[
z_{i,t}=C_i q_{\lambda_i}^t(1+o(1)).
\]
Thus the objective gap has a geometric asymptotic rate.

**Fixed target error.** Suppose \(c\ne\ell_\star\), and write
\[
\delta=|\ell_\star-c|>0,\qquad D=\alpha\delta.
\]
If \(c<\ell_\star\), impose no additional restriction on \(x_0\). If \(c>\ell_\star\), assume the natural below-target basin condition
\[
\frac12 x_0^\top Hx_0<c-\ell_\star.
\]
Then there is a finite real constant \(B\), depending on the trajectory, such that
\[
\boxed{b_t^2=Dt+B+o(1).}
\]
For every active eigenvalue \(\lambda_i\) and nonzero initial eigencoordinate \(z_{i,0}\), a nonzero constant \(K_i\) (with the same sign as \(z_{i,0}\)) exists for which
\[
\boxed{
 z_{i,t}
 =K_i\,t^{-\frac{\eta^2\lambda_i^2}{2D}}
 \exp\!\left(-\frac{2\eta\lambda_i}{\sqrt D}\sqrt t\right)
 (1+o(1)).
}
\]
In particular, for every active component,
\[
\frac{z_{i,t+1}}{z_{i,t}}\longrightarrow1,
\]
so the convergence is *not* geometric, although the iterates still converge to the unique minimizer.

Let \(\lambda_\star\) denote the smallest Hessian eigenvalue represented in \(x_0\), and let \(I_\star\) be its active eigencoordinates. The objective gap obeys the exact sharp asymptotic
\[
\boxed{
 F(x_t)-\ell_\star
 =C_\star\,t^{-\frac{\eta^2\lambda_\star^2}{D}}
 \exp\!\left(-\frac{4\eta\lambda_\star}{\sqrt D}\sqrt t\right)
 (1+o(1)),
}
\]
where
\[
C_\star=\frac{\lambda_\star}{2}\sum_{i\in I_\star}K_i^2>0.
\]
Thus any fixed nonzero target offset causes a genuine transition from exponential-in-iteration to stretched-exponential-in-square-root-iteration decay. The leading square-root exponent and logarithmic power correction are explicit in curvature and target error, not unspecified rate constants.

The result is invariant under adding the same constant to both objective and target; shifting the objective value without adjusting \(c\) can change the convergence class even though the gradients are identical.

## Assumptions and scope

The update is the loss-value accumulator printed in AdaLoss Algorithm 1, specialized to a single deterministic sample. The objective is a finite-dimensional strongly convex quadratic with a positive baseline; the baseline and chosen target are positive, so the source's positive-target convention is respected.

The condition \(b_0>\eta L\) is a transparent sufficient condition that keeps every modal multiplier strictly inside \((0,1)\). It is not asserted necessary. It avoids transient sign flips and exact annihilation of eigencomponents, allowing a sharp nonzero asymptotic prefactor for every active mode.

An underestimated target \(c<\ell_\star\) is covered for every nonzero initialization. For an overestimated target \(c>\ell_\star\), the sublevel-basin restriction makes the sign of the absolute-value accumulator constant along the whole trajectory. No statement is made about overestimated targets outside that basin.

For a repeated eigenvalue, an arbitrary orthonormal eigenbasis may be chosen; the formula applies to all coordinates with nonzero initial projection. Equivalently, the entire spectral projection onto a given eigenspace is multiplied by the same scalar factor.

These are deterministic statements for a fixed Hessian, not stochastic finite-sum convergence assertions or claims about nonquadratic objectives.

## Proof

Choose an orthonormal eigendecomposition
\[
H=U\operatorname{diag}(\lambda_1,\ldots,\lambda_d)U^\top,
\qquad0<\lambda_i\le L,
\]
and write \(z_t=U^\top x_t\). Put
\[
a_i=\eta\lambda_i,\qquad
G_t=F(x_t)-\ell_\star=\frac12\sum_i\lambda_i z_{i,t}^2.
\]
The update is exactly
\[
 z_{i,t+1}=\left(1-\frac{a_i}{b_{t+1}}\right)z_{i,t},
\qquad b_{t+1}^2=b_t^2+\alpha|\ell_\star-c+G_t|.
\]
Because the squared accumulator is nondecreasing,
\[
b_t\ge b_0>\eta L\ge a_i,
\]
so each multiplier lies strictly between zero and one. Therefore each nonzero eigencoordinate preserves its sign and decreases in magnitude, and \(G_t\) is strictly decreasing to a nonnegative limit.

First establish a uniform summability lemma. Since \(G_t\le G_0\), irrespective of the choice of target,
\[
 b_t^2\le b_0^2+\alpha\bigl(|\ell_\star-c|+G_0\bigr)t.
\]
Thus, for a constant \(M>0\),
\[
 b_t\le M\sqrt{t+1}.
\]
The modal product and \(\log(1-v)\le-v\) for \(0<v<1\) yield
\[
 |z_{i,t}|
 \le |z_{i,0}|\exp\!\left(-a_i\sum_{k=1}^t\frac1{b_k}\right)
 \le C_i'\exp(-c_i\sqrt t)
\]
for suitable positive constants \(C_i'\) and \(c_i\), because
\[
 \sum_{k=1}^t b_k^{-1}\ge M^{-1}\sum_{k=1}^t k^{-1/2}
 =\frac2M\sqrt t+O(1).
\]
Consequently,
\[
\boxed{\sum_{t=0}^\infty G_t<\infty.}
\]
In particular all eigencoordinates tend to zero and \(G_t\to0\).

For the exact target \(c=\ell_\star\), the accumulator identity is
\[
 b_t^2=b_0^2+\alpha\sum_{j=0}^{t-1}G_j,
\]
so \(b_t\uparrow b_\infty<\infty\). Each active modal multiplier tends to
\[
 q_i=1-\frac{a_i}{b_\infty}\in(0,1).
\]
There is actually a full asymptotic prefactor, not merely a limiting ratio. The bound
\[
 0<1-\frac{a_i}{b_{t+1}}
 \le1-\frac{\eta\lambda_{\min}}{b_\infty}=:q_{\max}<1
\]
shows \(G_t=O(q_{\max}^{2t})\). Hence
\[
 0\le b_\infty-b_t
 \le\frac{\alpha}{b_\infty}\sum_{j=t}^\infty G_j
 =O(q_{\max}^{2t}),
\]
so the differences between each modal multiplier and its limiting \(q_i\) are absolutely summable. The product of their positive ratios therefore converges to a finite, strictly positive constant, giving the displayed \(C_i q_i^t(1+o(1))\) law.

Now assume a nonzero target error. Let
\[
 \delta=|\ell_\star-c|,
 \qquad s=\operatorname{sign}(\ell_\star-c)\in\{-1,1\}.
\]
For an underestimated target the absolute-value sign is positive for every iterate. For an overestimated target, the initial assumption \(G_0<\delta\), together with monotonic decrease of \(G_t\), keeps the sign negative for every iterate. Both cases thus satisfy the **exact** identity
\[
 b_{t+1}^2=b_t^2+\alpha\delta+\alpha sG_t.
\]
Summing and applying the proved summability gives
\[
 b_t^2
 =\alpha\delta t+
 \underbrace{\left(b_0^2+\alpha s\sum_{j=0}^\infty G_j\right)}_{B}
 -\alpha s\sum_{j=t}^\infty G_j
 =Dt+B+o(1).
\]
Since \(D>0\), the asymptotics of the inverse accumulator are
\[
 \frac1{b_k}=\frac1{\sqrt D}\,k^{-1/2}+O(k^{-3/2}),
 \qquad
 \frac1{b_k^2}=\frac1D\,k^{-1}+O(k^{-2}).
\]
(The preceding stretched-exponential bound makes the remainder in the squared accumulator much smaller than any negative power.) Therefore both centered partial sums converge:
\[
 \sum_{k=1}^t\frac1{b_k}-\frac2{\sqrt D}\sqrt t\longrightarrow A_1\in\mathbb R,
\]
\[
 \sum_{k=1}^t\frac1{b_k^2}-\frac1D\log t\longrightarrow A_2\in\mathbb R.
\]
Also, \(\sum_k b_k^{-3}<\infty\).

For every active eigencoordinate,
\[
 \log\left|\frac{z_{i,t}}{z_{i,0}}\right|
 =\sum_{k=1}^t\log\left(1-\frac{a_i}{b_k}\right).
\]
The expansion
\[
 \log(1-v)=-v-\frac{v^2}{2}+O(v^3)
\]
can be applied uniformly in the tail because \(b_k\to\infty\). Its cubic remainder is summable. Thus for a finite real constant \(A_i\),
\[
 \log|z_{i,t}|
 =-\frac{2a_i}{\sqrt D}\sqrt t
 -\frac{a_i^2}{2D}\log t+A_i+o(1).
\]
Exponentiation proves the sharp modal law with
\[
 K_i=\operatorname{sign}(z_{i,0})e^{A_i}\ne0.
\]
The one-step modal ratio tends to one because the accumulator diverges.

Finally, among finitely many active modes, those with the smallest eigenvalue \(\lambda_\star\) dominate all larger-curvature components by an exponentially separated \(\sqrt t\)-scale. Substituting the modal asymptotics into
\[
 G_t=\frac12\sum_i\lambda_i z_{i,t}^2
\]
proves the asserted objective-gap asymptotic and its strictly positive coefficient.

## Verification

The standalone `verify.py` reconstructs the scalar accumulator and all Hessian eigenmodes from the source update, including both signs of a positive target mismatch and the correctly specified target. The checker compares direct vector-coordinate recurrences with the formula in an orthonormal eigenbasis, the exact accumulated-error identity, the numerical matched asymptotic after removing both the square-root exponential and logarithmic correction, and the geometric ratio in the exact-target case.

These finite computations guard against transcription errors only. The all-iteration theorem follows from the analytic product and summability arguments above.

## Relationship to prior work

Wu, Xie, Du, and Ward introduce AdaLoss and its accumulation of \(|F(x_t)-c|\), with \(c\) explicitly serving as a surrogate optimum loss. Their linear-regression analysis specializes the accumulator to the correctly centered squared regression residual, and its geometric convergence argument uses a bounded final accumulator. Neither the source algorithm nor its relevant convergence statements supplies a sharp regime for a persistent mismatch between \(c\) and the attained optimal loss.

Xie, Wu, and Ward establish geometric convergence for AdaGrad-Norm under suitable curvature/interpolation assumptions. That method accumulates squared gradient norms, which vanish at an optimum independently of additive shifts in objective value. Its theorem therefore does not imply the present loss-baseline transition.

Loizou, Vaswani, Laradji, and Lacoste-Julien use function optimum values in a stochastic Polyak step-size. Their step size divides the current function gap by the squared gradient norm rather than accumulating absolute loss discrepancies. The optimum-value dependence is a shared motivation, but its mathematical recurrence does not dominate this AdaLoss-specific asymptotic classification.

Generic diminishing-step gradient-descent theory predicts a leading stretched exponential when the stepsize is externally specified as a multiple of the inverse square root of iteration. Here the law of the stepsize is endogenous. The proof derives its exact drift from the discrepancy in the source loss accumulator and establishes the second-order logarithmic power correction and mode-by-mode constants. These quantitative conclusions are not supplied by the inspected source results.

## Limitations

The theorem assumes a stationary finite-dimensional SPD quadratic and an initial scale large enough that no modal sign reversal occurs. The overestimated-target side is restricted to the below-target basin. It does not claim that every initialization has the stated simple asymptotic.

The constants \(B\), \(K_i\), and \(C_i\) depend on the trajectory, while the displayed leading exponents are explicit. No closed elementary expression for those trajectory constants is claimed.

The source's linear convergence guarantee is not contradicted: its regression analysis uses the correctly centered residual. The finding concerns the effect of target misspecification, a different assumption explicitly separated from that guarantee.

## References

1. Xiaoxia Wu, Yuege Xie, Simon Shaolei Du, and Rachel Ward, “AdaLoss: A Computationally-Efficient and Provably Convergent Adaptive Gradient Method,” arXiv:2109.08282v1, first publicly submitted 2021-09-17; AAAI 2022, DOI:10.1609/aaai.v36i8.20848.
2. Yuege Xie, Xiaoxia Wu, and Rachel Ward, “Linear Convergence of Adaptive Stochastic Gradient Descent,” AISTATS 2020, PMLR 108, pp. 1475–1485.
3. Nicolas Loizou, Sharan Vaswani, Issam Hadj Laradji, and Simon Lacoste-Julien, “Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence,” AISTATS 2021, PMLR 130, pp. 1306–1314.
