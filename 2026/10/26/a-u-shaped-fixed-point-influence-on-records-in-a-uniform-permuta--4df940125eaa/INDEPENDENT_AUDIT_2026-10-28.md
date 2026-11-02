# Independent mathematical audit

## correctness

PASS

For uniform π∈Sn, condition on π(j)=j. If j>i, the first i positions retain uniform relative order and P(R_i|I_j)=1/i. If j<i, the remaining i−1 prefix entries necessarily include an entry >j, so the last among these is the prefix maximum with probability 1/(i−1). At i=j≥2, record status requires the preceding i−1 values to be exactly {1,...,i−1}, with probability binom(n−1,i−1)^−1. R_1 is certain. These cases give the full cross-covariance kernel, whose telescoping i-sum yields E[R|I_j]−H_n=binom(n−1,j−1)^−1−1/n. Binomial coefficient monotonicity proves positive signs at exactly first/second and last/two-end positions for n≥5, negative center, and U-shape. Summing over j gives Cov(F,R)=n^−1 sum_{k=1}^{n−1}binom(n−1,k)^−1=2/n²+O(n^−3). Independently enumerated all 5912 permutations across n=2..7, verifying every n×n exact rational cross covariance. Boundaries n2..4 and conditioning on exactly one specified fixed point are explicit; no independence claim.

## originality

PASS

Best-of-knowledge PASS for the finite-position conditional record-law and exact sign-changing cross-covariance matrix, not the known marginal harmonic expectation or fixed-point/record asymptotic phase. Dubach 2025/2026 treats global record asymptotics in conjugation-invariant random permutations classified by fixed-point count, not conditioning on one marked position. A relevant published Resultary record treats fixed-point versus adjacent descents; its conditional exchangeability is analogous but descents and records are different statistics with opposite support/covariance behavior. Historical exact first-moment identities for rencontres statistics may have an equivalent formulation, recorded as risk.

## value

PASS

Joint behavior of two classical permutation statistics—positional fixed points and left-to-right records—is a natural combinatorial question not settled by their separate marginal means. The exact location-resolved cross-covariance reveals a nontrivial U-shaped sign reversal: the fixed-point count has positive aggregate covariance although most interior positions are negatively correlated with total records. The full indicator kernel and telescoping structure give more than a routine aggregate first moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
