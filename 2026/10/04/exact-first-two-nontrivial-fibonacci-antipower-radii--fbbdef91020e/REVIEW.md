# Independent mathematical audit

## correctness

PASS

The finite-to-infinite bridge is valid because the Fibonacci word is Sturmian, hence has exactly \(N+1\) distinct factors of length \(N\). A fresh regeneration of the fixed point found exactly 19 length-18 factors and 41 length-40 factors. Exact block comparisons reproduced the claimed minimum-block histograms: for \(k=3\), \(2:8,3:4,4:1,5:2,6:4\); for \(k=4\), \(3:4,4:2,5:4,6:27,7:2,9:1,10:1\), with a unique minimum-10 factor. Therefore the finite lists are exhaustive, not stabilization heuristics, and \(R_{\mathbf f}(3)=6\), \(R_{\mathbf f}(4)=10\).

## originality

PASS

Garg’s primary Fibonacci antipower paper proves a uniform linear upper bound, specifically a constant at most about 2.89, and uses the Sturmian framework, but it does not give exact uniform radii for \(k=3\) or \(4\). Berger--Defant formulate the broader morphic-word problem, again without these exact values. Fresh exact-number and Resultary searches found no covering statement. The exact small radii require the complete factor census rather than following from the asymptotic/general bound.

## value

PASS

These are the first two nontrivial exact values of the uniform Fibonacci antipower radius directly motivated by the central all-index theorem. The \(k=4\) computation also isolates a unique extremal obstruction factor. Exact natural finite cutoffs of this central radius function are mathematically meaningful even without a general closed formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
