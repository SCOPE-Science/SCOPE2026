# Sharp finite-population outer edge for harmonically coupled planar run-and-tumble rings

## Finding

For every fixed integer \(N\geq2\) and every persistence ratio \(\alpha>0\), the stationary distance \(L\) of one planar run-and-tumble particle from the centroid of an all-to-all harmonically attracting population is **compactly supported**, with sharp outer radius
\[
L_*=\frac{2(N-1)}{N}\frac{v_0}{N\kappa}.
\]
As \(\varepsilon\downarrow0\), its upper-tail probability has the exact asymptotic
\[
\Pr\{L>L_*(1-\varepsilon)\}
\sim C_{N,\alpha}\,\varepsilon^{\,N\alpha+(N-1)/2},
\]
where
\[
C_{N,\alpha}=\frac{2^{\,2N\alpha+1/2}(N-1)^{(N-1)(\alpha+1/2)}\Gamma(1+\alpha)^N}
{\pi^{(N-1)/2}\Gamma\bigl(N\alpha+(N+1)/2\bigr)}.
\]
The additional exponent \((N-1)/2\), beyond the \(N\alpha\) radial boundary cost, is the cost of aligning \(N\) independent planar orientation vectors within an angular window of order \(\sqrt\varepsilon\). In particular a finite-population unbounded Gaussian outer tail cannot be exact for this model.

## Assumptions and scope

Fix \(N\in\{2,3,\ldots\}\), attraction \(\kappa>0\), propulsion speed \(v_0>0\), and independent orientation-renewal rate \(\gamma>0\). Positions \(\mathbf r_j(t)\in\mathbb R^2\) solve
\[
\dot{\mathbf r}_j(t)=-\kappa\sum_{k\ne j}\bigl(\mathbf r_j(t)-\mathbf r_k(t)\bigr)+v_0\mathbf n_j(t).
\]
Each \(\mathbf n_j(t)\) is piecewise constant on the unit circle, refreshed to an independent uniform direction at the jump times of an independent rate-\(\gamma\) Poisson process. There is no additional translational or rotational diffusion. Let \(\bar{\mathbf r}=N^{-1}\sum_j\mathbf r_j\), \(L=\lVert\mathbf r_1-\bar{\mathbf r}\rVert\) in the unique stationary law of the *relative-coordinate* process, \(\mu=N\kappa\), \(R=v_0/\mu\), and \(\alpha=\gamma/\mu\). The overall centroid need not be stationary. All limits here hold with \(N,\kappa,v_0,\gamma\) fixed.

## Proof

**1. Exact finite-population representation.** Subtract the centroid equation from the particle equation:
\[
\dot{\boldsymbol\ell}_j=-\mu\boldsymbol\ell_j+v_0\left(\mathbf n_j-\frac1N\sum_i\mathbf n_i\right),\qquad
\boldsymbol\ell_j=\mathbf r_j-\bar{\mathbf r}.
\]
The unique stationary filter is obtained by integration over the entire independent two-sided stationary orientation processes. Set
\[
\mathbf U_i=v_0\int_0^\infty e^{-\mu s}\mathbf n_i(-s)\,ds.
\]
Then \(\mathbf U_1,\ldots,\mathbf U_N\) are independent, isotropic and satisfy \(\lVert\mathbf U_i\rVert\le R\) almost surely. Linearity gives the exact identity in distribution
\[
\boldsymbol\ell_1=\frac{N-1}{N}\mathbf U_1-\frac1N\sum_{i=2}^{N}\mathbf U_i.
\]
For planar uniform-direction Poisson reorientation, the exact single-filter law is
\[
\Pr\!\left\{\frac{\lVert\mathbf U_i\rVert^2}{R^2}\in du\right\}
=\alpha(1-u)^{\alpha-1}\,du,\quad 0<u<1,
\]
with independent uniform polar direction (the two-dimensional beta radial law in Guéneau–Majumdar–Schehr, [2]). It may also be obtained from the renewal equation of the exponentially trapped planar run-and-tumble particle. In terms of \(s_i=1-\lVert\mathbf U_i\rVert/R\), the density is
\[
q_\alpha(s)=2\alpha(1-s)(2s-s^2)^{\alpha-1}
=2^\alpha\alpha s^{\alpha-1}(1+O_\alpha(s)),\quad s\downarrow0.
\]

