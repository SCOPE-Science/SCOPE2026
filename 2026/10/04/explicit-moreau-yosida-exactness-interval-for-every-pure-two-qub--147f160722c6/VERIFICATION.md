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

The claim is proved analytically in `RESULT.md`. Checks reproduced the Schmidt-form partial-transpose spectrum, the trace-norm subgradient witness, the convex-roof inequality \(2N\le C\), the formulas for \(f'(c)\) and \(f''(c)\), and the exact spectral diameter \(2f'(c)\). Supplementary random-state stress tests at six reference concurrences found no violation; they are not used as proof.

The package does not certify optimality of the threshold and makes no statement for arbitrary mixed reference states.
