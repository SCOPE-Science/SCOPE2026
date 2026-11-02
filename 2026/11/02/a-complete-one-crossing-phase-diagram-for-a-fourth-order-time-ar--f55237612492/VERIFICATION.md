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

# Reproducibility checks

Run `python verify.py` in a Python environment with NumPy, SciPy, and SymPy. The script uses direct stationary generator equations and an independently formed polynomial resolvent; it checks the exact transform, the inverse-Laplace decomposition, rate-one endpoint, asymptotic residues, then compares 35 direct matrix exponentials against separately integrated positive-filter ODEs. Eight spot-sign tests check the predicted regions. Execution on the packaged source returned:

`PASS: symbolic stationary moments, resolvent, factorization, limits, 35 cross-method numerical comparisons and 8 sign checks.`

`Example at rate=1.5: A(1)=-0.021306965280, A(3)=0.025443791234`

The infinite-parameter sign classification and uniqueness are established by algebra, convexity and convolution sign-variation in `RESULT.md`, not by finite numerical enumeration. Independent audit was not performed. The result requires a stationary initialized process with finite fourth moments; alternative noise/reset specifications are outside the proof.
