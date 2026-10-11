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

# Exact verification

`verify_exact.py` and `endpoint_certificates.json` implement a self-contained integer/rational certificate for the real \(4\times4\) sharp ratio. Run `python3 verify_exact.py` from any working directory, with both files beside one another. The verifier uses Python's standard `fractions.Fraction` to reconstruct all \(512\) canonical sign masks, all \(128\) rank-one signed bilinear vertices, and all certificate coefficients. It checks, entry by entry, that each canonical sign mask is a nonnegative rational combination of vertices with total mass at most \(12/5\). The verifier independently computes the integer witness's \(24\) absolute-entry sum and \(10\) cut/signed-bilinear norm, so it establishes the matching lower bound.

The finite exhaustive scan is mathematically exhaustive because arbitrary matrix entry signs are equivalent, under independent row/column sign flips, to exactly the \(512\) canonical masks. The proof in RESULT.md provides the symbolic argument reducing all real matrices to those masks; the checker validates the complete finite certificate, not an infinite sampling approximation. No third-party package, external service, or numerical optimization is required to replay the proof. It does not establish originality or prove any high-dimensional assertion. No independent audit has been performed.
