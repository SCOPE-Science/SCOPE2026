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
The all-parameter proof is given in `RESULT.md`.

Critical checks:
- the source six-facet realization is
  \[
  s,t,v\ge0,\quad
  Al-s-dt-\Delta_Av\ge0,\quad
  bl-t-\Delta_bv\ge0,\quad
  l-v\ge0;
  \]
- the two non-unit normal lengths are \(N_A=\sqrt{1+d^2+\Delta_A^2}\) and \(N_b=\sqrt{1+\Delta_b^2}\);
- radius-\(\rho\) feasibility is exactly the six normalized-clearance inequalities;
- since \(d,\Delta_A,\Delta_b\ge0\), replacing a feasible center by \((\rho,\rho,\rho)\) preserves feasibility;
- the remaining three inequalities give the exact three barrier values;
- the shifted source inequalities at the optimal radius give the complete incenter set.

`verify.py` independently solves the four-variable Chebyshev linear program for hundreds of deterministic parameter choices by active-set enumeration and Gaussian elimination, and compares the optimum against the closed formula. The finite replay is corroborative only and does not assess originality.
