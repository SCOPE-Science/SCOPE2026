# Unique phase-speed minimum for finite-depth two-layer gravity-capillary waves

## Finding

For two inviscid, incompressible layers with densities \(0<\rho_u<\rho_l\), finite depths \(h_u,h_l>0\), gravity \(g>0\), rigid horizontal lids, and interfacial tension \(T>0\), the linear interfacial gravity-capillary dispersion relation is
\[
\omega^2(k)=\frac{g(\rho_l-\rho_u)k+Tk^3}{\rho_l\coth(kh_l)+\rho_u\coth(kh_u)}.
\]
Writing \(c(k)=\omega(k)/k\), the squared phase speed is
\[
c^2(k)=\frac{g(\rho_l-\rho_u)+Tk^2}{k\bigl(\rho_l\coth(kh_l)+\rho_u\coth(kh_u)\bigr)}.
\]
Define the critical interfacial tension
\[
T_c=\frac{g(\rho_l-\rho_u)(\rho_l h_l+\rho_u h_u)}{3(\rho_l/h_l+\rho_u/h_u)}.
\]
Then \(c(k)\) has exactly one global minimizer \(k_*>0\) if and only if \(0<T<T_c\). If \(T\ge T_c\), \(c(k)\) is strictly increasing on \((0,\infty)\); equality gives a horizontal tangent only at the limiting endpoint \(k=0\), not a positive-wavenumber minimum.

The critical threshold is known in the interfacial-wave literature. The result here is the global uniqueness classification and the strict monotonicity on the complementary parameter range.

## Assumptions and scope

The fluids are inviscid, incompressible, homogeneous, and at rest before perturbation. The interface is flat in equilibrium, gravity is downward, and the two layers have rigid horizontal boundaries at finite distances \(h_l\) below and \(h_u\) above the interface. The disturbance is a linear, horizontally periodic mode with wavenumber \(k>0\); there is no background current, viscosity, compressibility, or additional free surface. The density ordering \(\rho_l>\rho_u>0\) makes the unperturbed interface gravitationally stable. Only the linear dispersion curve is classified; no nonlinear solitary-wave existence or stability statement is claimed.

## Proof

Set \(A=g(\rho_l-\rho_u)>0\), \(y=k^2\), and
\[
D(y)=\sum_{j\in\{l,u\}}\rho_j\sqrt y\,\coth(h_j\sqrt y),\qquad F(y)=c^2(\sqrt y)=\frac{A+Ty}{D(y)}.
\]
For \(z>0\), Euler's product for \(\sinh z/z\), after logarithmic differentiation, gives the convergent partial-fraction identity
\[
z\coth z=1+2z^2\sum_{n=1}^{\infty}\frac{1}{z^2+\pi^2n^2}.
\]
Consequently, for \(y\ge0\),
\[
D(y)=D_0+2y\sum_{j\in\{l,u\}}\rho_jh_j\sum_{n=1}^{\infty}\frac{1}{h_j^2y+\pi^2n^2},\qquad D_0=\frac{\rho_l}{h_l}+\frac{\rho_u}{h_u}>0.
\]
Every nonconstant summand is a positive multiple of \(y/(ay+b)\) with \(a,b>0\). Termwise differentiation is valid on compact subsets of \([0,\infty)\), since the derivative series are dominated by convergent constant multiples of \(n^{-2}\) and \(n^{-4}\). Hence \(D'(y)>0\) and \(D''(y)<0\) for every \(y\ge0\), and
\[
D'(0)=\frac{\rho_lh_l+\rho_uh_u}{3}.
\]
Define \(H(y)=D(y)-yD'(y)\). Strict concavity gives \(H(y)\ge D(0)=D_0>0\), while \(H'(y)=-yD''(y)>0\) for \(y>0\). Now set
\[
R(y)=\frac{A D'(y)}{H(y)}.
\]
Its derivative is
\[
R'(y)=A\frac{D''(y)H(y)-D'(y)H'(y)}{H(y)^2}<0,
\]
so \(R\) is strictly decreasing. The same partial-fraction representation and dominated convergence give \(D'(y)\to0\) as \(y\to\infty\); since \(H(y)\ge D_0\), it follows that \(R(y)\to0\). At the left endpoint,
\[
R(0)=\frac{A D'(0)}{D_0}=T_c.
\]
Direct differentiation yields the exact sign identity
\[
F'(y)=\frac{H(y)}{D(y)^2}\bigl(T-R(y)\bigr).
\]
If \(T\ge T_c\), then \(R(y)<T_c\le T\) for every \(y>0\), so \(F'(y)>0\) throughout the positive axis. If \(0<T<T_c\), strict decrease of \(R\), together with \(R(0)=T_c\) and \(R(\infty)=0\), gives exactly one \(y_*>0\) with \(R(y_*)=T\); the sign identity makes \(F\) strictly decreasing before \(y_*\) and strictly increasing after it. Finally, as \(k\to\infty\), \(D(k^2)\sim(\rho_l+\rho_u)k\), so \(F(k^2)\sim Tk/(\rho_l+\rho_u)\to\infty\). Thus the unique stationary point is the unique global minimum. Since the square root is strictly increasing on positive values, the same minimizer and monotonicity conclusions hold for \(c(k)\).

## Verification

The proof is analytic for every admissible density, depth, gravity, tension, and wavenumber. The hyperbolic-cotangent expansion is derived from Euler's product, not assumed as a new physical law. The endpoint value and derivative are explicit: \(D(0)=\rho_l/h_l+\rho_u/h_u\) and \(D'(0)=(\rho_lh_l+\rho_uh_u)/3\). The threshold follows from these exact quantities. No finite numerical scan is used to establish uniqueness, and no computation is offered as a substitute for the all-parameter proof.

## Relationship to prior work

Sun and Shen study nonlinear solitary waves in a two-layer fluid with surface tension between rigid boundaries and identify a critical surface-tension regime. A later finite-depth interfacial-wave analysis gives the critical Bond threshold by expanding the phase-speed curve at zero wavenumber and discusses the appearance of a nonzero-wavenumber minimum below that threshold. These works motivate the same threshold, which is not claimed as new here. The present statement supplies a global uniqueness proof: it shows that the phase-speed curve cannot have a second positive stationary point, and that above threshold it is strictly increasing for all positive wavenumbers.

## Limitations

The theorem concerns the standard linear interfacial dispersion relation with two finite-depth layers and rigid lids. It does not provide a closed-form expression for \(k_*\), prove nonlinear solitary-wave existence, classify finite-amplitude branches, include background currents or viscosity, or cover a free surface coupled to a second interface. The critical tension is an endpoint criterion; the unique minimizer below threshold is specified implicitly by \(R(k_*^2)=T\).

## References

1. S. M. Sun and M. C. Shen, “Solitary waves in a two-layer fluid with surface tension,” *SIAM Journal on Mathematical Analysis* 24(4), 866–891 (July 1993), DOI 10.1137/0524054. The available bibliographic record gives the issue month rather than an exact day.
2. V. K. Kadari, N. Yewale, P. K. Farsoiya, Y. S. Mayya, and R. Dasgupta, “Interfacial waves from pressure forcing: revisiting classical theories from an IVP perspective,” arXiv:2605.12254v1 (2026), §2. This later source gives the finite-depth critical Bond threshold and discusses the nonzero-wavenumber minimum.
