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

`python3 verify_cherries.py` uses only the standard library. It enumerates all \((n-1)!\) increasing-parent trees for each integer \(3\le n\le9\), derives the number of leaf-sibling pairs and the root degree from parent vectors, and compares exact rational means, covariances, event probabilities and conditional means for every admissible triple. The run performed for this package yielded `PASS 434 exact identities, exhaustive n=3..9`.

The arbitrary-size theorem is justified by the event decomposition and telescoping sums in `RESULT.md`, not by the finite check. The event assumptions \(v<a<b\), \(n\ge3\), and empty-product boundaries are handled explicitly. The packaged verifier is self-contained. Independent scientific validation has not been performed.
