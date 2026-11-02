# Exact query-noise universality for structured zeroth-order descent on isotropic quadratics

## Finding

Consider a random orthogonal-frame forward-difference method on a strictly convex isotropic quadratic, with independent centered measurement noise at every oracle call and a single baseline evaluation reused for all directional differences. Its expected squared iterate norm obeys an **exact finite-time scalar recurrence**, valid for every admissible frame distribution, every initial point and every dimension. Consequently, the optimal difference radius is time- and stepsize-independent, and the optimal-fast-contraction stationary squared-error floor is independent of the number of sampled directions. Reusing one noisy baseline costs no additional expected squared error compared with independent baselines, while using fewer oracle calls when there is more than one direction.

For the notation below, write
\[
 r=1-2\eta\lambda+\eta^2\lambda^2\frac d\ell,\qquad
 b(h)=\eta^2\left(\frac{\lambda^2d^3h^2}{4\ell^2}+\frac{2d\sigma^2}{h^2}\right).
\]
Then, for every integer \(n\ge1\),
\[
 \boxed{\mathbb E\|X_n\|_2^2=r^n\|X_0\|_2^2+b(h)\sum_{j=0}^{n-1}r^j.}
\]
The unique minimizer of this quantity with respect to the difference radius \(h>0\), holding \(\eta,n,d,\ell,\lambda,\sigma,X_0\) fixed, is
\[
 \boxed{h_*=\left(\frac{8\sigma^2\ell^2}{\lambda^2d^2}\right)^{1/4}.}
\]
Its mean-square stationary error is finite and approached geometrically exactly for
\[
 0<\eta<\frac{2\ell}{\lambda d}.
\]
The **homogeneous** mean-square contraction factor \(r\) is minimized uniquely at \(\eta_*=\ell/(\lambda d)\); at this stepsize and \(h=h_*\),
\[
 \boxed{\lim_{n\to\infty}\mathbb E\|X_n\|_2^2=\frac{\sqrt2\,d\sigma}{\lambda},}
\]
which is independent of the number \(\ell\) of directions. This last expression is **not** a global minimum over stepsizes of the stationary noise floor: smaller stable stepsizes can trade a slower rate for a lower floor.

## Assumptions and scope

Fix integers \(d\ge2\) and \(1\le\ell\le d\), and real constants \(\lambda,\sigma,\eta,h>0\). Let the objective be \(f(x)=\lambda\|x\|_2^2/2\) on \(\mathbb R^d\). The initial point \(X_0\) is deterministic. At each integer iteration \(n\), independently of the past, sample a matrix \(P_n\in\mathbb R^{d\times\ell}\) with
\[
 P_n^\top P_n=\frac d\ell I_\ell\quad\text{almost surely},\qquad
 \mathbb E[P_nP_n^\top]=I_d,\qquad
 \mathbb E[P_n\mathbf1_\ell]=0.
\]
Haar-distributed orthogonal subframes, scaled by \(\sqrt{d/\ell}\), and uniformly chosen coordinate subframes with independent random column signs both satisfy these assumptions. Independently of all frames and past quantities, each function-value query has a fresh centered additive error of variance \(\sigma^2\); the noise law need not be Gaussian and need not have moments beyond order two.

At iteration \(n\), one baseline measurement \(f(X_n)+\varepsilon_{n,0}\) is shared across the \(\ell\) directional differences, and each displaced value \(f(X_n+hP_{n,:,j})+\varepsilon_{n,j}\) is measured independently. Thus \(\ell+1\) noisy evaluations occur per iteration. Define
\[
 G_n=\sum_{j=1}^{\ell}P_{n,:,j}\frac{f(X_n+hP_{n,:,j})+\varepsilon_{n,j}-f(X_n)-\varepsilon_{n,0}}h,
 \qquad X_{n+1}=X_n-\eta G_n.
\]
The comparison procedure takes an independent baseline for every direction, using \(2\ell\) noisy evaluations, with all other choices unchanged.

## Proof

Write \(c=d/\ell\), \(u=\mathbf1_\ell\), \(P=P_n\) and \(\zeta=(\varepsilon_{n,1},\ldots,\varepsilon_{n,\ell})^\top-\varepsilon_{n,0}u\). The quadratic expansion is exact, not asymptotic:
\[
 G_n=\lambda PP^\top X_n+\frac{\lambda hc}{2}Pu+\frac1hP\zeta.
\]
Orthogonality gives \((PP^\top)^2=cPP^\top\), \(\|Pu\|^2=c\ell=d\), and \(PP^\top Pu=cPu\). The frame symmetry and isotropy give \(\mathbb E[Pu]=0\) and \(\mathbb E[PP^\top]=I_d\). Since the oracle errors are independent and centered,
\[
 \mathbb E[\zeta\zeta^\top]=\sigma^2(I_\ell+uu^\top).
\]
The zero-mean oracle-noise cross terms vanish conditionally on \(P,X_n\). The cross term between \(\lambda PP^\top X_n\) and \(\lambda hcPu/2\) vanishes after averaging over \(P\), since it is proportional to \(X_n^\top\mathbb E[Pu]\). The remaining terms give the two conditional identities
\[
 \mathbb E[G_n\mid X_n]=\lambda X_n,
\]
\[
 \mathbb E[\|G_n\|_2^2\mid X_n]
 =\lambda^2c\|X_n\|_2^2
 +\frac{\lambda^2h^2c^2d}{4}
 +\frac{\sigma^2}{h^2}\left(\operatorname{tr}(P^\top P)+\|Pu\|^2\right)
 =\lambda^2\frac d\ell\|X_n\|_2^2
 +\frac{\lambda^2d^3h^2}{4\ell^2}
 +\frac{2d\sigma^2}{h^2}.
\]
In the first equality of the last display, the trace term is constant for every admissible frame. Expanding \(\|X_n-\eta G_n\|^2\) and conditioning yields
\[
 \mathbb E[\|X_{n+1}\|_2^2\mid X_n]=r\|X_n\|_2^2+b(h).
\]
Independence from the past permits repeated conditioning, proving the claimed exact formula for every \(n\ge1\). Furthermore,
\[
 r=(1-\eta\lambda)^2+\eta^2\lambda^2\left(\frac d\ell-1\right)\ge0,
\]
so \(r<1\) is equivalent to \(0<\eta<2\ell/(\lambda d)\). Since \(b(h)>0\), at \(r=1\) the expected squared norm grows linearly and at \(r>1\) it grows exponentially; for \(0\le r<1\) it converges to \(b(h)/(1-r)\). For \(r=0\), the same expression gives the constant expected squared error after the first update.

