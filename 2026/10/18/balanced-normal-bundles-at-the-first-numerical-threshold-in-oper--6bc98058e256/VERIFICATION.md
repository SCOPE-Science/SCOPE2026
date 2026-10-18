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
The proof uses the adjacent syzygy resolutions for two complete monomial systems, the Veronese differential, and a split normal-bundle extension on \(\mathbf P^1\). It does not depend on finite numerical tests. `CHECK.py` executed successfully with Python 3 for each integer \(2\le k\le10\), verifying exact syzygies, derivative identities, arithmetic ranks/degrees, and sample-point nonvanishing. Its finite tests cannot independently certify the infinite-family theorem or literature uniqueness.

The irreversible mathematical inputs not reproduced in the checker are the standard evaluation bundle resolution on \(\mathbf P^1\), the irreducibility of the fixed-degree rational-map parameter space in the Grassmannian, and the upper semicontinuity of bundle cohomology. Independent audit is not performed.
