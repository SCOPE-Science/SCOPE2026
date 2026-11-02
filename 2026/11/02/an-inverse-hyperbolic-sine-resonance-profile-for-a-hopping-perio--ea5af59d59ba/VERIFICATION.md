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

# Verification evidence and scope

The analytic proof in `RESULT.md` establishes the parameter-uniform asymptotics; the finite diagnostics are checks rather than substitutes for its quantifiers. The companion `verify_eos.py` was run with `python verify_eos.py`, returning `PASS: 15 period-three residual, tangent, slope, and gap diagnostics`. The cases span \(a\in\{72,96,120\}\) and \(\sigma\in\{-2,-1/2,0,1/2,2\}\), using 95 decimal digits. Every three-step residual was smaller than \(10^{-70}\). The orbit ordering and the physical invariant interval were checked for each case.

At \(a=72\), the worst relative slope discrepancy was approximately \(0.001781\); at \(a=120\) all displayed relative slope discrepancies were below \(1.1\times10^{-6}\). The exact chain-rule relation between the derivative of the rescaled return function and the Floquet multiplier was also checked numerically. These results test consistency only; no numerical experiment validates all sufficiently large parameters.

No independent audit has been conducted. Historical priority and global basin classification are outside the verification performed here.
