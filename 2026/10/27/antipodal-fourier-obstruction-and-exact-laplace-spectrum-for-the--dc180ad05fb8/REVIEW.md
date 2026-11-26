# Independent mathematical audit

## correctness

PASS

Under normalized Haar measure the first-quadrant axial marginal is [t f(t)+∫_t^π f(s)ds]/π. Its derivative is t f′(t)/π and vanishes at zero; two integrations by parts followed by Riemann–Lebesgue give the two signed antipodal limits with the factor 1/π. Independently, write F_f=f(π)−∫ f′(r)1_{[-r,r]²}dr. For n≠0 the normalized box factors are sin(nr)/(πn), and for n=0 the factor is r/π. For the exponential, integrating the product by cosine subtraction gives the mixed formula with B_{n−m}^{−1}−B_{n+m}^{−1}>0 for positive n,m, even when n=m. The constant is a positive integral; direct integration of r e^(−ar)sin(nr) gives the axial formula. Odd terms are positive, and for even n the sign of 2a(1−e^(−πa))−π e^(−πa)(a²+n²) gives the exact threshold including equality. Q(a)>a², so the first strictly negative even frequency is the stated strict rounding, asymptotic to √(2a/π)e^(πa/2). Compact-group Fourier positivity rules out positive definiteness for every a>0. The one-circle transform has the positive coefficients given; the Euclidean sup kernel is the product of two positive 1D Laplace pullbacks. An independent midpoint integration of the layer formula at a=1 gives approximately −0.000138259 at (4,0), and direct real Gram contractions give −7.740924236 and −85.99081613 on the 16 and 32 grids. These computations corroborate the proof, not certify the infinite statements; the frozen checker was inspected, not run.

## originality

PASS

Credit the supremum-endpoint theorem and especially the exact all-frequency sign cutoff at every damping, not the general Fourier/antipodal method. The strongest earlier record proves the closely related finite-p antipodal-tail obstruction, including the identical one-circle comparison transform. The actual mirror text explicitly assumes finite p. Neither that text nor the primary general-purpose criteria give the complete endpoint sign spectrum.

## value

PASS

The supremum product of intrinsic circle distances is a natural compact covariance input, and its behavior contrasts with both the one-circle and Euclidean-supremum cases. Identifying that every finite damping fails only on even axes above a precise threshold explains why a low-frequency numerical test can misleadingly report positivity, particularly when the first negative mode grows exponentially with damping. The exact cutoff is independently useful beyond a negative-type obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
