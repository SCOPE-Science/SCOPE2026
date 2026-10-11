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

Run `python verify.py`. The standard-library verifier reconstructs the Wagner graph, enumerates every rooted-forest simplex, checks all Hasse covers, recreates the staged matching, and topologically sorts the complete matched Hasse orientation to certify acyclicity. It reconstructs the signed gradient-path Morse boundary and evaluates the specified unit minor with the fraction-free Bareiss determinant. It also computes full simplicial boundary ranks over three finite fields.

The accepted claim uses the exact determinant \(-1\), not the finite-field calculations, to prove integral surjectivity. The finite-field calculations are cross-checks. No larger-family statement is inferred.
