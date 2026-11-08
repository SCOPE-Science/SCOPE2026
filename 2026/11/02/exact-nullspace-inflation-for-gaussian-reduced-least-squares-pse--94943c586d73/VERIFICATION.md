---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

By orthogonal invariance take J=[I_r 0] and S=[G;B]. Coefficient minimum gives B G†c; conditional variance ||G†c||² with reciprocal chi-square_{ell-r+1} by Gaussian Schur complement, independent chi-square_{d-r} numerator. Haar random ell-plane=ker H; physical minimum solves H2y=-H1c, giving independent chi-square_{d-ell}/chi-square_{ell-r+1} marginal, or exactly zero at ell=d. Beta-prime/Gamma integration gives each moment for 0<q<ell-r+1, divergence at/above cutoff and sharp t^{-nu} tails. Checks included Gaussian feasibility and minimum-norm inequality; (d,r,ell)=(2,1,2) deterministic S example confirms coefficient can inflate despite full span. The two marginal laws are NOT a joint law.

## originality

PASS

The inverse-Wishart chi-squared identity is standard; the contribution is the exact finite-dimensional joint comparison of two explicitly different tie-breaking conventions, sharp moment/tail thresholds and full-span pathology. LeJeune et al. inspect asymptotics of sketched pseudoinverses, while Cartis et al. concern globalized safeguarded random-subspace Gauss–Newton; neither reviewed result states this precise two-selector finite marginal pairing. Residual broad classical literature priority risk remains.

## value

PASS

The exact identification of coefficient-norm versus physical-norm selection is a useful numerical linear algebra distinction: even when a random subspace equals the full ambient space the coefficient solution can have infinite mean-square excess while the geometric solution is exact. Sharp finite-n thresholds quantify it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
