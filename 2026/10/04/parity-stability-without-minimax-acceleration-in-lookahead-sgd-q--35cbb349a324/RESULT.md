# Parity stability without minimax acceleration in Lookahead-SGD quadratics
## Finding

Let
\[
f(x)=\frac12 x^{\mathsf T}Hx,
\]
where \(H\) is symmetric positive definite and
\[
0<\mu I\preceq H\preceq L I,\qquad \mu<L.
\]
Consider deterministic Lookahead whose inner optimizer is plain gradient descent. At the beginning of an outer cycle the fast weights equal the slow weights \(\phi_t\). Run
\[
\theta_{i+1}=\theta_i-\eta H\theta_i,\qquad i=0,\ldots,k-1,
\]
with \(\theta_0=\phi_t\), then perform the fixed interpolation
\[
\phi_{t+1}=(1-\alpha)\phi_t+\alpha\theta_k,
\qquad
\eta>0,\quad \alpha\in(0,1].
\]

One outer cycle is exactly
\[
\phi_{t+1}
=
\left[(1-\alpha)I+\alpha(I-\eta H)^k\right]\phi_t.
\]
Hence a curvature mode \(\lambda\) has multiplier
\[
p(\lambda)=1-\alpha+\alpha(1-\eta\lambda)^k.
\]

There is an exact parity split in the universal stability boundary.

For even \(k\), slow-weight convergence for every spectrum contained in \([\mu,L]\) holds exactly when
\[
0<\eta L<2.
\]

For odd \(k\), it holds exactly when
\[
0<\eta L<
1+\left(\frac{2}{\alpha}-1\right)^{1/k}.
\]

Thus fixed interpolation with \(\alpha<1\) can stabilize inner gradient descent beyond its classical \(\eta L=2\) boundary only when \(k\) is odd. For the common choice \(\alpha=1/2\), the odd-\(k\) ceiling is
\[
\eta L<1+3^{1/k}.
\]
At \(k=5\), this is approximately
\[
\eta L<2.2457309396.
\]

The sharp boundary dynamics differ as well. For even \(k\), at \(\eta L=2\) the top-curvature mode has multiplier \(+1\), so that slow component freezes rather than converging. For odd \(k\), at
\[
\eta L=
1+\left(\frac{2}{\alpha}-1\right)^{1/k}
\]
the top-curvature mode has multiplier \(-1\), producing an exact sign-alternating two-cycle. Beyond the respective boundary, its magnitude grows geometrically.

Despite this stability enlargement, fixed Lookahead interpolation gives no minimax spectral acceleration on a known positive-definite interval. Define
\[
\kappa=\frac{L}{\mu},
\qquad
q=\frac{\kappa-1}{\kappa+1}.
\]
Then
\[
\min_{\eta>0,\;0<\alpha\le1}
\max_{\lambda\in[\mu,L]}
\left|
1-\alpha+\alpha(1-\eta\lambda)^k
\right|
=
q^k.
\]
For every \(k\ge2\), the minimizer is unique:
\[
\eta_\star=\frac{2}{L+\mu},
\qquad
\alpha_\star=1.
\]
Thus the best robust outer-cycle contraction is exactly the contraction of \(k\) ordinary fixed-step gradient updates, with the interpolation switched off. For \(k=1\), every pair satisfying
\[
\alpha\eta=\frac{2}{L+\mu}
\]
attains the same factor \(q\).

Equivalently, the sharp worst-case objective ratio per outer cycle is \(q^{2k}\).

## Assumptions and scope

The result concerns deterministic Lookahead with plain gradient descent as the inner optimizer, a constant inner stepsize, a fixed slow interpolation coefficient, and a symmetric positive-definite quadratic. The slow and fast weights are synchronized at the beginning of every outer cycle exactly as in the original Lookahead algorithm.

The stability statement is a universal interval statement: it holds for every symmetric positive-definite matrix whose eigenvalues lie in \([\mu,L]\), and sharpness is witnessed by a matrix containing the endpoint \(L\).

