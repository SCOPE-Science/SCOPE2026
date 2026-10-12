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

# Reproduction of checks

Run `python3 verify.py` with Python 3 standard library. The checker constructs \(A=\operatorname{diag}(\kappa,1)R_\theta^\top\) for twelve rational rotations and four positive distinct rational singular-value ratios. For eight rational mixture values per configuration, it evaluates projectors for the coordinate and all-sign supports and confirms the exact discriminant identity
\[
(M_{11}-M_{22})^2+4M_{12}^2
=\frac{r^2}{(1-r^2v^2)(1-r^2u^2)}
\left[u^2v^2+(1-r^2)(t-u^2)^2\right],
\]
with \(r=(\kappa^2-1)/(\kappa^2+1)\), \(u=\sin(2\theta)\), and \(v=\cos(2\theta)\). It separately checks trace one, the exact completed-square comparison against \(t_*=u^2\), and the Bernoulli/mixture parameter transformation. Expected output: `PASS: 1152 exact-rational matrix/projector/polarization identities`.

These finite tests diagnose normalization and algebra; the universal claim follows from the closed-form projector calculation and completed-square proof in `RESULT.md`. No infinite property is asserted on the basis of enumeration. Neither independent audit nor empirical runtime performance is claimed.
