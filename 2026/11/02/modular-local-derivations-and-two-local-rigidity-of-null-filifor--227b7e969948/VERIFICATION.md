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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 with its standard library. A successful execution concludes with `MODULAR_LEIBNIZ_LOCAL_DERIVATIONS_OK`.

The program constructs the right Leibniz product from the stated basis table, independently generates derivation maps from coefficient vectors, confirms the derivation identity, enumerates every endomorphism and every vector in six small prime-field configurations, and compares actual pointwise locality against the modular triangular criterion. It also checks the exact count of local maps coinciding with a derivation fixed by the image of the first generator. Larger samples check the ordinary derivation identity.

Verified cases: characteristic \(2\) in dimensions \(2,3,4\), characteristic \(3\) in dimensions \(2,3\), and characteristic \(5\) in dimension \(2\). For dimension four over \(\mathbb F_2\), the exhaustive census gives \(256\) linear local maps among \(65{,}536\) endomorphisms, with \(16\) ordinary derivations. The infinite-field and arbitrary-dimension conclusions follow from the symbolic proof, not these finite tests. No external independent audit has been performed.
