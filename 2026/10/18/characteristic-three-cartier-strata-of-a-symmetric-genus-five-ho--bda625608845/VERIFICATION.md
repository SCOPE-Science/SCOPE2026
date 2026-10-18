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

Execute `python3 verify_howe5.py` using Python 3 and its standard library. The script must print `VERIFY_OK` and also independently reports the four \((f_3,a)\) counts over the \(42\) admissible ordered parameter pairs in \(\mathbf F_9\). It expands the defining genus-three quotient polynomial as a sparse polynomial over \(\mathbf F_3[s,t]\), verifies the Cartier coefficient positions, computes twisted matrix stable ranks for each rational ordered pair, and confirms that the deepest four-parameter subset forms one orbit under swapping and inversion.

The infinite-parameter claims are proved algebraically in `RESULT.md`: the genus and \(2\)-primary isogeny, coefficient matrix, Frobenius-twisted product, elliptic Cartier scalars, and reduced intersection calculation. An exhaustive finite-field test is **not** a proof over the algebraic closure and does not establish independence or publication priority. The checker does not calculate Newton polygons, assert supersingularity, or classify the entire genus-five moduli problem.
