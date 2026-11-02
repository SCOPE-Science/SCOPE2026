# Independent mathematical audit

## correctness

PASS

The perturbation f=sin^m(theta) cos(mphi)=Re(x+iy)^m restricts an odd spherical harmonic with Laplacian -m(m+1) and antipodal parity f(-u)=-f(u); therefore width is 2. For a C^2 support function convexity is equivalently PSD of the spherical principal-radius tensor I+epsilon A, A=Hess_S2 f+f I. Direct coordinate covariant differentiation yields A=(m−1)sin^(m−2)(theta) B with B=[[(m+1)cos²(theta)−1]cos(mphi), −m cos(theta)sin(mphi)]; [−m cos(theta)sin(mphi), −(m+1−cos²(theta))cos(mphi)]]. For t=sin²(theta), x=cos(mphi), B+(m+1)I has nonnegative diagonals and determinant 2m+1+m²t−(m+1)(m+2)t x+(m+1)t² x². Its derivative in x is nonpositive on x∈[-1,1], and at x=1 it factors as (1−t)[2m+1−(m+1)t]>=0. Rotating phi by pi/m maps B to -B, giving |eigenvalue(A)|<=m²−1. At theta=pi/2,x=1 the smallest eigenvalue of A equals −(m²−1), so the interval is sharp and equality points precisely the specified m equatorial directions (opposite sign shifted). Positive-definite inside, PSD at endpoint; min h>0 makes body full dimensional. Integrating volume V=(1/3)∫h det(I+epsilon A) over S², odd parity annihilates linear/cubic terms. Integrated Bochner and beta integral give deficit (m(m+1)−2)epsilon² I_m/2 with I_m=π 2^(2m+1)(m!)²/(2m+1)!, yielding exact endpoint 4π/3−π2^(2m)(m!)²(m+2)/[(2m+1)!(m−1)(m+1)²] and asymptotic π^(3/2)/(2m^(5/2)). Independently verified determinant polynomial symbolically and sampled Hessian eigenvalues/spherical volume quadrature for m=3,5,7; all-m proof analytic.

## originality

PASS

The exact sharp sectoral amplitude, discrete equatorial degeneracy set, endpoint volumes, and high-degree asymptotic are a legitimate refinement in a natural highest-weight harmonic family. Existing known exact zonal Legendre-mode results address a genuinely different harmonic orbit with different thresholds and curvature loci; generic support-function convexity criteria alone do not supply the sharp family-specific constant.

## value

PASS

Sectoral and zonal spherical harmonics are canonical extremal spectral modes of constant-width deformations. Their different sharp convexity boundaries and volume deficits form a motivated exact benchmark for 3D constant-width body theory, with a precise m^-5/2 hierarchy; no global Blaschke–Lebesgue minimizer claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
