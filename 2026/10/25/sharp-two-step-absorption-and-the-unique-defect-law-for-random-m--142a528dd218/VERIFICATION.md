---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the two-step absorption law

The direct exhaustive checker `CHECKER.py` enumerates all binary matrices for \(1\le n\le4\), computes Boolean products without relying on the missing-event formula, and checks the diagonal/off-diagonal marginal probabilities and total expected missing entries for the uniform Bernoulli model. It also counts matrices with no empty rows or columns and those with universal Boolean squares. The captured output is `CHECKER_OUTPUT.txt`.

For proof verification, one must separately check the formula \(\Pr(E_{ij})=s_pq_p^{n-2}\) when \(i\ne j\), as \(b_{ij}\) occurs in both endpoint intermediary choices, and ensure the pairwise bounds differentiate a shared source or target from disjoint endpoint roles. There are at most \(2n^3\) pairs of defect events of shared-source/shared-target type. The resulting second Bonferroni term is \(o(n^2q_p^n)\) for every fixed \(0<p<1\). The conditioning error \(2n(1-p)^n\) is also lower order.

Finite checking cannot establish the asymptotic statement and does not independently certify originality or mathematical value. The self-review is recorded in `REVIEW.md`; independent audit has not been performed.

