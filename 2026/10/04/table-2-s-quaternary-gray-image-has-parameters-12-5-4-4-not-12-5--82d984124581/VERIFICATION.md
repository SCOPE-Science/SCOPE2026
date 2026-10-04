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
`artifacts/verify.py` uses only the Python standard library and reconstructs the printed \(q=4\), \(l=3\), \(n=4\) Table 2 row from first principles.

It implements \(\mathbb F_4=\mathbb F_2(\omega)\) with \(\omega^2+\omega+1=0\), the Frobenius map \(\sigma_2(a)=a^2\), the inner derivation \(\delta_{\sigma_2,\omega}(a)=\omega(\sigma_2(a)-a)\), and the source pseudo-linear transformation. It constructs the three component generator bases and applies the source Gray map by right multiplication with the printed matrix.

The replay checks the explicit product-ring word \(c=(0,g_3,g_3)\) and its weight-\(4\) Gray image, verifies rank \(5\), exhausts all \(1024\) words, and recomputes the generalized Hamming weights from all distinct column-generated subspaces. It does not test or make claims about any other table row or about the general theorems.
