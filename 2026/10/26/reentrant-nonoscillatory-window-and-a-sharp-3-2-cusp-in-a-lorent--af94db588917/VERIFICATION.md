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
# Reproducibility and scope of checks

The analytic proof is in `RESULT.md`. Run `python checks/check_spectrum.py` with a recent Python installation containing SymPy and NumPy. This independently checks the characteristic determinant, discriminant, double-root parameterization, transverse discriminant derivative, cusp factorization, exact Taylor identities and illustrative numerical eigenvalues. It verifies exact polynomial identities rather than using numerical root samples to prove uniqueness. The finite sample checks demonstrate the three phases for one coupling and numerical approach to the stated cusp constant; the global assertions follow from the proof, not the samples. The data contain no external validation, experimental measurement, or independent mathematical audit.
