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

Exact standalone reproducibility: run `python3 verify.py` using Python 3 with no external packages. The checker derives characteristic-three affine and boundary Hasse derivatives, checks the full residual-intersection polynomial at each of the four fourth roots of unity in a degree-two field, enumerates the two finite incidence graphs, and verifies the support counts over fields of degrees one, two and three. These computations support the symbolic proof in RESULT.md; they are not independent scientific peer review. The geometric completeness proof uses the degree-six intersection theorem and the four possible values of the Artin–Schreier parameter, not an extrapolated finite-field census.