The minimax statement optimizes a single fixed pair \((\eta,\alpha)\) for the whole spectral interval. It does not cover adaptive slow steps chosen from the current iterate, nonstationary learning rates, stochastic gradients, momentum or Adam inner states, or nonquadratic objectives.

## Proof

Diagonalize \(H\). Since \(H\) is symmetric, the outer-cycle matrix is a polynomial in \(H\), so every eigenvector is invariant and the multiplier on curvature \(\lambda\) is
\[
p(\lambda)=1-\alpha+\alpha(1-\eta\lambda)^k.
\]

For stability, write
\[
h=\eta\lambda>0.
\]
The condition is
\[
-1<1-\alpha+\alpha(1-h)^k<1.
\]

Suppose \(k\) is even. The upper inequality is equivalent to
\[
(1-h)^k<1,
\]
which holds exactly for
\[
0<h<2.
\]
The lower inequality is automatic because
\[
(1-h)^k\ge0
\]
and \(0<\alpha\le1\). Therefore all modes are stable exactly when
\[
\eta L<2.
\]

Suppose \(k\) is odd. The upper inequality holds for every \(h>0\), because the odd power is strictly increasing and
\[
1-h<1.
\]
The lower inequality is
\[
(1-h)^k>1-\frac{2}{\alpha}.
\]
Taking the real odd root gives
\[
1-h>
-\left(\frac{2}{\alpha}-1\right)^{1/k},
\]
or
\[
h<
1+\left(\frac{2}{\alpha}-1\right)^{1/k}.
\]
Again the worst curvature is \(L\), proving the sharp parity frontier. Substitution at equality gives multiplier \(+1\) in the even case and \(-1\) in the odd case.

It remains to prove the minimax statement. Normalize the interval by
\[
x=\eta\mu,
\qquad
\kappa=\frac{L}{\mu},
\qquad
Q=q^k,
\qquad
q=\frac{\kappa-1}{\kappa+1}.
\]

First let \(k\) be even. Then
\[
(1-\eta\lambda)^k\ge0.
\]
Any candidate with an inner endpoint power at least one has outer factor at least one and cannot be minimax, because \(Q<1\). For candidates with all endpoint powers below one,
\[
1-\alpha+\alpha(1-\eta\lambda)^k
\ge
(1-\eta\lambda)^k.
\]
Therefore the worst outer factor is bounded below by
\[
\max\{|1-\eta\mu|^k,\;|1-\eta L|^k\}.
\]
The standard endpoint equioscillation argument minimizes this at
\[
\eta=\frac{2}{L+\mu}
\]
with value \(Q\). Equality in the interpolation bound then requires \(\alpha=1\). Hence the minimizer is unique for even \(k\).

Now let \(k\) be odd. Put
\[
a=(1-\kappa x)^k,
\qquad
b=(1-x)^k.
\]
The modal power is monotone in curvature, so for fixed \(x\) and \(\alpha\) the worst factor occurs at an endpoint.

The sign of \(a+b\) changes exactly at
\[
x_\star=\frac{2}{\kappa+1}.
\]
When \(x\le x_\star\), one has \(a+b\ge0\). Decreasing \(\alpha\) from one moves the larger endpoint multiplier toward \(+1\), so the optimal fixed-\(x\) interpolation is \(\alpha=1\), with factor at least
\[
b\ge q^k=Q.
\]

When \(x\ge x_\star\), one has \(a+b\le0\). The best fixed-\(x\) interpolation balances the endpoint multipliers:
\[
\alpha_x=\frac{2}{2-a-b}\le1,
\]
giving
\[
F(x)=\frac{b-a}{2-a-b}.
\]
To show \(F(x)\ge Q\), rearrange this inequality as
\[
H(x):=
(1+Q)b-(1-Q)a-2Q
\ge0.
\]
At \(x=x_\star\),
\[
a=-Q,\qquad b=Q,
\]
so \(H(x_\star)=0\). Moreover, for \(x\ge x_\star\),
\[
|1-\kappa x|\ge|1-x|.
\]
Since \(k-1\) is even,
\[
H'(x)
=
k\left[
\kappa(1-Q)(1-\kappa x)^{k-1}
-
(1+Q)(1-x)^{k-1}
\right].
\]
Also
\[
Q=q^k\le q
\]
and therefore
\[
\kappa(1-Q)\ge1+Q.
\]
These two inequalities imply
\[
H'(x)\ge0.
\]
Thus \(F(x)\ge Q\).

