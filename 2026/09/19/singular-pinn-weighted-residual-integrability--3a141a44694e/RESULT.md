# A boundary-integrability obstruction for singularity-weighted PINN residuals

## Statement

Consider the singular Dirichlet problem
\[
-\Delta u=u^{-\alpha}\quad\text{in }\Omega,\qquad u=0\quad\text{on }\partial\Omega,\qquad 0<\alpha<1,
\]
with the intended positive solution in the interior. The recent weighted-PINN formulation in arXiv:2609.19335v1 uses a smooth hard-constrained trial
\[
\widehat u(x)=\eta(x)\,\operatorname{Softplus}(g_\theta(x))
\]
and the strong residual
\[
R=-\Delta\widehat u-\widehat u^{-\alpha}.
\]
Its proposed weight is
\[
w=1+\beta\widehat u^{-\alpha},\qquad \beta>0.
\]

For any fixed finite smooth network and any smooth boundary patch on which \(\eta\) has a simple zero, the constrained trial vanishes linearly in the inward distance \(d\):
\[
\widehat u(y,d)=a(y)d+O(d^2),\qquad a(y)>0.
\]
Consequently
\[
R(y,d)=-a(y)^{-\alpha}d^{-\alpha}(1+o(1)).
\]
More generally, for
\[
w_p=1+\beta\widehat u^{-p},\qquad p>0,
\]
the weighted strong-residual density satisfies
\[
\boxed{
 w_pR^2
 \sim
 \beta a(y)^{-(2\alpha+p)}d^{-(2\alpha+p)}.
}
\]
A smooth codimension-one boundary collar has volume element \((1+O(d))\,d\sigma\,dd\), so the continuum weighted objective is locally finite at the boundary if and only if
\[
\boxed{2\alpha+p<1.}
\]

Two immediate specializations are therefore:

- standard strong-residual least squares \((p=0)\): finite only for \(\alpha<1/2\);
- the proposed singularity-aware factor \(p=\alpha\): finite only for
  \[
  \boxed{\alpha<1/3.}
  \]

Thus the factor intended to emphasize the singular region lowers the population-integrability threshold from \(1/2\) to \(1/3\). At the paper's one-dimensional baseline \(\alpha=1/2\), the standard population residual is already logarithmically divergent, while the proposed weighted population residual has a power divergence.

This is a fixed-trial statement. A finite collocation sample contains no boundary point almost surely and therefore has finite numerical loss. The obstruction concerns the continuum objective, the expectation under ordinary uniform interior sampling, and the resolution dependence of any fixed smooth trial.

## Why the divergence is structural

The source architecture uses smooth tanh hidden activations, Softplus output, and in one dimension
\[
\eta(x)=x(1-x).
\]
For every finite parameter vector, \(g_\theta\) and \(\operatorname{Softplus}(g_\theta)\) are smooth and finite at the endpoints, while Softplus is strictly positive. Hence, at \(x=0\),
\[
\widehat u(x)=a_0x+O(x^2),\qquad a_0>0,
\]
and \(\widehat u''(x)=O(1)\). The singular source instead behaves as
\[
\widehat u(x)^{-\alpha}=a_0^{-\alpha}x^{-\alpha}(1+o(1)).
\]
The bounded second derivative cannot cancel this divergence, so
\[
R(x)=-a_0^{-\alpha}x^{-\alpha}(1+o(1)).
\]
The same holds at \(x=1\).

