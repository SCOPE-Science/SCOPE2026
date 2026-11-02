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

# Reproducibility and verification

Run `python artifacts/verify_cycle_pade.py` from the extracted artifact directory after installing `requirements.txt` (SymPy). The actual extracted script was run and emitted `CHECKS_PASSED 118`.

The checks reconstruct the exact two-, three- and four-state rational Padé matrices, verify their coefficient factorizations and cyclic symmetries, test exact column mass conservation, confirm one positive quartic root between 6.135 and 6.136 by exact root counting, verify the group-inverse identity for all integer dimensions 2 through 14, and check direct asymptotic limits for dimensions 2 through 6. Exact-rational tests examine both sides of the four-state threshold.

These finite symbolic checks do not replace the analytical proof for every integer dimension, all real step lengths or all large-step asymptotics. The group-inverse coefficient computation, nonvanishing denominator argument and Descartes sign argument appear independently in the result's proof. No independently conducted audit or external certification is claimed.
