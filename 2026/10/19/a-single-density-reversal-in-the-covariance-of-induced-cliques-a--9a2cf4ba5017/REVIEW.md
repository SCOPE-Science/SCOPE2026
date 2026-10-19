# Scientific review

**Correctness: PASS.** The overlap calculation separates every pair of induced \(r\)-vertex motif indicators according to their number of common vertices, including the mutually exclusive diagonal. Dividing the resulting covariance by a strictly positive factor yields a strictly decreasing function with opposite endpoint signs, proving a unique root. Bernoulli's inequality bounds it, and a uniform fixed-size overlap expansion establishes the first finite-size correction. Exact edge-state enumeration and exact-rational checks corroborate, but are not used as infinite proofs.

**Originality: PASS (self-review, residual uncertainty).** The 2008 motif-count method derives marginal second moments through overlap counting, and the 1990 random-graph framework encompasses more general subgraph statistics. Their possible implication of this finite covariance identity is acknowledged. The distinctive claim assessed here is the strict single-crossing classification for all \(r,n\) and its sharp threshold location, not the generic second-moment technique. Relevant accessible primary texts on induced graphlets and subgraph approximation do not state or establish that classification. Full comparison was not possible for the 1990 framework and the original 2008 paper; independence of this finding from all earlier work is not established.

**Mathematical value: PASS.** The two motif counts quantify mutually exclusive local density classes. Their mixed covariance is a natural diagnostic for jointly standardizing graphlet features in a binomial random graph. The full sign-phase diagram, exact smallest ambient-size boundary, and universal large-\(n\) density with correction are structural consequences rather than a single low-order table entry. The sign reversal makes a qualitative prediction for every motif size.

**Limitations.** The result is for independent-edge binomial graphs, fixed \(r\) in the asymptotic, and exactly one defect edge. Marginal variance frameworks may implicitly contain pieces of the calculation. External comparison is substantial but not exhaustive.

Self-review: passed. Independent audit: not yet performed.
