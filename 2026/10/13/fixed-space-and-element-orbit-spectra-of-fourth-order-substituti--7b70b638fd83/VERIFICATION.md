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

# Reproduction

Run `python3 artifacts/verify.py` using Python 3 and the standard library. The program builds explicit finite fields of sizes \(2,3,4,5,7,8,9,11,13,16\), enumerates every invertible truncated substitution at each size, and computes the rank of the induced operator minus the identity. It checks each of the predicted fixed-dimension fibers, group-size normalization, and Burnside orbit count. For sizes \(2,3,4\), it also directly computes the orbits of **every** element to verify Burnside's result through a logically separate group-action enumeration.

The observed orbit totals at these three sizes are \(14\), \(27\), and \(52\), respectively. The execution must end in `VERIFY_OK`. This check is exhaustive over the named finite fields only; the general result for arbitrary prime powers is established by the case proof, not by experiments. No independent external validation has been performed.
