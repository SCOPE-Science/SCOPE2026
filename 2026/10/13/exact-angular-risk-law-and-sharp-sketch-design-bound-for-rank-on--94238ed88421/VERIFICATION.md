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

# Verification

In exact arithmetic, a one-column Nyström residual for \(A=\operatorname{diag}(a,b)\) and any nonzero \(g\) is \((ab/d)vv^{\mathsf T}\), where \(d=au_1^2+bu_2^2\), \(u=g/\lVert g\rVert_2\) and \(v=(-u_2,u_1)^{\mathsf T}\). This fixes the norm and the rank; all distributional claims follow from the angular distribution and an integral, not from numerical evidence.

Run `python3 verify.py` with Python 3 and the standard library. The script carries out 60 exact-rational matrix-residual checks, exact discrete-isotropic Jensen checks at five contrasts and four moment orders, and 32,000-point midpoint angular quadrature for Gaussian moments at contrasts \(1,4,9,100,10000\). The defined checks completed successfully. The exact Gaussian values tested were \(1,5,15,505,500050\) for the squared Frobenius ratios. The verifier has no external dependencies or filesystem inputs.

The Gaussian direction's arcsine density and the beta/elliptic integrals are established analytically in `RESULT.md`; numerical quadrature only checks finite instances. Finite tests do not establish every contrast or the high-contrast moment limits. The theorem is restricted to strict positive definiteness, dimension two, single-column, unshifted exact Nyström and an eigenbasis-aligned direction-class comparison. The theorem does not analyze any independent audit channel, floating-point stability, or arbitrary unknown orientation.
