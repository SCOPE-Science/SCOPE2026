---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The exact last-reset channel has survival S_t and additive replacement matrix B_t. Its adjoint is invertible since S_t>0. Algebraic adjacent dual intertwiner equals k_t Ad_(U^-1) plus scalar functional tr(F_t Y) I, with F_t a positive scalar-unitary conjugate of B_t-B_(t-1). Since k_t>=0, d>=2, positivity iff F_t is PSD: for negative F eigenvector choose output orthogonal to its rotated vector; F PSD gives sum of CP maps. The renewal increment identity decomposes B_t-B_(t-1) as sum_j (nu_(t-j)-nu_(t-1-j)) S_j sigma_j, so nondecreasing absolute-time reset-event masses imply CP for all. At a first decrease m a dimension-m cyclic gate and pure reset make sigma_j pairwise orthogonal, forcing negativity. Rising hazards (1/10,9/10,91/100,...) give nu1=1/10, nu2=41/50, nu3=2449/10000 and min F3 eigenvalue -639/100 while Schr intermediates remain CPTP. The universal quantifier over varying d is essential; fixed qubit necessity is not asserted.

## originality

PASS

Carollo–Wald 2026 introduces both reset-picture intermediates and unequal divisibility phenomena; Settimo et al. general picture distinctions and Wald et al. renewal formulas are also prior. The qualified novelty is an all-gate necessary-and-sufficient criterion in terms of absolute-time renewal-event monotonicity, its cyclic witness for every decrease and exact fixed-pair PSD condition, not the already-observed nondivisibility phenomenon.

## value

PASS

The iff criterion converts an all-system quantum positivity question into testable classical renewal probabilities, while pinpointing a sharp distinction from the known hazard criterion for Schrödinger CP-divisibility. This is a motivated complete classification, not a routine rephrasing of general CP map properties.

The dated certificate retains the supplied scientific assessment, sources and limitations.
