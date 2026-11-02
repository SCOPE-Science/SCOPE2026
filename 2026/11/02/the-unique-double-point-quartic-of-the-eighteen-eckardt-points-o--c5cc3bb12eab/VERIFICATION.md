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

# Reproducibility and verification

The algebraic proof is in `RESULT.md`. Run `python3 verify.py` with standard Python 3 and no third-party packages. The code builds the eighteen Fermat-model Eckardt points in \(\mathbb F_7\), \(\mathbb F_{13}\), and \(\mathbb F_{19}\), constructs first-order projective jet equations, and compares their kernels against the image of the explicitly generated ideal \(I^2+(Q)\) in degrees \(4\) through \(8\). The results are supplied separately in `verification-results.json`.

Expected dimensions of the symbolic ideal in degrees \(4,5,6,7,8\) are \((1,4,19,48,93)\). The ordinary square's degree-six part has dimension \(15\), compared with \(19\) for the symbolic square. The verifier prints `VERIFY_OK` on success. Independent auditing has not been carried out.

The program is finite-field corroboration, not a replacement for the arbitrary-field proof or a check of publication priority. In particular, the proof's key use of Cohen--Macaulayness is the known uniform-matroid symbolic-power theorem, cited in `RESULT.md`.
