# Exact first-moment stability frontier for two-client scalar SPAM
## Finding

Consider exact SPAM with a constant refresh probability \(p\in(0,1]\) and proximal stepsize \(\gamma>0\) on iid equiprobable scalar clients
\[
f_\pm(x)=\frac12(a\pm\delta)x^2,\qquad a>0,\qquad 0\le\delta\le a.
\]
Write \(q=1-p\), \(\rho=\delta/a\), and \(t=\gamma a\). For the first-moment state \(z_k=(x_k,x_{k-1},g_{k-1})^\top\), the deterministic mean transition matrix is Schur stable if and only if
\[
(2-p)\rho^2t^2<(1+t)^2.
\]
Thus, if \(\rho\sqrt{2-p}\le 1\), the first-moment state is stable for every \(t>0\). If \(\rho\sqrt{2-p}>1\), the exact stability interval is
\[
0<t<\frac{1}{\rho\sqrt{2-p}-1}.
\]
At maximal heterogeneity \(\rho=1\) and \(t=20\), this becomes \(p>0.8975\). Hence \(p=0.9\) is just inside the first-moment stable region, whereas \(p=0.1\) is far outside it.

## Assumptions and scope

The client index at step \(k\) is independent of the past and selects \(h_k=a-\delta\) or \(h_k=a+\delta\) with probability \(1/2\) each. The losses have a common minimizer at \(0\), and the proximal subproblem is solved exactly.

The SPAM recursion specialized to a scalar quadratic with current curvature \(h_k\) is
\[
g_k=h_kx_k+q\bigl(g_{k-1}-h_kx_{k-1}\bigr),
\]
\[
x_{k+1}=\operatorname{prox}_{\gamma f_{h_k}}
\bigl(x_k+\gamma(h_kx_k-g_k)\bigr)
=x_k-\frac{\gamma}{1+\gamma h_k}g_k.
\]
The result is an exact statement about Schur stability of the linear recursion for \(\mathbb E[z_k]\). It is not a claim about second moments, expected squared gradients, almost-sure convergence, or individual sample paths.

## Proof

For a realized curvature \(h\), let
\[
r_h=\frac{1}{1+\gamma h}.
\]
Then
\[
z_{k+1}=A_hz_k,\qquad
A_h=
\begin{pmatrix}
r_h & \gamma q h r_h & -\gamma q r_h\\
1&0&0\\
h&-qh&q
\end{pmatrix}.
\]
Because \(h_k\) is independent of \(z_k\),
\[
\mathbb E[z_{k+1}]=M\,\mathbb E[z_k],
\qquad
M=\mathbb E[A_h].
\]
Set
\[
\alpha=\mathbb E[r_h]
=\frac{1+t}{(1+t)^2-\rho^2t^2},
\qquad
D=(1+t)^2-\rho^2t^2.
\]
Using \(\mathbb E[\gamma h r_h]=1-\alpha\) and \(\mathbb E[h]=a\),
\[
M=
\begin{pmatrix}
\alpha&q(1-\alpha)&-q\gamma\alpha\\
1&0&0\\
a&-qa&q
\end{pmatrix}.
\]
A direct determinant calculation gives the factorization
\[
\det(\lambda I-M)
=(\lambda-q)
\left(
\lambda^2-\alpha\lambda+
\frac{q\rho^2t^2}{D}
\right).
\]
The root \(q=1-p\) lies strictly inside the unit disk for \(p\in(0,1]\). Put
\[
c=\frac{q\rho^2t^2}{D}.
\]
Since \(0\le\rho\le1\) and \(t>0\), one has \(D>0\). The Jury conditions for the monic quadratic \(\lambda^2-\alpha\lambda+c\) are
\[
1-\alpha+c>0,\qquad
1+\alpha+c>0,\qquad
1-c>0.
\]
The second is immediate, while
\[
1-\alpha+c
=\frac{t+t^2(1-p\rho^2)}{D}>0.
\]
Therefore Schur stability is equivalent to \(c<1\), namely
\[
q\rho^2t^2<D.
\]
Substituting \(D=(1+t)^2-\rho^2t^2\) yields
\[
(2-p)\rho^2t^2<(1+t)^2.
\]
All quantities are nonnegative, so this is equivalent to
\[
\rho\sqrt{2-p}\,t<1+t.
\]
If \(\rho\sqrt{2-p}\le1\), the inequality holds for every \(t>0\). Otherwise it is exactly
\[
t<\frac{1}{\rho\sqrt{2-p}-1}.
\]
For \(\rho=1\) and \(t=20\), squaring the positive inequality gives
\[
p>2-\left(1+\frac1{20}\right)^2=0.8975.
\]
At equality the quadratic factor reaches the unit-circle boundary, so strict Schur stability is lost.

