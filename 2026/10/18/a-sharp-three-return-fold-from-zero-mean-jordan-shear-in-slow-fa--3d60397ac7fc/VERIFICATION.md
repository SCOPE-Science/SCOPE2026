---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Direct integrating-factor solution gives v(y)=delta exp((y^2-1)/(2epsilon)) and u/v=kappa(y^3-y)/(3epsilon). For 0<y<1 set t=(1-y^2)/epsilon; equality of normalized squared norm 1 is equivalent to kappa=3sqrt((exp(t)-1)/((1-epsilon t)t^2)). Its log second derivative equals -1/(4sinh^2(t/2))+epsilon^2/(1-epsilon t)^2+2/t^2>0; endpoint divergence proves exactly zero, one double, or two interior roots, plus y=1. Positive nonzero second derivative and nonzero kappa derivative ensure a fold; implicit function theorem yields kappa_epsilon/kappa_0=1+t_0 epsilon/2+O(epsilon^2). Independent SciPy root solver checked 5 positive epsilon, all regimes, and the three-return numerical example. No claim about periodic full-state returns or arbitrary norms.

## originality

PASS

Borsotti 2026 analyzes entry-exit for a fixed nonzero nilpotent Jordan block and notes possible extra returns near initial entry; the audited system has sign-changing polynomial shear, zero accumulated shear at balance and two additional positive exits near y=1. Kaklamanos et al. main theorem requires a unique intersection of distinct eigenvalue branches, but these eigenvalues agree identically for all y, so it does not imply this fold. Scalar entry-exit balance predicts only the baseline return.

## value

PASS

Exact bifurcation of observable norm-return multiplicity under a minimal zero-mean variable shear is a natural counterexample to scalar delayed-return uniqueness and quantifies when nonnormal dynamics generates extra crossings. The natural quadratic shear is the lowest nonconstant even zero-integral polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
