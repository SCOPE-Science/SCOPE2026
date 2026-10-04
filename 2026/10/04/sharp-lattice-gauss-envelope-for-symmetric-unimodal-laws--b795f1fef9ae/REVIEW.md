# Review

## Correctness

PASS. Every symmetric unimodal integer mass function has the unique centered
discrete-uniform mixture
\[
\alpha_k=(2k+1)(p_k-p_{k+1}).
\]
Variance and the two-sided threshold tail are linear in these weights, so the
problem is exactly a planar upper-hull problem. The initial-ray slopes have a
single explicit maximum, and all later consecutive slopes equal
\[
\frac{3(2a-1)}{(k+1)(2k+1)(2k+3)},
\]
which decreases strictly. This determines the hull and equality cases. The
continuum limit follows from the explicit breakpoint and
\(V_k=k(k+1)/3\).

## Originality

PASS, with a residual historical-lattice risk. The full four-page
Dharmadhikari--Joag-Dev article was inspected. It establishes continuous
Gauss--Tchebyshev inequalities through convex mixtures of uniforms, but does
not state the discrete centered-uniform hull, the lattice breakpoint, or the
variance-by-variance piecewise-linear envelope.

Huber's full arXiv text was inspected. Its Theorem 3 gives a discrete
unimodal two-sided inequality obtained by smoothing, and the paper explicitly
states that this inequality is not tight. The inspected argument does not
solve the symmetric integer-lattice extremal problem.

Targeted web and semantic-database searches for discrete Gauss inequalities,
symmetric unimodal lattice tails, discrete-uniform mixture extremizers, and
sharp variance-tail envelopes did not return an equivalent formula.

## Value

PASS. Gauss's inequality is a foundational sharp concentration result for
unimodal laws. The integer lattice changes the exact extremizer geometry: it
creates an explicit arithmetic breakpoint and a piecewise-linear variance
frontier. The result supplies the exact symmetric discrete envelope and
recovers the classical Gauss curve in the continuum scaling limit.

Same-model review: passed. Independent audit: not yet performed.
