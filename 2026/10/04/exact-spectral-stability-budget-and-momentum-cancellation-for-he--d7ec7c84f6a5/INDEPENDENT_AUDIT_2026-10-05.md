# Independent mathematical audit

## correctness

PASS

Diagonalizing the SPD quadratic gives the scalar recurrence u_{k+1}=(1+m-s)u_k-mu_{k-1} with m=alpha-theta lambda and s=beta lambda. Applying the three strict Jury inequalities gives exactly -1<m<1 and 0<s<2(1+m). With 0<=alpha<1 and theta>=0, the uniform condition reduces to the worst curvature lambda=L: L(beta+2theta)<2(1+alpha), which also enforces m>-1. For fixed stable m, the root product gives the lower bound sqrt(|m|); it is attained on the full conjugate-root interval when m>=0 and uniquely at zero trace when m<0. The matched-curvature choice theta=alpha/lambda, beta=1/lambda gives m=0,s=1 and annihilates that mode in one update. Independent exact arithmetic and spectral-radius checks agree with every boundary and rate formula.

## originality

PASS

Originality passes. The defining full text gives the same Hessian-corrected heavy-ball iteration and sufficient convergence restrictions for a much broader strongly-quasiconvex/nonconvex setting. It does not give the exact SPD-quadratic Schur region, the coefficient-two stability budget for theta, the complete modewise rate optimum for signed effective momentum, or matched-curvature one-step cancellation. Classical heavy-ball spectral results are the theta=0 subfamily and do not imply the corrected budget.

## value

PASS

An exact quadratic phase diagram is the natural sharp baseline for a newly proposed Hessian-corrected inertial method whose published theorem is deliberately conservative because it covers much broader objectives. The result quantifies the precise stability price of correction, identifies signed effective-momentum rate regimes, and exhibits exact curvature cancellation. These are structural method facts, not a routine numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
