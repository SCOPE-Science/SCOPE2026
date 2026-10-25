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

The expected-count kernel was derived from the constant-normal-stress seismicity-state equation and matched to the existing cumulative-seismicity integral. The maximum was checked by a strict chord inequality plus the monotone-weight rearrangement theorem, and the minimum by an explicit pointwise strictly convex Lagrangian with a uniquely solvable stress budget.

`verify.py` was run from the delivered package. It checked one symbolic-radical parameter example numerically, computed 600 feasible fixed-budget piecewise-constant stress profiles, verified the analytical extrema bounded each computed event count, and independently propagated the exact state ODE across every block and instantaneous stress jump. The program printed `VERIFICATION_OK`. Numerical sampling does not certify the universal theorem; the preceding analytic proof does.

The original model assumes fixed normal stress, spatial uniformity and unchanged source properties. No empirical data analysis, finite slew-rate optimization, statistical calibration, or independent audit was performed. The inaccessible full text of Dieterich (1994) and possible general convex-allocation analogues remain originality risks.
