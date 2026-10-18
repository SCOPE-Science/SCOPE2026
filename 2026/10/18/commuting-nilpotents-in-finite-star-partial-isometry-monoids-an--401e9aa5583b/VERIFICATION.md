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

The self-contained `checks/verify.py` enumerates distance-preserving partial injections from the defining metric, not the structural theorem. Nilpotence is tested by following arrows until termination or encountering a cycle. Ordered pairs are tested by directly evaluating both compositions. The script separately calculates the partition-weighted correction and asserts equality at every order from \(n=1\) through \(n=6\).

Observed correction values: \(0,6,34,168,1068,8530\). Observed ordered commuting-nilpotent pair totals in the star monoid: \(1,7,41,229,1753,17891\). The leaf-only totals are \(1,1,7,61,685,9361\).

These are **finite** checks only. The universal proof uses the explicit classification of possible hub-involving nilpotents, arrow-by-arrow commutation criteria, and integer-partition counting. Neither computational tests nor search results are presented as independent certification. No external independent audit has been performed.
