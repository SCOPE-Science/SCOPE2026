# Sharp two-step termination frontier for coupled Gaussian subspace Newton

## Finding

An exact two-step planar subspace Newton method can terminate with positive probability even though **both individual sketch vectors have precisely the standard Gaussian law**. Dependence between the sketches is decisive: the sharp achievable success probability for condition number \(\kappa\ge1\) is
\[
q_*(\kappa)=\frac4\pi\arctan\!\left(\frac1{\sqrt\kappa}\right).
\]
A nonjointly-Gaussian dependence achieves this bound. For \(\kappa>1\), no jointly Gaussian sketch pair with these same marginals achieves exact termination with positive probability. The sharp success probability equals one at the isotropic endpoint and decays as \(4/(\pi\sqrt\kappa)\) as \(\kappa\to\infty\).

## Assumptions and scope

Let \(H\) be a real symmetric positive-definite \(2\times2\) matrix, with ordered eigenvalues \(\lambda_1\ge\lambda_2>0\) and condition number \(\kappa=\lambda_1/\lambda_2\). Minimize the scalar quadratic \(f(x)=\tfrac12 x^\mathsf THx\), starting from an arbitrary deterministic \(x_0\ne0\), and make exact rank-one subspace Newton steps with unit gain:
\[
x_{k+1}=x_k-\frac{s_{k+1}s_{k+1}^\mathsf THx_k}{s_{k+1}^\mathsf THs_{k+1}}.
\]
The sketch pair \((s_1,s_2)\) is allowed any coupling such that *separately* \(s_i\sim N(0,I_2)\) for \(i\in\{1,2\}\). Its joint law need not be Gaussian and is allowed to depend on the fixed Hessian \(H\), but not on the initial vector. Almost-sure termination and work statements use *independent copies of a common coupled pair* across consecutive two-step blocks; within a block the two sketches remain dependent. Every statement concerns exact algebraic equality, not floating-point convergence to a tolerance.

## Proof

**1. Projective reduction.** Rotate to eigenvectors of \(H\) and divide by \(\lambda_2\), which do not affect a standard Gaussian sketch marginal or the projected update. Thus take \(H=\operatorname{diag}(\kappa,1)\). Write \(y=H^{1/2}x\) and \(u=H^{1/2}s/\|H^{1/2}s\|_2\). A step becomes \(y^+=(I-uu^\mathsf T)y\). Since the initial vector is nonzero and \(u_1\) has a continuous angular density, \(y_1\ne0\) almost surely. In the plane, \(y_1\) lies on the line perpendicular to \(u_1\), so \(y_2=0\) if and only if \(u_2\perp u_1\), outside a null event. Consequently the maximum termination probability is independent of the initial nonzero vector.

**2. Angular marginal and upper bound.** For \(s\sim N(0,I_2)\) and \(u=(\cos\theta,\sin\theta)\), the centered elliptical Gaussian \(H^{1/2}s\) has direction density
\[
p_\kappa(\theta)=\frac{\sqrt\kappa}{2\pi(\cos^2\theta+\kappa\sin^2\theta)},\qquad 0\le\theta<2\pi.
\]
This follows by integrating its joint density in polar coordinates, since the conditional radial precision is \(a(\theta)=\cos^2\theta/\kappa+\sin^2\theta\). On the *projective* circle \(\theta\bmod\pi\), the two marginal densities to match for perpendicularity are \(2p_\kappa(\theta)\) and \(2p_\kappa(\theta+\pi/2)\). In any coupling of two real random variables with respective densities \(f\) and \(g\), the probability of equality is at most \(\int\min(f,g)\), because the law restricted to the equality diagonal is dominated by both marginals. Hence
\[
\Pr(y_2=0)\le \int_0^{2\pi}\min\{p_\kappa(\theta),p_\kappa(\theta+\pi/2)\}\,d\theta.
\]
By quadrant symmetry the minimum changes branch at \(\pi/4\). With \(t=\tan\theta\), the overlap evaluates *exactly* to
\[
8\int_0^{\pi/4}\frac{\sqrt\kappa\,d\theta}{2\pi(\sin^2\theta+\kappa\cos^2\theta)}
=\frac{4\sqrt\kappa}{\pi}\int_0^1\frac{dt}{t^2+\kappa}
=\frac4\pi\arctan\!\left(\frac1{\sqrt\kappa}\right).
\]

**3. Achievability with exact Gaussian marginals.** Define \(p(\theta)=p_\kappa(\theta)\), \(g(\theta)=p_\kappa(\theta+\pi/2)\), and \(h(\theta)=\min(p(\theta),g(\theta))\) on the full angular circle. Draw \(\theta_1\sim p\), then with conditional probability \(h(\theta_1)/p(\theta_1)\) put \(\phi=\theta_1\). Otherwise draw \(\phi\) from density \((g-h)/(1-q_*)\). Set \(\theta_2=\phi+\pi/2\) modulo \(2\pi\). This is the explicit maximal-coupling construction: \(\phi\) has density \(g\), therefore \(\theta_2\) has density \(p\); and \(\Pr(\theta_2=\theta_1+\pi/2)=q_*\). At \(q_*=1\), omit the zero-mass residual branch.

