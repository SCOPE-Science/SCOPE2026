# Quartic Detachment at a Surface-Wave Existence Threshold

## Finding

Consider the complete isotropic Toupin–Mindlin gradient-elastic half-space. Fix a tangential wavenumber \(\xi>0\) and a simple bulk-shear threshold \(k_0\) such that \(S(k_0)=\xi^2\), \(S'(k_0)>0\), and \(T(k_0)>0\), where \(S(k)=\sigma(k)^2\) and \(T(k)=\tau(k)^2\) are the characteristic-root functions in the exact dispersion formulation. Define \(\gamma_0=\sqrt{\xi^2+T(k_0)}\) and \(V_{\mathrm{bulk}}=c_sk_0/\xi\). As the nonzero signed coupling \(\alpha\to0\), the surface-wave decay exponent and phase-speed gap satisfy
\[
\beta(\xi,\alpha)=\frac{\xi^4}{\gamma_0^3}\alpha^2+O(\alpha^6),
\qquad
V_{\mathrm{surf}}-V_{\mathrm{bulk}}
=-\frac{c_s\xi^7}{\gamma_0^6S'(k_0)}\alpha^4+O(\alpha^8).
\]
The surface mode therefore loses localization at quadratic order in \(\alpha\), while its phase speed approaches the bulk-shear branch from below at quartic order.

## Assumptions and scope

The result concerns the exact traction-free surface-wave problem for a homogeneous, isotropic half-space in the complete Toupin–Mindlin strain-gradient theory. The tangential wavenumber \(\xi\) is fixed and positive. The bulk-shear threshold is assumed simple, \(S'(k_0)>0\), with \(T(k_0)>0\). The coupling is nonzero but tends to zero within the physically admissible parameter range. The result is local in parameter space; it does not assert uniformity as \(\xi\to0\), \(\xi\to\infty\), or \(S'(k_0)\to0\), and it does not cover damping, anisotropy, finite layers, or degenerate thresholds.

## Proof

Let \(k=\omega/c_s\), \(S(k)=\sigma(k)^2\), and \(T(k)=\tau(k)^2\). The normal decay exponents satisfy
\[
\beta^2=\xi^2-S(k),\qquad \gamma^2=\xi^2+T(k).
\]
The exact determinant in the cited Toupin–Mindlin analysis, after using its normalized coupling \(\alpha\), is
\[
\beta\gamma(\gamma^2-\beta^2)=\alpha^2\xi^4. \tag{1}
\]
At \(\alpha=0\), the surface branch reaches \(\beta=0\), so the limiting frequency parameter is the bulk-shear threshold \(k_0\) with \(S(k_0)=\xi^2\).

Because \(S'(k_0)>0\), the relation \(\beta^2=\xi^2-S(k)\) can be inverted locally as an even smooth function of \(\beta\):
\[
k-k_0=-\frac{\beta^2}{S'(k_0)}+O(\beta^4). \tag{2}
\]
Consequently \(\gamma=\gamma_0+O(\beta^2)\), and
\[
\gamma(\gamma^2-\beta^2)=\gamma_0^3+O(\beta^2).
\]
Equation (1) therefore gives
\[
\beta\bigl(\gamma_0^3+O(\beta^2)\bigr)=\alpha^2\xi^4.
\]
The implicit-function theorem at \((\beta,\alpha^2)=(0,0)\), where the derivative with respect to \(\beta\) is \(\gamma_0^3>0\), yields
\[
\beta=\frac{\xi^4}{\gamma_0^3}\alpha^2+O(\alpha^6). \tag{3}
\]
Squaring (3) and substituting into (2) gives
\[
k-k_0=-\frac{\xi^8}{\gamma_0^6S'(k_0)}\alpha^4+O(\alpha^8).
\]
Since \(V_{\mathrm{surf}}=c_sk/\xi\) and \(V_{\mathrm{bulk}}=c_sk_0/\xi\), division by \(\xi\) and multiplication by \(c_s\) proves the stated phase-speed gap. The negative leading coefficient follows from \(c_s>0\), \(\xi>0\), \(\gamma_0>0\), and \(S'(k_0)>0\). The penetration depth \(1/\beta\) has leading asymptotic \(\gamma_0^3/(\xi^4\alpha^2)\).

## Verification

The proof uses the exact determinant and characteristic-root definitions, not numerical fits. The simple-root hypothesis is used precisely to invert \(S(k)\) near \(k_0\). The expansion orders follow from the fact that the determinant depends on the signed coupling through \(\alpha^2\), and the local frequency shift depends on \(\beta^2\). No computation is used as a substitute for proof.

## Relationship to prior work

Gourgiotis and Georgiadis establish the existence threshold for torsional and SH surface waves in the complete isotropic Toupin–Mindlin theory, derive the exact dispersion determinant, and present dispersion curves. Their stated results do not give the fixed-wavenumber singular asymptotic as the coupling tends to zero. Earlier simplified gradient-elastic models treat different constitutive or surface-energy assumptions and frequency ranges. Eremeyev, Rosi, and Naili compare strain-gradient and surface-stress models and report a range of slow displacement decay; the accessible abstract does not state the coupling-detachment coefficient derived here. The present result is a local asymptotic refinement of the complete model, not a new existence theorem.

## Limitations

The coefficient is valid only at a simple threshold with \(S'(k_0)>0\). It need not remain uniform near a multiple root or in a simultaneous wavenumber limit. The 2019 comparison paper's full PDF was restricted at the repository inspected, so its abstract was the only material available from that source. The literature search did not establish absolute novelty; the exact determinant is known, and the specific parameter-limit expansion is the additional claim.

## References

1. P. A. Gourgiotis and H. G. Georgiadis, “Torsional and SH surface waves in an isotropic and homogenous elastic half-space characterized by the Toupin–Mindlin gradient theory,” *International Journal of Solids and Structures* 62 (2015), 217–228. arXiv:1509.06590, first arXiv version dated 2015-09-18. https://arxiv.org/abs/1509.06590 ; https://doi.org/10.1016/j.ijsolstr.2015.02.032
2. H. G. Georgiadis, I. Vardoulakis, and G. Lykotrafitis, “Torsional surface waves in a gradient-elastic half-space,” *Wave Motion* 31(4) (2000), 333–348. https://doi.org/10.1016/S0165-2125(99)00035-9
3. V. A. Eremeyev, G. Rosi, and S. Naili, “Comparison of anti-plane surface waves in strain-gradient materials and materials with surface stresses” (2019), repository record and abstract. https://iris.unica.it/handle/11584/307172
