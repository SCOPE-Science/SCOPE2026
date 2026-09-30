# Independent audit — 2026-09-29

Record: `2026/09/17/stationary-occupancy-variable-length-nonoverlap--effa1409f1ac`  
Assigned and audited source tree: `81883854a3bd7af53df944cea5a522f940f59df6`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported_with_definition_convention_noted**. The stationary occupancy inequality is correct: for every codeword and every offset covering the origin, stationarity gives the same cylinder probability, while two distinct such occurrences would either overlap properly (forcing a prohibited prefix-suffix match) or be nested (forcing a prohibited codeword subword). The offset events are therefore pairwise disjoint and their probabilities sum to at most one. The iid specializations follow immediately. The mean-length arguments also check: the discrete sequence a_k=k q^{-k} has nonnegative second differences for integer k>=2, its piecewise-linear interpolation is convex, and for q>=3 the continuous function x q^{-x} is convex on [2,infinity]. The resulting inequalities q^{L+1}>=ML and, for q>=3, q^L>=ML yield the stated fixed-q log-log lower terms. Those mean-length deductions use the standard variable-length non-overlapping-code convention that codeword lengths are at least 2, as in the cited Wang-Wang definition; the stationary inequality itself remains valid even if length-one words are admitted.

## Originality

**qualified_stationary_formulation**. Modern Wang-Wang work already studies variable-length non-overlapping codes, average length and a generating-function framework from which the uniform weighted inequality is closely related. The explicit stationary-law occupancy theorem, arbitrary iid source specialization, and the fixed-alphabet log-log mean-length consequences were not located in the inspected modern sources. Older comma-free/self-synchronizing literature uses different terminology and was not exhaustively available in full text, so priority is deliberately not asserted beyond this narrow formulation.

## Scientific value

**useful_source_sensitive_bound**. The result gives a one-line probabilistic mechanism behind an additional synchronization length cost and extends the bound from uniform counting to arbitrary stationary sources. The fixed-alphabet log-log overhead is a concrete strengthening of the elementary prefix-code entropy scale, even though it does not improve the best maximum-cardinality bounds for a prescribed maximum length.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/stationary-occupancy-variable-length-nonoverlap--effa1409f1ac
- https://arxiv.org/abs/2402.18896
- https://arxiv.org/abs/2108.06934
- https://doi.org/10.1109/TIT.2017.2742506
- https://doi.org/10.1093/comjnl/28.4.379

## Limitations

- The sharper mean-length consequences use the standard convention that variable-length non-overlapping codewords have length at least 2.
- The uniform inequality is closely connected to prior avoidance-generating-function machinery; novelty is not claimed for the abstract principle of disjoint cylinder events.
- Older variable-length comma-free literature was not exhaustively available in full text, so the originality assessment remains qualified.
- No claim is made to improve the strongest known maximum-cardinality bound at fixed maximum codeword length.
