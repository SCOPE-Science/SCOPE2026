# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed the normalized curved-hemisphere moments: height uniform on [0,1], horizontal centered variances 1/3 and vertical centered variance 1/12. The orthonormal basis yields K(x,y)=1+3 x_h·y_h+12(x3−1/2)(y3−1/2). At equatorial x, K=4+3y1−6y3=4−3√5 v·y; its negative cap lies entirely within the hemisphere. Integrating that cap gives row norm L=61√5/15−7. Conditional azimuth symmetry makes row integral nondecreasing with unrestricted horizontal radius; convexity in the height coordinate bounds all rows with z≤1/3 strictly below the equator except z=0, while Cauchy–Schwarz K(x,x)=7−12z+9z²≤4 controls z≥1/3. Duality gives identical L1 and L∞ operator norms. Equality in the triangle inequality forces equatorial kernel signs for L∞; since the maximal-row set has measure zero, L1 has no nonzero extremizer. Negative cap mass gives overshoot (L−1)/2. Independent two-dimensional quadrature at five heights confirms constant and strict height comparisons, without replacing global analytic proof.

## originality

PASS

PASS (qualified): Sloan–Hall–Hart–Snyder (SIGGRAPH 2003) is a highly relevant antecedent: its Appendix 9.1 already constructs least-squares-optimal hemispherical spherical-harmonic projection using Gram-matrix inversion, which covers the projector itself and explicitly motivates it. It does NOT in the inspected 10-page text compute the sharp L1/L∞ operator norm, characterize exact equatorial maximizing rows, all extremizers, or negative overshoot. Defant et al. provide exact full-sphere projection constants (degree one gives 5/3) but their rotationally invariant sphere lacks the hemisphere truncation. General manifold kernel projector stability and the published affine-simplex example do not supply the exact hemispherical bound. The contribution is strictly the sharp stability/equality characterization, not invention of hemisphere least squares.

## value

PASS

PASS: A degree-one affine projector on the uniform hemisphere is the canonical smallest nontrivial hemispherical least-squares approximation and already appears in applied spherical-harmonic radiance projection. Exact sharp worst-case amplification and negative overshoot quantify robustness of that established procedure. The unexpected fact that all worst-case evaluations lie precisely on the measure-zero equator and that L1 extrema are unattainable is a complete natural equality classification, not just a numerical bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
