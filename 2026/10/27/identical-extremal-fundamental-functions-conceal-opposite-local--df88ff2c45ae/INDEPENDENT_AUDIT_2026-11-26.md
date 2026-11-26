# Independent mathematical audit

## correctness

PASS

The exact weights are at least one with finite excess integrals, hence give Banach function norms and finite norms on finite-measure indicators. The minimum functions are sqrt(a) and a because each unit-weight region has infinite measure; the interval-swap involution makes the two targets equimeasurable and gives exact equality of their maximal functions for every a. On 16^(−N)≤a<16^(1−N), the target maximum is at most (16/3)4^(−N) and the squared source maximum is at least the n≥N+1 sum of 1/n², hence at least 1/(N+1). The source is admissible in the cited sense and the target-to-source maximal ratio tends to zero. Cauchy–Schwarz with the test function proportional to (v/w)1_E gives the exact squared fixed-E norm ∫_E v²/w, including an infinite supremum by truncation. In the aligned case the joint quotient has plateaus n² of mass 16^(−n). With D_j=(16/15)16^(−j) and D_j≤a<D_(j−1), the exact top-a integral is Σ_(n≥j)n²16^(−n)+(a−D_j)(j−1)²: any choice omitting higher plateaus cannot improve on taking them and part of the next one. The series gives this integral as a(j²+O(j)); j=log(1/a)/log(16)+O(1) gives the constant 1/(4 log 2), with natural logarithms. In the separated case each J_n has quotient integral one, and arbitrarily many whole J_n fit below every positive measure by going far enough into the tail. Thus the modulus is infinite, not merely bounded away from zero. Independently evaluated the aligned greedy formula at 24 exact rational scales; replay: python3 /workspace/branches/reproduce_frozen.py weights; log /workspace/branches/reproduction-weights.txt. The proof, not the finite check, establishes the asymptotic and extended-value claims.

## originality

PASS

The necessary target-to-source ratio and the basic weighted duality formula are not new. The supported distinct claim is a specific matched-marginal counterexample to sufficiency even with the entire individual extremal data fixed, with the sharp aligned modulus and the separated infinite modulus. No equivalent construction was established in the inspected literature or catalogue.

## value

PASS

This explicit witness isolates a missing datum in an actual necessary embedding test. It rules out all criteria based only on the four individual extremal functions for this setting, rather than merely exhibiting failure of one asymptotic ratio. Exact weight alignment, the quantified optimal decaying modulus, and divergence at every scale make the witness useful and reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
