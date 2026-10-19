# Sharp objective distortion for distance-calibrated local gradient steps on positive-definite quadratics

## Finding

For every dimension \(d\ge2\), every symmetric positive-definite matrix \(Q\in\mathbb R^{d\times d}\) whose least and greatest eigenvalues are \(\mu>0\) and \(L=\kappa\mu\), and every nonzero \(x\), let \(f(x)=\tfrac12 x^{\mathsf T}Qx\), \(\theta=2\sqrt\kappa/(1+\kappa)\), and let the unrestricted local linear-minimization step be \(T(x)=x-\theta\|x\|Qx/\|Qx\|\). Then \(f(T(x))\le f(x)\) for every \(Q,x\) with condition number at most \(\kappa\) if and only if \(1\le\kappa\le\kappa_{\mathrm{crit}}\), where \(\kappa_{\mathrm{crit}}=7.306674433\ldots\) is the unique real root exceeding one of \(s^3-6s^2-9s-4=0\). For every \(\kappa>\kappa_{\mathrm{crit}}\), a two-dimensional diagonal quadratic gives strict objective increase, despite the guaranteed contraction in distance to the minimizer. Moreover the sharp supremum, jointly over all dimensions, condition numbers, and nonzero initial vectors, of \(f(T(x))/f(x)\) is \(5\), not attained at finite condition number. Specifically, if \(\kappa\to\infty\), \(1<\gamma<2\), \(d=\lceil\kappa^\gamma\rceil\), \(Q=\operatorname{diag}(\kappa,1,\ldots,1)\), and \(x\) is uniformly distributed on the Euclidean unit sphere in dimension \(d\), then \(f(T(x))/f(x)\to5\) in probability.

## Assumptions and scope

All vectors and matrices are real. Let \(d\ge2\), let \(Q=Q^{\mathsf T}\succ0\) have smallest and largest eigenvalues \(0<\mu\le L\), and put \(\kappa=L/\mu\). The objective is \(f(x)=\frac12x^{\mathsf T}Qx\) on the full Euclidean space. Its unique minimizer is \(0\). For \(x\ne0\), set
\[
 \theta=\frac{2\sqrt{\mu L}}{\mu+L}=\frac{2\sqrt\kappa}{\kappa+1},\qquad
 T(x)=x-\theta\|x\|\frac{Qx}{\|Qx\|}.
\]
This is the exact ball-restricted linear oracle with radius \(\theta\|x\|\), as in the strong-convexity radius of Richtárik, Gruntkowska, and Li. All one-step assertions hold in any finite dimension; the probabilistic statement uses a varying dimension, independent uniform-sphere draws, and convergence in probability. No claim is made for constrained feasible sets, nonlinear objectives, stochastic oracle errors, or a finite-dimensional limit as dimension tends to infinity independently of the condition number.

## Proof

Rescaling \(Q\) by \(\mu\) and \(x\) by its Euclidean norm changes neither the relative objective factor nor the update. Thus assume \(\mu=\|x\|=1\). In an orthonormal eigenbasis of \(Q\), write the squared-coordinate masses \(p_i\ge0\), with \(\sum_i p_i=1\), and eigenvalues \(1\le\lambda_i\le\kappa\). Put \(m_j=\sum_i p_i\lambda_i^j\). A direct expansion gives
\[
 \frac{f(T(x))}{f(x)}=1-\frac{2\theta\sqrt{m_2}}{m_1}+\frac{\theta^2m_3}{m_1m_2},
 \qquad f(T(x))\le f(x)\iff\theta m_3\le2m_2^{3/2}.
\]
The function \(z\mapsto z^{3/2}\) is convex on \([1,\kappa^2]\). The chord through its endpoint values lies above it. Consequently, with \(A=\kappa^3-1\), \(B=\kappa^2-1\), and \(a=(m_2-1)/B\in[0,1]\),
\[
 m_3\le1+A a,\quad m_2=1+B a,
 \quad\frac{m_3}{m_2^{3/2}}\le H_\kappa(a):=\frac{1+A a}{(1+B a)^{3/2}}.
\]
For \(\kappa>1\) the bound is attained with a two-point spectral distribution on \(\{1,\kappa}\), with upper-eigenvalue squared mass \(a\). Differentiating \(H_\kappa\) shows its unique maximum in \([0,1]\) occurs at
\[
 a_* =\frac{2\kappa+1}{(\kappa+1)(\kappa^2+\kappa+1)},\qquad
 \max H_\kappa=\frac{2(\kappa^2+\kappa+1)^{3/2}}{3\sqrt3\,\kappa(\kappa+1)}.
\]
Therefore universal objective descent is equivalent to
\[
 4(\kappa^2+\kappa+1)^3\le27\kappa(\kappa+1)^4.
\]
The difference of the two sides factors exactly as
\[
 (\kappa^3-6\kappa^2-9\kappa-4)(4\kappa^3+9\kappa^2+6\kappa-1).
\]
The second factor is positive for \(\kappa\ge1\); the cubic has exactly one root larger than one (its derivative has one minimum for \(\kappa>1\), and its value at one is negative). This proves the stated sharp threshold. At \(\kappa=1\), the update reaches the minimizer in one step and the descent assertion holds. Beyond the threshold the two-point endpoint distribution at \(a_*\) witnesses a strict increase. For example, \(Q=\operatorname{diag}(1,8)\), \(x=(6,1)\) yields \(f(x)=22\) and
\[
 f(T(x))=\frac{125654}{2025}-\frac{40\sqrt{74}}{9} >22.
\]
The paper's Euclidean distance contraction is compatible with this value increase; in this witness the squared distance falls from \(37\) to \(4181/81-176\sqrt{74}/45<37\).

