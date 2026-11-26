# Independent mathematical audit

## correctness

PASS

The two residual maps leave the lone components r_2-(c/a)r_1 and r_1-(c/b)r_2, respectively. For c=0 the mean is a diagonal contraction; changing sign of one coordinate reduces c<0 to c>0. With p=c/a, q=c/b the diagonals of I-M are q(1-p^2)/(p+q), p(1-q^2)/(p+q). Its determinant is pq[(1-pq)^2-(p+q)^2]/(p+q)^2, hence nonnegative exactly when p+q<=1-pq, since pq<1. That inequality also makes both diagonals nonnegative. Equivalently (a+b)|c|<=det A. Fix eigenvalues mu and kappa*mu; the trace and determinant are fixed and the largest possible |c| is half the eigenvalue gap, attained at equal diagonals. Substitution gives (kappa^2-1)/2<=kappa, precisely kappa<=1+sqrt(2) including equality. The incoming residual (1,-1) at the stated equal-diagonal witness yields the ratio 2*kappa^2/(kappa+1)^2 and in particular 9/8 at kappa=3; every residual is realizable because A is invertible. Independent exact checks built the residual maps directly for 1,032 rational SPD examples (610 unsafe, 8 exactly on the determinant boundary). The proof, not this finite check, controls all orientations and all residuals.

## originality

PASS

The method and coordinate-proportional sampling are established; the distinct claim is the necessary-and-sufficient Euclidean equation-residual condition and its worst-orientation condition-number frontier. Neither the inspected convergence theorems nor the closest same-day records cover those quantifiers. The originality decision is limited to the available comparative evidence.

## value

PASS

The ordinary residual norm is a natural progress/stopping diagnostic, different from the energy that coordinate minimization controls. The exact per-matrix test and the sharp condition-number cutoff tell when one can trust that diagnostic in conditional expectation; even a modestly conditioned kappa=3 example separates the two metrics. This is a useful narrow boundary, not a competing general convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
