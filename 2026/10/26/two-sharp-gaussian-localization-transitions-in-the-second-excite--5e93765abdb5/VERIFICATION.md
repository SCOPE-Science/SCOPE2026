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

# Reproduction
Run `python3 verify_gaussian.py` with a standard Python 3 interpreter; no external libraries are required. The checker evaluates the normalized gamma-polynomial integrals using exact rational fractions at eight damping parameters and all indices from zero to twenty, then checks the two adjacent crossing identities, strict tail difference identities, undamped normalization and the winning sectors at six damping strengths.

The machine-verifiable tests are finite and do not establish positivity for all real damping parameters; the proof in `RESULT.md` supplies the algebraic sum-of-squares and discriminant arguments for all indices and parameters. The reviewed claim concerns no symbols beyond a centered Gaussian in this single excited Fock level. Independent audit has not been performed.
