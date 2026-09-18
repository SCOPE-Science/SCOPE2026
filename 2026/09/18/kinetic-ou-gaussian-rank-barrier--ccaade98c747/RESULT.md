# A sharp Gaussian-rank barrier for kinetic Ornstein--Uhlenbeck innovations

## Result

Consider the free underdamped Langevin (kinetic Ornstein--Uhlenbeck) system in \(\mathbb R^d\),
\[
 dX_t=V_t\,dt,\qquad
 dV_t=-\gamma V_t\,dt+\sqrt{2\gamma\alpha}\,dW_t,
 \qquad \gamma,\alpha>0.
\]
Over a step of length \(h>0\), conditional on \((X_t,V_t)\), the exact stochastic innovation in \((X,V)\) is a centered Gaussian in \(\mathbb R^{2d}\). Define
\[
A_h=\frac{h}{\gamma^2}-\frac{2(1-e^{-\gamma h})}{\gamma^3}
   +\frac{1-e^{-2\gamma h}}{2\gamma^3},
\]
\[
B_h=\frac{(1-e^{-\gamma h})^2}{2\gamma^2},
\qquad
C_h=\frac{1-e^{-2\gamma h}}{2\gamma}.
\]
Its covariance is
\[
\boxed{
\Sigma_h=2\gamma\alpha
\begin{pmatrix}A_h&B_h\\B_h&C_h\end{pmatrix}\otimes I_d.
}
\]
The \(2\times2\) block is positive definite for every \(h>0\). Hence
\[
\boxed{\operatorname{rank}\Sigma_h=2d.}
\]
Consequently, any exact **affine-Gaussian** simulation of the conditional transition requires at least \(2d\) independent scalar standard-normal degrees of freedom, equivalently at least two independent \(d\)-dimensional standard-normal draws. Two such draws are sufficient by a Cholesky factorization of the displayed \(2\times2\) block.

More quantitatively, suppose an approximation uses only one \(d\)-dimensional standard normal \(\xi\sim N(0,I_d)\) through an affine innovation \(L\xi\), with arbitrary deterministic mean and arbitrary \(L\in\mathbb R^{2d\times d}\). Let \(\lambda_+(h)\ge\lambda_-(h)>0\) be the two eigenvalues of the one-coordinate covariance block
\[
2\gamma\alpha\begin{pmatrix}A_h&B_h\\B_h&C_h\end{pmatrix}.
\]
Then the smallest possible one-step \(2\)-Wasserstein error against the exact conditional transition is
\[
\boxed{
\inf_{m,L}
W_2\!\left(
N(m,LL^T),
N(m_\star,\Sigma_h)
\right)
=
\sqrt{d\,\lambda_-(h)}.
}
\]
The optimum uses the exact mean \(m=m_\star\) and retains the \(d\)-fold top eigenspace of \(\Sigma_h\). In particular,
\[
\boxed{
\lambda_-(h)
=\frac{\gamma\alpha}{6}h^3+O(h^4),
\qquad
\inf W_2
=\sqrt{\frac{d\gamma\alpha}{6}}\,h^{3/2}(1+O(h)).
}
\]
Thus one \(d\)-Gaussian affine innovation has an unavoidable local \(\Theta(\sqrt d\,h^{3/2})\) Wasserstein defect even for the force-free kinetic OU subsystem. No such one-draw affine-Gaussian rule can reproduce the exact OU transition, or attain local \(W_2=o(h^{3/2})\), uniformly over this subsystem.

This gives a sharp resource interpretation for the two-Gaussian-per-step cost highlighted by the recent low-cost ULMC integrators of Lyu, Wang, and Yang (arXiv:2609.20713): within the standard affine-Gaussian innovation model, two \(d\)-normal draws are already the minimum needed to reproduce the free kinetic OU noise exactly. The statement is deliberately about the conditional transition and does not assert that two Gaussians are necessary for every long-time or invariant-measure accuracy objective.

## Exact covariance and full-rank proof

Variation of constants gives
\[
V_{t+h}=e^{-\gamma h}V_t+
\sqrt{2\gamma\alpha}\int_0^h e^{-\gamma(h-s)}\,dW_{t+s},
\]
\[
X_{t+h}=X_t+\frac{1-e^{-\gamma h}}{\gamma}V_t+
\sqrt{2\gamma\alpha}\int_0^h
\frac{1-e^{-\gamma(h-s)}}{\gamma}\,dW_{t+s}.
\]
For one coordinate, Itô isometry therefore yields the covariance entries \(A_h,B_h,C_h\) above.

