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

# Verification record

The complete result and its proof are in `RESULT.md`. Execute `python3 verify.py` in the directory containing the extracted artifacts; the checker uses only Python standard-library integer arithmetic. It performed **467,463 exact assertions** and printed:

`PASS: 467463 exact integer assertions (n<=75 adjacent, n<=22 all minors, n<=8 independent enumeration)`

Specific checks: independent restricted-growth-string enumeration of every partition through eight labels; coefficient-versus-enumeration agreement; all Stirling-number block-count marginals through \(n=75\); every adjacent TP\(_2\) determinant through \(n=75\); and every four-index TP\(_2\) determinant through \(n=22\).

Finite checks are not exhaustive over all \(n\). The infinite theorem relies on the proof in `RESULT.md`, especially the full root-interlacing statement in Bóna–Mező (arXiv:0705.2734, Theorem 1), the elementary Bernoulli-convolution inequality, Newton's inequalities, and the exact adjacent-minor recurrence. The claim does not depend on any unpublished computational certificate. Historical priority is qualified, and independent validation has not been performed.
