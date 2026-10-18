# Independent mathematical audit

## correctness

PASS

For a Gaussian projected-gradient control-variate estimator, write m=P_S g, r=g-m, s=||r||²/||g||² and t_d(s)=min(1,1/(ds)), with t(0)=1. Wick symmetry gives the exact one-step expected quadratic objective difference -alpha||g||²+(alpha²/2)[g^T H g+||r||² tr(H)+r^T H r+tau² M3(H)/4], M3=(tr H)^3+6 tr H tr(H²)+8 tr(H³). At tau=0 the criterion is gamma>=t_d(s) R/2. For d>=3 the trace defect Q=I-H/L, tr Q>=delta=1-1/kappa, and a minimum-eigenvalue direction orthogonal to gradient/hint span yield exact gamma=1+1/(2d kappa). For d=2 the minimum eigenvalue of gg^T+rr^T equals [1+s-sqrt(1-2s+5s²)]/2, and one-sided derivatives show the maximum at s=1/2, yielding gamma=5/4-(5-sqrt5)(1-1/kappa)/8. Equality witnesses exist for every kappa and dimension; gamma=1 is safe only if d=2 and kappa>=(5+sqrt5)/2. For tau>0 an explicit nonnegative sixth-moment term remains. Independent rational moment and spectral witness tests corroborated core formulas, not substituted for proof.

## originality

PASS

Best-of-knowledge new exact one-step minimax expected-objective safety frontier for the same Gaussian projected-gradient oracle estimator, including a sharp two-dimensional golden-ratio transition and a higher-dimensional obstruction. Source estimator and general variance/convergence results are credited.

## value

PASS

This theorem supplies a sharp, attained safety criterion for the reference step of a newly studied Gaussian hinted zeroth-order optimizer. The unexpectedly different two-dimensional golden-ratio transition versus the d>=3 unavoidable discount is an informative exact boundary that a researcher implementing or analyzing this precise oracle would need, not an arbitrary parameter slice; it also identifies the finite-radius noise-floor limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
