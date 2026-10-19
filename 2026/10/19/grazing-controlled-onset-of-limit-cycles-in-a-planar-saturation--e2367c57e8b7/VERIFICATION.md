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

# Reproduction and verification

Run `python verify.py` in a Python 3 environment with NumPy and SciPy installed. The program integrates the exact clockwise polar flow, constructs a section return, and checks its attracting fixed point for four indicated parameter pairs. It integrates an auxiliary physical-time equation and a piecewise divergence equation along the same trajectory.

Observed finite checks for \((a,b)=(0.004,1.5),(0.0006,1.5),(0.004,2),(0.0006,2)\) gave the respective normalized amplitude values approximately \(1.02393,1.00682,1.02555,1.00736\); normalized period corrections approximately \(1.02027,1.00643,1.01753,1.00557\); and normalized negative log multipliers approximately \(0.98842,0.99634,0.98820,0.99629\). The program printed `VERIFY_OK`.

The four-cap coefficient is also checked as \(4(4\sqrt2/3)=16\sqrt2/3\) and checked against \((16\sqrt2/3)C_*^{3/2}=2\pi\). The program does not exhaust arbitrary small parameters or verify the uniform asymptotic error analytically; those steps are contained in the proof in `RESULT.md`. There is no external or independent audit.
