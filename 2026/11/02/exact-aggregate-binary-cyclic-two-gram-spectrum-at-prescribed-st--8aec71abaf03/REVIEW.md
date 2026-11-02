# Review: aggregate cyclic binary two-gram spectrum

## Correctness

**PASS.** The cyclic degree-balance equation and positive alternating-run decomposition are proved directly. Each active cycle with \(t\ge1\) realizes every integral equal-pair allocation between the two symbols via the explicit word \(0^{A+1}1^{B+1}(01)^{t-1}\); inactive cycles contribute only all-zero or all-one profiles. Minkowski sums of the intervals establish the complete profile criterion. A unit-capacity allocation for all-active cycles gives the sharp full-layer threshold, with length-two cycles providing the obstruction one transition earlier. The two-cycle exceptional interval gap, exact layer sum and deterministic code-capacity interpretation all follow without computational assumptions. Standalone exhaustive finite comparisons were run, but are not treated as proof of infinite assertions.

## Originality

**PASS, with residual risk.** Tesler (2017, arXiv:1708.03654) studies cyclic and multicyclic realizations for prescribed read multiplicities, but does not give a formula for fixed **individual cycle lengths** and the missing binary two-read observation when they match; Theorem 9.3 allows generic multicycle decompositions without fixing their lengths. Yehezkeally–Marcovich–Yaakobi (2021, arXiv:2108.11725) addresses multiple **linear** strings and multi-substring reconstruction, not this cyclic fixed-length short-read spectrum. Kiah–Puleo–Milenkovic (2015, arXiv:1502.00517) provides related linear sequence-profile methods. Public research-record searches for fixed-length cyclic multistrand aggregated dinucleotide types did not identify an equivalent formula. An undiscovered reduction from general multicycle-flow theory remains a concrete novelty risk.

## Value

**PASS.** A natural sequencing observation loses strand labels while retaining exact circular digram multiplicities. The theorem completely characterizes its attainable information states for *any* fixed number of prescribed-length cycles, proves a sharp dimensionless saturation threshold, and derives a closed finite-length zero-error capacity with a previously non-obvious equal-length defect for two cycles. This is a structural profile classification, not merely a numerical example or application of a listed prior bound.

## Limits

Only noiseless complete binary cyclic two-read observations and known lengths at least two are covered. The theorem does not give the sizes of ambiguous reconstruction fibers nor address errors, unknown lengths or alphabets with more than two symbols. Published multicyclic flow theory could contain an equivalent specialization. Finite computations verify tested lengths only; the written proof establishes the general statement.

Self-review: passed. Independent audit: not yet performed.
