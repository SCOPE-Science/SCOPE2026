# Independent mathematical audit

## correctness

PASS

PASS: Each marginal record probability is 1/i or 1/j. For i<j condition on unordered values of first i positions: the event B_j requires j to lie in suffix (because j>i); A_i depends only on the independent order of the prefix and is 1/i conditionally. For i>j condition instead on positions of values 1..j: B_j depends on their ordering, while A_i sees a larger value in first i and depends only on complementary values, giving independent conditioned indicators. At i=j, the only conditional overlap is when first i values are exactly 1..i, an event probability 1/binom(n,i); then A_i=B_i marks the event pi(i)=i, adding conditional variance (i-1)/i^2. Total covariance is exactly delta_ij*(i-1)/(i^2 binom(n,i)); summing yields 1/n+1/(2n^2)+O(n^-3) and correlation ~1/(n log n). Fully independent exact enumeration n<=7 of inverse words and both flag vectors checked all n^2 entries including n=1; finite tests are not the proof.

## originality

PASS

Exact index-resolved diagonal matrix and off-diagonal Bernoulli independence are not implied by inspected marginal or aggregate permutation record statistics, including inverse-descent generating functions. Historical refined record point-process work may nevertheless contain an equivalent law.

## value

PASS

PASS: Pairwise independence off matching position/value indices and an explicit positive diagonal cross-covariance are a sharp coupling law not visible in marginal record-count distributions. The O(1/n) total covariance and O(1/(n log n)) correlation quantify this near-independence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
