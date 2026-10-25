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

# Mathematical verification

The analytic identity can be reproduced by expanding the base weighted-ball kernel \(C_{d,\alpha}(1-u-t)^{-s}\) in orthogonal monomials and retaining exactly terms of positive \(t\)-degree. Dividing by \(t\) implements the isometry \(f\mapsto z_1f\). The limiting value at \(t=0\) is \(C_{d,\alpha}s(1-u)^{-s-1}\), which is nonzero.

For every pair of interior points, Cauchy–Schwarz ensures \(|u|+|t|<1\) and hence \(|q|<1\). Every scalar disk point can be realized with both points on the first coordinate axis. In the principal logarithm strip, \((1-q)^{-s}=1\) yields \(q_j=1-e^{2\pi ij/s}\) with \(|j|<s/4\). These satisfy \(|q_j|<1\) exactly for \(0<6|j|<s\). The case \(j=0\) is excluded because the continued quotient equals \(s\).

Endpoint replay: \(s=6\) has no interior root; \(s=7\) has \(j=\pm1\) with \(|q|=2\sin(\pi/7)<1\); \(s=12\) has only \(j=\pm1\); \(s=13\) has \(j=\pm1,\pm2\). These checks illustrate the strict count; the complete proof covers every real \(s>1\) arising from the hypotheses.

No numerical plot, finite enumeration, external assistant, or uninspected code is offered as certification. The originality comparison is bounded to the identified literature; no independent audit or validation has been performed.
