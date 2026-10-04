# An explicit finite-wavenumber wave instability in an IL-2 tumour–immune reaction–diffusion model
## Finding
For the tumour–immune–IL-2 reaction–diffusion system of Brennan et al., keep the source values \(\mu_u=167/1000\), \(\rho_u=173/250\), \(\gamma_v=1/10\), and \(\rho_w=5/2\), and take \(\gamma_w=6\), \(\mu_w=11/1000\), \(\alpha=27/250\), \(\sigma_w=1/25000\), \(\delta_u=543\), and \(\delta_w=7/125\). With \(v_0=1/500\), define \(u_0=(\gamma_v+v_0)(1-v_0)=25449/250000\), \(w_0=(\sigma_w+\rho_wu_0v_0/(\gamma_w+v_0))/\mu_w=37453/3301100\), and choose \(\sigma_u=35597167429/2225702000000\), which makes this a positive coexistence equilibrium exactly. At the homogeneous mode \(k=0\), the characteristic cubic has positive Routh–Hurwitz quantities \(a_2,a_1,a_0,a_2a_1-a_0\). At \(k^2=1/4000\), it still has \(a_2,a_1,a_0>0\) but \(a_2a_1-a_0<0\). Hence diffusion destabilizes the homogeneous equilibrium through an unstable complex-conjugate pair, giving a finite-wavenumber wave-type instability.

The witness is deliberately outside the calibrated IL-2 kinetic and mobility regime used in the motivating oncology study. Its role is therefore structural rather than clinical: it shows that the same three-field reaction–diffusion equations genuinely support a diffusion-driven oscillatory mode, rather than merely allowing such a possibility in generic three-component systems.

## Assumptions and scope
Consider the dimensionless system
\[
 u_t=\delta_u\Delta u+\alpha v-\mu_u u+\frac{\rho_u u w}{1+w}+\sigma_u,
\]
\[
 v_t=\Delta v+v(1-v)-\frac{uv}{\gamma_v+v},
\]
\[
 w_t=\delta_w\Delta w+\frac{\rho_wuv}{\gamma_w+v}-\mu_w w+\sigma_w.
\]
All parameters in the witness are positive. The values \(\mu_u=0.167\), \(\rho_u=0.692\), \(\gamma_v=0.1\), and \(\rho_w=2.5\) match the nondimensional values in Brennan et al. The witness changes the IL-2 saturation, clearance, and relative diffusion parameters to \(\gamma_w=6\), \(\mu_w=0.011\), and \(\delta_w=0.056\); consequently it is not a claim about the calibrated clinical parameter range.

## Proof
Set
\[
 v_0=\frac1{500},\qquad u_0=(\gamma_v+v_0)(1-v_0)=\frac{25449}{250000},
\]
and
\[
 w_0=\frac{\sigma_w+\rho_wu_0v_0/(\gamma_w+v_0)}{\mu_w}=\frac{37453}{3301100}.
\]
Define
\[
 \sigma_u=\mu_u u_0-\alpha v_0-\frac{\rho_u u_0w_0}{1+w_0}=\frac{35597167429}{2225702000000}>0.
\]
The three equilibrium residuals then vanish identically over the rationals.

For a Fourier mode with \(s=k^2\), let the characteristic polynomial of the linearized matrix be
\[
 p_s(\lambda)=\lambda^3+a_2(s)\lambda^2+a_1(s)\lambda+a_0(s).
\]
At \(s=0\), exact rational arithmetic gives
\[
 a_2=\frac{288824993}{1891846700}>0,
\]
\[
 a_1=\frac{155573429383931857}{189480914274753000000}>0,
\]
\[
 a_0=\frac{12024574606690547}{236851142843441250000}>0,
\]
and
\[
 a_2a_1-a_0=\frac{8911524407314355166662027}{119489614127891452121700000000}>0.
\]
Thus the homogeneous equilibrium is Hurwitz by the cubic Routh–Hurwitz criterion.

At \(s=1/4000\), exact arithmetic instead gives
\[
 a_2=\frac{2730713150269}{9459233500000}>0,
\]
\[
 a_1=\frac{738487925127447847}{75792365709901200000000}>0,
\]
\[
 a_0=\frac{12778153690270919087467}{505282438066008000000000000}>0,
\]
but
\[
 a_2a_1-a_0=-\frac{31472914511354501508969179611}{1400268915561227954551171875000000}<0.
\]
Therefore the finite-wavenumber mode is unstable. Because every coefficient of \(p_s\) is positive, Descartes' rule of signs excludes a positive real eigenvalue. Since the polynomial is real and cubic, the unstable roots must therefore be a complex-conjugate pair with positive real part. This is a wave-type diffusion-driven instability.

## Verification
The accompanying `verifier.py` uses only Python's standard-library `fractions.Fraction`. It reconstructs the equilibrium and all characteristic coefficients from the displayed rational parameters, asserts the three equilibrium residuals are exactly zero, checks the Routh–Hurwitz inequalities at \(k=0\), and checks \(a_2,a_1,a_0>0\) together with \(a_2a_1-a_0<0\) at \(k^2=1/4000\).

## Relationship to prior work
Brennan et al. derive the same three-component dispersion polynomial and explicitly distinguish stationary Turing loss from wave instability. They report no wave instabilities in the parameter regimes they explored numerically, while noting that this does not exclude wave instabilities in other regimes. The witness above supplies a concrete exact parameter point outside their calibrated IL-2 regime.

Suddin et al. study a closely related effector-cell/cancer/IL-2 reaction–diffusion model and report stable limit-cycle behaviour for some diffusion choices, describing Hopf analysis as an open problem; that work does not give the finite-wavenumber Routh–Hurwitz witness above. General diffusion-driven wave criteria are available in Villar-Sepúlveda and Champneys, but they do not specialize those criteria to this explicit tumour–immune–IL-2 parameter point.

## Limitations
The altered values \(\gamma_w=6\), \(\mu_w=0.011\), and \(\delta_w=0.056\) are far from the calibrated IL-2 values used by Brennan et al.; no clinical interpretation is claimed. The finding is a local linear instability statement for one homogeneous coexistence equilibrium. It does not establish nonlinear wave persistence, supercriticality, travelling-versus-standing-wave selection, or robustness over a large parameter set.

## References
1. M. Brennan, A. L. Krause, E. Villar-Sepúlveda, C. B. Prior, “Pattern Formation as a Resilience Mechanism in Cancer Immunotherapy,” *Bulletin of Mathematical Biology* 87 (2025), article 106. arXiv:2503.20909. DOI: 10.1007/s11538-025-01485-3.
2. S. Suddin, F. Adi-Kusumo, L. Aryati, Gunardi, “Reaction-Diffusion on a Spatial Mathematical Model of Cancer Immunotherapy with Effector Cells and IL-2 Compounds' Interactions,” *International Journal of Differential Equations* (2021), 5535447. DOI: 10.1155/2021/5535447.
3. E. Villar-Sepúlveda, A. R. Champneys, “General conditions for Turing and wave instabilities in reaction-diffusion systems,” *Journal of Mathematical Biology* 86 (2023), 39. DOI: 10.1007/s00285-023-01870-3.
4. A. Matzavinos, M. A. J. Chaplain, “Travelling-wave analysis of a model of the immune response to cancer,” *Comptes Rendus Biologies* 327 (2004), 995–1008. DOI: 10.1016/j.crvi.2004.07.016.