**2. Sharp support.** Define \(w_1=(N-1)/N\), \(w_i=1/N\) for \(i\ge2\), and \(W=\sum_iw_i=2(N-1)/N\). By isotropy, negate \(\mathbf U_i\) for \(i\ge2\) without changing the joint law. Thus \(L/R\) has the law of \(\lVert\sum_i w_i\mathbf V_i\rVert\) with independent vectors \(\mathbf V_i\) having the above radial law. The triangle inequality gives \(L\le RW=L_*\). Positivity of the density near unit radii and of angular probability near any common direction shows that every neighborhood below \(RW\) has positive probability; thus \(L_*\) is the exact essential supremum.

**3. Quantitative localization near the outer edge.** Write \(\mathbf V_i=(1-s_i)(\cos\theta_i,\sin\theta_i)\) and let \(S=\sum_iw_i(1-s_i)\). If \(\lVert\sum_iw_i\mathbf V_i\rVert>W(1-\varepsilon)\), then \(\sum_iw_is_i<W\varepsilon\), whence \(s_i=O_{N}(\varepsilon)\). Furthermore,
\[
S^2-\left\lVert\sum_iw_i\mathbf V_i\right\rVert^2
=2\sum_{i<j}w_iw_j(1-s_i)(1-s_j)\bigl[1-\cos(\theta_i-\theta_j)\bigr].
\]
Since the left side is \(O_N(\varepsilon)\), all angular differences modulo \(2\pi\) are \(O_N(\sqrt\varepsilon)\). Rotational invariance permits taking \(\theta_1=0\). Define \(y=(\theta_2-\theta_1,\ldots,\theta_N-\theta_1)\) with the principal differences near zero and \(v=(w_2,\ldots,w_N)^\mathsf T\). Taylor expansion, uniform on the localized event, yields
\[
W-\left\lVert\sum_iw_i(1-s_i)e^{i\theta_i}\right\rVert
=\sum_iw_is_i+\tfrac12y^\mathsf THy+o(\varepsilon),
\qquad H=\operatorname{diag}(w_2,\ldots,w_N)-\frac{vv^\mathsf T}{W}.
\]
For every nonzero real \(y\), \(y^\mathsf THy>0\): it is the weighted variance with the reference angle fixed at zero. By the matrix determinant lemma,
\[
\det H=\frac{\prod_{i=1}^Nw_i}{W}>0.
\]
This proves, not merely assumes, that the relevant integral localizes to a bounded rescaled radial simplex and angular ellipsoid.

**4. Endpoint integral and exact constant.** Put \(m=N-1\), \(\beta=N\alpha+m/2\), and \(P=\prod_iw_i\). The \(N-1\) independent angular differences have density \((2\pi)^{-m}\) after integrating out the common direction. Apply the radial scaling \(s_i=W\varepsilon x_i/w_i\) and angular scaling \(y=\sqrt{W\varepsilon}\,H^{-1/2}z\). The scaled event converges (outside a boundary of zero measure) to
\[
\sum_{i=1}^{N}x_i+\tfrac12\lVert z\rVert^2<1,\qquad x_i\ge0,\quad z\in\mathbb R^m.
\]
Localization in step 3 and the bound \(q_\alpha(s)\le K_\alpha s^{\alpha-1}\) on sufficiently small positive \(s\) yield domination by an integrable Dirichlet density on the bounded scaled domain. Hence dominated convergence applies for *every* \(\alpha>0\), even when \(q_\alpha\) diverges at the radial edge. Integrating the angular ball and the radial simplex gives
\[
\int_{\substack{x_i\ge0,\,z\in\mathbb R^m\\\sum x_i+\lVert z\rVert^2/2<1}}
\prod_i x_i^{\alpha-1}\,dx\,dz
=\frac{(2\pi)^{m/2}\Gamma(\alpha)^N}
{\Gamma(N\alpha+m/2+1)}.
\]
Consequently
\[
\Pr\{L>RW(1-\varepsilon)\}
\sim\frac{[2^\alpha\Gamma(1+\alpha)]^N W^{\beta+1/2}}
{(2\pi)^{m/2}\Gamma(\beta+1)P^{\alpha+1/2}}\,\varepsilon^{\beta}.
\]
Substituting \(W=2(N-1)/N\), \(P=(N-1)/N^N\), and \(m=N-1\) gives exactly the coefficient stated in the Finding. This proves both the exponent and normalization.

