# Independent mathematical audit

## correctness

PASS

Monotone OR sweep commutes with unions, reducing worst nonzero binary state to singleton. First-infection along either simple arc costs first sweep plus the number of rank descents after the first edge. Each target is reached by its shorter arc in at most floor(n/2) sweeps. On even n=2m only antipodal target can force m; this requires two length-m descending chains, with n binom(n−2,m−1) orders per source and unique source when m>=3 (opposite rankings contradict overlap). Thus n² binom(n−2,m−1) orders. For n=4 all 24 orders extremal. Independently enumerated 24, 720 and 40,320 permutations at n=4,6,8, confirming 24,216,1280 extremals and universal latency bound. Finite tests only corroborate all-n proof.

## originality

PASS

Best-of-knowledge distinct mathematical contribution established by comparison of actual statements, not titles. A prior theorem would need to classify both antipodal descending rank chains and show unique extreme source n≥6, yielding n² C(n−2,m−1). Periodicity/duality results cited do not imply the enumeration without new argument. General ingredients and established results explicitly credited; no priority guarantee.

## value

PASS

Sequential CA consensus latency and exact permutation extremal probabilities are natural dynamics invariants. Sharp all-size time and unique antipodal witness geometry plus infinite even-n labeled schedule count go beyond routine order-independence and can be used to calibrate asynchronous update protocols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
