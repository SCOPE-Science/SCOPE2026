# Finite Entropy-SGD inner loops interpolate between raw and local-entropy conditioning
## Finding

Entropy-SGD defines a smoother local-entropy objective but estimates its gradient with finitely many inner Langevin steps. On an SPD quadratic, the ideal objective and finite estimator are both exactly solvable.

Let
\[
f(x)=\frac12x^\top Hx,\qquad H\succ0,\qquad \sigma(H)\subseteq[\mu,M],\qquad 0<\mu<M,
\]
with \(\kappa=M/\mu\). Fix \(\gamma>0\), \(\eta'>0\), \(\alpha\in(0,1]\), and \(K\ge1\). Initialize as in Entropy-SGD Algorithm 1,
\[
x'_0=x,\qquad \mu_0=x,
\]
and use
\[
x'_j=x'_{j-1}-\eta'[Hx'_{j-1}+\gamma(x'_{j-1}-x)]+\zeta_j,
\qquad \mathbb E[\zeta_j]=0,
\]
\[
\mu_j=(1-\alpha)\mu_{j-1}+\alpha x'_j.
\]
The paper-form estimate is \(\widehat g_K=\gamma(x-\mu_K)\).

With \(r=1-\alpha\) and
\[
S_K(z)=\alpha\sum_{j=1}^K r^{K-j}[1-(1-z)^j],
\]
one has
\[
\boxed{\mathbb E[\widehat g_K]=\Phi_K(H)x},
\qquad
\boxed{\phi_K(h)=\gamma\frac{h}{h+\gamma}S_K(\eta'(h+\gamma))}.
\]

The exact local-entropy Gibbs mean is
\[
\langle x'\rangle=\gamma(H+\gamma I)^{-1}x,
\]
so the ideal response is
\[
\phi_\infty(h)=\frac{\gamma h}{h+\gamma},
\]
with
\[
\boxed{\kappa_\infty=\kappa\frac{\mu+\gamma}{M+\gamma}}.
\]

Assume
\[
0<\eta'(M+\gamma)\le1.
\]
For one inner step,
\[
S_1(z)=\alpha z,
\]
so
\[
\Phi_1(H)=\alpha\gamma\eta'H,
\qquad
\boxed{\kappa_1=\kappa}.
\]
Thus one inner step gives no conditioning improvement.

For every finite \(K\ge2\),
\[
\boxed{\kappa_\infty<\kappa_K<\kappa},
\qquad
\kappa_K=\frac{\phi_K(M)}{\phi_K(\mu)}.
\]
Moreover,
\[
\boxed{\lim_{K\to\infty}\kappa_K=\kappa_\infty},
\qquad
\boxed{\lim_{\eta'\downarrow0}\kappa_K=\kappa}
\]
for fixed finite \(K\).

Finite inner sampling therefore realizes only part of the ideal local-entropy spectral smoothing.

## Assumptions and scope

The theorem concerns deterministic SPD quadratics and the expectation of the source inner estimator. Zero-mean thermal noise is allowed because it does not change that expectation. The restriction \(\eta'(M+\gamma)\le1\) keeps all deterministic inner modes nonoscillatory. The theorem does not characterize estimator variance or nonlinear outer training trajectories. The source later removes the factor \(\gamma\) from the practical outer update; uniform scaling does not change condition numbers.

## Proof

Fix an eigendirection with eigenvalue \(h\in[\mu,M]\) and let
\[
q_h=1-\eta'(h+\gamma).
\]
Taking expectations gives
\[
y_j=q_hy_{j-1}+\eta'\gamma x_h,
\qquad y_0=x_h,
\]
so
\[
y_j=x_h\left[\frac{\gamma}{h+\gamma}+\frac{h}{h+\gamma}q_h^j\right].
\]
Hence
\[
x_h-y_j=\frac{h}{h+\gamma}(1-q_h^j)x_h.
\]
The exponential average satisfies
\[
\mathbb E[\mu_K]=r^Kx+\alpha\sum_{j=1}^K r^{K-j}y_j,
\]
whose coefficients sum to one. This yields the displayed \(\phi_K\).

Completing the square in the quadratic Gibbs density gives mean \(\gamma(H+\gamma I)^{-1}x\), proving the ideal response.

Set \(z=\eta'(h+\gamma)\in(0,1]\). Each \(1-(1-z)^j\) is increasing in \(z\), so \(S_K(z)\) is strictly increasing. Since \(h/(h+\gamma)\) is also increasing, \(\phi_K(h)\) is increasing and the condition number is the endpoint ratio. Furthermore,
\[
\frac{\kappa_K}{\kappa_\infty}
=
\frac{S_K(\eta'(M+\gamma))}{S_K(\eta'(\mu+\gamma))}>1.
\]

For the upper bound,
\[
\frac{S_K(z)}{z}
=
\alpha\sum_{j=1}^K r^{K-j}\sum_{\ell=0}^{j-1}(1-z)^\ell.
\]
For \(K\ge2\), this is strictly decreasing in \(z\). Since
\[
\frac{\phi_K(h)}{h}=\gamma\eta'\frac{S_K(z)}{z},
\]
the effective curvature divided by raw curvature decreases with \(h\), proving \(\kappa_K<\kappa\).

For fixed admissible \(z>0\), the expected inner state converges to the Gibbs mean and the exponential average forgets its initialization, so \(S_K(z)\to1\) and \(\kappa_K\to\kappa_\infty\).

For fixed \(K\),
\[
1-(1-z)^j=jz+O(z^2),
\]
so
\[
S_K(z)=c_Kz+O(z^2),
\qquad c_K=\alpha\sum_{j=1}^K r^{K-j}j>0.
\]
Therefore \(\phi_K(h)=\gamma\eta'c_Kh+O((\eta')^2)\), proving \(\kappa_K\to\kappa\) as \(\eta'\downarrow0\).

## Verification

The accompanying `verify.py` reconstructs the expected scalar inner recurrence, checks the closed response over randomized parameters, verifies the one-step identity, checks the finite-\(K\) condition-number inequalities, and tests both limiting regimes.

The computations are transcription guards. The exact filter and strict interpolation are proved analytically above.

## Relationship to prior work

Chaudhari and coauthors define local entropy as a log-partition function and derive
\[
-\nabla F(x,\gamma)=\gamma(x-\langle x'\rangle).
\]
Their Algorithm 1 initializes both the inner position and exponential mean at the outer iterate, estimates the Gibbs mean with a finite SGLD loop, and uses exponential averaging with \(\alpha=0.75\). The paper reports \(5\) to \(20\) inner Langevin iterations in its experiments.

The source proves that the ideal local-entropy objective is smoother under a Hessian spectral-gap assumption. Its appendix uses the saddle-point approximation
\[
x-\langle x'\rangle\approx(H+\gamma I)^{-1}\nabla f(x).
\]
For an SPD quadratic this relation is exact, but the inspected source does not analyze the finite number of inner steps as a spectral filter, state that one inner step preserves the raw condition number exactly, or give the strict interpolation \(\kappa_\infty<\kappa_K<\kappa\).

Dziugaite and Roy later analyze Entropy-SGD through PAC-Bayes generalization and SGLD-based data-dependent priors. That work addresses generalization rather than finite-horizon quadratic conditioning.

## Limitations

The theorem concerns estimator expectation, not thermal-noise covariance. The exact Gaussian calculation depends on the quadratic model. The strict interpolation is proved only for nonoscillatory inner modes. No optimal inner-loop length or outer learning rate is claimed.

## References

1. Pratik Chaudhari, Anna Choromanska, Stefano Soatto, Yann LeCun, Carlo Baldassi, Christian Borgs, Jennifer Chayes, Levent Sagun, and Riccardo Zecchina, “Entropy-SGD: Biasing Gradient Descent Into Wide Valleys,” arXiv:1611.01838v1, 2016; ICLR 2017.
2. Gintare Karolina Dziugaite and Daniel M. Roy, “Entropy-SGD optimizes the prior of a PAC-Bayes bound: Generalization properties of Entropy-SGD and data-dependent priors,” Proceedings of Machine Learning Research 80, 2018.
