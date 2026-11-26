# Independent mathematical audit

## correctness

PASS

For each chord the minor-arc start is uniform independent of its minor-arc length, by uniform translation of the two endpoints. Chords therefore have independent uniform rotations given their lengths, using the natural regular conditional version; repeated endpoint and diameter exceptions are null. For short arcs of fractions r,s≤1/2, the intersection of an interval of length r and its translate by s has length (r−s)_+ (no wraparound contributes positive length). Their symmetric difference has length 2min(r,s), exactly the endpoint-alternation event. Distinct crossing indicators on disjoint chord pairs use independent rotations. For pairs sharing a chord, fixing its rotation leaves the two other rotations independent with crossing probabilities constant in the fixed rotation, so the indicators are pairwise independent given the lengths. This suffices to sum the Bernoulli variances, not to assert mutual independence. For a moment replay, set W_i=2r_i, iid Uniform(0,1); g=min(W_i,W_j) has density 2(1−g) and moments 1/3 and 1/6. Its one-chord average is w−w²/2, with mean 1/3 and second moment 2/15, hence variance 1/45. There are three unordered pairs of edges sharing one endpoint per index triple; counting both covariance orders yields Var(M_n)=binom(n,2)/18+6 binom(n,3)/45. The integrated conditional variance is binom(n,2)/6. Their sum gives the quoted total variance, and their ratio gives the explained fraction, also at n=2. The L² projection property gives uniqueness up to almost-sure equality. The analytic argument proves the finite-n formulas. The frozen symbolic code and simulation record were inspected, not rerun; sampling is corroboration only.

## originality

PASS

Marginal crossing-count moments are prior and explicitly excluded from the novelty claim. The supported distinct contribution is the full Euclidean-length-vector conditional mean and variance and the sharp decomposition of prediction risk, not the complete conditional distribution. The closest catalogue comparison uses only the additive one-chord projection, and the primary literature inspected does not supply the full geometric conditioning calculation.

## value

PASS

The natural prediction problem asks how much of a topological count can be recovered from metric observations. The exact full-vector optimal risk separates the O(n²) residual rotation effect from O(n³) total variance, and the conditional variances apply even for fixed inhomogeneous length profiles. The exact residual also distinguishes conditioning on all lengths from the simpler additive one-chord predictor. No significance is claimed for other chord models or for conditional tail laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
