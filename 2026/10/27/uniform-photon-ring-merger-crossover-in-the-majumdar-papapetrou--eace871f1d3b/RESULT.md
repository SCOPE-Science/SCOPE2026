# Uniform photon-ring merger crossover in the Majumdar–Papapetrou dihole

## Finding

For the equal-mass Majumdar–Papapetrou dihole on the symmetry plane \(z=0\), in units where the half-separation is \(1\), let \(M_*=\sqrt{27/8}\), \(\rho_*=\sqrt{5}\), \(\delta=M-M_*>0\), \(\rho_0=\rho_*+\sqrt{\delta}X\), \(\Phi(X)=aX-bX^3\), \(a=128\sqrt{30}/703125\), \(b=8\sqrt{5}/140625\), and \(c=\sqrt{a/(3b)}=\sqrt{16\sqrt{6}/15}\). For each fixed \(X>c\) or \(X<-2c\), the equatorial scattering deflection angle obeys
\[
\lim_{\delta\downarrow0}\delta^{1/4}\bigl[\hat\alpha(\rho_0;M)+\pi\bigr]
=\frac{8}{125}\int_X^\infty\frac{dY}{\sqrt{\Phi(X)-\Phi(Y)}}.
\]

The integral is finite and real on both stated open branches. It supplies a uniform crossover profile when the stable and unstable circular photon rings merge, rather than treating the fixed-supercritical and exactly critical cases separately.

## Assumptions and scope

Use the static equal-mass Majumdar–Papapetrou dihole metric, with the half-coordinate-separation set to \(1\), and restrict null geodesics to the reflection-symmetry plane. The radial coordinate is \(\rho>0\), the mass-to-half-separation parameter is \(M\), and only scattering rays that come from infinity, have one closest-approach turning point, and return to infinity are considered. The claim concerns \(M=M_*+\delta\) with \(\delta\downarrow0\), and fixed scaled turning-point coordinate \(X\) on either \(X>c\) or \(X<-2c\). It is not a statement about generic three-dimensional null geodesics or realistic binary-black-hole dynamics.

## Proof

On the symmetry plane, the metric function and effective potential used for radial null scattering are
\[
U(\rho;M)=1+\frac{2M}{\sqrt{\rho^2+1}},
\qquad
V(\rho;M)=\frac{1}{\rho^2U(\rho;M)^4}.
\]
The circular-orbit equation is
\[
(\rho^2+1)^{3/2}=2M(\rho^2-1).
\]
With \(\eta=\sqrt{\rho^2+1}\), this becomes \(\eta^3-2M\eta^2+4M=0\). Its positive double root occurs at \(M_*=\sqrt{27/8}\), \(\eta_*=\sqrt6\), hence \(\rho_*=\sqrt5\).

Direct differentiation of the displayed \(V\) gives
\[
V_*=\frac{16}{3125},\qquad
V_\rho|_* = V_{\rho\rho}|_* = 0,
\]
\[
V_{\rho M}|_*=\frac{128\sqrt{30}}{703125}=a,
\qquad
V_{\rho\rho\rho}|_*=-\frac{16\sqrt5}{46875}=-6b,
\]
where \(b=8\sqrt5/140625>0\). Thus, uniformly for \(X\) in a fixed compact interval,
\[
V(\rho_*+\sqrt{\delta}X;M_*+\delta)
=V_*+V_M|_*\,\delta+\delta^{3/2}\Phi(X)+O(\delta^2).
\]
The parameter-only term cancels in a difference of potentials, so for bounded \(X,Y\),
\[
V(\rho_0;M)-V(\rho_*+\sqrt{\delta}Y;M)
=\delta^{3/2}\bigl(\Phi(X)-\Phi(Y)\bigr)+O(\delta^2).
\]

