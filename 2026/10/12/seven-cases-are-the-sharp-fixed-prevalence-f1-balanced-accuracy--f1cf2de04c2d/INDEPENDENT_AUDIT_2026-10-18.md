# Independent mathematical audit

## correctness

PASS

With P actual positives and Q=N-P negatives, positive-cell matrices are uniquely (a,b,P-a,Q-b), with 1≤a≤P-1 and 1≤b≤Q-1. Their scores are rational functions F1=2a/(P+a+b) and B=(1+a/P-b/Q)/2. Independent exhaustive rational enumeration over all a,b,P for N=4..8 examined every same-(N,P) unordered pair, including boundary N=4 with one matrix: N=4,5 no disagreement; N=6: 10 matrices, 0 strict reversals, 1 weak-only mismatch; N=7: 20 matrices, exactly 3 strict reversals and no weak-only; the three pairs match the package. This is an actual finite complete proof for N≤7, not a partial sample. The concrete N=7 P=3 witness scores 2/5<1/2 and 13/24>11/24, and scaling preserves both scores.

## originality

PASS

The general bias/disagreement of F1 and balanced accuracy/Informedness is established prior; the apparently new component is the exact smallest strictly positive fixed-prevalence boundary and complete three-pair first stratum.

## value

PASS

The minimum nondegenerate fixed-prevalence binary example and complete first reversal layer form a natural exact finite cutoff for two ubiquitous performance metrics. The positivity and fixed-prevalence constraints remove trivial degeneracies and expose metric tradeoffs cleanly; exact small examples can be useful as test cases and pedagogy without a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
