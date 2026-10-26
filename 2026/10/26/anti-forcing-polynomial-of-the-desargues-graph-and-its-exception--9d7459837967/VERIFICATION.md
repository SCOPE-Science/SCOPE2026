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

# Verification record

Execute `python3 verify.py` in a directory containing the extracted verifier. A completed run printed three orbits, `PROFILE 6*z^5 + 54*z^6; perfect_matchings=60; automorphism_actions=240`, and `VERIFY_OK`.

The verifier independently counts perfect matchings using a row-by-row bijection recursion and a subset-permanent dynamic program; enumerates the natural group action; computes every orbit's complementary two-factor lengths and permutation cycle types; evaluates the minimum feedback arc set through all \(1024\) subsets for each matching; and independently checks all smaller edge-deletion sets by direct confrontation with the other fifty-nine matchings for the three representatives. Lower bounds are exact, not search timeouts.

These computations establish only the named finite graph's invariant. A separately conducted independent audit and a comprehensive search of unavailable full texts have not been performed.
