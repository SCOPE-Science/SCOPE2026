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
The algebraic proof uses only two exact identities: the regular-polygon Vandermonde/resultant factorization and the strict convexity/strict concavity reduction to one cosine parameter. The exact weight-independent optimizing condition is \(\cos\theta=-\cosh(nh)/2\) until this quantity reaches \(-1\), at \(nh=\log(2+\sqrt3)\). For larger gaps the sole optimizer has \(\theta=\pi\).

The accompanying `check_three_ring.py` constructs independent explicit sample points and Fock-normalized evaluation matrices, compares direct log-Gram-determinants with the general formula, and uses an independent two-angle numerical global optimizer as a finite numerical cross-check. Executable dependencies: Python 3, NumPy, SciPy. Run `python check_three_ring.py` in the directory containing the packaged files. Actual recorded stdout is in `check_three_ring.out`. The tests do not certify universal correctness or bibliographic novelty; those require the proof and source comparisons.
