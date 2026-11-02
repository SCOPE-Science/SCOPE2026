# Chirality avoids the diffusion-isotropy crossing of an orientationally reset swimmer

## Finding

For a planar active Brownian swimmer with a fixed laboratory-frame heading reset, the long-time diffusion tensor is isotropic at a positive reset rate **if and only if** the intrinsic angular drift vanishes and the reset rate is one half of the rotational diffusivity. Any nonzero chirality removes that exact isotropy point at every finite positive reset rate.

Precisely, let \(\mathsf K\) be the diffusion tensor in the convention \(\lim_{t\to\infty}\operatorname{Cov}(X_t-X_0)/(2t)=\mathsf K\). Put
\[
Z=(\mathsf K_{11}-\mathsf K_{22})+2i\mathsf K_{12}.
\]
For every \(r,d,v>0\), \(\omega\in\mathbb R\), and \(D\ge0\),
\[
\boxed{Z=\frac{v^2r\bigl(d^2-2dr-\omega^2-2id\omega\bigr)}{(r+4d-2i\omega)(r+d-i\omega)^3}.}
\]
Consequently the exact diffusion-eigenvalue separation is
\[
\boxed{
\lambda_{\max}(\mathsf K)-\lambda_{\min}(\mathsf K)
=\frac{v^2r\sqrt{(d^2-2dr-\omega^2)^2+4d^2\omega^2}}{
\bigl((r+d)^2+\omega^2\bigr)^{3/2}\sqrt{(r+4d)^2+4\omega^2}}.
}
\]
It vanishes precisely when \(\omega=0\) and \(r=d/2\). In particular, chirality produces an *avoided isotropy crossing*, not merely a shift of the achiral crossing to another reset rate.

The degeneracy is lifted linearly in the angular-drift magnitude. With \(h=r-d/2\), for fixed \(d,v>0\) as \((h,\omega)\to(0,0)\),
\[
\boxed{Z=-\frac{16v^2}{243d^2}(h+i\omega)
+O\!\left(\frac{v^2(h^2+\omega^2)}{d^3}\right).}
\]
Thus
\[
\lambda_{\max}-\lambda_{\min}=
\frac{16v^2}{243d^2}\sqrt{h^2+\omega^2}
+O\!\left(\frac{v^2(h^2+\omega^2)}{d^3}\right).
\]
At \(r=d/2\) and \(\omega\to0^+\), the off-diagonal diffusivity is \(\mathsf K_{12}=-8v^2\omega/(243d^2)+O(v^2\omega^2/d^3)\), and the two principal axes approach the two diagonals of the laboratory coordinate system. This is a local statement near the former isotropy point, not a global minimization over reset rates.

## Assumptions and scope

A particle moves in \(\mathbb R^2\) according to
\[
 dX_t=v(\cos\theta_t,\sin\theta_t)\,dt+\sqrt{2D}\,dB_t,
\]
where \(B_t\) is a standard two-dimensional Brownian motion independent of the angular noises. Between independent rate-\(r\) Poisson reset events, \(d\theta_t=\omega\,dt+\sqrt{2d}\,dW_t\) modulo \(2\pi\). At every reset, the orientation becomes exactly \(0\) in the fixed laboratory frame, **but the position is not reset**. The parameters obey \(r,d,v>0\), \(\omega\in\mathbb R\), and \(D\ge0\). The angular variable is initialized in its unique invariant law (the large-time diffusion limit is unchanged by any fixed initial angle). No spatial stationary law is asserted.

The diffusion tensor is the symmetric matrix \(\mathsf K=\lim_{t\to\infty}(2t)^{-1}\operatorname{Cov}(X_t-X_0)\). Isotropy means \(\mathsf K\) is a scalar multiple of the identity, not merely equality of the two coordinate variances. The eigenvalue separation is independent of \(D\), which adds only an isotropic component.

## Proof

**First and second angular harmonics.** The backward generator acting on a smooth periodic angular function is
\[
\mathcal L f=d f''+\omega f'+r\bigl(f(0)-f(\theta)\bigr).
\]
For \(n\ne0\), applying stationary generator balance to \(e^{in\theta}\) gives the exactly determined invariant Fourier moments
\[
 m_n:=\mathbb E e^{in\theta}=\frac{r}{r+n^2d-in\omega}.
\]
In particular \(m_1=r/(r+d-i\omega)\) and \(m_2=r/(r+4d-2i\omega)\). The invariant angular law exists uniquely because positive-rate resets couple any initial angle to the same refreshed process.

