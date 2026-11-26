---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python verify.py` with Python 3 (standard library only). The unchanged checker exercises exact rational residual-pivot and triangular-output identities and rational near-breakdown witnesses. Its numerical gamma-convolution quadratures concern the scalar density background credited in `RESULT.md`; they are not evidence for originality of the two-column finding.

The joint-density and transverse-coordinate argument in `RESULT.md` gives an unconditional probability lower bound for every fixed finite integer \(s\ge2\) and every \(n\ge3\). Integrating that bound proves divergence for every moment order \(r\ge1\). The rational witnesses do not establish probabilities or replace that argument.
