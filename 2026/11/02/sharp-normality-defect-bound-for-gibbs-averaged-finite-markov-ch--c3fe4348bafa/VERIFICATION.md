---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For all N>=2 and integer t>=1, checked the actual Gibbs projection G(x,y)=1_C(x,y)pi(y)/pi(C), weighted Hilbert space adjoint and Pi; A=P-Pi, B=GAG. The compression M->GMG is an orthogonal Hilbert–Schmidt projection, giving ||A||_F²=||B||_F²+D. Individual s_j(B)<=s_j(A), and noncommutative Schatten Hölder yields ||B^t||_F²<=sum s_j(B)^{2t} without assuming B normal. With x_j=s_j(A)^2, y_j=s_j(B)^2, the inequalities x_j^t-y_j^t>=(x_j-y_j)^t and Jensen for N-1 entries give D^t/(N-1)^{t-1}. Cyclic trace identity gives delta_2=1/2||P*P-PP*||_F², normal A makes delta_t=0. For ergodic normal P spectral radius on mean-zero <1 and ||B||op<1 ensures primitive Q. Rank k-1 variant and rI+(1-r)Pi sharpness are compatible with all edge cases k=1,N. Bounded independent rational checks cover a directed normal chain, normal-to-nonnormal compression, time-two defect and eight powers. Computations are corroborative only; this analytic chain supplies the unbounded time theorem.

## originality

PASS

Compared actual all-time squared weighted Frobenius inequality, singular-value correction and sharp D^t coefficient to Choi–Wang Theorem 4.1/Corollaries (reversible case). Their statement has self-adjoint baseline/average, while current theorem permits normal nonreversible baseline with nonnormal GPG and supplies exact nonnormal defect at t=2. Generic noncommutative Schatten Hölder and Eckart–Young are classical ingredients but do not state the combined sharp Markov comparison. Resultary published nearest binary-event chain theorem treats different operators. Best-of-knowledge O passes; an older general compression inequality might subsume.

## value

PASS

A dimension-sharp, all-positive-time comparison for conditional Gibbs compression of finite Markov chains is a motivated strengthening of reversible mixing acceleration. The exact commutator defect quantifies how nonnormality obstructs the comparison, and the sharp loss term makes equality/strictness and finite threshold mixing ordering explicit. This is not simply a renaming of spectral contraction: normal P may yield nonnormal GPG, so Hölder is essential. Useful as a benchmark when designing block samplers. The result does not imply total-variation improvement from every start or reduced computational cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
