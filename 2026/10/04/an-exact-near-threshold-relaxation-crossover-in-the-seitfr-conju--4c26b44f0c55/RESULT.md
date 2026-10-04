# An exact near-threshold relaxation crossover in the SEITFR conjunctivitis model
## Finding
For the SEITFR conjunctivitis model of Al-Hdaibat et al., keep the baseline parameter values from Table 2 and vary the transmission coefficient according to the paper's numerical parametrization \(\beta=\mathcal R_0\beta_c\). The full Jacobian at the endemic equilibrium always has the demographic eigenvalue \(-\mu=-4\times10^{-5}\). However, this eigenvalue cannot be the spectral-abscissa mode arbitrarily close to the transcritical threshold.

After removing the total-population direction, let \(J_{\mathrm{tan}}(\mathcal R_0)\) denote the five-dimensional tangent Jacobian. Exact rational reduction gives
\[
\det\bigl(J_{\mathrm{tan}}(\mathcal R_0)+\mu I\bigr)
=
\frac{13\bigl(386467087274709075099662209-386355335676178838352248250\,\mathcal R_0\bigr)}
{1040825423873790930625000000000000}.
\]
Therefore the shifted determinant vanishes exactly at
\[
\mathcal R_\times=
\frac{386467087274709075099662209}{386355335676178838352248250}
=1.0002892456456818\ldots.
\]
For every \(1<\mathcal R_0<\mathcal R_\times\), the tangent spectrum contains an eigenvalue with real part strictly greater than \(-\mu\). At \(\mathcal R_0=\mathcal R_\times\), \(-\mu\) itself is a tangent eigenvalue. Hence the paper's reported equality \(\max_i\operatorname{Re}(\sigma_i)=-\mu\) on the sampled range \(1.01\le\mathcal R_0\le2.50\) cannot extend all the way down to the endemic threshold.

## Assumptions and scope
The model is
\[
\begin{aligned}
\dot S&=\Pi-(\lambda+\mu)S+\delta R,\\
\dot E&=\lambda S-(\Phi+\mu)E,\\
\dot I&=\Phi E-(\alpha_1+\kappa+\mu)I,\\
\dot T&=\kappa I-(\alpha_2+\Psi+\mu)T,\\
\dot F&=\Psi T-(\alpha_3+\mu)F,\\
\dot R&=\alpha_1I+\alpha_2T+\alpha_3F-(\mu+\delta)R,
\end{aligned}
\qquad
\lambda=\frac{\beta(I+\epsilon T)}{N},
\]
with \(N=S+E+I+T+F+R\). The baseline values used in the exact computation are \(\mu=0.00004\), \(\epsilon=0.05\), \(\Phi=0.25\), \(\kappa=0.15\), \(\Psi=0.02\), \(\alpha_1=0.14\), \(\alpha_2=0.30\), \(\alpha_3=0.20\), and \(\delta=0.001\), all with the source's stated units. Recruitment \(\Pi\) cancels from the tangent spectral calculation.

The finding concerns the endemic equilibrium for \(\mathcal R_0>1\) and the source's parametrization \(\beta=\mathcal R_0\beta_c\). It is a statement about the linearized spectrum. It does not claim global stability of the endemic equilibrium, nonlinear convergence rates, or dominance of \(-\mu\) above \(\mathcal R_\times\).

## Proof
Summing the six model equations gives the exact scalar equation
\[
\dot N=\Pi-\mu N.
\]
Consequently the full Jacobian has an exact eigenvalue \(-\mu\), corresponding to the total-population direction.

Set
\[
d_1=\Phi+\mu,\qquad
d_2=\alpha_1+\kappa+\mu,\qquad
d_3=\alpha_2+\Psi+\mu,\qquad
d_4=\alpha_3+\mu,
\]
and
\[
L=\frac{d_2}{\Phi}+1+\frac{\kappa}{d_3}+\frac{\Psi\kappa}{d_3d_4}
+\frac{\alpha_1+\alpha_2\kappa/d_3+\alpha_3\Psi\kappa/(d_3d_4)}{\mu+\delta}.
\]
On the endemic branch, the source's equilibrium formulas give
\[
\frac{I^*}{N^*}=\frac{\mathcal R_0-1}{\mathcal R_0L},
\qquad
\frac{T^*}{I^*}=\frac{\kappa}{d_3}.
\]
Writing
\[
B=\frac{d_1d_2}{\Phi\bigl(1+\epsilon\kappa/d_3\bigr)},
\qquad
\ell=\frac{d_1d_2}{\Phi L}(\mathcal R_0-1),
\]
the identities \(\beta/\mathcal R_0=B\) and \(\lambda^*=\ell\) follow directly from the reproduction-number formula and the endemic equilibrium.

