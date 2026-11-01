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

# Verification and reproducibility

The included standalone `check_chialvo.py` runs with Python 3 standard library only. Execute `python3 check_chialvo.py`. It checks the activation derivative constants, the mean-field projection cancellation for four coupling values, and trajectories of a heterogeneous 17-node Chialvo network at \(q=0.03,0.01,0.003,0.001\). The code asserts the analytic error bounds after a finite transient. The tested parameters are \((a,b,c)=(0.89,0.18,0.28)\) and equally spaced quenched inputs between \(0.026\) and \(0.030\).

For rigorous verification, the critical equalities to check independently are (i) the exact orthogonal projection of the voltage update, (ii) the sharp elementary global derivative suprema for the activation term on the positive half-line, (iii) the backward geometric series for each bounded complete recovery trajectory, and (iv) the geometric bound \(S_x\le q\|\boldsymbol\kappa\|_2+qLS_x\). Each step is derived in RESULT.md and yields the stated quantified inequality without invoking finite numerical data.

No independent audit, formal proof certification, or external validation has been performed. The coupling threshold is sufficient, not optimal. The source paper's numerical Griffiths-phase coupling range is not covered by the strong-coupling theorem.
