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

# Reproducibility and limits

Run `python verify.py` in a Python 3 environment. It builds the token graph from the original swap rule, uses GF(2) Gaussian elimination independent of the symbolic proof, and exhaustively compares every parity kernel word against the explicit polynomial for \((m,n)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\). These cases contain respectively 16, 16, 512, 128, 2048 and 262144 binary kernel words. It also checks the total dimension formula for all \(2\le m\le n\le10\). A successful run ends in `VERIFY_OK`.

The exact all-parameter result comes from the incidence-block proof and character orthogonality. Neither bounded brute-force enumeration nor the existence of a working script establishes absolute priority, independent audit or an extension to arbitrary graph families.
