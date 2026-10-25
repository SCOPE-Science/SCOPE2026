# Sharp phase-controlled two-step mass fluctuations in stochastic cubic Schrodinger splitting

## Finding
For a scalar cubic stochastic Schrödinger Lie–Trotter step with **real, rank-one additive Gaussian noise**, preserving the expected squared amplitude does not determine its fluctuations. With \(v=\sigma^2h\), \(\theta=\omega h\), and \(\beta=\kappa hv\), the exact mass after two steps has
\[
\mathbb E M_2=2v,\qquad
\frac{\operatorname{Var}(M_2)}{v^2}=6+2(1+16\beta^2)^{-3/4}
\cos\left(2\theta+\frac32\arctan(4\beta)\right).
\]
The sharp phase-controlled range is
\[
6-2(1+16\beta^2)^{-3/4}
\ \le\ \frac{\operatorname{Var}(M_2)}{v^2}\ \le\
6+2(1+16\beta^2)^{-3/4}.
\]
The lower and upper bounds are attained, respectively, exactly when
\[
\theta=\frac\pi2-\frac34\arctan(4\beta)\pmod\pi,
\qquad
\theta=-\frac34\arctan(4\beta)\pmod\pi.
\]
For every \(\beta>0\), the minimum is strictly greater than \(4\). In comparison, replacing the real kick by **circular isotropic complex Gaussian noise with the same mean squared kick** makes the mass variance exactly \(4v^2\), independently of both phases. This shows that the mean-mass trace law is insensitive to noise geometry while its first nontrivial mass fluctuation is not.

For zero linear phase, \(\theta=0\), there is exactly one nontrivial minimizing nonlinear strength:
\[
\beta_*=\tfrac14\tan(2\pi/5)=0.7694208842938133\ldots,
\qquad
\frac{\operatorname{Var}(M_2)}{v^2}\bigg|_{\beta_*}
=6-2\cos^{5/2}(2\pi/5)=5.893833889735546\ldots.
\]
The variance is strictly decreasing before this point and strictly increasing afterward, approaching \(6v^2\) from below as \(\beta\to\infty\).

## Assumptions and scope
Fix arbitrary \(h>0\), \(\sigma>0\), \(\kappa\ge0\), and \(\omega\in\mathbb R\). Let independent \(G_1,G_2\sim N(0,1)\). The scalar stochastic Schrödinger model is
\[
 i\,dZ_t=(\omega+\kappa|Z_t|^2)Z_t\,dt+\sigma\,dW_t,
\]
where \(W\) is a **real** Brownian motion and \(Z_0=0\). Its stated numerical scheme alternates the exact nonlinear phase flow and an exponential-linear additive-noise step:
\[
Z_{j+1}=e^{-i\omega h}
\bigl(e^{-i\kappa h|Z_j|^2}Z_j-i\sigma\sqrt h\,G_{j+1}\bigr),
\qquad j=0,1.
\]
The scalar complex amplitude has squared mass \(M_j=|Z_j|^2\). All probability statements are with respect to the two independent real Gaussian increments. The phase envelope optimizes \(\theta=\omega h\) while holding \(h,\sigma,\kappa\), hence \(\beta\), fixed; varying the linear frequency is permitted. No restriction on \(\theta\) is needed because \(\omega\) may be any real number.

The isotropic comparison replaces each real kick \(-i\sqrt v\,G_j\) by \(-i\sqrt{v/2}(G_j+iH_j)\), with all \(G_j,H_j\) mutually independent standard real Gaussians. Thus both noise conventions have \(\mathbb E|\text{one kick}|^2=v\), but different noise covariance geometry. The comparison is not a claim that these models have identical driving noise.

## Proof
Set \(v=\sigma^2h\), \(\theta=\omega h\), and \(\beta=\kappa hv\). The first step is exactly
\[
Z_1=-i\sqrt v\,e^{-i\theta}G_1.
\]
Substitute this into the second step and remove a common unit-modulus factor. This gives the pathwise identity
\[
\frac{M_2}{v}
=G_1^2+G_2^2+2G_1G_2\cos(\theta+\beta G_1^2).
\tag{1}
\]
Oddness and independence make the cross term mean zero, proving \(\mathbb EM_2=2v\). Let \(A=G_1^2+G_2^2\) and \(B=2G_1G_2\cos(\theta+\beta G_1^2)\). By conditional expectation in \(G_2\), \(\mathbb E(AB)=0\). Since \(\operatorname{Var}(A)=4\), the variance of (1) is
\[
\frac{\operatorname{Var}(M_2)}{v^2}
=4+4\,\mathbb E\left[G_1^2\cos^2(\theta+\beta G_1^2)\right].
\tag{2}
\]
The classical Gaussian integral, with its principal analytic branch, is
\[
\mathbb E(e^{itG_1^2})=(1-2it)^{-1/2},\qquad
\mathbb E(G_1^2e^{itG_1^2})=(1-2it)^{-3/2}.
\tag{3}
\]
The second identity follows by differentiation under the Gaussian integral; this is justified by the integrable factor \(G_1^2\). Insert \(\cos^2 x=(1+\cos(2x))/2\) into (2), take \(t=2\beta\) in (3), and obtain
\[
\frac{\operatorname{Var}(M_2)}{v^2}
=6+2\operatorname{Re}\left[e^{2i\theta}(1-4i\beta)^{-3/2}\right]
=6+2(1+16\beta^2)^{-3/4}
\cos\left(2\theta+\tfrac32\arctan(4\beta)\right).
\tag{4}
\]
The amplitude is positive for all finite \(\beta\ge0\). Therefore the exact minima and maxima over \(\theta\), including **all equality classes modulo \(\pi\)**, follow by setting the cosine to \(-1\) and \(+1\). At positive \(\beta\), the amplitude is strictly smaller than \(2\), so the lower variance is strictly greater than \(4v^2\).

