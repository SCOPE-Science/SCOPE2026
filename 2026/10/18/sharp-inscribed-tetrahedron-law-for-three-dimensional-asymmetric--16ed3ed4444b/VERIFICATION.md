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

# Reproduction of the exact tetrahedral determinant certificate

Run `python3 verify.py` using a standard Python 3 interpreter; no external packages are necessary. The script independently forms the twelve ordered-pair vertices of the standard 3-simplex difference sum, enumerates all \(\binom{12}{4}=495\) four-vertex choices, expands the homogeneous 4-by-4 determinant using all 24 permutation terms in exact integer polynomial arithmetic, canonicalizes signs and checks the complete ten-row multiplicity table in `RESULT.md`. It also checks that exactly six top quadruples consist of directed Hamiltonian four-cycles and that no two share more than one vertex. The output on success is `VERIFY_OK quadruples=495 determinant_classes=10 maximum_orbits=6`. This exact script was run successfully against the included source.

The checker establishes only the finite algebraic certificate and graph incidence. Uniformity for arbitrary positive real \(s\) requires the positivity inequalities shown in `RESULT.md`; unrestricted vertex reduction and nonvertex optimizer exclusion require its analytic determinant argument. The volume identity and strict occupancy monotonicity require the orthant integration and derivative in the proof. None of these is inferred merely from a numeric parameter sweep. Independent audit is not yet performed. The historical-priority evaluation is bounded by the accessible literature.
