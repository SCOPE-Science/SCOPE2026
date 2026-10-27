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
# Verification

The standalone `verify.py` uses NumPy and SciPy. Executing `python verify.py` passed exactly 3,937 finite checks on diagonal and rotated orthonormal inputs, every possible leading-block rank in the tested sizes, QR reconstruction, sketched-orthogonality, reciprocal least-singular-value identities, Gram defects, and Gaussian QR chi-law comparisons. The analytic argument in `RESULT.md` supplies all infinite-dimensional-parameter quantifiers and critical divergent-moment conclusions. No finite experiment is treated as an infinite proof.

Reproduction: extract `verify.py` alongside this file and execute it with Python, NumPy and SciPy installed; the deterministic random seed is set inside the script. This verifies identities and distributions on the tested finite samples only. The self-review passed; independent scientific audit has not been performed.
