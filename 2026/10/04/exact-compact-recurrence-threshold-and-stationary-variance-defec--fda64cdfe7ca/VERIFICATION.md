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

The proof was reconstructed from the printed vector field rather than inferred from phase portraits or finite-time Lyapunov calculations. For a compactly supported invariant probability measure, the generator identities for \(x\), \(y\), \(x^2/2\), and \(xy\) were checked explicitly. These identities remove the linear \(y\), linear \(z\), and \(xy\) terms from the stationary average and establish the rigidity step when the nonnegative defects vanish.

The sign check uses the elementary global fact that \(\operatorname{erf}(z)\) has the same sign as \(z\); hence \(z\operatorname{erf}(z)\ge0\), with equality only at \(z=0\). The equilibrium quadratic was factored exactly, and its discriminant was checked as \(a^2+(33/25)\mu\).

The bundled `verify.py` was executed after packaging and returned `VERIFY_OK`. It checks exact rational normalization, the hidden-case equilibria, the critical forcing, and the sharp half-gap bound. Those computations support the arithmetic but do not replace the invariant-measure proof.

Limits: the verification does not prove that the source’s numerically displayed hidden attractor exists as a compact invariant set, does not certify its Lyapunov spectrum, and does not exclude nonrecurrent compact orbit structures at the critical parameter. Independent audit has not been performed.
