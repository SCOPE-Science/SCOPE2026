# Independent mathematical audit

## correctness

PASS

With 1<R, epsilon>0 and G=diag([[-1,1],[1,-1]],[[-R,R],[R,-R]]), the two-dimensional Krylov subspace spanned by z=(1,0,epsilon,0) and Gz has no nonzero vector in ker G, so its Ritz nodes satisfy lambda_-<lambda_+<0. The standard 2-node Lanczos polynomial p_t(s) interpolating e^(ts) yields component multipliers (p_t(-1), positive slope, epsilon p_t(-R), R epsilon positive slope)/(1+epsilon). Rayleigh inequalities force p_t(-1)>0. At t>0 only p_t(-R) can become negative, exactly when the lower Ritz node exceeds -R; then it has the unique crossing t*=log((R+lambda_+)/(R+lambda_-))/(lambda_+-lambda_-). Sylvester criterion on H+RM=(Z^T(G+RI)Z) with first principal minor R-1>0 gives det(H+RM)=-R[R³epsilon^4+2R(R²-2R+2)epsilon²+2-R]. Thus all-time positivity iff that polynomial is >=0; for R>2 it has one positive root in u=epsilon². The epsilon->0 positive limit of t* is half log(R/(R-2)), though epsilon=0 exactly is an invariant exact 2-state case. Independently reconstructed H,M and symbolic determinant using SymPy, confirming exact witness R=4,epsilon=1/8 with polynomial -47/64 and Gram values. No claim about irreducible or general Markov chains.

## originality

PASS

The 2013 Frommer–Güttel–Schweitzer and 1992 Saad Krylov papers supply basic Ritz-interpolation tools, not all-time Markov probability sign conditions. Closest Resultary SCOPE-the-exact-positivity-horizon-of-the-two-step-lanczos-exponential--fb3579f163d8 proves a related *diagonal positive definite matrix with strictly positive physical-coordinate start* horizon, whose core affine-interpolant formula is a true prior ingredient. Here the exact Markov generator has zero eigenvalues, a non-diagonal physical basis, a start with zeros and specific variable rate/mass parameters, and a different unconditional safe regime R<=2; that diagonal theorem does not directly entail the explicit R-epsilon positivity phase and crossing threshold. The retained novelty is the complete mass-conditioned reversible two-link classification, not a new general interpolation identity.

## value

PASS

Positivity is a physical probability constraint for a Markov semigroup, so an exact safe/unsafe criterion for the ordinary minimal nontrivial Lanczos approximation provides an analytically sharp benchmark. The rare-block late-time negative component and nonzero finite epsilon->0 crossing time distinguish semigroup positivity from projected Krylov behavior, with explicit limits and no claim of universality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