Because \(r\) is independent of \(h\), the difference-radius problem for any finite horizon and any positive stepsize reduces to minimizing
\[
 A h^2+B h^{-2},\qquad A=\frac{\lambda^2d^3}{4\ell^2}>0,\quad B=2d\sigma^2>0.
\]
The arithmetic-geometric mean inequality gives the unique minimum at \(h^4=B/A\), establishing \(h_*\). The quadratic polynomial \(r(\eta)\) is strictly convex and is minimized at \(\eta_*\), where \(r_*=1-\ell/d\). At \(h_*\) the innovation's parenthesis is \(2\sqrt{AB}=\sqrt2\lambda\sigma d^2/\ell\). Therefore
\[
 \frac{\eta_*^2\,2\sqrt{AB}}{1-r_*}
 =\frac{\sqrt2\sigma d}{\lambda}.
\]
Finally, replacing the single shared baseline error by \(\ell\) independent baseline errors replaces the covariance \(\sigma^2(I_\ell+uu^\top)\) with \(2\sigma^2 I_\ell\). Since \(P^\top P=cI_\ell\), both covariances give the identical noise contribution \(2d\sigma^2/h^2\) to \(\mathbb E\|G_n\|^2\). The two oracle schemes consequently have identical expected squared iterate norms at **every** horizon, although their joint covariance matrices and full iterate distributions need not coincide. For \(\ell>1\), sharing a baseline saves \(\ell-1\) evaluations per iteration.

## Verification

The included `verify.py` uses exact symbolic arithmetic and exhaustive independent signed-coordinate-frame and Rademacher-oracle branches for several dimension/rank choices. It independently checks gradient means, gradient squared norms, iterate squared norms, the two-step recurrence and the optimal-radius identities. Run `python verify.py` after installing `sympy` as specified by `requirements.txt`. The enumerations test finite parameter instances only; the proof above establishes all stated continuous parameters, all admissible frame laws and every horizon.

## Relationship to prior work

Rando, Molinari, Villa and Rosasco (2022, subsequent revisions), *Stochastic Zeroth Order Descent with Structured Directions*, introduced the structured \(\ell\)-direction stochastic finite-difference scheme and convergence analysis for a stochastic function model in which the same sampled input is used in the directional differences. The independent-error **per-query** model considered here does not cancel noise across the two evaluations and is not equivalent to their common-input model. Their convergence rates do not directly imply the present all-horizon squared-error identity, exact constant-step stability boundary, optimal radius or shared-baseline comparison.

Kozak, Molinari, Rosasco, Tenorio and Villa (2021), *Zeroth order optimization with orthogonal random directions*, analyze orthogonal finite differences primarily with exact function values and give general rates; their finite-difference discretization error is not a substitute for independently resampled query noise. Berahas, Cao, Choromanski and Scheinberg (2019), *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*, analyze approximation accuracy and sampling radii under bounded (possibly deterministic) function errors, without the current exact iterative noise law. Ordinary finite-difference bias/noise balancing and random-projector calculations are acknowledged classical ingredients; the asserted contribution is their exact joint structural consequence for this independent-query, arbitrary-isotropic-frame, all-horizon setting. A more general unlocated theorem may imply the formulas; no claim of exhaustive publication priority is made.

## Limitations

The result concerns Euclidean mean-square error, an isotropic strictly convex quadratic, independent fresh query errors, sign-balanced isotropic orthogonal frames, and fixed positive parameters. It does not cover a general Hessian, correlated oracle noise, nonzero-mean or infinite-variance errors, arbitrary non-symmetric frame distributions, an optimal iteration budget, floating-point errors, or a universal stationary law. The equality of shared and separate baseline schemes is for the expected squared iterate norm, not equality of full distributions. The stationary floor reported at \(\eta_*\) is specific to the fastest homogeneous mean-square contraction criterion. Independent scientific validation and exhaustive publication-priority assessment have not been performed.

## References

1. Marco Rando, Cesare Molinari, Silvia Villa and Lorenzo Rosasco. *Stochastic Zeroth Order Descent with Structured Directions*. arXiv:2206.05124, first posted 10 June 2022. https://arxiv.org/abs/2206.05124
2. David Kozak, Cesare Molinari, Lorenzo Rosasco, Luis Tenorio and Silvia Villa. *Zeroth order optimization with orthogonal random directions*. arXiv:2107.03941, first posted 8 July 2021. https://arxiv.org/abs/2107.03941
3. Albert S. Berahas, Liyuan Cao, Krzysztof Choromanski and Katya Scheinberg. *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*. arXiv:1905.01332, first posted 3 May 2019. https://arxiv.org/abs/1905.01332
