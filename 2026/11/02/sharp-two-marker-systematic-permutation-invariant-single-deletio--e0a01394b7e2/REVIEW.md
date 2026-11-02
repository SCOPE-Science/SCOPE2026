# Scientific review

**Correctness — PASS.** The all-length one-marker lower bound follows from a proved singleton-deletion characterization: a permutation whose standardized one-deletion outputs all agree must be monotone. The explicit codebooks contain all messages exactly once and their deletion-output sets are disjoint. Replaying `verify.py` from the supplied package checks all codewords and every one-deletion output, with independent rank implementations and a finite cross-check of the critical lemma.

**Originality — PASS, subject to residual priority risk.** The directly relevant Wu–Bui–Niu–Vu–Wang 2026 full text provides four-marker one-PID constructions for sufficiently large lengths, not the sharp three- and four-symbol two-marker examples. Gao–Shum 2024 supplies known perfect codes for the different symbol-invariant channel, not standardized PID correction. Claim-level searches of indexed mathematics and accessible prior claims revealed no equivalent full-systematic two-marker finite optimum. The 2016 precursor's full journal text was not accessible; an unindexed equivalent short-block construction cannot be ruled out.

**Value — PASS.** The problem is the precise redundancy cost of systematic rank-modulation storage under an unknown single deletion. The theorem gives a universal structural obstruction to one marker, and exact first nontrivial two-marker optima for the two next message lengths. These are sharply optimal finite encoder benchmarks, requiring only half as many markers as the published general PID construction in those small instances; no unproved asymptotic improvement is implied.

The principal comparison is arXiv:2609.37578v1, Sections II–III and VI; the independent SID comparison is arXiv:2411.08258. The boundaries are exactly specified: all-length lower bound, exact values at information lengths two through four, no general two-marker upper bound.

Self-review: passed. Independent audit: not yet performed.
