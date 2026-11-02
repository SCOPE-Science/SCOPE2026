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

# Reproducibility and limitations

Run `python3 VERIFY.py` using Python 3 standard library after extracting this package. The checker prints `PASS: 2666 finite exact/numerical assertions; 176 admissible parameter triples`. It checks rational crossing identities and branch inequalities, compares a closed-form spectral decomposition with an independent Jacobi-rotation eigensolver, probes distinct nonsymmetric leaf scaling perturbations, and checks dimension-transition examples.

The full proof, including unrestricted-global uniqueness and all parameter quantifiers, is contained in `RESULT.md`. Numerical and finite exact sample tests **do not prove** a quantified theorem or historical novelty. Relevant older general block-scaling papers were not fully accessible. Independent mathematical audit is not performed.
