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

The standalone standard-library-only Python program `sixth_moment_checker.py` computes every degree-six moment exactly as an integer using two distinct constructions of the degree-three polynomial coefficients: ordered triples of frequency sites and multisets with multinomial weights. The program compares them for every \(2^6+3^6=793\) normalized phase assignment, asserts both minima and numbers of optimizer vectors, verifies completeness, and prints all 82 distinct alphabet-specific moment levels. The CSV data are generated from the same checked values and are not a substitute for executing the proof certificate.

The proof's completeness uses the free three-parameter coefficient phase action, which is a true global scalar plus two torus translations, not arbitrary independent row/column phases. Each normalized assignment represents exactly \(q^3\) labelled arrays. Complex norms use the exact quadratic integer form for Eisenstein coefficients, not floating-point approximations.

An independent numerical check evaluated both explicit minimizer polynomials by sufficiently fine angular quadrature, finding moments 1641 and 1197. The quadrature was corroborative only; the exact integer algorithms provide the finite exhaustive certificate.

No all-phase complex minimum, dimension extrapolation, independent audit or external proof certification is asserted.
