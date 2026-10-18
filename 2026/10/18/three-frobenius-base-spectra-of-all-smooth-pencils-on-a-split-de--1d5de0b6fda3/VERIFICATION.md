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

# Reproducible mathematical checks

All finite-field enumeration is exact. `verify_exact.py` (Python standard library) independently recomputes the 60 smooth cubics, 104 qualifying pencils, thirteen full-symmetry orbits and their point-count multisets; reference output: `verification_exact.json`. `verify_groebner.py` (SymPy) independently tests the smoothness of all 255 cubic masks by chart Gröbner bases and checks the complete automorphism action; reference: `verification_groebner.json`.

`verify_elimination.py` (SymPy) reconstructs all thirteen lexicographic Gröbner bases over \(\mathbf F_2\) and checks squarefree degree-seven elimination polynomials with irreducible factors; exact bases and factorizations are in `verification_elimination.json`. The proof that these seven distinct chart points are the full strict-transform base scheme also uses Bézout degree nine and the two prescribed projective points, as specified in `RESULT.md`.

`verify_frobenius.py` (standard library) independently constructs fields \(\mathbf F_{2^k}\), \(1\le k\le7\), counts the plane common points, and uses Möbius inversion to derive the Frobenius partitions. It reproduces `verification_frobenius.json` and `orbit_frobenius.csv`.

All programs were executed successfully on their delivered source versions; finite-extension agreement is corroboration, while the rigorous geometric-smoothness and scheme-theoretic statements use algebraic rank/Groebner/Bézout arguments. No external independent audit was performed.
