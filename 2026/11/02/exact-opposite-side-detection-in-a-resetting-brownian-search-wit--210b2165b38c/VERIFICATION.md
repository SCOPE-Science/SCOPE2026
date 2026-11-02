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

Execute `python3 verify.py` using the standard Python library. The checks reconstruct both full half-line solutions and verify the active/inactive boundary and reset conditions at hundreds of deterministic parameter samples. Event-time simulation uses independent exponentially distributed reset and gate-switch intervals, unconditional normal Brownian endpoints, and the exact Brownian-bridge crossing probability when the gate is active; it avoids time-step sign-crossing approximations.

Observed output: `PASS 5406 analytic-boundary/residual/ordering and fixed-seed Monte Carlo diagnostics`. Four Monte Carlo comparisons have fixed pseudorandom seeds, sample size 18,000 each, and explicit six-standard-error tolerances. These simulations are supplementary. Mathematical completeness relies on the displayed unique bounded backward-value solution, strict derivative inequalities, and exact limit calculations. Nothing in the package constitutes independent external review or publication-priority certification.
