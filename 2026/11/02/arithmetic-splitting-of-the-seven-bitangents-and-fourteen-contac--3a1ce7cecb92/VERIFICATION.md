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

# Reproducible verification
Run `python3 klein_char2_verify.py` using Python 3 with the standard library only. Its field is \(\mathbb F_{64}=\mathbb F_2[W]/(W^6+W+1)\); the polynomial is irreducible and the multiplicative generator is checked to have order 63.

It enumerates all \(t\) with \(t^7=1\), all \(w\) with \(w^2+w+1=0\), and every binary point on every corresponding line over \(\mathbb F_{64}\). It verifies that the quartic restriction is the square of the stated quadratic, that the fourteen contact points are pairwise distinct and lie on the curve, that the pairwise bitangent intersections consist of seven off-curve triple vertices, and that Frobenius cycle decompositions are exactly \((1,3,3)\) and \((2,6,6)\). It checks the rational fixed-point counts through twelve extension degrees.

The standalone script is a finite exact check, not a substitute for the proof that the line charts exhaust all geometric bitangents or that the complete zeta formulas hold in arbitrary extensions. Those assertions follow from the symbolic complete-chart argument and the separability of the parameter equations in `RESULT.md`.
