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

# Reproduction and limits

Run `python3 verify.py` with Python 3's standard library. The checker uses exact `fractions.Fraction` operations and verifies the denominator-clearing identity at 4032 rational parameter/input points; it also verifies 288 interior fixed-point and local-stability cases and the explicit \(n=5\) example. A successful execution prints a `PASS` line and exits with status zero.

The proof is analytic for all \(n\geq3\), \(g>1\), and \(0<h<1\). The finite verification suite is a falsification aid, not an exhaustive search or formal proof over infinite parameter sets. The stochastic part invokes Theorems 3 and 4 of the cited published model; neither the numerical suite nor this review constitutes independent auditing of those published theorems.
