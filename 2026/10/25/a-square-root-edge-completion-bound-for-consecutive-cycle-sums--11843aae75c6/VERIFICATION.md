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

# Computational checks and limitations
Run `python3 verify.py` using Python 3 and the standard library. Its expected final line begins `VERIFY_OK`.

The script computes subset sums for each constructed parameter, checks exact interval coverage for every integer \(9\le n\le124\), directly checks every declared witness is a connected vertex set of the required weight for \(9\le n\le22\), and independently enumerates all connected subsets for \(9\le n\le14\). It also checks parameters \(n=125,240,500,1000,2000\). The general theorem has a separate explicit proof. The check does not certify optimality and finite testing alone cannot establish an infinite result.
