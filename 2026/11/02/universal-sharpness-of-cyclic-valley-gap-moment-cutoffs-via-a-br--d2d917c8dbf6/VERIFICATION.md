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

# Reproducibility of exact boundary corrections

Run `python verify.py` to exhaustively enumerate permutations of four through ten sites for the listed parameter cases. The script computes exact first/second moments as fractions and confirms the four source-slope discrepancy identities. If NumPy is installed, 200-point Gauss–Legendre quadrature checks four trace integrals numerically; this optional computation has a declared numerical tolerance.

The recorded execution (`verification_output.txt`) reports 26 passed assertions. Exhaustive enumeration is limited to these finite cycles. The all-parameter theorem is established by the operator-kernel proof in `RESULT.md`; finite checks and quadrature are not substituted for a proof of infinitely many cases. No independent audit has been performed.
