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

# Verification of the finite corroborating computation

Run `python3 verify_forest_mis.py` using Python 3 and the standard library. It independently enumerates all labeled simple forests of order zero through six. For each forest it obtains the maximal independent sets by direct vertex-subset testing, obtains all shattered supports by direct trace testing, and separately obtains all sides of all ordinary induced matchings by edge-subset testing and side choices. Equality is checked for each graph, not inferred from a sampled graph. It additionally checks the 5-cycle obstruction.

Expected output is embedded as `verification_output.txt` and can be reproduced byte-for-byte. The computation checks 3,272 labeled forests and 197,635 candidate supports across all orders, including empty/isolated cases. It **does not prove** the unrestricted all-orders theorem; see the mathematical leaf induction in `RESULT.md`. No external audit is claimed.
