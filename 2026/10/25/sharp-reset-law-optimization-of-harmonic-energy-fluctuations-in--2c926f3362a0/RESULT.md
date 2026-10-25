# Sharp reset-law optimization of harmonic-energy fluctuations in a logarithmic-harmonic diffusion

## Finding

Consider diffusion in the logarithmic-harmonic potential \(U(x)=-\alpha\log x+\beta x^2/2\) and independent Poisson resets to fresh locations. The stationary variance of the **harmonic contribution** \(H(x)=\beta x^2/2\) has a global and unique optimal reset law precisely in the open parameter region \(\alpha>D\), \(0<r<\beta(\alpha-D)/D\). The optimizer is a point mass at
\[
R_{\mathrm{opt}}=\sqrt{\frac{\alpha-D}{\beta}-\frac{Dr}{\beta^2}}.
\]
Outside that region the infimum is approached as the reset point tends to the origin, but is not attained by any reset law supported on strictly positive positions. Even among all randomized reset protocols, no nondegenerate reset law can tie the optimal point reset. The exact stationary fluctuation penalty is quadratic in both the mean squared reset location's displacement and the dispersion of squared reset locations.

## Assumptions and scope

Fix \(\alpha,\beta,D,r>0\). Between resets let the nonnegative process \(Y\) be the canonical Cox–Ingersoll–Ross (squared-radial) diffusion
\[
dY_t=2(\alpha+D-\beta Y_t)\,dt+2\sqrt{2DY_t}\,dW_t,
\qquad X_t=\sqrt{Y_t}.
\]
For \(X_t>0\), Itô's formula gives exactly the logarithmic-harmonic Langevin equation
\[
dX_t=(\alpha/X_t-\beta X_t)\,dt+\sqrt{2D}\,dW_t.
\]
This squared-process definition specifies the standard nonnegative extension when the origin is accessible. At independent rate-\(r\) Poisson event times, replace \(X\) by a fresh independent draw \(R\) from any fixed probability law on \((0,\infty)\) with \(\mathbb E[R^4]<\infty\). The Brownian motion, reset clock, and reset locations are independent. A deterministic reset is a point-mass law.

Write \(Z=R^2\), \(z=\mathbb EZ>0\), \(w=\operatorname{Var}(Z)\ge0\), and \(a=\alpha+D\). The observable under optimization is the harmonic contribution \(H=\beta Y/2\). It is **not** the full potential \(U\); no claim is made about full-potential-energy fluctuations, heat, work, or resetting cost.

## Proof

**1. Existence, uniqueness and moment finiteness.** At a reset, the post-reset value is sampled independently of the past. Couple two copies using the same Poisson clock, reset draw, and Brownian increments: after their first common reset they coincide. Therefore their total-variation distance is at most the probability of no reset, \(e^{-rt}\), and there is at most one stationary law. The stationary renewal-age mixture exists: sample an independent exponential age \(T\) of rate \(r\), an independent reset value \(Z\), and run the nonreset CIR diffusion for time \(T\) from \(Z\). CIR transition moments up to order two are bounded by constants times \(1+Z^2\), so the mixture has a finite second moment in \(Y\). It is invariant under the reset semigroup by the exponential renewal identity, hence unique.

**2. Two closed generator equations.** For a smooth polynomial \(f\), the complete reset generator is
\[
\mathcal Lf(y)=2(a-\beta y)f'(y)+4Dyf''(y)+r(\mathbb Ef(Z)-f(y)).
\]
Let \(m_1=\mathbb E_*Y\), \(m_2=\mathbb E_*Y^2\) denote stationary moments. Applying the generator to \(f(y)=y\) and \(f(y)=y^2\), respectively, yields
\[
(2\beta+r)m_1=2a+rz,\qquad
(4\beta+r)m_2=4(a+2D)m_1+r(z^2+w).
\]
These two identities, justified by the finite-moment renewal representation, are sufficient to determine \(m_1\) and \(m_2\), without integrating any confluent-hypergeometric stationary density.

**3. Exact completed-square identity.** Substitute the preceding equations into \(\operatorname{Var}_*(Y)=m_2-m_1^2\). Define
\[
z_*:=\frac{\alpha-D}{\beta}-\frac{Dr}{\beta^2},\qquad
K:=\frac{4\beta^2r}{(2\beta+r)^2(4\beta+r)}>0.
\]
Direct expansion and cancellation give, identically for every admissible reset law,
\[
\boxed{\operatorname{Var}_*(Y)=
\frac{4D[2\beta(\alpha+D)-Dr]}{\beta^2(4\beta+r)}
+K(z-z_*)^2+\frac{r}{4\beta+r}w.}
\]
Multiplication by \(\beta^2/4\) gives the exact variance of \(H=\beta Y/2\). The displayed constant is an *algebraic reference value at the unconstrained optimum*; it need not itself be positive when \(z_*\le0\), because in that regime the unconstrained point lies outside the physical domain.

