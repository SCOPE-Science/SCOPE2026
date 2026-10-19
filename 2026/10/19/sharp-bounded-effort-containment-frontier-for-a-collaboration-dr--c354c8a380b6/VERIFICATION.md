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

The included `verify.py` uses only the Python standard library. Reproduce with `python verify.py` in a directory containing that file. Successful execution reports 162 exact rational derivative-transformation identities, exact \(U=1\) and \(U=2\) critical-control examples for \(N_0=4\), seven strictly decreasing sampled critical cost values as \(U\) rises, and consistency of the exact terminal-schedule gap identity for front-loaded versus uniform controls. The quadrature comparison is numerical, not an exact infinite certificate.

The scientific proof rests on the explicit integrating-factor solution of the controlled power equation, the pointwise cumulative-effort inequalities, the exact constant-rate hitting solution, and the separate integral representation of the minimal budget. Finite verification cannot establish unrestricted optimality over measurable controls, positivity beyond the reference domain, or any claims for modified stochastic or congestion models.
