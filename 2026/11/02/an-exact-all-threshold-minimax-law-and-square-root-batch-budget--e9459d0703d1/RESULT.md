# An exact all-threshold minimax law and square-root batch budget for planar Gaussian random-line descent

## Finding

**Theorem (simultaneous best-of-batch minimax).** For every two-dimensional symmetric positive-definite matrix \(H\), every symmetric positive-definite Gaussian direction covariance \(\Sigma\), every integer \(m\ge1\), and every gain threshold \(0<t<1\), the worst-start probability of failing to remove a fraction \(t\) of the current quadratic objective is exactly

\[
\boxed{\sup_{x\ne0}\Pr\{G_m(x)<t\}=\left[\frac2\pi\arctan\sqrt{\frac{Kt}{1-t}}\right]^m,\qquad K=\operatorname{cond}_2\bigl(H^{1/2}\Sigma H^{1/2}\bigr).}
\]

Here \(G_m(x)\) is the largest fractional improvement obtained by minimizing the quadratic *separately* along \(m\) independently drawn candidate lines through \(x\), then choosing the best candidate. If \(K>1\), the worst starts are exactly the nonzero directions for which \(H^{1/2}x\) is an eigenvector corresponding to the *smaller* eigenvalue of \(H^{1/2}\Sigma H^{1/2}\). If \(K=1\), every nonzero start is worst (all starts have the same gain law).

Among all positive-definite Gaussian covariances \(\Sigma\), the unique simultaneous minimax choice, up to multiplication by a positive scalar, is \(\Sigma\propto H^{-1}\). It achieves for every \(m\) and \(t\) the universal minimal worst-start failure probability

\[
\left[\frac2\pi\arcsin\sqrt{t}\right]^m.
\]

For isotropic Gaussian directions, write \(\kappa=\operatorname{cond}_2(H)\). To make the failure probability at most \(\delta\in(0,1)\) uniformly over all nonzero starts, the exact minimal number of independent candidates is

\[
m_{\min}(\kappa,t,\delta)=\left\lceil\frac{\log\delta}{\log\!\left[\frac2\pi\arctan\sqrt{\kappa t/(1-t)}\right]}\right\rceil.
\]

For fixed \(t,\delta\in(0,1)\) and \(\kappa\to\infty\),

\[
m_{\min}(\kappa,t,\delta)\sim\frac\pi2\sqrt{\frac{t}{1-t}}\,\sqrt\kappa\,\log(1/\delta).
\]

In the critical window \(m/\sqrt\kappa\to c\in(0,\infty)\), worst-start failure tends to \(\exp[-(2c/\pi)\sqrt{(1-t)/t}]\). If this ratio tends to zero, failure tends to one; if it tends to infinity, failure tends to zero. For one isotropic candidate at the worst start, the exact mean fractional gain is \(1/(1+\sqrt\kappa)\), while its median is \(1/(1+\kappa)\).

## Assumptions and scope

Let \(H\in\mathbb R^{2\times2}\) and \(\Sigma\in\mathbb R^{2\times2}\) be symmetric positive definite. Consider \(f(x)=\tfrac12 x^\top Hx\) with minimizer zero. Fix \(x\in\mathbb R^2\setminus\{0\}\), an integer \(m\ge1\), and independently sample \(u_1,\ldots,u_m\sim\mathcal N(0,\Sigma)\). For each \(i\), minimize \(f(x+s u_i)\) **exactly** over \(s\in\mathbb R\), obtaining \(x_i\). The one-candidate fractional decrease and batch fractional decrease are

\[
Z_i(x)=\frac{f(x)-f(x_i)}{f(x)},\qquad G_m(x)=\max_{1\le i\le m}Z_i(x).
\]

All probabilities are conditional on the fixed initial point. This is *parallel candidate selection from the same point*, not sequential application of \(m\) accepted line minimizations and not a joint minimization over the span of \(m\) vectors (which in two dimensions would reach the optimum almost surely for \(m\ge2\)). The threshold range is strictly \(0<t<1\). Positive scalar rescaling of \(\Sigma\) leaves the line-direction law unchanged. No claim is made for other dimensions, nonlinear objectives, inexact line searches, or correlated candidate directions.

## Proof

**1. Fractional gain and energy coordinates.** Exact differentiation of the scalar line profile gives

\[
x_i=x-\frac{u_i^\top Hx}{u_i^\top Hu_i}\,u_i,\qquad
Z_i=\frac{(u_i^\top Hx)^2}{(u_i^\top Hu_i)(x^\top Hx)}.
\]

Cauchy--Schwarz in the \(H\)-inner product gives \(0\le Z_i\le1\); the Gaussian direction has nonzero norm almost surely. Set \(y=H^{1/2}x/\|H^{1/2}x\|\) and \(v=H^{1/2}u/\|H^{1/2}u\|\). Then \(Z=(y^\top v)^2\). The unnormalized direction \(H^{1/2}u\) is Gaussian with covariance \(\Omega=H^{1/2}\Sigma H^{1/2}\). Rotate into its orthonormal eigenbasis and rescale: \(\Omega=\operatorname{diag}(1,K)\) up to a positive factor, with \(K\ge1\). Neither rotation nor positive rescaling alters the probability law relevant to angles.

