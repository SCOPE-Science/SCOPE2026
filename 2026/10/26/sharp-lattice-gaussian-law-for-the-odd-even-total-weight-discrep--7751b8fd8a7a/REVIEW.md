# Review of the odd–even total-weight discrepancy local law

## Correctness — PASS

The odd/even partition split gives exact counts \(N_n(d)=Q((n+d)/2)p((n-d)/4)\) with the requisite integrality conditions. The standard asymptotics of ordinary and distinct/odd partitions lead, after a uniform quadratic expansion, to the stated \(n^{3/4}\)-scale Gaussian law and the exact balanced count. The proof handles arbitrary congruence classes of \(n\) modulo four and all fixed local windows; the Riemann-sum normalization accounts for lattice spacing four. The `verify.py` checks are auxiliary, not a proof of the limit.

## Originality — PASS with stated priority risk

The Andrews–Ghosh Dastidar and Bardhan–Saikia original papers on `SOME(n)` were inspected, including all nineteen pages of the latter. Their theorems concern aggregated signed weights, identities, congruences and monotonicity, not the partition-level local distribution. Craig–Li's alternating sum is by position, not by part-size parity; Bringmann and collaborators analyze numbers rather than weights of residue-class parts. The closest indexed published result involving weighted-representation partitions does not logically entail this exact coefficient distribution. Nevertheless, a more general partition ensemble theorem could contain the law implicitly; independent bibliographic confirmation is outstanding.

## Mathematical value — PASS

The statement obtains a complete Gaussian local description of the distribution of a natural arithmetic weight-imbalance statistic, fixes the first-order constant and lattice, and determines an asymptotic probability of exact odd/even weight balance. It is more informative than an aggregate moment congruence. The triviality of the factorization alone is not offered as mathematical value.

## Scientific limits

Fixed compact scaling windows only; no rate or large-deviation tail asymptotics are claimed. General-priority risk remains; the underlying Hardy–Ramanujan asymptotics are classical.

Self-review: passed. Independent audit: not yet performed.
