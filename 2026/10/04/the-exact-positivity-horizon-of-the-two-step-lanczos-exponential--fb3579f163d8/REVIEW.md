# Same-model review

## Correctness
PASS. The two-step approximation is exactly an affine polynomial in \(A\), obtained by interpolating the exponential at the two Ritz values. Strict interior Ritz bounds follow because an affine polynomial cannot isolate an extreme eigenspace when the starting vector has at least three distinct active eigenvalues. The affine interpolant is strictly decreasing, so all physical-coordinate signs reduce to the single scalar \(q_t(L)\), whose unique zero gives the stated horizon. The minimal-dimension claim follows from exactness when the active minimal polynomial has degree at most two. The exact witness and its Lanczos coefficients were independently replayed from the packaged checker.

## Originality
PASS with residual literature risk. Classical Krylov sources cover polynomial exactness, convergence, and preconditioning. Druskin's especially close full-text monotonicity result proves Euclidean norm monotonicity with Krylov dimension and positivity of the reduced Jacobi-system coefficients, not sign preservation in the original coordinates after multiplication by the Lanczos basis. Searches using positivity-preserving, nonnegative-vector, sign-loss, interpolation, and matrix-exponential aliases did not locate the exact physical-coordinate horizon or the inevitable late-time sign loss for every nontrivial two-step diagonal instance. Older matrix-function or positive-systems literature remains a residual risk.

## Value
PASS. Matrix-exponential Krylov methods are used for parabolic and diffusion-type evolution, where coordinatewise positivity can have physical meaning. The result identifies a qualitative failure invisible to standard norm-monotonicity theory, gives a complete sharp safe-time interval for the first nontrivial Lanczos dimension, proves the minimal dimension of failure, and supplies an exact reproducible witness. The invariant is not an arbitrary slice: it is the precise time at which a positivity-preserving exact diagonal semigroup ceases to be represented by a positive two-step Krylov approximation.

Same-model review: passed. Independent audit: not yet performed.
