# Independent mathematical audit

## correctness

PASS

The stationary generator on x^p y^q has reset loss only for q>0. Normalizing time by r and position and driver by sqrt(D/r), I recovered the three forward moments by recursive symbolic evaluation (replay: python /workspace/branches/independent_moments.py, SymPy; output /workspace/branches/independent_moments.log). The exact fourth-moment cross difference is -2(b-c)(7bc+3b+3c-27). Its derivative and K-2=b(9-b)/((b+2)(b+3)) give precisely two positive preimages for 2<K<Kmax; the lower endpoint b=0 is excluded, K=2 occurs only at b=9, and the maximum has a single preimage. As an independent sign check, on distinct positive equal-K pairs write t=b+c; then 0<t<9 and both arguments satisfy x^2-t*x+(27-3*t)/7=0. Reduce the numerator and denominator of H to linear residues. The numerator of (H(b)-H(c))/(b-c), with the original positive denominator Q(b)Q(c), is 14256(t+5)^2(307760+63141t-290t^2-51t^3)/2401. Since 290t^2+51t^3<6741t, it is strictly positive. Thus the larger branch strictly increases H. A prescribed positive variance can be matched at either branch by adjusting s, so the ambiguity is real without m6. Once the branch is known, variance gives s; simultaneous rescaling of mu,r,D changes only the clock, not the stationary distribution. Neither statistical accuracy from samples nor separate recovery of all three rates is claimed.

## originality

PASS

The exact inverse folding and separation classification is distinct from the known model, scaling, and forward moments, which are excluded from the originality claim. No inspected equivalent or dominating result supplies the same classification; this is a bounded comparison, not certification of priority.

## value

PASS

For an established exactly solvable persistent-noise model, the result identifies where variance and kurtosis genuinely fail to distinguish a memory ratio, and which next consecutive even moment resolves it uniformly over admissible positive parameters. The global ordering is usable for choosing between two moment-matched parameter sets, not just a new parametrization of a tabulated moment. The result is about population observability, not practical estimator conditioning or absolute parameter recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
