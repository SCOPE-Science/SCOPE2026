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

# Reproduction and proof boundaries

Run `python artifacts/verify.py` from the result directory. It uses only the standard Python library and ends with `VERIFY_OK`. The tested cases include all \(16\) elements and all two-sided factors of the two-element magma monoid, the entire \(19{,}683\)-element triple spectrum at size three and \(109{,}902\) constructed factorizations from its twenty type representatives, and explicitly reconstructed two-sided products for seeded random examples at sizes three through five.

The theorem for arbitrary finite \(n\) is justified by the equivariant orbit factorization and section construction in `RESULT.md`; a finite test does not prove its general quantifiers. Exact combinatorial summation is performed symbolically in the proof, not inferred from a short numerical table. The 2022 precursor and any unindexed more-general Green relation treatment remain literature-comparison limitations. No independent review has occurred.
