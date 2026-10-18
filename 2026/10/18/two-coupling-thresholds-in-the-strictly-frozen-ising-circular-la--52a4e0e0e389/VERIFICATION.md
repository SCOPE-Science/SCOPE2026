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

Run `python3 verify.py` using Python 3 with no third-party dependencies. The script reports 54 passed complete spin-space/coupling comparisons on circular ladders of three to eight rungs, including negative and positive rung couplings, zero coupling, and the strict-neutral threshold. It also reports 28 passed coefficient-wise transfer-matrix polynomial comparisons for three through thirty rungs.

The proof of the all-size coefficient formula is combinatorial. The Perron-root calculation establishes the limiting complexity, and differentiability of its logarithmic generating function establishes concentration of the wall density. Finite enumeration is a consistency test, not a proof of the infinite-family theorem. No independent audit has been performed.