**4. Global optimality and sharp boundary.** Every admissible reset law has \(z>0\) and \(w\ge0\); \(w=0\) holds exactly when \(R\) is almost surely constant (since \(R>0\)). If \(z_*>0\), the two strictly nonnegative penalty terms vanish simultaneously only at the single deterministic law \(R=\sqrt{z_*}\). Thus this is the unique minimizer even among all distributions, with exact quantitative stability. The condition \(z_*>0\) is equivalent to \(\alpha>D\) and \(0<r<r_c\), where \(r_c=\beta(\alpha-D)/D\). The optimizing location is below the physical potential minimum because \(z_*<\alpha/\beta\).

If \(z_*\le0\), then for any \(z>0\), \((z-z_*)^2>(0-z_*)^2\), and the dispersion penalty is nonnegative. No admissible reset law reaches the boundary infimum, which is approached using deterministic \(R=\varepsilon\downarrow0\). For the critical line approached from below,
\[
z_* =\frac D{\beta^2}(r_c-r),\qquad
R_{\mathrm{opt}}=\frac{\sqrt D}{\beta}\sqrt{r_c-r}.
\]
This proves the unique interior-to-boundary transition, its exact square-root vanishing, and all asserted equality conditions.

## Verification

The standalone reproducibility program `verify.py` checks stationary moments from an independently sampled CIR transition mixture (an exponential time since the last reset, followed by a noncentral chi-square CIR transition). Its fixed-seed tests cover deterministic interior reset, a two-point randomized law with the same mean square, an off-optimum deterministic reset, boundary-regime resets, and an accessible-origin parameter choice. It also verifies the completed-square and reset-law dispersion-penalty identities at several parameter values. The independent stationary samples agree with the analytical means and variances to the recorded Monte Carlo tolerances. An additional symbolic expansion directly checks the completed-square equality; the proof above is analytic and does not depend on Monte Carlo tests.

For example, at \((\alpha,\beta,D,r)=(3,2,1,1)\), one has \(r_c=4\), \(z_*=3/4\), \(R_{\mathrm{opt}}=\sqrt3/2\), and \(\operatorname{Var}_*(Y)=5/3\). Replacing the point reset by a law with \(Z\in\{1/4,5/4\}\) equally likely increases the variance by exactly \(1/36\), entirely due to reset-law dispersion.

## Relationship to prior work

Gültekin (arXiv:2306.08770) gives the original logarithmic-harmonic reset model and its fixed-point-reset stationary density in confluent-hypergeometric form, including morphology changes depending on \(\alpha/D\), \(r\), and the reset location. The stationary density and those morphology thresholds are prior results. The contribution here is a sharp, explicit **global variance minimization over arbitrary reset-location laws**, a reset-rate critical boundary, and the exact penalty for stochastic reset-site dispersion.

Olsen (arXiv:2310.04840; *Physical Review E* 108, 044120) develops a general stationary moment method for resetting to distributions and applies it to additive Ornstein–Uhlenbeck and run-and-tumble dynamics in harmonic potentials. Its additive OU variance formula is not the variance of \(X^2\) for a logarithmic-harmonic diffusion. In the present process, the squared coordinate has square-root multiplicative noise (CIR), not the additive OU noise treated there. The method of using generator moment equations is not claimed as original; the parameter-complete global optimal-law classification is the claim.

## Limitations

The variance minimized is that of the **harmonic component** \(\beta X^2/2\), not the logarithmic-harmonic total potential or physical dissipation. Resetting has no energetic cost in the objective, reset events occur at a constant independent Poisson rate, and reset sites are independently identically distributed with finite fourth moment. The model uses the canonical nonnegative squared-radial extension at an accessible origin. No claim is made for state-dependent resets, finite-time fluctuations, time-dependent protocols, or non-Markovian driving. The originality comparison is finite and does not exclude an unlocated equivalent treatment in general affine jump-diffusion or reset-control literature. Independent scientific assessment has not been performed.

## References

- Ö. Gültekin, *The steady state distribution for diffusion in a logarithmic-harmonic potential with stochastic resetting*, arXiv:2306.08770 (first public preprint, 14 June 2023), https://arxiv.org/abs/2306.08770 .
- K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (7 October 2023); *Physical Review E* **108**, 044120 (2023), https://doi.org/10.1103/PhysRevE.108.044120 .
- D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, *Physical Review E* **98**, 022129 (2018), https://doi.org/10.1103/PhysRevE.98.022129 (background on reset generators; not a source of the optimization theorem).
