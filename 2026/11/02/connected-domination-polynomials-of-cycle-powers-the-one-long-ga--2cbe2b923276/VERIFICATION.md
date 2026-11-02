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

# Reproduction and scope

Run `python3 verify.py` using Python 3 standard library. Expected successful output begins with `VERIFY_OK:`.

The checker independently constructs \(C_n^r\) with edge adjacency determined by shortest cyclic distance, then tests every nonempty vertex subset for ordinary domination and connectivity of its induced subgraph. It compares the resulting full size distribution to the closed coefficient formula for 26 noncomplete parameter pairs (\(1\le r\le4\)), totaling 74,390 tested nonempty subsets. It separately checks the predicted minimum sizes and multiplicities, the universal saturation threshold and its sharpness, complete graph cases, and the standard cycle specialization.

The infinite assertions are established by the cyclic-gap proof and counting identities in RESULT.md; finite instances do not certify infinite quantifiers. A mathematical audit independent of the present self-review has not occurred.
