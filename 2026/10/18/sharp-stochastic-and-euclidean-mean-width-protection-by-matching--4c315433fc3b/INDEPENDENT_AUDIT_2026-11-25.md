# Independent mathematical audit

## correctness

PASS

For distinct scores, any surviving edge other than the extreme pair misses at least the lesser endpoint gap D. When the extreme pair is deleted by a matching both next-best candidates survive, so the loss equals D there and zero elsewhere. Rank labels are uniform independently of order statistics, giving the independent Bernoulli factor k/binom(n,2). Two deleted edges sharing the maximum label give strict loss on the open configuration where their other endpoints are smallest and next smallest, and the bottom gap is smaller than the top; positive density on an interval gives it positive probability. Projection of a standard Gaussian onto H_n preserves edge differences, with independent chi_(n−1) radius of mean a_(n−1), so central symmetry gives width loss 2 EΔ/a_(n−1). Integrating the joint extreme density with all interior scores in (x+t,y−t) gives the displayed η integral. Gaussian rare-event counts on upper and lower disjoint windows converge jointly to independent Poisson processes; their first decreasing gaps are independent Exp(1) by the exponential-arrival ratio. Conditioning on the second largest and its event V≥u_n/2 gives the conditional scaled-gap upper tail e^(−s/2); the complementary binomial event contributes vanishing mean by Cauchy–Schwarz and the second moment bound for the Gaussian maximum. Thus u_n η_n→1/2, and the relative width-deficit error is independent of k by exact linearity. Independent exact enumeration checked 21,55,575 deletion sets at n=4,5,6 and found equality for the 9,25,75 matchings and strict average loss for every other set on the tested score vectors. Replay: /workspace/branches/204cddac-b09d-4cae-9c6c-abd9f4b61052/independent_finite_check.py and independent_finite_check_results.md. Uploaded code was inspected, not executed; finite checks are not the proof.

## originality

PASS

The supported distinct claim is the sharp finite-n, fixed-deletion-cardinality optimization and stochastic comparison, including matching equality and strict expected loss for other deletion patterns. Spherical normalization and Poisson gaps are standard and overlap materially with a same-day indexed finding. The strongest overlapping result concerns independent random edge retention at fixed p and does not imply the finite deterministic claim or its matching asymptotic by setting p to a function of n.

## value

PASS

This optimizes a natural geometric invariant of the standard edge-root realization and classifies all maximizing fixed-size deletion patterns. The atomless-score stochastic statement is stronger than mean width alone and gives a reusable rank-order comparison, not just a computation on isolated graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