To lift each coupled angle to its full standard Gaussian vector marginal, conditionally and independently choose \(R_i\ge0\) with density \(a(\theta_i)r\exp(-a(\theta_i)r^2/2)\), where \(a(\theta)=\cos^2\theta/\kappa+\sin^2\theta\). Define \(s_i=H^{-1/2}R_i(\cos\theta_i,\sin\theta_i)^\mathsf T\). The angular density multiplied by this radial density is precisely the polar decomposition of \(N(0,H)\), so each \(s_i\) is *exactly* \(N(0,I_2)\). On the matching branch the transformed directions are perpendicular, giving \(x_2=0\). This attains the upper bound.

**4. Joint-Gaussian rigidity.** Suppose the full pair is jointly Gaussian with the stated marginals. Its conditional representation is \(s_2=Cs_1+Z\), where \(Z\) is a centered Gaussian independent of \(s_1\) with covariance \(I-CC^\mathsf T\ge0\). Perpendicularity means \(s_1^\mathsf THs_2=0\). If \(\operatorname{Cov}(Z)\ne0\), this scalar, conditionally on almost every \(s_1\), has a nondegenerate normal distribution; hence its zero event has probability zero. If instead \(Z=0\) almost surely, then \(C\) is orthogonal. A nonzero positive-probability zero event for the polynomial \(s_1^\mathsf THCs_1\) forces \(HC+C^\mathsf TH=0\). In two dimensions this entails \(HC=c\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), and \(C^\mathsf TC=I\) forces \(H\) to have equal eigenvalues. Therefore every jointly Gaussian coupling has zero two-step success probability for \(\kappa>1\). When \(\kappa=1\), the coupling \(s_2=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}s_1\) is jointly Gaussian and succeeds surely.

**5. Exact finite-termination clock.** Generate successive pairs independently, each with the optimal within-pair coupling above. Conditional on a nonzero iterate at the beginning of a pair, the independent first Gaussian sketch has zero probability of solving immediately. The pair solves exactly if and only if its own two transformed sketch directions are perpendicular, an event with probability \(q_*\) independent of the current iterate and of other pairs. Thus if \(T=\inf\{k\ge1:x_k=0\}\), then
\[
\Pr(T=2j)=q_*(1-q_*)^{j-1}\quad(j=1,2,\ldots),\qquad \mathbb ET=\frac2{q_*}.
\]
In particular \(T<\infty\) almost surely for every finite positive-definite \(H\), including arbitrarily large finite condition number.

## Verification

The standalone `verify.py` uses only the Python standard library and a deterministic random seed. It implements the *actual* full-Gaussian marginal lift, residual-density sampling in the maximal coupling, the exact Newton iterates, and quadrature of the analytic overlap. Running `python verify.py` checked \(64{,}000\) generated sketch pairs over four spectral ratios, two marginal variances for each sketch, and successful-update residuals at numerical roundoff level. These are finite diagnostics; the identity, all-condition-number optimality, Gaussian rigidity, and the infinite-horizon stopping law are established by the exact argument above, not the simulation.

## Relationship to prior work

Gower, Kovalev, Lieder, and Richtárik introduced randomized subspace Newton and its unit-gain exact-quadratic specialization in **RSN: Randomized Subspace Newton**, arXiv:1905.10874v1 (first public 2019-05-26), Algorithm 1 and associated projection lemmas. The iteration uses fresh sketches and its convergence results concern standard marginal/incremental rates, rather than sharp exact finite termination under two-step dependence. Dereziński and Rebrova, arXiv:2208.09585v1, give sharp expected one-step sketch-and-project spectral bounds, including randomized subspace Newton in Section 3.4, but do not give a two-sketch coupling law. Yu and collaborators' **Orthogonal Random Features**, arXiv:1610.09072v1, construct orthogonal Gaussian-marginal rows by angular orthogonalization and independent chi radii. This covers the isotropic orthogonality *mechanism* but does not imply the anisotropic sharp overlap probability under fixed standard Gaussian marginals or the impossibility within the jointly Gaussian class. The standard maximal-coupling inequality is an essential known tool; the result's specific contribution is its exact evaluation for the algorithmic Hessian geometry, an explicit Gaussian lift, and the joint-Gaussian obstruction.

## Limitations

The theorem is planar, uses a fixed strongly convex quadratic and exact arithmetic, and permits pairs whose joint distribution is not Gaussian and is designed using \(H\). It does not offer a computationally efficient general-purpose sketching scheme or a higher-dimensional extension. The claimed optimality is only for two sketches with the stated *marginal* laws; unrestricted deterministic or other non-Gaussian sketches can solve a two-dimensional quadratic in two steps with certainty. It does not contradict convergence guarantees proved under independent sketches. Equivalent specialized treatments in unindexed literature remain possible.

## References

1. R. M. Gower, D. Kovalev, F. Lieder, P. Richtárik, *RSN: Randomized Subspace Newton*, arXiv:1905.10874v1, first submitted 2019-05-26, https://arxiv.org/abs/1905.10874.
2. M. Dereziński and E. Rebrova, *Sharp Analysis of Sketch-and-Project Methods via a Connection to Randomized Singular Value Decomposition*, arXiv:2208.09585v1, first submitted 2022-08-20, https://arxiv.org/abs/2208.09585.
3. F. X. Yu et al., *Orthogonal Random Features*, arXiv:1610.09072v1, first submitted 2016-10-28, https://arxiv.org/abs/1610.09072.
4. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM J. Matrix Anal. Appl. 36 (2015), 1660–1690, https://doi.org/10.1137/15M1025487.
