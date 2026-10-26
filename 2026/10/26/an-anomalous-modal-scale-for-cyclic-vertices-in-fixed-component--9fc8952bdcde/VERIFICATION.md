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

Run `python3 verify.py` with Python 3 standard library. The program independently enumerates all functions on labeled sets of size at most five and determines their cyclic-point and component counts by orbit traversal. It checks those counts against the forest/Stirling enumeration; separately computes reciprocal-symmetric polynomials using rational arithmetic and verifies exact descending adjacent ratios throughout sizes at most fifty. Finally it compares selected numerical modes against the asymptotic approximation.

Result: `PASS 62604 exact/analytic-identity assertions plus numerical mode smoke checks`. All assertions were actually executed on the included script. The infinite strict inequalities and mode limit rely on the written matrix-tree/Newton/asymptotic proof, not on the finite checks. No independent audit was performed.
