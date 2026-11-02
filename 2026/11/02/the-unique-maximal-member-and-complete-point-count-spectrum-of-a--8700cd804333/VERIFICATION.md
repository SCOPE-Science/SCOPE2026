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

# Computational verification and limitations

Run `python3 verify_f25.py` with standard Python 3. The verifier uses the explicit field of 25 elements, checks field axioms by exhaustive triples and nonzero inverses, and cross-checks independently enumerated affine solutions against the cube-root count identity for all 23 permitted parameters. It then checks the seven frequencies, unique maximal parameter, and three quotient point counts.

The geometric proof of degree-nine connectedness, genus four, tame inertia, and three rational points over infinity is in RESULT.md; this checker does not substitute for it. The enumeration is complete only for parameters in the finite field, and it does not prove historical priority, isomorphism uniqueness, or results over extensions.
