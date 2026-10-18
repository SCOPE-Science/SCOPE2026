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

# Reproducing the exact finite theorem

Run `python3 verify.py` with Python 3.10 or later. The verification performs a complete trial-division prime enumeration and an independent sieve, checks all \(429680\) ordered distinct odd-prime initial pairs with entries no larger than 4919 using both naive factoring and memoized sieve factors, and verifies all claimed sharp seed thresholds. It also checks that exactly one seed has length at least \(23\) within the cap, evaluates all 23 entries of its trajectory, and confirms the terminal sum is \(8\).

Proof of global optimality for each threshold is finite and does not depend on probabilistic sampling: once a witness occurs at ceiling B, all possible starting prime pairs with smaller ceilings are present in the exhaustive scan. For lengths at least 24 no upper bound or exhaustive classification is asserted. This scientific review has not been independently audited.
