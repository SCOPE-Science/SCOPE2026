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
# Reproducibility and limits

Execute `python3 verify.py` from this directory with Python 3; no third-party packages are needed. The program computes exact rational Kaczmarz projector identities for unit rows \((1,0)\) and \((3/5,4/5)\), checks finite covariance propagation and the strict rational horizon reversal, compares 169 admissible probability triples with the closed-form spectral expressions, and tests 45 coherence/cost phase-regime signs. Expected program output starts `VERIFY_OK`. The direct execution completed successfully.

The universal equal-work optimizer theorem is proved in `RESULT.md` through eigenvalues of \(p_0I+p_1P_1+p_2P_2\), the Perron eigenvalue of the covariance operator, strict balancing of singleton probabilities, and two affine budget optimizations. Enumerations and finite recurrences are consistency checks only; they are not infinite proofs. The companion 2026 source's complete text was unavailable for scientific overlap inspection. Independent review or certification was not performed.
