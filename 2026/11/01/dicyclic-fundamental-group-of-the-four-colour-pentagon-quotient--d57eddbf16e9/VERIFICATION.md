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

The result has an exact, noncomputational covering-space proof in `RESULT.md`. The accompanying `verify_pentagon_four_color_quotient.py` checks the integral cellular consequences independently of that covering-group argument. To reproduce, install the dependency specified in `requirements.txt` and run `python verify_pentagon_four_color_quotient.py` in the directory containing the files.

The executed checker enumerated 240, 780, 840 and 300 product cells in degrees zero through three and verified that all 2,160 cells have trivial dihedral stabilizer. It found 24, 78, 84 and 30 quotient cell orbits. It checked the signed coordinate-permutation chain action against every cellular boundary and all ten dihedral elements; it also verified both consecutive matrix products vanish. The exact integer Smith diagonal invariants for the quotient boundary maps are 23 copies of 1, then 54 copies of 1 and one 4, then 29 copies of 1. The resulting integral homology is \((\mathbb Z,\mathbb Z/4,0,\mathbb Z)\). The actual terminal output is embedded in `verification_output.txt`.

The verifier does not compute the fundamental group. That part is proved from the published equivariant reflection theorem and the finite central extension argument in `RESULT.md`; it is not inferred from the abelianized boundary matrices. The computation is finite and exhaustive for this fixed four-colour complex. It does not establish claims for other colour counts, prove full-dihedral equivariant homeomorphism, or supply independent mathematical certification.