Restrict perturbations to the tangent hyperplane \(\delta N=0\), eliminate \(S\), and order the remaining perturbations as \((E,I,T,F,R)\). The tangent Jacobian is
\[
J_{\mathrm{tan}}=
\begin{pmatrix}
-d_1-\ell & B-\ell & \epsilon B-\ell & -\ell & -\ell\\
\Phi & -d_2 & 0 & 0 & 0\\
0 & \kappa & -d_3 & 0 & 0\\
0 & 0 & \Psi & -d_4 & 0\\
0 & \alpha_1 & \alpha_2 & \alpha_3 & -(\mu+\delta)
\end{pmatrix}.
\]
Substituting the baseline values and expanding \(\det(J_{\mathrm{tan}}+\mu I)\) over the rationals gives the affine expression stated in the Finding. Its unique zero is \(\mathcal R_\times\).

It remains to interpret the sign. For \(1<\mathcal R_0<\mathcal R_\times\), the determinant of the real five-dimensional matrix \(J_{\mathrm{tan}}+\mu I\) is positive. If every tangent eigenvalue \(\lambda_j\) satisfied \(\operatorname{Re}\lambda_j\le-\mu\), then every shifted eigenvalue \(\lambda_j+\mu\) would lie in the closed left half-plane. Because the determinant is nonzero, none could be zero. In odd real dimension, nonreal eigenvalues occur in conjugate pairs with positive product, leaving an odd number of negative real eigenvalues; the determinant would therefore be negative. This contradicts the exact positive determinant. Hence at least one tangent eigenvalue satisfies
\[
\operatorname{Re}\lambda_j>-\mu.
\]
At \(\mathcal R_0=\mathcal R_\times\), the determinant is zero, so \(-\mu\) is a tangent eigenvalue as well as the independent demographic eigenvalue of the full Jacobian.

## Verification
The accompanying `verify.py` uses only exact rational arithmetic from the Python standard library. It reconstructs \(J_{\mathrm{tan}}+\mu I\) as a matrix whose entries are affine polynomials in \(\mathcal R_0\), expands its determinant by all \(5!\) permutations, verifies that the result is affine, verifies the exact rational value of \(\mathcal R_\times\), and checks the determinant signs on both sides of the crossing. Running the file prints `VERIFY_OK`.

The sign argument is analytic and does not infer an infinite statement from sampled eigenvalue computations. Numerical eigenvalues are not used as proof.

## Relationship to prior work
Al-Hdaibat et al. derive the SEITFR model, the endemic equilibrium, and a forward transcritical bifurcation at \(\mathcal R_0=1\). Their numerical local-stability study samples \(1.01\le\mathcal R_0\le2.50\) in increments of \(0.01\) and reports \(\max_i\operatorname{Re}(\sigma_i)=-\mu\) throughout that tested range. The exact crossover above lies below the first sampled value by more than an order of magnitude, so it is not resolved by that grid.

General center-manifold theory for epidemic models, including van den Driessche and Watmough's treatment of reproduction-number bifurcations, explains why a critical eigenvalue approaches zero near a transcritical threshold. That qualitative fact does not provide the model-specific collision with the demographic mode or the exact value \(\mathcal R_\times\). Searches of the source title, model aliases, dominant-eigenvalue wording, critical-slowing terminology, and the exact source DOI did not locate a prior statement of this crossover.

## Limitations
The exact value \(\mathcal R_\times\) is tied to the source's baseline parameter set and to varying \(\beta\) through \(\beta=\mathcal R_0\beta_c\). The determinant argument proves that the spectral abscissa is greater than \(-\mu\) below the crossover; it does not by itself prove local asymptotic stability at every point in the whole interval \(1<\mathcal R_0<\mathcal R_\times\). The source's forward-transcritical analysis does ensure a stable endemic branch sufficiently close to the threshold, giving the slower-mode interpretation there.

The result also does not prove that \(-\mu\) remains the dominant mode for every \(\mathcal R_0>\mathcal R_\times\); the paper establishes that observation numerically only on its stated sampled range. No claim is made about nonlinear convergence times away from the linear regime.

## References
Al-Hdaibat, B., Safi, M. A., Almuneef, A., Alqahtani, Z., DarAssi, M. H., and Attoum, O. “Bifurcation and stability analysis of an SEITFR conjunctivitis model with standard incidence and treatment failure.” *AIMS Mathematics* 11(8), 26640–26676 (2026). DOI: 10.3934/math.20261069.

van den Driessche, P., and Watmough, J. “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission.” *Mathematical Biosciences* 180, 29–48 (2002). DOI: 10.1016/S0025-5564(02)00108-6.
