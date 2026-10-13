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
# Reproducibility

Run `python artifacts/verify.py` using a Python 3.9+ interpreter. The standalone standard-library checker uses independent enumerations of functions and a suffix-image recurrence. The brute-force census enumerates every function on 31 different finite weak-order posets of at most five points (52,165 tested functions), and compares the entire image-rank distribution. Six uniform parameter pairs are compared with brute force; 36 larger uniform cases use the independent recurrence. For six small posets, the complete finite table of Heyting implication is separately used to decide whether inverse images preserve implication for each of 319 functions; this agrees exactly with the bounded-morphism predicate.

The bounded-morphism test uses its own explicit principal-upset images rather than invoking the counting recurrence. The algebraic check invokes neither the bounded-morphism condition nor the rank formula to decide homomorphism preservation. Exhaustive checks only apply to the displayed finite ranges and do not establish the unrestricted theorem; the structural proof does.

Expected terminal marker: `VERIFY_OK`.