For \(k\ge2\), \(Q<q\), so the derivative comparison is strict away from \(x_\star\), and the equality case is uniquely
\[
x=x_\star,\qquad \alpha=1.
\]
This is
\[
\eta=\frac{2}{L+\mu},\qquad \alpha=1.
\]
When \(k=1\), the outer polynomial reduces to
\[
p(\lambda)=1-(\alpha\eta)\lambda,
\]
so every pair with \(\alpha\eta=2/(L+\mu)\) attains the usual gradient-descent minimax factor \(q\).

## Verification

The accompanying `verify.py` reconstructs the outer polynomial directly from \(k\) inner gradient steps. It checks the parity stability boundary, both sharp boundary multipliers, the closed minimax factor over several condition numbers and synchronization periods, and a dense parameter grid against the analytic lower bound.

The grid search is only a transcription guard. The universal stability and minimax statements follow from the exact modal proof above.

## Relationship to prior work

The original Lookahead paper defines the synchronization rule, emphasizes that Lookahead can benefit from larger inner learning rates, analyzes noisy diagonal quadratics, and gives a general deterministic quadratic linear-system formulation whose eigenvalues can be computed numerically. It also derives an adaptive quadratic line-minimizing slow step. That adaptive result is a different object from the present theorem: here \(\alpha\) is fixed globally and the question is the exact robust spectral behavior over an entire curvature interval.

The original paper does not state the even-versus-odd fixed-\(\alpha\) stability frontier or solve the fixed-parameter interval minimax problem. The present minimax result is deliberately stronger than a scalar one-mode cancellation observation: it shows that any stability gained by interpolation cannot improve the best worst-case interval contraction, and for \(k\ge2\) the robust optimum uniquely turns interpolation off.

Subsequent Lookahead analyses establish convergence to stationary points, optimization/generalization guarantees, or convergence via nonexpansive/Krasnosel'skii-Mann interpolation. The latter gives a broad sufficient convergence principle when the base optimizer is quasi-nonexpansive and a cocoercive guarantee through the classical gradient step ceiling. It does not imply the odd-\(k\) supercritical stability region, because that region explicitly allows the inner gradient map to be expansive before the outer interpolation stabilizes the \(k\)-step endpoint. Nor do the inspected sources state the interval minimax no-acceleration theorem above.

## Limitations

The theorem concerns fixed-parameter deterministic quadratics. It does not assert that interpolation is useless for stochastic variance reduction, nonquadratic training, generalization, transient behavior, adaptive inner optimizers, or robustness to model mismatch.

The minimax result uses a known positive spectral interval and measures asymptotic slow-weight contraction per outer synchronization cycle. Comparing computational cost per gradient evaluation gives the corresponding \(k\)-th root and does not change the conclusion that the optimal fixed parameters reduce to repeated gradient descent.

The result does not cover adaptive \(\alpha\). In particular, the source paper's quadratic line-minimizing slow step can exploit the current state and is outside the fixed-parameter minimax class.

## References

1. Michael R. Zhang, James Lucas, Geoffrey Hinton, and Jimmy Ba, “Lookahead Optimizer: \(k\) steps forward, 1 step back,” arXiv:1907.08610v1, 2019.
2. Jianyu Wang, Vinayak Tantia, Nicolas Ballas, and Michael G. Rabbat, “Lookahead Converges to Stationary Points of Smooth Non-convex Functions,” ICASSP 2020, DOI:10.1109/ICASSP40776.2020.9054014.
3. Pan Zhou, Hanshu Yan, Xiao-Tong Yuan, Jiashi Feng, and Shuicheng Yan, “Towards Understanding Why Lookahead Generalizes Better Than SGD and Beyond,” NeurIPS 2021.
4. Thomas Pethick, Wanyun Xie, and Volkan Cevher, “Stable Nonconvex-Nonconcave Training via Linear Interpolation,” arXiv:2310.13459v1, 2023.
