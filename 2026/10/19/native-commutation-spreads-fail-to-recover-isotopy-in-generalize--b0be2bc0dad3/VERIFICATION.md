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

# Reproducible checks

Run `python3 verify_semifield.py` with standard Python 3. It implements prime-power test fields via polynomial residues, searches monic irreducible polynomials, finds admissible norm-nonunit coefficients, and computes the native products literally. For field sizes \(27,81,125\) it exhausts each nonzero-product and commuting-pair condition over every element. For order \(27\) it additionally exhausts all ordered triple commutation constraints. For order \(729\) it tests all second coordinates against forty first coordinates, and the prescribed bounded nonzero-product grid; these are explicitly **not** exhaustive counts for the order-\(729\) field. Both relevant degree-six exponent pairs are included. The program should print six `PASS` records and finally `VERIFY_OK_TWISTED_FIELDS`.

The infinite family theorem is deduced algebraically; tests neither certify literature priority nor independently establish the Albert nucleus theorem. The nonisotopy comparison invokes the full original Theorem 1 of Albert (1961). No external mathematical audit has been performed.
