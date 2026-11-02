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
# Reproduction and scope

From a directory containing `check_fano.py`, run `python check_fano.py`. The script requires the widely available Python packages `sympy` and `mpmath`. It creates the recurrence polynomials directly from their defining relation, checks values and first two derivatives at \(e=-1\), symbolically verifies the first two outgoing-pole expansion coefficients in the exact secular equation, and uses 60-digit precision to compare outgoing resonance poles with both the quadratic interior-band and the fifth-halves threshold laws. It also tests real below-band eigenvalues under positive coupling detuning at the critical background coupling.

Observed execution: `PASS: 48 exact symbolic identities; 45 high-precision resonance tests`.

The code is diagnostic and does not constitute an exhaustive test over infinitely many cavity sizes or continuous couplings. The general proof uses the exact recurrence and secular equation, nondegeneracy of its reference zero, and analytic continuation near the lower propagation threshold. Scientific validity and priority have not been independently audited.
