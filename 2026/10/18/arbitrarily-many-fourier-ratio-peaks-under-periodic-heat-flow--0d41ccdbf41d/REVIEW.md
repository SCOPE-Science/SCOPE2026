# Independent mathematical audit

## correctness

PASS

At positive heat time t, Fourier magnitudes of the explicit ±jL frequencies are b_j=a_j exp(-j²L²t), giving R=√2 Σb_j/(Σb_j²)^{1/2}. Exact adjacent log-amplitude identity log(b_j/b_(j−1))=((2j−1)L²)(τ_j−t), τ_j=(m−j+1)T/m. At each of m−1 crossings exactly two neighboring amplitudes match and every other is ≤η² times them, so R>1.99. At the K+1 alternating separating endpoints/midpoints all other b_j are ≤η of one dominant b_j, so R<1.43. Real analytic, nonconstant R achieves strict extrema between separated comparison points, K maxima and K−1 minima in (0,T). For q synchronized Fourier pairs at t*, R(t*)=√(2q) while as L→∞ R(0)→√2, yielding amplification →√q; B arbitrary. Checked explicit finite K=1..5 and q=4,16,100 in fresh independent checks. No bound for fixed bandwidth/dynamic range is claimed.

## originality

PASS

The temporal trajectory assertion is not a restatement of static Fourier-ratio norm or sufficient sampling bounds. Iosevich et al. treat fixed-time a priori heat/sampling bounds with signal-regularity dependence and do not supply all-K oscillatory counterexamples or unbounded class-free transient amplification. Prior standard exponential-mode domination suggests the construction but does not imply the specific alternating extrema without its quantified gap proof.

## value

PASS

Construction demonstrates an exact, structurally meaningful obstruction to a plausible monotonicity/unimodality heuristic for heat smoothing, and to signal-independent transient-amplification control; it informs the necessary bandwidth/regularity hypotheses of sampling or PDE estimates, rather than arbitrarily testing a small Fourier support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
