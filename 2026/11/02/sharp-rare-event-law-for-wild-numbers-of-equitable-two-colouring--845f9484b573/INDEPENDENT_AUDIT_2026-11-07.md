# Independent mathematical audit

## correctness

PASS

For N=binom(n,2), d=n-1 and m=floor(N/2), the known component identity W=kappa(red)+kappa(blue)-2 equals isolated monochromatic vertices plus excess nontrivial components. A specified monochromatic cut of k vertices has probability at most e*2^{-k(n-k)} even under fixed balanced edge totals; summing k=2..floor(n/2) gives O(n^2*4^{-n}) excess. Pairwise isolated vertices of the same color also have probability O(n^2*4^{-n}), while opposite-color isolates are incompatible. Exact expectation p_n=n[(m)_d+(N-m)_d]/(N)_d follows by symmetry. The logarithm of each falling-factorial ratio is -d*log 2 - d(d-1)/(2N)+O(1/n), giving p_n=(4/e)n*2^{-n}(1+O(1/n)); hence the full stated P(W=0), P(W=1), P(W>=2), E W hierarchy and conditional single-isolate event. Explicitly checked odd N, n>=4 and asymptotic limitations; no finite computation substitutes for these bounds.

## originality

PASS

Dawkins et al. give the exact wild-number component identity and E[W_n]->0 for balanced random complete graph coloring but not an asymptotic equivalent, sharp e^{-1} balance correction or higher-wild-number error hierarchy. The older dense G(n,m) connectivity literature treats the same fixed-edge event family and may contain stronger isolated-vertex asymptotics; inspected Bender–Canfield–McKay multiplicative connected-graph estimates do not by themselves yield the exponentially small disconnection complement. PASS is a qualified statement-level judgment, not a new claim for isolated-vertex arguments generally.

## value

PASS

This completes an explicitly studied random-coloring question by a sharp rare-event rate, physically significant balance-vs-independent-model constant and the typical exact repair cost of one wild edge. These are not obtained from the prior mere convergence to zero; the exponential remainder separates singleton isolation from multi-component failures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
