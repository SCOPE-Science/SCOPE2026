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

# Verification record

The reproducibility program `verify_generalized_henon.py` uses Python's exact `fractions.Fraction` arithmetic. Run from the containing directory using `python verify_generalized_henon.py`.

The program executed successfully. It checked all rational identities in the proof for every integer \(3\le m\le20\) and \(b\) equal to \(1/9\), \(1/2\), \(4/5\) or \(9/10\). Checks include the drift identity both at and away from the fold, Perron projection, quadratic center coefficient equations and the logarithmic coefficient simplification. Its numerical supplementary trials used \((m,b)=(3,0.5),(4,0.7),(5,0.2)\), 80,000 critical iterates per trial, and estimated the logarithmic coefficient from separated time windows, with observed signs and coefficients consistent with the theorem. The complete output reported `PASS` for both test groups.

**Proof boundary:** Finite-dimensional tests over sampled parameters are not exhaustive proofs over all dimensions or real damping values; finite orbit trials do not establish asymptotics. Equations (1)–(2) and the general closed-form center-manifold calculation in RESULT.md provide the mathematical argument. The independent-audit channel has not been performed; it is neither simulated nor implied by the checker.
