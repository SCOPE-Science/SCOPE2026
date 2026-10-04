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
# Verification

The exact checker `artifacts/verify.py` reconstructs the published quartic family over the rational polynomial ring using SymPy. It verifies the complete local expansion at the marked point on three affine parameter charts, the factorization of the binary-cubic discriminants, the generic factor type on each discriminant component, all pairwise incidences of the seven parameter lines, and the squarefree four-line tangent form at all nine arrangement singularities.

The calculation proves only the reduced support of the discriminant divisor. It does not determine scheme-theoretic multiplicities of that divisor or classify unrelated singular points of every specialized quartic.

Replay command: `python artifacts/verify.py`

Expected terminal line: `VERIFY_OK`
