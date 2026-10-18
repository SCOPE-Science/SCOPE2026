# Review

**Correctness — PASS.** The lower bound uses a proved 1-Lipschitz variation lemma on cyclic-distance labels of adjacent required weight-two windows, and the upper bound uses an explicit alternating gap list. Every step applies for all integer window lengths \(k\ge4\); the finite verifier exercises the construction through 200 and enumerates small exact minima.

**Originality — PASS against inspected sources.** Sawada, Williams and Wong (2013) supply an interval-weight universal cycle whose \(\{1,2\}\) specialization is one character longer than the new construction; King et al. (2014, arXiv:1405.5938v1) obtain fixed-weight overlap cycles in a different stride model. Neither published result yields the present cyclic-variation lower bound and sharp linear correction. Earlier terminology-equivalent work remains a literature risk.

**Value — PASS.** Constant-weight window coverage is a natural constrained indexing problem. The result finds a cyclic host within one or two positions of optimum for every \(k\ge4\), establishing the precise second-order coefficient and a constructive near-optimum with a uniform proof.

**Limitations.** The exact general minimum for \(k\ge6\) remains undecided within the stated one-/two-position interval. Computations are checks, not infinite proofs; no independent scientific validation was performed.

Self-review: passed. Independent audit: not yet performed.