**5. Exact characteristic function (independent check).** Fourier transforming the beta-disk law gives the single-filter characteristic function \(\phi_U(k)={}_0F_1(;1+\alpha;-R^2k^2/4)\). Independence yields the *exact*, finite-\(N\) vector characteristic function
\[
\mathbb E\,e^{i\mathbf k\cdot\boldsymbol\ell_1}
={}_0F_1\!\left(;1+\alpha;-\frac{R^2\lVert\mathbf k\rVert^2}{4}\left(\frac{N-1}{N}\right)^2\right)
\left[{}_0F_1\!\left(;1+\alpha;-\frac{R^2\lVert\mathbf k\rVert^2}{4N^2}\right)\right]^{N-1}.
\]
This identity is not the claimed novel asymptotic but provides a reproducible cross-check of the finite-population law.

## Verification

The accompanying standalone `verify.py` checks the coefficient algebra and the angular Hessian determinant for \(2\le N\le14\). For \(N=2\) and \(\alpha=1\), the single-filter law is uniform area measure on a disk, so the tail is independently computed by a one-dimensional overlap-area integral for two uniform disks. At \(\varepsilon=0.12,0.06,0.03,0.015,0.0075\), ratios of exact tail to the theorem's leading asymptotic are approximately \(0.90253,0.95099,0.97543,0.98770,0.99384\). Sobol quadrature checks the general \(N=2,\alpha=0.5\) and \(N=3,\alpha=0.3\) edge behavior; further Sobol sampling independently compares nine Fourier–Bessel characteristic-function values for \(N=2,3,5\). All tests ran successfully. The infinite-limit theorem is proved by the localization and dominated-convergence argument; numerical tests alone do not prove it.

Run the Python program with NumPy and SciPy installed: `python verify.py`.

## Relationship to prior work

Dutta and Basu [1] introduce and analyze exactly this interacting active-particle model, including the centroid-relative dynamics. Their stationary radial tails use an effective Gaussian/Ornstein–Uhlenbeck description of the finite sum of other particles' orientation forces, justified for large populations. This approximation has unbounded support and therefore cannot determine the true finite-\(N\) outer edge. No claim is made that the dynamics or its Gaussian approximation is new.

Guéneau, Majumdar and Schehr [2] derive the exact stationary beta radial law for a *single* planar run-and-tumble particle in a harmonic potential, used as a premise here. Their single-particle result does not provide the exact outer-edge law of the interacting population's centroid-relative observable. General endpoint convolution methods may in principle imply a related formula; the explicit finite-population edge exponent and all-parameter coefficient are the scope of the present claim, not the beta law itself.

Hashorva [3] studies tails of aggregated Dirichlet risks with dependent components and a common radial factor, whereas this edge problem involves independent beta-disk vectors and their angular alignment. Its theorem has not been shown to imply the finite-population coefficient. Possible broader implicit mathematical coverage remains a literature risk.

## Limitations

The theorem assumes planar isotropic Poisson direction renewals, no translational Brownian noise, equal propulsion and coupling parameters, and fixed finite \(N\). It is not a joint limit in population size and deficit, does not describe Gaussian crossover at large \(N\), and does not assert a corresponding formula for continuously rotating active Brownian particles. The absolute centroid does not have a stationary position law; only relative coordinates do. The result's originality has been reviewed against the identified primary sources, but there is no independent external audit and there remains some risk of coverage through more general endpoint-convolution theory.

## References

[1] D. Dutta and U. Basu, *Collective Ring Formation in Active Matter*, arXiv:2607.16905, first publicly posted 2026-07-18. https://arxiv.org/abs/2607.16905

[2] M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436, first publicly posted 2026-02-09. https://arxiv.org/abs/2602.08436

[3] E. Hashorva, *Extremes of Aggregated Dirichlet Risks*, arXiv:1404.3304 (2014). https://arxiv.org/abs/1404.3304