Their determinant has the exact factorization
\[
\boxed{
A_hC_h-B_h^2
=
\frac{(e^x-1)\,[xe^x+x-2e^x+2]e^{-2x}}
{2\gamma^4},
\qquad x=\gamma h.
}
\]
For \(x>0\), the first factor is positive. Let
\[
q(x)=xe^x+x-2e^x+2=e^x(x-2)+x+2.
\]
Then
\[
q(0)=q'(0)=0,
\qquad
q''(x)=xe^x>0\quad(x>0).
\]
Hence \(q'(x)>0\) and \(q(x)>0\) for every \(x>0\). Therefore
\[
A_hC_h-B_h^2>0,
\]
so the one-coordinate covariance has rank two and \(\Sigma_h\) has rank \(2d\).

A single affine \(d\)-Gaussian innovation \(L\xi\) has covariance \(LL^T\) of rank at most \(d\), proving impossibility of exact matching. Conversely, if \(\xi,\eta\sim N(0,I_d)\) are independent, a Cholesky factor \(R_hR_h^T=2\gamma\alpha\begin{psmallmatrix}A_h&B_h\\B_h&C_h\end{psmallmatrix}\) gives the exact innovation as
\[
(R_h\otimes I_d)
\binom{\xi}{\eta}.
\]
Thus two \(d\)-normal draws are both necessary and sufficient in this model.

## Sharp one-Gaussian Wasserstein defect

For centered Gaussians with covariances \(\Sigma,\Gamma\), the squared \(W_2\) distance is the Bures--Wasserstein distance
\[
d_B^2(\Sigma,\Gamma)
=\operatorname{tr}\Sigma+\operatorname{tr}\Gamma
-2\operatorname{tr}
\left(\Sigma^{1/2}\Gamma\Sigma^{1/2}\right)^{1/2}.
\]
Equivalently,
\[
d_B^2(\Sigma,\Gamma)
=
\min_{O\in O(2d)}
\|\Sigma^{1/2}-\Gamma^{1/2}O\|_F^2.
\]
If \(\operatorname{rank}\Gamma\le d\), every matrix \(\Gamma^{1/2}O\) has rank at most \(d\). The Eckart--Young theorem therefore gives
\[
d_B^2(\Sigma_h,\Gamma)
\ge
\sum_{j=d+1}^{2d}\lambda_j(\Sigma_h).
\]
The spectrum of \(\Sigma_h\) consists of \(d\) copies of \(\lambda_+(h)\) and \(d\) copies of \(\lambda_-(h)\). Hence
\[
d_B^2(\Sigma_h,\Gamma)\ge d\lambda_-(h).
\]
Equality is attained by the spectral rank-\(d\) truncation that keeps the \(\lambda_+\) eigenspace. A mean mismatch contributes the additional term \(\|m-m_\star\|_2^2\), so the exact mean is optimal and
\[
\inf_{m,L}W_2^2=d\lambda_-(h).
\]

Explicitly,
\[
\lambda_-(h)
=\gamma\alpha\left[
A_h+C_h-
\sqrt{(A_h-C_h)^2+4B_h^2}
\right].
\]
For small \(h\),
\[
A_h=\frac{h^3}{3}+O(h^4),\qquad
B_h=\frac{h^2}{2}+O(h^3),\qquad
C_h=h+O(h^2),
\]
and
\[
A_hC_h-B_h^2=\frac{h^4}{12}+O(h^5).
\]
The larger unscaled eigenvalue is \(h+O(h^2)\), so the smaller one is
\[
\frac{h^3}{12}+O(h^4).
\]
Multiplication by \(2\gamma\alpha\) gives the stated expansion for \(\lambda_-(h)\).

## Interpretation for low-cost underdamped Langevin integrators

Lyu, Wang, and Yang introduce low-cost randomized and UBU-type underdamped Langevin integrators requiring one gradient evaluation and two Gaussian draws per iteration, improving the Gaussian count of several existing counterparts. Their reported convergence rates concern long-time sampling errors; the theorem here addresses a different, local question: how many independent Gaussian degrees of freedom are needed to represent the exact force-free kinetic OU innovation, and what is the best possible local \(W_2\) error if only one \(d\)-Gaussian affine draw is allowed?

The answer is sharp: exact reproduction needs two draws, while one draw incurs exactly \(\sqrt{d\lambda_-(h)}\). This identifies a concrete resource boundary beneath the new two-Gaussian constructions without asserting a lower bound for all possible samplers or all notions of accuracy.

## Relation to prior work and originality boundary

Several ingredients are classical and are **not** claimed as new:

- the exact Gaussian solution of linear Langevin/Ornstein--Uhlenbeck systems and the covariance of integrated OU noise;
- the Bures--Wasserstein formula for \(W_2\) between Gaussian measures;
- low-rank Bures--Wasserstein approximation of covariance matrices;
- the existence of one-Gaussian numerical methods for second-order stochastic systems when the goal is stationary-density accuracy rather than exact conditional-transition matching.

In particular, Bréchet, Papagiannouli, An, and Montúfar (ICML 2023) characterize minimizers for rank-bounded covariance approximation under Bures--Wasserstein loss. Burrage and Lythe (SIAM J. Numer. Anal. 2009) explicitly construct second-order-in-time stochastic methods using one Gaussian random variable per timestep for stationary-density objectives, and Burrage, Lenane, and Lythe (SIAM J. Sci. Comput. 2007) analyze one-Gaussian methods for damped stochastic oscillators. Those results show why the present claim must be local and conditional-transition-specific.

The originality claim is restricted to the **kinetic-OU resource theorem** above: the exact determinant/rank obstruction stated as a minimum Gaussian-draw count in the resource model used by the new ULMC paper, together with the sharp best-one-draw Bures--Wasserstein defect and its \(\sqrt{d\gamma\alpha/6}\,h^{3/2}\) asymptotic. To the best of our knowledge, the inspected Langevin-integrator and Bures--Wasserstein sources do not state this combined lower bound.

## Reproducibility check

`artifacts/verify_ou_rank.py` evaluates the closed-form covariance, determinant, rank, spectral truncation identity, small-step asymptotic, and a two-draw Cholesky reconstruction. `artifacts/verification_output.txt` records the deterministic output for \(\gamma=1.7\), \(\alpha=0.8\), and \(d=5\). The ratio of the exact optimal one-draw error to
\[
\sqrt{d\gamma\alpha/6}\,h^{3/2}
\]
approaches one as \(h\) decreases, while the full innovation covariance retains rank \(2d\). The computation supports the formulas but is not a substitute for the analytic proof.

## Limitations

- The lower bound is for **affine-Gaussian conditional innovations**. A nonlinear measurable transformation of a lower-dimensional continuous random source can evade a literal covariance-rank count, although that is not the Gaussian-draw model used in the numerical schemes considered here.
- The result concerns the one-step conditional transition in standard Euclidean \(W_2\) on phase space. It does not imply that two Gaussian draws are necessary for high-order weak accuracy, invariant-measure accuracy, or every long-time Wasserstein guarantee.
- One-Gaussian stationary-density methods are known and do not contradict the theorem; they optimize a different target and generally do not reproduce the exact joint \((X,V)\) transition.
- The \(h^{3/2}\) obstruction is a local transition-kernel statement. It should not be converted without additional analysis into a lower bound on the global or stationary bias of a Markov chain.
- The theorem assumes scalar friction \(\gamma I\) and isotropic noise as in the displayed model. Full-rank extensions to more general positive-definite friction are natural but are not claimed here.

## References

1. W. Lyu, X. Wang, and B. Yang, *A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New*, arXiv:2609.20713, 2026. https://arxiv.org/abs/2609.20713
2. P. Bréchet, K. Papagiannouli, J. An, and G. Montúfar, *Critical Points and Convergence Analysis of Generative Deep Linear Networks Trained with Bures-Wasserstein Loss*, ICML 2023, PMLR 202:3106--3147. https://proceedings.mlr.press/v202/brechet23a.html
3. K. Burrage and G. Lythe, *Accurate Stationary Densities with Partitioned Numerical Methods for Stochastic Differential Equations*, SIAM J. Numer. Anal. 47 (2009), 1601--1618. https://doi.org/10.1137/060677148
4. K. Burrage, I. Lenane, and G. Lythe, *Numerical Methods for Second-Order Stochastic Differential Equations*, SIAM J. Sci. Comput. 29 (2007), 245--264. https://doi.org/10.1137/050646032
5. L. Ning, X. Jiang, and T. T. Georgiou, *On the Geometry of Covariance Matrices*, IEEE Signal Processing Letters 20 (2013), 787--790. https://doi.org/10.1109/LSP.2013.2266273
