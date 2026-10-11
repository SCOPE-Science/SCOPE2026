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

# Reproducibility and scope

Run `python checker.py` in the extracted package with SymPy installed according to `requirements.txt`. The checker asserts the identity
\[
G(x)=-\frac{x^2(P+Qx)}{(u+knx)(1+qx)},
\]
under both critical equations, and confirms the exact rational example with \(P=11\), \(Q=3\) and \(u/(2P)=1/11\). Its expected output is `CHECK_OK: exact cubic, positive coefficients, rational witness, critical amplitude`, and this output was observed by running the actual checker file.

The analytic global step additionally uses positivity, upper and lower logistic bounds, planar Poincaré–Bendixson and index theory, and attraction near the nonhyperbolic equilibrium. The asymptotic step uses a smooth center manifold, identification of the invariant strong-stable branch \(x=0\), and integration of the reciprocal-square evolution. These infinite-time conclusions are proved in `RESULT.md`; the symbolic checker is not a formal proof of them. No positive-delay extension or independent mathematical audit is claimed.
