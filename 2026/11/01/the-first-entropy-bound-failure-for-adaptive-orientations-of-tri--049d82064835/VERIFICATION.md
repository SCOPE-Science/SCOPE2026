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

Run `python verify.py CERTIFICATE.json` with Python 3.10 or newer. The checker constructs all acyclic orientation hypotheses for each of the seven finite book graphs, independently confirms acyclicity by source elimination, checks the complete-shattering recurrence and failure at the next depth, and checks the explicit tree certificates. The six-page or smaller results use the same exhaustive routine. The depth-12 failure for seven pages is not inferred from cardinality or timeout. Expected output is in `verification_output.txt`.

The finite search supports no claim at eight or more pages and gives no independently audited proof.
