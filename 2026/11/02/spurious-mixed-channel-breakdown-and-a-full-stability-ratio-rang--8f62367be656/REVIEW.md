# Independent mathematical audit

## correctness

PASS

Orthogonalizing A^-1v gives v2=(A^-1v-alpha v)/beta, hence A v2=(v-alpha Av)/beta and (I-P)A v2=-(alpha/beta)(I-P)Av exactly. Opposite-sign eigenweight construction with three distinct eigenvalues uses nonzero Vandermonde determinant, and necessity follows from the inverse Rayleigh quotient and Krylov minimal polynomial. Independent SymPy computation confirms determinant 36r^2, alpha=9(r^2-1)/(9+17r^2), exact gamma^2 rational expression, and endpoint constants. Continuity gives full range on 0<r<1; no approximate rounding premise.

## originality

PASS

Best-of-knowledge new exact mixed-versus-split third-step cancellation condition, sharp symmetric existence iff, and fixed-condition-two complete ratio range; prior SPD residual ordering excludes the indefinite breakdown and earlier indefinite numerical experiments do not prove this exact theorem.

## value

PASS

Structural explanation for a genuine premature algorithmic basis breakdown with unexhausted Laurent-Krylov space, and a fixed well-conditioned counterexample to any global residual-ratio bound; this clarifies the scope of established SPD stability comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
