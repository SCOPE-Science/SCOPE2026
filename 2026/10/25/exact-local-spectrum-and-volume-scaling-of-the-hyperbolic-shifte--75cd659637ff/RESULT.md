# Exact local spectrum and volume scaling of the hyperbolic shifted Gauss flow

## Finding

Let \(n\ge2\), \(R>0\), and \(\alpha>0\). In curvature \(-1\) hyperbolic space \(\mathbb H^{n+1}\), consider
\[
\partial_tX=(\phi-\widetilde K^{\alpha/n})\nu,\qquad
\widetilde K=\prod_{i=1}^n(\kappa_i-1),\qquad
\phi=\frac{1}{|M|}\int_M\widetilde K^{\alpha/n}\,d\mu.
\]
For a geodesic sphere of radius \(R\), define \(\lambda_R=\coth R-1>0\). If \(u\) is a normal-graph perturbation and \(\bar u\) its average on the sphere, the linearized operator is
\[
L_Ru=\frac{\alpha}{n}\lambda_R^{\alpha-1}\left(\Delta_{S_R}u+n\operatorname{csch}^2R\,(u-\bar u)\right),
\]
where \(\Delta_{S_R}\) has nonpositive spectrum. The degree-zero mode changes the radius and the degree-one modes change the center. For every degree \(\ell\ge2\),
\[
\mu_\ell=-\frac{\alpha}{n}\lambda_R^{\alpha-1}\operatorname{csch}^2R\left(\ell(\ell+n-1)-n\right)<0.
\]
Consequently the sharp nonzero linearized decay gap is
\[
\gamma_2(R)=-\mu_2=\frac{\alpha(n+2)}{n}\lambda_R^{\alpha-1}\operatorname{csch}^2R
=\frac{\alpha(n+2)}{n}\frac{2^{\alpha+1}e^{-2\alpha R}}{(1-e^{-2R})^{\alpha+1}}.
\]
It is strictly decreasing in \(R\). Writing \(V(R)=\omega_n\int_0^R\sinh^n s\,ds\), with \(\omega_n=|\mathbb S^n|\), gives
\[
\gamma_2(R)\sim \frac{\alpha(n+2)}{n}2^{1-\alpha}\left(\frac{\omega_n}{n}\right)^{2\alpha/n}V(R)^{-2\alpha/n}\qquad(R\to\infty).
\]

## Assumptions and scope

The ambient sectional curvature is normalized to \(-1\); \(M=S_R\) is a geodesic sphere in \(\mathbb H^{n+1}\); \(n\ge2\); and \(\alpha>0\). The speed is the positive \(\alpha/n\)-power of the product of the shifted principal curvatures. The claim concerns the Fréchet linearization at the stationary sphere, not a global nonlinear rate for arbitrary initial hypersurfaces.

## Proof

At \(S_R\), all principal curvatures equal \(\kappa=\coth R\), so each shifted curvature equals \(\lambda_R=\coth R-1\), and the speed is constant \(\lambda_R^\alpha\). Thus \(\phi=\lambda_R^\alpha\) and the sphere is stationary.

For an outward normal variation with height \(u\), the shape-operator variation in curvature \(-1\) is
\[
\delta\mathcal W=-\nabla^2u-u(\mathcal W^2-I).
\]
Taking the trace at \(S_R\), using \(\coth^2R-1=\operatorname{csch}^2R\), gives
\[
\delta H=-\Delta_{S_R}u-n\operatorname{csch}^2R\,u.
\]
Since \(\widetilde K=\prod_i(\kappa_i-1)\), differentiating \(F=\widetilde K^{\alpha/n}\) at the umbilic sphere yields
\[
\delta F=\frac{\alpha}{n}\lambda_R^{\alpha-1}\sum_i\delta\kappa_i
=-\frac{\alpha}{n}\lambda_R^{\alpha-1}\left(\Delta_{S_R}u+n\operatorname{csch}^2R\,u\right).
\]
The derivative of the area-average \(\phi=|M|^{-1}\int_M F\,d\mu\) is \(\delta\phi=\overline{\delta F}\), because \(F\) is constant at the reference sphere and the area-variation terms cancel. Therefore the linearized normal speed \(L_Ru=\delta\phi-\delta F\) is the displayed operator.

The spherical Laplacian eigenvalue on degree \(\ell\) is \(-\ell(\ell+n-1)/\sinh^2R\). The mean projection removes degree zero, and the formula gives zero for degree one. For \(\ell\ge2\), it gives the stated negative eigenvalues. Since \(\ell(\ell+n-1)\) strictly increases, the least magnitude among the nonzero shape eigenvalues occurs at \(\ell=2\), yielding \(\gamma_2(R)\).

With \(q=e^{-2R}\), one has \(\lambda_R=2q/(1-q)\) and \(\operatorname{csch}^2R=4q/(1-q)^2\). Hence
\[
\gamma_2(R)=\frac{\alpha(n+2)}{n}\frac{2^{\alpha+1}q^\alpha}{(1-q)^{\alpha+1}},
\]
which increases strictly in \(q\in(0,1)\); because \(q\) decreases with \(R\), the gap decreases strictly with radius.

Finally, \(V(R)=\omega_n\int_0^R\sinh^n s\,ds\sim \omega_n e^{nR}/(n2^n)\), while \(\lambda_R\sim2e^{-2R}\) and \(\operatorname{csch}^2R\sim4e^{-2R}\). Substitution gives the claimed \(V(R)^{-2\alpha/n}\) asymptotic and its coefficient.

## Verification

The derivation uses the normal-variation identity for the shape operator, the product rule for \(\widetilde K\), the cancellation in the derivative of an average at a constant function, and the standard spherical-harmonic spectrum. The large-volume coefficient follows by substituting the leading terms of \(V(R)\), \(\lambda_R\), and \(\operatorname{csch}^2R\). No finite numerical experiment is used as a proof.

## Relationship to prior work

The recent work on curvature measures and volume-preserving flows in h-convex hyperbolic geometry proves global existence and exponential convergence for this shifted \(\alpha\)-Gauss flow. Earlier work treats degree-one homogeneous shifted-curvature flows or volume-preserving flows driven by the unshifted Gauss curvature. The present statement supplies the explicit full spherical-harmonic linearization and the radius/volume dependence of its sharp local gap; it does not replace or strengthen the global existence theorem.

## Limitations

This is a local linearized result. It does not prove that nonlinear solutions attain this rate for arbitrary data, nor does it give volume-uniform constants for nonlinear estimates. The spectral gap tending to zero rules out a positive lower bound for this linearized gap across all sphere radii. Literature searches may miss unindexed sources, so historical priority remains subject to residual literature risk.

## References

1. X. Zhang, *Curvature measures and volume preserving flows in h-convex geometry*, arXiv:2610.18423v1 (first public version: 13 October 2026).
2. B. Andrews, X. Chen, Y. Wei, *Volume preserving flow and Alexandrov–Fenchel type inequalities in hyperbolic space*, Journal of the European Mathematical Society 23 (2021), 2467–2509; arXiv:1805.11776.
3. Y. Wei, B. Yang, T. Zhou, *Volume preserving Gauss curvature flow of convex hypersurfaces in the hyperbolic space*, arXiv:2210.06035.
4. Y. Wei, B. Yang, T. Zhou, *Volume preserving nonhomogeneous Gauss curvature flow in hyperbolic space*, arXiv:2406.05159.