**2. The exact angular law.** Write \(H^{1/2}u=R(\cos\phi,\sin\phi)\) with direction angle \(\phi\) defined modulo \(\pi\). Integrating the two-dimensional Gaussian density over radius yields its projective angular density

\[
p_K(\phi)=\frac{\sqrt K}{\pi\,[K\cos^2\phi+\sin^2\phi]},\qquad 0\le\phi<\pi.
\]

Equivalently, the ratio of independent standard Gaussians is standard Cauchy: when \(y=(1,0)\),

\[
Z=\frac{g_1^2}{g_1^2+Kg_2^2}=\frac1{1+K(g_2/g_1)^2},
\quad g_1,g_2\overset{\mathrm{iid}}\sim\mathcal N(0,1).
\]

For \(0<t<1\), its one-candidate failure probability is therefore

\[
F_K(t)=\Pr(Z<t)=\frac2\pi\arctan\sqrt{\frac{Kt}{1-t}}.
\]

The law is continuous at \(t\in(0,1)\), so using strict failure versus non-strict failure is immaterial.

**3. Prove the hard starting direction is worst at *every* threshold.** Let \(\theta\) be the projective angle of \(y\) relative to the small-eigenvalue axis, and \(r=\arccos\sqrt t\in(0,\pi/2)\). The success event \(Z\ge t\) is exactly the angular interval \([\theta-r,\theta+r]\) modulo \(\pi\), so

\[
s_K(\theta,t)=\int_{\theta-r}^{\theta+r}p_K(\phi)\,d\phi.
\]

By symmetries it suffices to examine \(0\le\theta\le\pi/2\). With \(D_K(\alpha)=K\cos^2\alpha+\sin^2\alpha\), differentiation of the endpoints gives the *exact* identity

\[
\frac{\partial s_K}{\partial\theta}=
\frac{\sqrt K\,(K-1)\sin(2\theta)\sin(2r)}
{\pi D_K(\theta+r)D_K(\theta-r)}.
\]

All factors in the denominator are strictly positive; the numerator is nonnegative, and for \(K>1\) is strictly positive in the interior. Thus \(\theta=0\) is the **unique worst projective direction** if \(K>1\), while \(K=1\) gives a rotationally uniform law. This establishes the worst-case one-candidate formula with no unproved angular optimality assumption.

**4. Batch independence and covariance minimax.** Given \(x\), the \(m\) gains are independent and identically distributed; hence \(\Pr(G_m<t)=\Pr(Z<t)^m\). The same angle \(\theta=0\) is worst for every threshold, so the previous formula raises exactly to the \(m\)-th power and is attained. Moreover \(F_K(t)\) is strictly increasing in \(K\) for \(0<t<1\); therefore every anisotropic \(\Omega\) with \(K>1\) gives strictly greater worst-start failure probability than \(K=1\). The condition \(K=1\) is equivalent to \(H^{1/2}\Sigma H^{1/2}=cI\), namely \(\Sigma=cH^{-1}\) with \(c>0\). This proves uniqueness up to scale and simultaneous minimaxity for all thresholds and batch sizes. At \(K=1\), \(\arctan\sqrt{t/(1-t)}=\arcsin\sqrt t\).

**5. Candidate budget and the sharp square-root threshold.** For isotropic covariance, \(K=\kappa\). Since \(0<F_\kappa(t)<1\), the inequality \(F_\kappa(t)^m\le\delta\) is equivalent to \(m\ge\log\delta/\log F_\kappa(t)\), proving the exact ceiling formula. For fixed \(0<t<1\), the standard expansion \(\arctan z=\pi/2-z^{-1}+O(z^{-3})\) as \(z\to\infty\) implies

\[
F_\kappa(t)=1-\frac2{\pi\sqrt\kappa}\sqrt{\frac{1-t}t}+O(\kappa^{-3/2}),
\quad
\log F_\kappa(t)=-\frac2{\pi\sqrt\kappa}\sqrt{\frac{1-t}t}+O(\kappa^{-1}).
\]

Substitute into the exact budget to obtain the asymptotic coefficient. Raising \(F_\kappa(t)\) to powers in the three regimes of \(m/\sqrt\kappa\) gives the stated trichotomy (using \(\log(1-z)\sim-z\) where needed). There is no hidden logarithmic factor in \(\kappa\).

**6. Mean and median diagnostic.** At the worst direction, direct integration of the Cauchy density, or a standard trigonometric integral, gives

\[
\mathbb E Z=\frac2\pi\int_0^{\pi/2}
\frac{\cos^2\phi}{\cos^2\phi+K\sin^2\phi}\,d\phi
=\frac1{1+\sqrt K}.
\]

