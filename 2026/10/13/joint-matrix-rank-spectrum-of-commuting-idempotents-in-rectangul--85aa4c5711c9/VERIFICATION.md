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

# Computational and mathematical verification

Run `python3 checker.py` from this directory with Python 3 standard library. It enumerates full rectangular matrix spaces over the finite fields of sizes 2, 3, and 4 in ten small configurations and recomputes all idempotent and commuting-pair joint-rank counts. The expected terminal marker is `VERIFY_OK`.

Critical proof checks are the block equations for sandwich idempotents, sufficiency of the three displayed commutation equations (including the bottom-right corner), simultaneous decomposition of commuting projections in all characteristics, the ordinary rank factorization, and the orbit-stabilizer count. The program probes these through direct brute-force field matrices; it is not an exhaustive proof for unbounded parameters.

The proof's reduction to standard sandwich rank relies on invertible row and column changes, preserving the ambient rectangular rank. The stated asymptotic fixes both field order and sandwich rank while the dimension excess tends to infinity. Literature originality has a documented residual risk; no independent audit was performed.
