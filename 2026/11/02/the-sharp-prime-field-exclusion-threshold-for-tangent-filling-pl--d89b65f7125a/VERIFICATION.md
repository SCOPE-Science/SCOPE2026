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

# Reproducibility and limits

Run `python3 verify_classification.py`: it exhausts all admissible short-Weierstrass coefficients over each of the two prime fields, recognizes scaling classes, computes the three quotient classes of degree-three embeddings by explicit elliptic addition, and checks tangent incidences. Expected final markers: `EXACT_PRIME_CHECK_OK 11` and `EXACT_PRIME_CHECK_OK 13`.

Run `python3 verify_incidence.py`: it uses independent fixed homogeneous polynomial coefficients, independent point enumeration and a separate tangent incidence implementation. Expected marker: `INDEPENDENT_INCIDENCE_OK`; the six coverage sizes are 114,112,112 and 145,156,156, and the characteristic-seven witness covers 57 points.

Run `python3 verify_smoothness.py` with SymPy: three geometric gradient ideals for the characteristic-seven witness reduce to the unit ideal. Expected marker: `GEOMETRIC_SMOOTHNESS_OK`.

The enumeration does not prove the general prime bound by itself. The published nonexistence theorem for \(p\ge17\), Blokhuis's prime-order blocking-set bound, and the degree-three line-bundle classification of elliptic-curve embeddings are mathematical inputs. Not independently audited or globally certified for novelty.
