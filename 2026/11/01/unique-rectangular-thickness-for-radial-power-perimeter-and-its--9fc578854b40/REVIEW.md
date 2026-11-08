# Independent mathematical audit

## correctness

PASS

Direct four-side integration gives Fp/4=∫0^a(x²+b²)^{p/2}dx+∫0^b(a²+y²)^{p/2}dy. For p≥0 derivative is positive (p=0 handled). For p=−q, t=a/b, its sign is that of 1−Rq(t) with Rq=q(1+t²)^{q/2}∫0^t(1+u²)^{−1−q/2}du. Each factor is positive and strictly increasing in t; Rq(0)=0 and →∞, yielding a unique sign-change and global minimum. Rq increases with q at fixed t, giving strict t_q decrease; at q=1 the integral yields R1(t)=t. As q↓0, t_q→∞ and dominated convergence in the root equation gives t_q^{−q}/q→π/2. For q→∞, Rq(c/q)→c and squeezing gives qt_q→1. Independent high-precision four-exponent bisection and direct F(b) checks confirm minimizer ordering and q=1; finite checks are supplemental.

## originality

PASS

Best-of-knowledge after comparing hypotheses and implications with two accessible full primary arXiv preprints: their Hausdorff continuity/inclusion monotonicity and fixed-standard-perimeter optimization do not yield the fixed-side-length negative-exponent minimizer, strict exponent monotonicity, square crossing or essential singularity.

## value

PASS

A fixed-width rectangle is a natural constrained convex shape, and radial negative-power weighting creates nontrivial competition between side length and distance to the singularity. The unique optimizer, exact square transition and essential singularity as p↑0 give a sharp phase profile that neither basic calculus monotonicity for p≥0 nor generic weighted-perimeter results imply. The boundary cases are explicit, making the result useful for shape-optimization examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
