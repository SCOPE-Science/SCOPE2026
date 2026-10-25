---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The inverse-branch formulas give a four-by-four transfer matrix on discontinuous cellwise affine coefficients. The invariant mass row J and fixed vector r satisfy JP=J, Pr=r, Jr=1. Characteristic roots on ker J are -phi^-2 and phi^-2 exp(±2πi/3), all with sixth power phi^-12 and distinct, yielding the sixth-power identity and L1 equality. For g=(x-mu)rho in ker J, covariance is integral (x-mu)P^n g; six exactly evaluated phases determine all lag n. Independent symbolic SymPy calculations reconstructed P^6 and twelve covariance coefficients, rather than trusting old output.

## originality

PASS

The ChaosBook golden-mean pruned-map spectral determinant supplies the key known Perron-Frobenius eigenvalues, so spectrum novelty is expressly disclaimed. Wang et al use this tent map and invariant density as a fluid-statistics model but do not supply six-step density interpolation or the exact six coordinate-covariance amplitudes in inspected material. An algebraic corollary from the known spectral data is possible, but the explicit observable amplitudes and exact convex relaxation are distinct computed identities.

## value

PASS

Quantifying exactly the convergence rate in total variation on a natural invariant finite-dimensional density family and alternating all-lag coordinate covariance supplies a useful mixing/observable benchmark for a standard explicitly solvable nonuniform tent map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
