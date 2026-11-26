# Independent mathematical audit

## correctness

PASS

The two outer-product updates give a 2-by-2 block of trace 9 and determinant 8 for M_u alongside an eigenvalue 1, and M_v is diagonal. Thus the spectra are (1,1,8) and (0,4,5), with unique unsmoothed winner u and traces 10 and 9. Set t=exp(-1/mu); the sign of the objective difference is the negative of the sign of P=2t+t^8-1-t^4-t^5=(t-1)Q(t). Descartes' bound of two positive zeros counted with multiplicity and the exact signs at 1/2, 3/5 and 9/10 prove two simple roots, all ties and all three winner intervals. Independent 60-digit bisection on P, not the frozen script, gives 1.879597222729257440 and 6.819744289599112074 for the two mu values. For d=2 the sorted smaller eigenvalue and the trace are the two ascending partial sums; strict advantage in both makes the sum of the strictly decreasing convex exponentials smaller. Concretely, at fixed trace that sum decreases as the smaller eigenvalue moves toward half the trace, while at fixed smaller eigenvalue it decreases as the trace increases. Increase the trace first and the smaller eigenvalue second; the intermediate ordered pair is feasible. Dimension one is immediate. The claim is about binary choices, not fractional optimization.

## originality

PASS

The normalized smoothing, Bayesian E-design setting, low-smoothing stability, and the elementary d<=2 majorization argument are not new. The contribution that survives comparison is the explicit minimal-dimensional shared-prior rank-one witness, with a singular interior winner, strict agreement at both endpoints, and exactly delimited reversals; it is not supplied by the inspected smoothing results or the distinct indexed two-switch examples.

## value

PASS

This is a compact counterexample to reading the low- and high-smoothing rankings as evidence for intermediate smoothing. It works for two legitimate rank-one experiments on a common prior, selects a singular design on a whole open interval despite a full unit loss in the exact E-objective, and locates that interval exactly in the smallest possible dimension. This supplies a reproducible diagnostic instance for a standard objective without claiming a solver failure or general switch bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
