---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The full-dimensional uniform-matroid independence polytope is exactly the Boolean capped cube P=[0,1]^n∩{sum x_i≤k} for integers 1≤k≤n. Symmetry gives lambda_parallel=Var(S)/n and lambda_perp=E(X1−X2)^2/2. Under uniform cube sampling X is the vector of independent Uniform[0,1] variables conditioned on T_n≤k. Reflection at exact balanced n even k=n/2 fixes squared differences, proving lambda_perp=1/12, and conditional centered T_n variance equals n/12−(E|T_n−n/2|)^2. Uniformly integrable Gaussian truncation yields the central Mills-ratio longitudinal limit; exponential tilting and a uniform density local limit produce the subcritical exponential gap with n theta² lambda_parallel→1; Hoeffding gives the supercritical cube limit. The volume large-deviation rate, determinant decomposition and all near-half subsequences yield the normalized isotropic constant. Independent exact rational integrations verified 35 (n,k) from n=2..8 and four balanced transverse cases; this bounded test does not prove the infinite limits.

## originality

PASS

Best-of-knowledge PASS for the combined continuous-volume covariance spectrum, sharp integer-balanced rigidity, critical transition and isotropic constant, not for exponential tilting, conditioned CLT or the Irwin–Hall formula themselves. Ferroni 2020 studies Ehrhart coefficients of precisely the uniform-matroid independence polytope, a distinct lattice-counting invariant. Broniatowski–Caron 2014 derives general Gibbs conditioning and overshoot approximations that cover important probabilistic ingredients but neither states these exact eigenvalues nor the geometric isotropic transition. Other published capped-hypercube John-ellipsoid results optimize enclosure geometry, not uniform covariance. No stronger exact covariance theorem found; older conditional-limit work may imply some pieces through specialization.

## value

PASS

The complete three-regime answer describes anisotropy of a canonical matroid family and isolates the one decaying longitudinal direction under a rank cap, an exact balanced eigenvalue, and an affine-invariant limit. These are geometrically meaningful continuous invariants, not a parameter renaming of a general theorem or an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
