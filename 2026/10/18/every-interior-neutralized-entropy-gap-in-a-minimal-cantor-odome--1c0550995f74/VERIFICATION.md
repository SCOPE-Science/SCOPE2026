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

# Verification and limits

Execute `python verify.py` with Python 3 and no third-party dependencies. The script enumerates all unordered pairs of finite \(7\)-bit odometer states for six translation amounts and checks preservation of the first differing digit and both sides of the Euclidean–ultrametric inequality with exact rational arithmetic. It also evaluates the finite level-endpoint dimension ratios over eight block indices. Its recorded output is `PASS 146320 finite exact-rational/computed endpoint assertions`.

This computation cannot establish the infinite coding or asymptotic entropy theorem. The proof in RESULT.md independently establishes the tail inequality by telescoping, the full all-iterates Lipschitz inequality, bounded-cutoff entropy sandwich, oscillating block-endpoint subsequences for every \(r>0\), and uniform empirical-measure convergence. The finite checker is intentionally supplementary and its numerical endpoint tests are not used as an infinite-limit argument.

The first source is publicly dated 2026-10-08 on arXiv. Priority is based on comparison of accessible literature, not on external independent verification; the latter is not performed.
