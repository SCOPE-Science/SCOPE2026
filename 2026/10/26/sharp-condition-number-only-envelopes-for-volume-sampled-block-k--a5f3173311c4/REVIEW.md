# Scientific assessment

**Correctness — PASS.** The exact expected-projector formula follows by a determinant-generating identity and independently checked row-space projector enumeration. Newton's elementary-symmetric inequalities give rigorous coordinatewise monotonicity and reduce global spectral optimization to the two attainable endpoint profiles. The one-step error factor follows from orthogonal projection. Exact-rational enumeration and rotated-matrix numerical tests are supporting checks rather than evidence of infinite generality.

**Originality — PASS (subject to historical-priority uncertainty).** The polynomial formula for the expected projector is explicitly credited to earlier work, notably arXiv:2610.12346. Full inspected treatments of that article, arXiv:2503.13941, and arXiv:1904.04587 did not state the sharp four fixed-condition-number envelopes, paired extremal profiles, or exact minimax block-budget threshold. No equivalent mathematical claim was identified in the available semantic research records. Prior results entail the formula once the additional nontrivial sharp optimization is supplied; priority for that optimization still requires independent assessment.

**Value — PASS.** A user choosing an expensive determinantal block sampler often has only the Gram condition number, not its full spectrum. The result supplies a universal and optimal contraction certificate, converts a target error decrease to the exact necessary-and-sufficient block size, and quantifies the sharp range of spectral equalization. These are algorithmically motivated sharp extremal answers, not a parameter substitution or a recomputation of the already-known projector identity.

**Closest work and limits.** The spectral polynomial identity is known (Entezari–Banerjee–Kalantari 2026; Rodomanov–Kropotov 2019). Xiang–Xie–Zhang 2025 offer a different block-Kaczmarz convergence bound. Only exact determinantal sampling, consistent systems, and conditional one-step squared-error rates are covered. Independent scientific audit and historical-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
