# Review

## Correctness

**PASS.** The reproducing-kernel formula reduces the sampling inequality to a frame inequality for \(u_\lambda(\xi)=R_m(\lambda\xi)|\xi|^{-s}\) in \(L^2([-a,a])\). The integral defining \(C_{s,m}\) is finite and positive precisely on \(m+\frac12<s<m+\frac32\). Large-parameter norm growth forces bounded sample locations; continuity and the Bessel property force their only accumulation point to be zero. The first nonzero Taylor term then makes the sum of squared frame-vector norms finite, so the frame operator is compact, contradicting a positive lower frame bound.

## Originality

**PASS, with residual literature risk.** The closest primary source, [1], Section 5, proves nonexistence only for \(0<s<\frac12\) and explicitly discusses whether real sampling sequences exist. Its supercritical kernel family has a Taylor-subtracted exponential depending on the sampling parameter, so the fixed-window frame criterion cited there does not imply the present theorem. Searches of indexed mathematical literature returned no statement covering this same supercritical fractional Paley–Wiener sampling claim. This is not a proof that no unindexed source exists.

## Value

**PASS.** The result settles the supercritical noncritical half of a natural sampling question raised in [1]. It shows that stable recovery by real point values of \(f\) is impossible throughout this range, and distinguishes that obstruction from the available reconstruction by samples of the fractional Laplacian.

## Limitations and closest literature

The critical exponents \(\frac32,\frac52,\ldots\) are not covered. Complex sampling and alternative measurements remain open here. The theorem is an infinite-dimensional proof; it does not rely on finite numerical experiments.

Self-review: passed. Independent audit: not yet performed.
