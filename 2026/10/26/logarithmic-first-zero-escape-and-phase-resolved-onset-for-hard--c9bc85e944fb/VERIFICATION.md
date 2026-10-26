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

The proof is analytic and unrestricted in the real cutoff \(L>0\) for the fixed-cutoff zero census. The large-cutoff statements use a uniformly controlled endpoint-Laplace expansion.

Run `python check.py` with the versions recorded in `requirements.txt`. The checker independently evaluates exact complex-error-function expressions against direct high-precision quadrature, records the first positive zeros for multiple cutoffs, compares the rescaled transform to its phase asymptotic, and tests phase-locked sequences. Its printed values are saved in `check_output.txt`.

Crucial inequalities verified algebraically in the proof are \(|e^{-u}-1|\le u\) for \(u\ge0\), \(\int_0^\infty v^2e^{-2v}\,dv=1/4\), and \(e^u>1+u\ge\cos u+\sin u\) for \(u>0\). Direct numerical agreement does not certify the infinite-frequency zero count, and numerical phase-locking examples do not establish subsequential convergence. No independent audit has been performed.
