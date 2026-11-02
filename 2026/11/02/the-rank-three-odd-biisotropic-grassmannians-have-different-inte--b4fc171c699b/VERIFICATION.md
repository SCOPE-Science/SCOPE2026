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

# Reproducible exact checks

The standalone `verify_degree.py` uses only Python's standard library. It expands nine linear factors into a 30-term integer polynomial, forms falling-factorial polynomials in the integer variable \(n\), and checks the required closed factorization coefficient by coefficient, for **every** \(n\). It compares direct coefficient degrees with the closed formula for \(3\le n\le9\), and checks the ratio identity. An independent exact rational torus-localization calculation on the ambient Grassmannian confirms the degrees for \(n=3,4,5,6\).

Command: `python3 verify_degree.py`.

Observed output includes \(61\) versus \(5\) at \(n=3\), \(10329\) versus \(462\) at \(n=4\), and the terminal marker `VERIFY_OK`. Finite tests cannot by themselves establish the all-parameter theorem; the polynomial coefficient identity and geometric argument establish the infinite claim. General-pencil smoothness, the cellular comparison, and the standard normal form are externally cited mathematical premises. Independent audit has not been performed.
