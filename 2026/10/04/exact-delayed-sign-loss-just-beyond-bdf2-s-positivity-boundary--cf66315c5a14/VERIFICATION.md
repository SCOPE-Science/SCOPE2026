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
The proof reduces the backward-Euler-started BDF2 scalar test equation to an exact second-order recurrence. Below the known threshold, its real-root representation is positive term-by-term after comparing the two geometric modes. At the threshold, the repeated-root solution is explicit. Above the threshold, the complex conjugate roots give a phase representation whose first crossing of \(\pi/2\) is exactly the first negative iterate.

`verify.py` replays the recurrence with exact rational arithmetic for representative values, checks the boundary formula exactly, and cross-checks the phase-index formula and critical-delay asymptotic numerically. The numerical checks do not replace the analytic proof.

No claim is made about variable steps, different starters, nonlinear problems, or coupled-system positivity.
