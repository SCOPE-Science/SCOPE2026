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

Rotational orthogonality gives T_m e_n=w_n e_(n+m) with w_n=M(n+m/2)/sqrt(M(n)M(n+m)). The diagonal Q_m eigenvalues are q_n=w_n^2-w_(n-m)^2, with negative index weight zero. Triangular integration of g=log M yields B(x)=-log w(x)^2 as average of g'' and B prime as average of g'''; strict signs guarantee all q_n>0. Given g''~c x^-gamma and g'''~-gamma c x^-gamma-1, fixed-width integration gives q_n~gamma c m^3/4 n^(-gamma-1). Telescoping yields trace m. Tail-count inversion handles nonmonotone q_n and gives ordered singular-value asymptotic, precise Schatten and critical-log endpoints. Gamma/polygamma moments give disk gamma=2,c=alpha+1 and Fock gamma=1,c=1/a. Independently used high precision moment ratios at n=5000 for alpha=0,2, a=1,2 and m=1,2,4 to approach the predicted coefficients; these numerical checks corroborate but do not imply infinity.

## originality

PASS

Standard angular weighted-shift reduction and index/trace formula are known; inspected quasi-radial and quasihomogeneous Toeplitz literature does not state this moment-curvature-to-singular-value asymptotic with sharp coefficient for angular unimodular winding. Quasi-homogeneous finite-rank brackets are not a dominating infinite-rank Schatten law.

## value

PASS

A precise spectral curvature criterion with sharp coefficient, exact Schatten threshold and Dixmier-style logarithmic endpoint on natural disk/Fock spaces is a motivated operator invariant useful for functional analysis; the disk and Fock models exhibit different decay orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
