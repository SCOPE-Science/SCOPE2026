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

# Reproducible scientific checks

Run `python3 check_nij.py` in a Python 3 environment; no third-party dependencies are required. This independently evaluates the original \(\mathfrak{sl}_2\) bracket and the original Nijenhuis torsion for *every* rank-one tensor map over four finite fields, including \(\mathbb F_9\) represented by \(\mathbb F_3[t]/(t^2+1)\). The square-zero test is direct, as are pairwise commutation and the ordered pair/triple censuses.

Observed triples of nonzero square-zero maps, compatible ordered pairs including zeros, compatible ordered triples including zeros: \(q=3:(32,369,3345)\); \(q=5:(144,4225,100945)\); \(q=7:(384,21217,983521)\); \(q=9:(800,71361,5469921)\). These agree with the symbolic enumerator for each tested field. The replay marker is `LIE_NIJENHUIS_SL2_ALL_DIRECT_CHECKS_OK` and the actual output is provided in `check_output.txt`.

The component theorem and formulas for arbitrary fields and arbitrarily many tuple positions require the incidence proof given in `RESULT.md`. Finite enumeration alone cannot certify them. No independent audit is claimed.
