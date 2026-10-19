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
The sharp constant and constant-modulus necessity come from the cited theorem. The classification proof uses fiberwise phase coherence, a third-difference rigidity relation, trace-pairing linearization, and a nonvanishing rational-conic witness for every nonzero Frobenius exponent. Its characteristic and root-count hypotheses are explicit.

The exact-arithmetic program `phase_extremizers_verifier.py` checks all ordered triples over fields of sizes 5, 7, 25 and 49. It verifies fiber-square counts, relation ranks, chirp constraints and nonzero off-diagonal Frobenius witnesses. Expected results are in `phase_extremizers_verification_output.txt`. These finite computations corroborate but do not prove the general theorem. No independent audit was performed.
