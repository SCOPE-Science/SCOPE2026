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

The infinite theorem is proved symbolically in `RESULT.md`. The bundled `verify.py` is a finite transcription and boundary check, not a substitute for the proof. It directly computes base-prime carry counts for doubling, compares them with the digit inequalities, checks the exact odd-prime count at each tested digit length, and checks the binary and \(p^a-1\) consequences.

The direct literature source establishes the only non-elementary premise used here: the row-wise maximum of \(v_p(G(N;m))\) is \(r_p(m)\). Kummer's theorem then makes the \(N=2m\) reduction exact.

Unproved limits: this package does not determine \(T_p(m)\) when the digit criterion fails and does not claim exhaustive historical priority beyond the documented searches and source inspections.