This follows, for example, by setting \(s=\tan\phi\) and decomposing \(1/[(1+s^2)(1+Ks^2)]\) into simple fractions (with the \(K=1\) case obtained continuously). The unique median solves \(F_K(t)=1/2\), giving \(t=1/(1+K)\). The mean and median differ parametrically for large \(K\).

## Verification

The standalone file `verify_planar.py` uses only the Python standard library. Run `python3 verify_planar.py` with Python 3.10 or later. It checks 849 assertions, including rational exact-line energy identities, numerical normalization of the derived angular density, the derivative identity, threshold monotonicity over a grid, Cauchy-CDF probabilities, exact candidate counts, exact mean/median, independent Gaussian Monte Carlo, and the scaling limit. Deterministic seed: `20261031`. These finite computations corroborate but are **not** substitutes for the analytic proof for all positive-definite matrices, all thresholds and arbitrary candidate counts.

For example, with \(H=\operatorname{diag}(1,9)\), \(\Sigma=I\), threshold \(t=1/2\) and permitted failure \(\delta=1/10\), exactly \(11\) candidates are needed in the worst case; \(\Sigma\propto H^{-1}\) needs exactly \(4\). At \(H=\operatorname{diag}(1,100)\), the corresponding counts are \(36\) and \(4\). These are candidate-line minimizations from one fixed start, not complete optimization trajectories.

## Relationship to prior work

Stich, Müller and Gärtner's **Random Pursuit** and **Variable Metric Random Pursuit** establish and analyze exact or approximate one-dimensional randomized line-search schemes and the benefit of covariance adaptation, including convergence bounds and expected single-step progress [1,2]. In particular, the inverse-Hessian direction metric as a *general design idea* is prior work and is **not** claimed as new. The quantitative contribution here is narrower and stronger in a different direction: the exact failure probability simultaneously for all thresholds and all planar initial directions, the proof of strict stochastic minimax uniqueness across all positive-definite covariance choices, the exact best-of-independent-candidates budget, and its sharp square-root conditioning limit. General expected-progress inequalities do not automatically imply these full-distribution statements.

Shao's thesis [3] and Cartis, Fowkes and Shao [4] give higher-dimensional randomized sketch/subspace optimization frameworks, including Gaussian sketches, and convergence/complexity guarantees. Roberts and Royer [5] study probabilistic descent in randomized reduced spaces; Hare, Roberts and Royer [6] analyze expected decrease in random subspaces. Those frameworks do not supply the present fixed-point planar *exact-line* candidate-selection CDF or all-threshold minimax criterion by direct specialization of their stated results. A published result on simultaneous multi-direction candidate selection with a full angular success law would be closer and remains a residual publication-priority risk.

The proof relies on classical Cauchy ratios, Gaussian angular densities, and elementary order statistics, which are acknowledged as standard ingredients; novelty is not attributed to those ingredients in isolation.

## Limitations

This is a complete theorem only for two-dimensional strictly positive-definite quadratic objectives, centered Gaussian candidates with a common fixed SPD covariance, independent candidate draws, exact real-valued line minimization and selection of the best single candidate. The conditioning \(\kappa\) enters the isotropic sampling specialization; the general theorem uses the *energy-covariance* condition number \(K\). Neither the law nor the square-root candidate count is claimed for finite-step polling, noisy/inexact function evaluations, repeated sequential accepted updates, joint-span sketch minimization, zero-eigenvalue covariances, non-Gaussian distributions or other dimensions. The proof does not yield a total objective-oracle complexity bound, since exact line minimizations may have a different implementation cost. Independent scrutiny of the literature and proof has not been performed; an unseen specialized earlier result could cover some or all of this claim.

## References

1. S. U. Stich, C. L. Müller and B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194 (first public 2011-11-01). https://arxiv.org/abs/1111.0194
2. S. U. Stich, C. L. Müller and B. Gärtner, *Variable Metric Random Pursuit*, arXiv:1210.5114 (first public 2012-10-18), particularly Section 4 and discussion of inverse-Hessian direction covariance. https://arxiv.org/abs/1210.5114
3. Z. Shao, *On Random Embeddings and Their Application to Optimisation*, arXiv:2206.03371v1, publicly submitted 2022-06-07; Section 4. https://arxiv.org/abs/2206.03371
4. C. Cartis, J. Fowkes and Z. Shao, *Randomised Subspace Methods for Non-Convex Optimization, with Applications to Nonlinear Least-Squares*, arXiv:2211.09873v1, publicly submitted 2022-11-17. https://arxiv.org/abs/2211.09873
5. L. Roberts and C. W. Royer, *Direct Search Based on Probabilistic Descent in Reduced Spaces*, arXiv:2204.01275 (first public 2022-04-04). https://arxiv.org/abs/2204.01275
6. W. Hare, L. Roberts and C. W. Royer, *Expected Decrease for Derivative-Free Algorithms Using Random Subspaces*, arXiv:2308.04734 (first public 2023-08-09). https://arxiv.org/abs/2308.04734