The exact deflection integral on this plane is
\[
\hat\alpha(\rho_0;M)+\pi
=2\int_{\rho_0}^{\infty}
\frac{\sqrt{V(\rho;M)}}{\rho\sqrt{V(\rho_0;M)-V(\rho;M)}}\,d\rho.
\]
Substitute \(\rho=\rho_*+\sqrt{\delta}Y\). On a bounded scaled interval, the integrand and differential give the factor
\[
\delta^{-1/4}\frac{2\sqrt{V_*}}{\rho_*}
\frac{dY}{\sqrt{\Phi(X)-\Phi(Y)}}.
\]
Since \(2\sqrt{V_*}/\rho_*=8/125\), this yields the stated coefficient. The tail is controlled by the cubic term: in the intermediate region \(\sqrt{\delta}\,Y\gg\sqrt{\delta}\), the scaled tail is \(O(R^{-1/2})\) after truncation at \(Y=R\); the region bounded away from \(\rho_*\) contributes only \(O(1)\) before multiplication by \(\delta^{1/4}\). Taking \(\delta\downarrow0\) and then \(R\to\infty\) gives the limit.

Finally, \(\Phi'(X)=a-3bX^2\) has roots \(\pm c\), and \(\Phi(-2c)=\Phi(c)\). For \(X>c\), \(\Phi\) decreases along \(Y>X\), so the denominator is positive. For \(X<-2c\), \(\Phi(X)>\Phi(c)\geq\Phi(Y)\) for all \(Y>X\), so the inner-return branch also has a positive denominator. Near \(X=c\) and \(X=-2c\) the profile has logarithmic endpoint divergence; for large \(|X|\) it has order \(|X|^{-1/2}\), matching the fixed-critical power law. The profile therefore describes the crossover between the two separate regimes.

## Verification

The critical parameter, orbit radius, potential value, and derivatives above follow by exact differentiation and substitution into the explicit potential. The cubic scaled profile is a Taylor expansion with a uniform remainder on bounded scaled intervals; the tail estimate is needed because a local Taylor expansion alone does not control the full deflection integral. No finite numerical experiment is used as a proof. The result is restricted to the stated symmetry plane, branch domains, and parameter scaling.

## Relationship to prior work

Patil, Mishra, and Narasimha derive the same dihole potential and critical parameter, and treat the logarithmic strong-deflection regime for \(M>M_*\) separately from the power-law divergence at \(M=M_*\). Tsukamoto derives a fixed-metric strong-deflection expansion for a marginally unstable photon sphere. Igata, Sasaki, and Tsukamoto give a later fixed-degenerate-orbit expansion with local geometric coefficients. Those results establish the endpoint regimes and the local cubic mechanism, but the inspected texts do not give the parameter-unfolding limit with \(\rho_0-\rho_*\) scaled as \(\sqrt{M-M_*}\), the two admissible branch domains, and the explicit dihole crossover integral above.

## Limitations

The result is an asymptotic statement for the static equal-mass Majumdar–Papapetrou model and equatorial scattering only. It does not classify off-plane null geodesics, calculate finite-source image positions, or provide higher-order corrections. A general catastrophe-theory treatment may yield analogous profiles for other models; no directly equivalent parameter-unfolding lensing formula was identified in the inspected primary texts.

## References

1. M. Patil, P. Mishra, and D. Narasimha, “Curious case of gravitational lensing by binary black holes: a tale of two photon spheres, new relativistic images and caustics,” arXiv:1610.04863, first submitted 2016-10-16. https://arxiv.org/abs/1610.04863
2. N. Tsukamoto, “Deflection angle of a light ray reflected by a general marginally unstable photon sphere in a strong deflection limit,” arXiv:2008.12244, first submitted 2020-08-27. https://arxiv.org/abs/2008.12244
3. T. Igata, T. Sasaki, and N. Tsukamoto, “Strong-deflection expansion of the deflection angle near a degenerate photon sphere,” arXiv:2603.08778, first submitted 2026-03-09. https://arxiv.org/abs/2603.08778
