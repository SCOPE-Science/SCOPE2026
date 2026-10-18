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

# Exact checks

From the standalone standard-library-only `verify.py`, run `python3 verify.py > reproduced.json` and compare with the bundled `certificate.json` (indentation and ordering are deterministic). The certificate establishes the full Prüfer-coded count of \(1441\) labeled trees across orders two through six, \(20796\) source pairs, \(609408\) coefficient comparisons, and zero conflicting signs, verifying the lower-bound claim by exhaustively examining every labeled tree, transmission edge subset, source, threshold and edge-count coefficient. This certificate is a finite exhaustive proof and cannot be generalized without further proof.

For the seven-vertex three-arm tree, the same verifier computes exact tail-polynomial coefficient arrays for thresholds two through seven; strictly positive and strictly negative tail differences prevent stochastic order for every \(0<p<1\). A second method based on exact rational rooted-tree generating functions verifies the two complete size distributions at \(p=1/2\). Equality of the witness mean difference \(p(1-p)\) follows by summing the tails. The generating-function cross-check at one probability does not by itself verify the all-probability polynomial identity; that identity is separately established from exact edge-subset expansion.

# Limits

No floating-point sampling is used. The certificate establishes the finite order-six enumeration and the specific order-seven counterexample, not claims for arbitrary non-tree graphs or dependent-transmission SIR models. Independent scientific audit has not been performed.
