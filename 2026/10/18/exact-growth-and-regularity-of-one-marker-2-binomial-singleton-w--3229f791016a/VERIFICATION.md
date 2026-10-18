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
Run `python3 artifacts/verify.py` after extracting the embedded files. The program constructs all ternary one-marker words for lengths 1 through 12, computes scattered pairs by a direct left-to-right signature, and counts singleton signatures. It independently sums composition-level cases and evaluates the rational generating function using integer binomial coefficients. It checks the full rational identity and the eventual cubic through length 200. It prints `ALL_CHECKS_PASS direct_lengths=1..12 formal_series=1..200` on success. No floating-point operations or third-party packages are required.

The verifier does not enumerate arbitrary lengths or independently certify bibliographic priority. The proof in RESULT.md supplies the infinite argument; its only literature-dependent binary sublemma is explicitly stated and supported by references [2,3]. Independent review has not been performed.
