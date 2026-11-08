# Independent mathematical audit

## correctness

PASS

For a rank-q real matrix error with positive singular values s_i and S=sum s_i, direct reconstruction gives polar-scaled descent E+=U diag(s_i-tS)V^T. Exact nonnegative line search gives t=1/q because <E,D>=lambda*S^2 and ||D||_F^2=lambda^2*S^2*q. Rank one vanishes in one step, rank two gives signed (s1-s2)/2 and its negative, hence equal new singular values and exact second-step cancellation. At rank r>=3 the vector a(1,...,1,r-1) is invariant in positive singular-value proportions with factor (r-2)/r>0, proving an infinite nonterminating ray. Equal-singular-value initialization forces the only potentially universal constant t=1/r; that ray rules out r>=3. The rank-raising example diag(3,1,eps) vs diag(3,1,0) has first-step difference norm tending sqrt(8/3). These are symbolic all-rank arguments, not extrapolation from finite tests.

## originality

PASS

The exact rank-two two-iteration theorem, universal-rank phase boundary, and discontinuous rank-raising limit are distinct from the established linear convergence bounds and equal-spectrum one-step resonance in Jawanpuria–Garai–Mishra 2026. The PolarGrad rank-calibrated method and unscaled polar-optimizer results do not imply finite termination for every rank-two singular-value pair. A general optimization theory might encode the centered-absolute-value map, so best-of-knowledge originality is qualified.

## value

PASS

Universal finite termination for exact-line-search polar descent is a natural qualitative algorithmic invariant, not a small numerical improvement. The r=2 versus r>=3 boundary and explicit discontinuity show why limiting rank-two behavior cannot predict the rank-three optimizer; the classification is self-contained and useful for comparing spectral optimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
