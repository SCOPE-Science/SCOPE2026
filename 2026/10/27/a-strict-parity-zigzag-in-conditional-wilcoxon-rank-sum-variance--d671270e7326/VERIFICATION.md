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

Execute `python3 verify.py` with Python 3 and the standard library. It exhaustively enumerates the words for each integer \(1\le a,b\le8\), groups each sample by attainable constant-run count, computes the exact conditional first and second moments, and checks all closed variance formulas and relevant strict parity comparisons using rational arithmetic. Expected output: `PASS conditional means, exact variances, and strict parity comparisons; assertions: 1340`.

The proof in `RESULT.md` is universal and independent of the test window. The exact variance differences have positive factorizations over all admissible parameters; the tests are corroboration only. The conditional law assumes distinct pooled ranks and uniformly random fixed-size assignment of labels. Historical originality is not independently certified, and some older publisher full texts could not be checked completely.
