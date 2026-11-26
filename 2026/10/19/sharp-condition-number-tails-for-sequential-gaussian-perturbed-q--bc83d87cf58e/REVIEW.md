# Independent mathematical audit

## correctness

PASS

Condition first on the entire predictable history, then use the fact that the radial perpendicular law depends only on the deterministic signal length to reduce to conditioning on B and the in-span Gaussian V. The perpendicular residual is positive almost surely. To bound each append, factor it as [Q,q] diag(R,1) for B=QR; the unit-column assumption puts 1 between the extreme singular values of R, and the two exceptional Gram eigenvalues of [Q,q] are 1 ± sqrt(1−ρ²). Thus κ is at most 2κ(B)/ρ, and central chi-square inverse moments (dominating the noncentral inverse moments) give Eκ(B)^d<∞ because B has final codimension d+1. At ρ=0 the bordered Gram has simple kernel spanned by (−B†u,1); differentiating in ρ² gives Rayleigh quotient 1/(1+||B†u||²), so the actual κ is asymptotic to D(B,u)/ρ. For fixed B,V with R=||V||>0, the append bound confines the large-κ event to ||W||<4κ(B)R/t for t>4κ(B). The local asymptotic therefore squeezes its conditional probability between Gaussian small balls of radii (1±o(1))RD/t. The bounded density and the complementary t≤4κ(B) case give integrable domination by a constant times κ(B)^d(1+R^d). Multiplying the volume and Gaussian density at zero by the chi moment of R gives the stated gamma-factor constant; integrating the positive tail gives exactly the positive-moment frontier. For two columns B is a single unit vector, so D=2, and the exact central two-column ratio test agrees in m=2 and 3.

## originality

PASS

The distinct contribution is the positive finite limiting coefficient for the actual condition number with normalized columns and predictable perpendicular signals. The closest same-model work supplies the residual distribution and a one-sided conditioning certificate. The exponent and moment cutoff are related to those inputs and are not the strongest originality basis; neither an upper certificate nor the unnormalized Wishart asymptotic computes this history-averaged coefficient.

## value

PASS

The exact rare-event coefficient distinguishes distributions having the same rectangular exponent, shows which history and signal enter the leading risk, and controls the actual spectral condition number rather than a sufficient certificate. The nonzero coefficient and sharp integrability threshold explain the qualitative square-versus-one-extra-row change in the mean even at small nonzero noise. This is a meaningful refinement for an existing model, not a claim about floating-point QR generally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