**Covariance and Green--Kubo reduction.** Write \(U_t=(\cos\theta_t,\sin\theta_t)\), \(\mu=\mathbb E U_t\), and \(S=\operatorname{Cov}(U_t)\). The conditional first-harmonic equation gives, for every \(t\ge0\),
\[
 \mathbb E[U_t-\mu\mid\theta_0]
 =e^{-(r+d)t}R(\omega t)(U_0-\mu),
\]
where \(R(\phi)\) is the planar rotation matrix. Hence the stationary velocity covariance is \(C(t)=e^{-(r+d)t}R(\omega t)S\). This covariance is absolutely integrable. Integrating the stationary position increments yields
\[
 \mathsf K=D I_2+\frac{v^2}{2}\bigl(AS+SA^\top\bigr),\qquad
 A=\frac{(r+d)I_2+\omega J}{(r+d)^2+\omega^2},\qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
The factor \(1/2\) follows from the \(2t\) diffusion convention. Absolute integrability justifies the limit and interchanging covariance integration with the long-time limit.

**Complex anisotropy.** Using the harmonic identities,
\[
 S_{11}-S_{22}+2iS_{12}=m_2-m_1^2.
\]
The symmetric Green--Kubo matrix multiplication therefore gives
\[
 (\mathsf K_{11}-\mathsf K_{22})+2i\mathsf K_{12}
 =\frac{v^2(m_2-m_1^2)}{r+d-i\omega}.
\]
Combining the two rational moments reduces the numerator to \(r(d^2-2dr-\omega^2-2id\omega)\), establishing the displayed formula for \(Z\). A real symmetric \(2\times2\) matrix has eigenvalue separation \(\sqrt{(\mathsf K_{11}-\mathsf K_{22})^2+4\mathsf K_{12}^2}=|Z|\), giving the exact gap formula.

Because \(d>0\), the imaginary part of the numerator can vanish only for \(\omega=0\); with \(\omega=0\), its real part vanishes only for \(r=d/2\). All denominators are nonzero in the stated domain. This proves both directions of the isotropy classification, without relying on a coordinate-diagonal assumption.

**Near-crossing coefficient.** The rational expression for \(Z\) is real-analytic in the two real parameters near \((r,\omega)=(d/2,0)\). Its first derivatives there are
\[
 \frac{\partial Z}{\partial r}=-\frac{16v^2}{243d^2},\qquad
 \frac{\partial Z}{\partial\omega}=-\frac{16iv^2}{243d^2}.
\]
Taylor's theorem with a locally bounded Hessian yields the stated remainder, and the reverse triangle inequality yields the gap expansion. The off-diagonal and principal-axis statements follow from \(2\mathsf K_{12}=\operatorname{Im}Z\) and the elementary eigenvectors of a symmetric \(2\times2\) matrix.

## Verification

The included `checker.py` checks the exact complex rational identity, the two crossing derivatives, and the complete achiral reduction against the known longitudinal and transverse effective-diffusion formulas. It independently integrates the Green--Kubo time-domain covariance for five parameter triples and solves a 128-state and 256-state circular Markov discretization's stationary and Poisson equations for three parameter triples. Refinement errors decrease in all three finite-grid comparisons. The discretization checks are numerical corroboration, not proofs of the continuum identities.

Run `python checker.py` with Python 3, SymPy, NumPy and SciPy installed. The analytic argument above establishes the continuum result for all parameters in its domain.

## Relationship to prior work

Baouche, Franosch, Meiners and Kurzthaler, arXiv:2405.06769v1, establish the orientational-only Poisson resetting process **without angular drift** and its exact longitudinal and transverse spreading coefficients. Their formulas imply the achiral crossing at \(r=d/2\), which is not claimed as new. The additional chiral angular drift, the exact full tensor eigenvalue-gap criterion and the two-parameter avoided-crossing law are the contribution assessed here.

Olsen and Löwen, arXiv:2405.14326v1, study a chiral swimmer with **relative-angle tumbles**, which preserve rotational covariance and lead to a scalar transport description; those jumps do not reset headings to the same absolute laboratory direction. Chaki, Olsen and Löwen, arXiv:2406.17550v1, examine anisotropic *passive* particles with angular resetting, where body-dependent translational noise produces the anisotropy. Ghosh and Mandal, arXiv:2501.05149v1, study shape-anisotropic active particles with orientational resetting but no intrinsic angular drift. These models and their diffusion formulas do not directly supply the nonzero-drift absolute-reset isotropy obstruction.

## Limitations

The theorem assumes a single fixed absolute reset heading, exponential reset intervals, constant angular drift, positive rotational diffusivity, and isotropic translational thermal noise. It does not classify general reset-angle distributions, relative tumbling, shaped-particle translational mobility, nonlinear angular torques, or finite-time contours. Its anisotropy gap tends to zero as the reset rate tends to zero or infinity; the statement is strict **at every finite positive rate**. The local avoided-crossing expansion must not be interpreted as a global minimum over reset rate. The comparison with accessible literature is not an independent publication-priority certification.

## References

1. Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1 (first posted 2024-05-10). https://arxiv.org/html/2405.06769v1
2. K. Stølevik Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326v1 (first posted 2024-05-23). https://arxiv.org/html/2405.14326v1
3. S. Chaki, K. Stølevik Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v1 (first posted 2024-06-25). https://arxiv.org/html/2406.17550v1
4. A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149v1 (first posted 2025-01-09). https://arxiv.org/html/2501.05149v1