By contrast, the exact one-dimensional solution has the fractional boundary correction required for cancellation. If \(a=u'(0^+)>0\), then
\[
\boxed{
 u(x)=ax-\frac{a^{-\alpha}}{(1-\alpha)(2-\alpha)}x^{2-\alpha}
 +o(x^{2-\alpha}).
}
\]
Therefore
\[
u''(x)\sim-a^{-\alpha}x^{-\alpha}.
\]
The exact solution is compatible with a singular second derivative even though it remains \(C^1\) in the weak-singularity regime. A fixed finite smooth hard-constrained network has the correct linear vanishing but not this fractional second-order term.

## Resolution law on a one-dimensional collocation grid

Let \(x_i=i/(N+1)\), \(i=1,\dots,N\), and suppose a fixed smooth hard trial has endpoint slopes \(a_0,a_1>0\). Put
\[
q=2\alpha+p.
\]
For \(p>0\), the weighted empirical mean has the sharp leading asymptotics
\[
\mathcal L_{p,N}
\sim
\begin{cases}
\beta\zeta(q)\left(a_0^{-q}+a_1^{-q}\right)N^{q-1},&q>1,\\[4pt]
\beta\left(a_0^{-1}+a_1^{-1}\right)\log N,&q=1.
\end{cases}
\]
The standard residual corresponds to exponent \(q=2\alpha\) with the same harmonic-sum mechanism and without the extra weight factor.

For the source choice \(p=\alpha\), the supercritical exponent is \(3\alpha-1\). In particular, at \(\alpha=1/2\),
\[
\boxed{
\mathcal L_{\rm std,N}
\sim \left(a_0^{-1}+a_1^{-1}\right)\log N,
}
\]
whereas
\[
\boxed{
\mathcal L_{\rm w,N}
\sim
\beta\zeta(3/2)
\left(a_0^{-3/2}+a_1^{-3/2}\right)N^{1/2}.
}
\]
Thus even if network parameters are held fixed, refining an otherwise ordinary collocation set changes the scale of the optimization objective without bound.

For i.i.d. uniformly distributed collocation points, the same threshold has a probabilistic interpretation: if \(2\alpha+p\ge1\), then one sample contribution has infinite expectation for every fixed smooth hard trial. Every finite sample is still finite almost surely.

## A boundary enrichment that cancels the leading singular residual

The obstruction identifies the missing local term. On a smooth boundary patch, consider instead an enriched expansion
\[
\widehat u(y,d)=a(y)d+b(y)d^{2-\alpha}+\text{higher-order terms}.
\]
Since
\[
\partial_d^2 d^{2-\alpha}=(2-\alpha)(1-\alpha)d^{-\alpha},
\]
the leading singular part of the strong residual cancels when
\[
\boxed{
 b(y)=-\frac{a(y)^{-\alpha}}{(1-\alpha)(2-\alpha)}.
}
\]
This is only a leading-order local repair, not a full convergence theorem, but it shows that the divergence is tied to a specific regularity mismatch rather than to the boundary condition itself.

## Comparison with weak and variational objectives

The source paper itself records the formal energy
\[
\mathcal J(v)=\frac12\int_\Omega |\nabla v|^2\,dx
-\frac{1}{1-\alpha}\int_\Omega v^{1-\alpha}\,dx.
\]
For a fixed smooth hard trial with \(v\sim ad\), both terms are locally integrable for every \(0<\alpha<1\). Hence this particular strong-\(L^2\) integrability obstruction is absent from the corresponding Ritz energy. Variational PINN formulations likewise replace pointwise strong residuals by weak residuals and are established alternatives in the literature.

This does not imply that weak or Ritz training is automatically superior on every benchmark. It only separates a boundary-integrability issue that is specific to squaring the singular strong residual, especially after multiplying it by another inverse power of the trial solution.

## Verification

`artifacts/verify_singular_weighted_loss.py` evaluates the source-compatible fixed trial
\[
\widehat u(x)=\log 2\;x(1-x),
\]
which is exactly obtained from the source architecture by taking the raw network output identically zero. With \(\beta=1\), the script evaluates standard and weighted residual losses on \(x_i=i/(N+1)\) up to \(N=2^{20}\).

For \(\alpha=1/2\), the measured weighted grid-doubling exponent approaches \(1/2\); at \(N=2^{20}\),
\[
\frac{\mathcal L_{\rm w,N}}{\sqrt N}=8.980352067,
\]
while the predicted limit is
\[
2(\log2)^{-3/2}\zeta(3/2)=9.053726710488.
\]
The standard loss divided by \(\log N\) increases toward the predicted constant
\[
2/(\log2)=2.885390081778.
\]
For \(\alpha=0.6\), the last observed grid-doubling exponents are approximately \(0.22484\) for the standard loss and \(0.80082\) for the weighted loss, approaching the predicted powers \(0.2\) and \(0.8\).

The verification is deterministic and uses direct evaluation of the closed-form trial; no trained network or stochastic fit is required.

## Relation to prior work and originality boundary

The broad fact that strong least-squares/minimum-residual formulations can be inappropriate for singular or non-square-integrable data is not new. Führer, Heuer, and Karkulik analyze regularized minimum-residual methods for second-order PDEs with singular data and explicitly motivate alternatives for loads outside \(L^2\). Exact hard boundary constructions using distance-like factors are also established in PINNs, and variational PINNs are established alternatives to strong collocation.

The claim here is narrower: for the specific singular equation, smooth positivity-preserving hard architecture, and inverse-solution weighting proposed in arXiv:2609.19335v1, the continuum strong-residual objective has the exact thresholds \(\alpha=1/2\) (unweighted) and \(\alpha=1/3\) (proposed weight), with the corresponding fixed-trial collocation-resolution laws and a direct boundary-regularity mechanism. No equivalent source-specific statement was located in the checked literature or repository records.

## Limitations

- The result does not show that a finite collocation training run must fail, nor that the trained solution error must be large. Parameters can depend on resolution and can form increasingly sharp boundary layers.
- The continuum and i.i.d.-expectation statements are for each fixed finite smooth trial. A parameter sequence with unbounded derivatives requires separate analysis.
- The multidimensional statement assumes a smooth boundary patch and a smooth hard factor with a simple zero. More exotic boundary factors can change the vanishing exponent.
- The fractional enrichment cancels the leading singular term only; it is not a complete architecture or convergence analysis.
- The motivating preprint is recent. The classical singular-PDE literature can contain sharper boundary expansions, and broader singular-data least-squares theory already covers the general principle that an \(L^2\) residual may be the wrong norm.

## References

1. B. Oulgiht, *Deep Learning for Singular PDEs: A Weighted Neural Network Approach*, arXiv:2609.19335v1 (2026). https://arxiv.org/abs/2609.19335
2. M. G. Crandall, P. H. Rabinowitz, L. Tartar, *On a Dirichlet problem with a singular nonlinearity*, Communications in Partial Differential Equations 2(2) (1977), 193–222. https://doi.org/10.1080/03605307708820029
3. T. Führer, N. Heuer, M. Karkulik, *MINRES for Second-Order PDEs with Singular Data*, SIAM Journal on Numerical Analysis 60(3) (2022), 1111–1135. https://doi.org/10.1137/21M1457023
4. N. Sukumar, A. Srivastava, *Exact imposition of boundary conditions with distance functions in physics-informed deep neural networks*, Computer Methods in Applied Mechanics and Engineering 389 (2022), 114333. https://doi.org/10.1016/j.cma.2021.114333
5. E. Kharazmi, Z. Zhang, G. E. Karniadakis, *Variational Physics-Informed Neural Networks For Solving Partial Differential Equations*, arXiv:1912.00873 (2019). https://arxiv.org/abs/1912.00873
