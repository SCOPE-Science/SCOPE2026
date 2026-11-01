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

# Reproducible mathematical checks

Run `python verify.py` with Python 3.10+ and SymPy. The program uses no external data, internet access, or random unseeded sampling.

The recorded execution completed successfully and reported:

```
symbolic center-manifold/normal-form identity: PASS
exact first Lyapunov coefficient: (-k**6 - 9*k**4 - 27*k**2 - 27)/(k**4 + 2*k**2 + 1)
exact Fourier polynomial identities: 500 random cases PASS
Schur crossing checks: 300 parameter cases PASS
sample emergent circle Fourier radii vs leading prediction: [(0.001, 1.0085692556514452), (0.0004, 0.9995704056585984)]
all tests PASS; finite computations do not establish existence or priority
```

The symbolic calculation verifies the rational identity for the first Lyapunov coefficient in a positive symbolic parameter. The 500 independently computed Fourier transforms verify the exact quadratic reduction up to the displayed floating-point tolerance. The 300 spectral tests cross the proposed threshold on both sides. At \(c=1\), two near-critical trajectories show radial scales consistent with the leading \(\sqrt{r-r_{\mathrm c}}\) law.

Analytical steps requiring human mathematical evaluation are the center-manifold reduction, justification that all nonresonance hypotheses are met, and application of the standard supercritical Neimark–Sacker theorem in a neighborhood where clipping is inactive. The checker is not an exhaustive verification of these infinite claims. No independent audit has been performed.