For the global amplification bound, \(m_3\le\kappa m_2\) and \(m_1\ge1\) give
\[
 \frac{f(T(x))}{f(x)}\le1+\frac{\theta^2m_3}{m_1m_2}
 \le1+\theta^2\kappa=1+\frac{4\kappa^2}{(\kappa+1)^2}<5
\]
for every finite \(\kappa\). Sharpness is stronger than an isolated adversarial vector: fix \(1<\gamma<2\) and \(d=\lceil\kappa^\gamma\rceil\), and take \(Q=\operatorname{diag}(\kappa,1,\ldots,1)\). If \(x\) is uniform on \(S^{d-1}\), let \(p=x_1^2\). It has the representation \(p=U/(U+V_d)\), where \(U\sim\chi^2_1\), \(V_d\sim\chi^2_{d-1}\) are independent. Hence \(dp\) converges in distribution to \(U\), and, since \(\kappa/d\to0\) and \(\kappa^2/d\to\infty\),
\[
 \kappa p\longrightarrow0,\qquad\kappa^2p\longrightarrow\infty
 \quad\text{in probability}.
\]
For this two-eigenvalue family \(m_j=1+(\kappa^j-1)p\), so \(m_1\to1\), \(m_2\to\infty\), \(m_3/(\kappa m_2)\to1\), and \(\theta\sqrt{m_2}\to0\) in probability. Substitution into the exact objective ratio gives \(f(T(x))/f(x)\to1+4=5\) in probability. This proves sharpness and the typical high-dimensional amplification statement.

## Verification

The spectral expansion and chord inequality are exact symbolic identities. Substituting the critical mass \(a_*\) reproduces the maximizing ratio algebraically. Exact symbolic expansion of the \(\kappa=8\) witness gives the radical expression above; its numerical ratio is approximately \(1.08267278555817\). Direct scalar optimization over two-point spectral mass at condition numbers \(8,10,20,100,1000\) gives objective factors approximately \(1.08277,1.29113,1.94387,3.19619,4.19289\), all below five. Uniform-sphere Monte Carlo tests for \(d\approx\kappa^{3/2}\) gave empirical objective-increase frequencies about \(0.916,0.975,0.992\) for \(\kappa=100,1000,10000\), respectively. These finite tests check the algebra and illustrate, but do not replace, the exact and probabilistic proofs.

## Relationship to prior work

Richtárik, Gruntkowska, and Li (arXiv:2605.08850, first public May 9, 2026) introduced the local LMO method, subsequently named Broximal Gradient Descent. Their May 2026 full text, Theorem 3.5, proves squared-distance contraction using precisely the radius \(\theta\|x\|\); the present result concerns the distinct one-step objective value on positive-definite quadratics. Richtárik and Mahran (arXiv:2609.33383, September 27, 2026) identify a projection interpretation and Fejér monotonicity under a Polyak-radius condition; neither implies objective-value monotonicity at the strong-convexity distance radius. Known exact Polyak-gradient and Cauchy trust-region objective bounds concern different scalar step prescriptions and cannot be substituted for this adaptive normalized-gradient rule without another argument.

## Limitations

The theorem is restricted to the unconstrained full-space quadratic model and to exact local linear oracles. The worst-case factor five is a supremum as the condition number grows, not an attainable finite-parameter value. The high-dimensional assertion is convergence in probability, not a finite-sample lower bound or almost-sure convergence for an arbitrary coupling of vectors. The 121-page September 2026 revision of arXiv:2605.08850 was not materially inspected beyond its abstract and its authors' change description; this creates a residual literature-overlap risk. Independent audit or validation has not been performed.

## References

1. P. Richtárik, K. Gruntkowska, H. Li, *Local LMO: Constrained Gradient Optimization via a Local Linear Minimization Oracle*, arXiv:2605.08850v1, May 9, 2026, https://arxiv.org/html/2605.08850v1 . Revised as *Broximal Gradient Descent: A Projection-Free Sister of Projected Gradient Descent*, arXiv:2605.08850v2, September 28, 2026, https://arxiv.org/abs/2605.08850 .
2. P. Richtárik, A. Mahran, *Local LMO is Secretly a Projection Method!*, arXiv:2609.33383v1, September 27, 2026, https://arxiv.org/html/2609.33383v1 .
3. Published research record, *Sharp one-step objective frontier for scaled Polyak steps on SPD quadratics*, September 20, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-polyak-objective-monotonicity-frontier--169a05cdc789 .
