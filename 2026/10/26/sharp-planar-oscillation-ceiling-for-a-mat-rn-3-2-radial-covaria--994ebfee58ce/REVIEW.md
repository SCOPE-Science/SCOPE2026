# Independent mathematical audit

## correctness

PASS

After scale a=1, the radial Fourier-Bessel integral 2pi ∫ r(1+r)e^-r cos(lambda r)J0(rho r)dr equals 2pi Re[-i lambda/(z²+rho²)^(3/2)+3z²/(z²+rho²)^(5/2)], z=1-i lambda. At rho=0 its sign is 3-6lambda²-lambda^4, giving necessary lambda²<=2sqrt3-3. For 0<lambda²=t<=2sqrt3-3, put sqrt(z²+rho²)=X-iY, XY=lambda and u=Y/(lambda X)∈(0,1]. Exact rationalization gives a degree-6 polynomial P(u,t) with a seven-term Bernstein expansion B_j(t), j=0..6. Independent symbolic derivation and expansion checked all coefficients and the transformed Fourier numerator; all B0..B5>0 and B6=(1+t)²(3-6t-t²)>=0 for 0<=t<=t*. Therefore spectral density is nonnegative at every rho, and strictly positive except at rho=0 at critical lambda. Bochner gives all finite-configuration PSD, while positive density on an open frequency set gives strict PD for distinct locations. Numerical Fourier checks for four ratios x 35 radii support but do not replace the global Bernstein proof.

## originality

PASS

The Matérn-3/2 covariance itself and damped-cosine families are classical, and Gneiting reviews positive radial kernel theory. The exact planar threshold for their radial product is a specific Fourier-Bessel calculation not established by inspected primary general/spectral SPDE sources. Inaccessible original 1993 damped-cosine study and potentially equivalent Matérn modulation literature are material priority risks.

## value

PASS

Planar isotropic covariance kernels are natural in Gaussian field modeling, and oscillation changes PSD nontrivially; the exact maximal oscillation-to-decay ratio with strict finite-site positivity is a meaningful stability/design cutoff, not an arbitrary parameter slice. Its difference from the higher-dimensional sufficient bounds is geometrically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
