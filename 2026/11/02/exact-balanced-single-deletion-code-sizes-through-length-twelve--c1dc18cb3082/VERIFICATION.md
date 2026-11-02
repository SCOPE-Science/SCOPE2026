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

# Verification of exact finite certificates

All files required for exact checks are included. From the containing directory run `python3 verify.py` and `python3 verify_independent.py`; both programs require only the Python standard library and return `VERIFY_OK` and `INDEPENDENT_VERIFY_OK` if all assertions hold.

The input universes contain respectively \(2,6,20,70,252,924\) balanced words. Both verifiers check all six integer dual inequalities over the entire finite universe and compare their sums with the next Catalan integer bound. The first verifies construction-color classes have pairwise disjoint deletion shadows. The second independently generates every deletion shadow with bit manipulation and verifies checksum-class noncollision. The length-eight rational primal has its complete output constraints checked exactly; its objective is \(1419498/100000>14\). The first three layers additionally have unit duals of sizes \(1,2,5\) certifying exact LP integrality there.

This is a finite, exhaustively checked certificate for lengths through twelve; it is not a proof for all lengths and is not independent external validation. The primal objective is not claimed to be the exact fractional optimum.
