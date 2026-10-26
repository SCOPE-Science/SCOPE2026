# Self-review

**Correctness — PASS.** The principal lemma uses only the spectral inequality \(B^2\preceq qB\), sparsity of the input tail, and an elementary one-variable maximization. Its extremal rank-one block reaches the coefficient exactly. Iterative support retention follows by induction and the tail-to-leading norm ratio contracts by at least \(q\) per step. The counterexample loses the leading support in one step and becomes a fixed eigendirection with eigenvalue \(q\). Finite exact-arithmetic witnesses and randomized numerical tests corroborate, but do not replace, the proof.

**Originality — PASS (qualified).** The 2026 sparsified-power paper proves general dimension-independent guarantees but does not provide this exact sharp one-sparse overlap threshold and equality/tie behavior. Yuan–Zhang (2013) established the algorithm and broader perturbation-based sparse recovery; their theorem's hypotheses and implications do not identify the present necessary-and-sufficient universal retention boundary. Search of relevant sparse power, sparse PCA, and published mathematical finding records found no equivalent threshold. This negative search alone is not a uniqueness proof; earlier equivalently phrased support-preservation analyses remain plausible.

**Value — PASS.** A single discarded leading coordinate makes every subsequent sparse iteration incapable of recovering an otherwise exact top eigenvector. The finding gives the sharp dimension-free line between guaranteed protection and a concrete irreversible failure, for every finite truncation budget, and quantitatively controls the surviving iteration. This is a structural limit of sparse eigensolvers, not a generic normalization or one-off finite calculation.

**Closest literature and limits.** The direct comparators are Hajlasz–Musco–Weare–Webber (2026, arXiv:2610.14620v1) and Yuan–Zhang (JMLR 2013). The result applies only to exactly one-coordinate leading eigenvectors, positive semidefinite matrices, already sparse starts, and exact arithmetic. A possible older alias for the extremal lemma is the principal originality risk.

Self-review: passed. Independent audit: not yet performed.