## Verification

The accompanying `verify.py` reconstructs the averaged \(3\times3\) transition matrix directly from the two realized client matrices. It checks, over a grid of admissible parameters, that the matrix characteristic polynomial equals
\[
(\lambda-q)\left(\lambda^2-\alpha\lambda+c\right)
\]
to floating-point tolerance and that direct quadratic-root tests agree with the closed-form Schur inequality. It also verifies the \(t=20\) classifications \(p=0.9\) stable and \(p=0.1\) unstable.

The symbolic determinant was independently reconstructed from the displayed matrix before acceptance; no finite experiment is being used as a substitute for the algebraic proof.

## Relationship to prior work

Karagulyan, Shulgin, Sadiev, and Richtárik introduce SPAM and prove a general nonconvex convergence theorem under Hessian similarity. Their constant-parameter theorem gives a sufficient stepsize restriction
\[
\gamma^2\le
\min\left\{\frac{1}{16\delta^2},
\frac{p}{96\delta^2(1-p)}\right\}.
\]
They also report that, with exact proximal solves and a large displayed choice \(\gamma=20/\delta\), increasing \(p\) from \(0.1\) to \(0.9\) changes the observed behavior from unstable to steady. The present scalar calculation explains a corresponding refresh-probability phase transition at the level of first moments, but it does not strengthen their theorem because their theorem controls a substantially stronger and more general convergence quantity.

Kim, Toulis, and Kyrillidis analyze a stochastic proximal point method with direct Polyak momentum on the iterate. Loizou and Richtárik likewise study momentum added to stochastic gradient, Newton, proximal-point, and subspace-descent recursions, including a sketch-and-project quadratic setting. Those updates are structurally different from SPAM's momentum-variance-reduced gradient estimator followed by the shifted client proximal map. Inspection of these sources did not reveal the mean transition matrix or stability boundary derived here.

## Limitations

The result is deliberately narrow. It uses two scalar, equiprobable, common-minimizer quadratics and exact client proximal steps. Schur stability of \(\mathbb E[z_k]\) can coexist with poor or unstable higher moments, so this boundary must not be read as a guarantee of mean-square or sample-path convergence. Unequal client probabilities, different client minimizers, vector Hessians, inexact proximal solves, and nonquadratic losses require separate analysis.

The \(p=0.9\) versus \(p=0.1\) comparison mirrors a qualitative switch reported in the source paper but is not a proof about that paper's high-dimensional synthetic experiment.

## References

1. V. Karagulyan, E. Shulgin, A. Sadiev, and P. Richtárik, *SPAM: Stochastic Proximal Point Method with Momentum Variance Reduction for Non-convex Cross-Device Federated Learning*, arXiv:2405.20127v1, first posted 2024-05-30.
2. K. Kim, P. Toulis, and A. Kyrillidis, *Convergence and Stability of the Stochastic Proximal Point Algorithm with Momentum*, Proceedings of AISTATS 2022, PMLR 168.
3. N. Loizou and P. Richtárik, *Momentum and Stochastic Momentum for Stochastic Gradient, Newton, Proximal Point and Subspace Descent Methods*, arXiv:1712.09677.
