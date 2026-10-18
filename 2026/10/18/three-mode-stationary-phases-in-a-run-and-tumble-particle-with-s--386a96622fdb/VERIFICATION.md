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

# Reproducibility and verification

The finding follows from the stationary transport equations, the fourfold hyperbolic-angle identity and a strict-concavity argument. Execute `python3 VERIFY.py` in the directory containing the bundled source. The program is standalone and uses only Python's standard library. It reports `PASS 6407 checks; example Q(y)=(-3+46y-83y^2-16y^3)/16`.

The rational checks independently compare the hyperbolic-angle polynomial identity, expanded stationary derivative, the exact witness signs, and endpoint derivatives over positive rational parameters. The float checks compare an independent direct stationary-log-derivative expression with the predicted cubic over 400 spatial values. The continuous global modal trichotomy rests on \(Q''(y)<0\), endpoint signs and the monotonic change of variables; finite tests cannot certify universal quantifiers.

The witness uses \((v_0,v_1,\gamma_0,\gamma_1,u,g)=(1,1/2,3/8,1/4,4,16)\) and is admissible with strict inequalities. Its three maxima and two minima are nondegenerate; this and the implicit function theorem establish open persistence. The result does not assert an unrestricted trichotomy for independently chosen positive steepness ratios, a stochastic-diffusion perturbation theorem, or an external independent certification.
