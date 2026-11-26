# Independent mathematical audit

## correctness

PASS

The original equations and universal asymptotic are correct; the original Finding's prose incorrectly said zero-or-light probabilities were lowered even though its own zero-probability and PGF inequalities run in the opposite direction. The complete corrected RESULT.md and SLOGAN.txt are in repairs/3; the new wording states only the exact expectations and tail comparisons. Conditioning gives G=exp(c(z exp(d(z-1))-1)); the log PGF difference is b-a-z h(1-z)>0 because h(t)=b exp(-at)-a exp(-bt) decreases from b-a and stays positive. Taking z=(log n-2 log log n)/d gives logarithmic Chernoff overhead o(n); the event K=floor(n/log n), Y=n-K has first-stage factorial cost -n+o(n), canceled by the +n+o(n) term from the second-stage factorial. Replacing (n-K) log log n by n log log n costs o(n). The resulting two log-tails differ by n log(b/a)+o(n), proving reversal at every sufficiently large integer threshold. An independently written positive incomplete-gamma survival sum (independent_recheck.py, compound_tail) confirms negative differences at thresholds 1–11 and +0.000306018554012509325 at 12. The frozen 646-check script was inspected, not run. No finite-population or uniform-threshold conclusion follows.

## originality

PASS

The supported distinct claim is the joint strict PGF order and quantitative eventual upper-tail reversal for cumulative two-generation counts for every fixed opposite ordering, not the invention of the PGF framework or of compound-Poisson tail methods. The corrected wording does not enlarge the theorem.

## value

PASS

For a natural cumulative count, even strict ordering of all discounted expectations and a smaller mean can coexist with a strictly larger extreme upper tail; the theorem identifies the exact exponential rate of that reversal, not just an instance. This is a useful benchmark for distinguishing risk metrics in an idealized branching model, not an operational intervention or finite-population prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
