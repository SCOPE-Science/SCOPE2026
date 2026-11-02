# Independent mathematical audit

## correctness

PASS

Zero GMRES(2) correction is optimal exactly when r^T Mr=r^T M²r=0. Writing Q=x²+y²+z² and P=y(ux+vz), normal equations give Q+P=0, Q+2P+uvxz=0, so Q=uvxz>0 and xz>0. Normalize xz=1, t=x²>0, eliminate y to obtain exactly uv=G_{v/u}(t), with converse. The function diverges at both ends and attains a positive minimum, proving iff. Q>x²+z²≥2xz implies threshold>2; test t=1 gives bound≤2+2rho/(rho²+rho+1)≤8/3; the balanced factorization proves 8/3. Exact radical example u=(5+sqrt5)/(2sqrt2), v=(5-sqrt5)/(2sqrt2), r=(1,-1/sqrt2,1) satisfies both normal equations. The TGA subspace span{r,Mr} gives the same first-cycle minimum; unaccelerated (I-M)^3=0. Five independent symbolic assertions corroborated critical identities, with analytic proof for all weights.

## originality

PASS

The known standard-Jordan (equal-superdiagonal) GMRES theory is explicitly excluded from novelty. The ratio-dependent Euclidean frontier for fixed unequal upper links, and same-product reversal, are not implied by equal-link bounds: diagonal similarity is nonunitary. A paper constructing some matrices with prescribed stagnation cannot solve the fixed pair (u,v) classification. The originating two-grid paper supplies algorithmic context but its full technical version was inaccessible; this remains a qualified best-knowledge assessment.

## value

PASS

A sharp readily evaluated two-weight failure boundary for a natural three-site Krylov prototype shows that identical spectra and positive link products can have opposite acceleration behavior. The comparison with finite-terminating Richardson demonstrates a genuine algorithmic instability mechanism without claiming higher-dimensional universality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
