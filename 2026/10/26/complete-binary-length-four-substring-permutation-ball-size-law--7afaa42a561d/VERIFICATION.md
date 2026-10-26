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

The direct finite experiment enumerates all distinct four-window permutation outputs for every binary center of length \(4\) through \(12\), totalling \(8{,}176\) words. The output cardinality is compared with a first-difference formula and an independent suffix-state histogram routine. The latter is also checked for lengths \(13\) through \(35\), including exact mean, variance, and near-maximal deficit frequencies. The recorded return status is `VERIFY_OK`, and the code is reproducible with the standard Python library.

A separate `verify_deficit_formal.py` certificate computes exact \(4\times4\) and \(5\times5\) determinants over \(\mathbb Z[s,z]\) and verifies the first six formal deficiency generating-function coefficients by a polynomial identity; its recorded output is `formal_coefficient_output.txt` with status `FORMAL_COEFFICIENTS_OK`. The mathematical proof of the full length range uses the exact transfer identity and algebraic coefficient extraction; finite checks are supportive, not an exhaustive proof for all lengths. The central limit theorem is proved using bounded finite dependence and independent-block approximation, not by simulation. Unchecked claims include extensions to nonbinary alphabets, cyclic-only shifts, and multiple bursts.
