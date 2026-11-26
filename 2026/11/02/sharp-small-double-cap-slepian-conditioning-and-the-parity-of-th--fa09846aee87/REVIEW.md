# Independent mathematical audit

## correctness

PASS

For integer m≥0 and equatorial parity ε, associated Legendre polynomial degrees give exactly e^{imφ}(sin θ)^m(cos θ)^ε p(u), u=sin²θ and deg p≤r=floor((L−m−ε)/2). The two hemispheres and azimuthal integrals cancel in the quotient, yielding the stated weight u^m(1−u)^{ε−1/2}. For fixed j≤r, the local monic orthogonal polynomial scaled by s^{-j} at u=sv depends analytically on s near zero: the scaled moments do, and their limiting Gram matrix is positive definite. Its limit is the monic shifted Jacobi polynomial q_j. The shifted Rodrigues expression has leading coefficient binom(m+2j,j); integrating it against that polynomial by parts j times gives squared norm 1/(m+2j+1) before monic normalization, hence the claimed local squared norm h_j. The full Gram entries of the unscaled monic polynomials are B(m+i+j+1,ε+1/2)+O(s), because their lower-degree coefficients vanish at least as O(s). In a locally orthonormal basis, multiplying the full Gram matrix by h_r leaves a single nonzero limiting diagonal entry B(m+2r+1,ε+1/2) with entrywise O(s) error. Its associated largest eigenvalue is simple for small s (including the scalar block) and the reciprocal gives the smallest quotient and its relative O(s) error. The largest exponent L+1 requires ε=0 and m≡L mod 2. In those blocks the unique largest binomial factor is at r=floor(L/2), hence |m|=0 or 1 by L parity; the ±1 blocks are exact symmetry copies. For the largest eigenvalue, integrate a tangential Taylor expansion of |f|² over each small cap: the linear term averages to zero, and the error is O_L(s²) uniformly on the unit sphere of V_L. Each cap has area πs+O(s²). The evaluation Gram matrix at the two poles has equal diagonal (L+1)²/(4π) and off-diagonal (−1)^L(L+1)/(4π) by the addition theorem. Its top eigenvalue gives the claimed coefficient after multiplying by πs. Taking the positive square root of the quotient gives κ, with the stated error.

## originality

PASS

The double-cap concentration operator and its exact order and parity blocks are known. The fixed-L sharp smallest-eigenvalue coefficient and the parity-dependent minimizer across the full low-pass space, with the resulting restriction condition number, are distinct from this operator formulation and from the related catalogue spectra inspected. The largest-eigenvalue coefficient follows comparatively directly from pole evaluations and is not the main novelty.

## value

PASS

The result specifies both the direction that is hardest to recover from antipodal polar measurements and the exact leading conditioning penalty. Which symmetry wins cannot be read off from the vanishing exponent alone: multiple angular sectors share that exponent, and the winning sector changes with cutoff parity. This is a useful refinement of qualitative polar-gap instability, at the natural fixed-bandwidth shrinking-data limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