For the zero-phase optimization put \(t=\arctan(4\beta)\in[0,\pi/2)\). Its \(\beta\)-dependent signed term is
\[
F(t)=\cos^{3/2}t\,\cos(3t/2),\qquad
F'(t)=-\tfrac32\cos^{1/2}t\,\sin(5t/2).
\tag{5}
\]
Here the derivative is negative for \(0<t<2\pi/5\), zero only at \(t=2\pi/5\), and positive for \(2\pi/5<t<\pi/2\). Since \(t\) increases strictly with \(\beta\), this proves the unique global minimum and its full monotonicity profile. At the minimum \(\cos(3\pi/5)=-\cos(2\pi/5)\), yielding the stated exact value. Equation (4) gives convergence to \(6v^2\) as \(\beta\to\infty\).

Finally, with the circular complex kicks defined above, \(|Z_1|^2\) has exponential distribution with mean \(v\) and variance \(v^2\). Conditional on \(Z_1\), the second isotropic kick has squared-norm variance \(v^2\), and the cross term \(2\operatorname{Re}(\overline Z_1\,\xi_2)\) has conditional variance \(2v|Z_1|^2\); their conditional covariance is zero by centered Gaussian symmetry. The law of total variance gives
\[
\operatorname{Var}(M_2)
=\underbrace{v^2}_{\operatorname{Var}(|Z_1|^2)}
+\underbrace{v^2+2v\,\mathbb E|Z_1|^2}_{\mathbb E\operatorname{Var}(M_2\mid Z_1)}
=4v^2.
\]
This holds irrespective of nonlinear phase rotation because such a rotation preserves \(|Z_1|\). It does not assert equality of the full real-noise and complex-noise schemes.

## Verification
The accompanying standalone Python 3 standard-library script, `verification/mass_variance.py`, evaluates (4) independently against numerical Gaussian integration of (2), checks the exact phase envelope at multiple parameter values, and checks the zero-phase critical value. Executing the packaged script produced **633 passing deterministic assertions**. Its finite numerical checks are not proofs of the universal statements; those follow from identities (1)–(5), Gaussian integration, and the conditional-variance argument above.

## Relationship to prior work
Bréhier and Cohen [1], Section 3, equation (8) and Proposition 6, established the splitting architecture and exact linear growth of the **expected mass** for additive-noise nonlinear Schrödinger equations; the construction here is its scalar phase-flow analogue. That result is acknowledged and not claimed as new. Anton and Cohen [2] studied exponential integration and mass/energy/momentum trace formulas for additive Itô Schrödinger noise; their expected-value formulas do not imply the phase-dependent two-step mass variance. The Gaussian quadratic characteristic function in (3), the generic variance decomposition, and the general strategy of stochastic splitting are classical tools, not originality claims. The assessed statement concerns the complete two-step rank-one mass-variance envelope, its phase optimizers, the unique zero-phase nonlinear minimum, and the sharp isotropic comparison. An equivalent specialized calculation may exist in other literature.

## Limitations
Exactly **two steps**, one **complex scalar** degree of freedom, independent standard Gaussian increments, exact phase evaluations, additive noise, and fixed physical parameters are essential to the proved statement. The phase envelope is not a finite-step global optimizer over arbitrary time-varying frequencies or adaptive integrators. The isotropic comparison changes the driving-noise covariance and is not an error bound or a model-equivalence claim. No result is asserted for spatially coupled PDE discretizations, higher steps, general fourth moments, independent external audit, long-time variance, strong error, or variance relative to the exact continuous-time solution. Publication priority for this specialized fluctuation calculation remains a risk notwithstanding targeted comparison.

## References
[1] C.-E. Bréhier and D. Cohen, *Analysis of a splitting scheme for a class of nonlinear stochastic Schrödinger equations*, arXiv:2007.02354, first posted 2020-07-05; especially Section 3.1, equation (8), Proposition 6. https://arxiv.org/html/2007.02354v2

[2] R. Anton and D. Cohen, *Exponential integrators for stochastic Schrödinger equations driven by Ito noise*, arXiv:1601.06623, first posted 2016-01-25; Sections 3–4. https://arxiv.org/html/1601.06623v1
