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

# Verification of the rowwise graph-labeling threshold

The analytic proof in `RESULT.md` establishes the general identity and both sides of the parameter threshold. The accompanying `verify_exact.py` uses Python standard-library `fractions.Fraction` and exhaustive enumeration of the nine possible hard labelings on its two-vertex, three-class test graph. Running `python3 verify_exact.py` returned `VERIFY_OK: rounding identities, threshold margins, and witness energy`.

The script verifies the expected-rounding formula for fifteen exact-rational test combinations, the explicit energy and first-order gaps for the two-vertex example, the flat boundary segment, and the indefinite full Hessian at \(\varepsilon=4/5\). It does not establish the universal statement by finite enumeration, certify numerical algorithms, or independently validate scientific priority. The analytic local-optimality proof supplies the neighborhood and quantifier argument for every \(1\le\varepsilon<2\) and every \(K\ge3\).
