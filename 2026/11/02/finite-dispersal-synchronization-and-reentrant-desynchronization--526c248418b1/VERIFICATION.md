---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The symmetric positive-definite drift A=[[a+m,-m],[-m,b+m]] yields a unique centered stationary Ornstein–Uhlenbeck Gaussian covariance solving AP+PA=gg^T. Direct symbolic solution independently reproduces det(P)=[((b-a)st+m(t²-s²))²]/[4(ab+(a+b)m)(a+b+2m)²]. The component variances/covariance are positive; C=1 precisely when the numerator vanishes, hence m*=(a-b)st/(t²-s²)>0 for a>b,t>s. Symmetric/antisymmetric eigenmodes give C→1 as m→∞ without claiming identical trajectories. At (a,b,s,t)=(3,1,1,2), an exact derivative factor has (3m-4) times cubic 54m³-309m²-664m-360; Descartes and sign brackets prove exactly one later minimum. For full-rank forcing covariance [[1,99/50],[99/50,4]], det Q=199/2500>0, its correlation derivative factor has quartic 2609152m⁴-17076864m³-10302432m²+25830809m+22887750, exactly two positive roots by Descartes and disjoint sign changes, giving a robust maximum/minimum. Exact SymPy comparisons were independently executed. Only explicit examples assert uniqueness; linear stationary model, not extinction or nonlinear population synchrony.

## originality

PASS

The standard OU Gramian and common-noise drift-eigenvector rank-one criterion are acknowledged prior mathematics, not new. The contribution is a sharp heterogeneous finite-dispersal tuning identity and global nonmonotonic correlation examples, including a nondegenerate environmental-noise covariance. Kendall et al. (2000) treat homogeneous two-patch discrete-time correlations, while Liebhold–Johnson–Bjørnstad (2006) study heterogeneous second-order discrete-time dynamics with simulation; their assumptions/conclusions do not directly subsume this continuous-time formula or two-extrema classification. Ripa (2000), Ly–Ermentrout (2010) are plausible unresolved comparison risks. No equivalent statement was found in the scoped published-research search; negative search is not priority certification.

## value

PASS

Spatial synchrony under environmental noise and dispersal is a naturally consequential population-model observable. A finite positive coupling can produce perfect stationary correlation even with unequal local relaxation and climate response; stronger mixing temporarily reduces correlation. An explicit full-rank forcing witness shows the reversal survives imperfectly correlated noise, giving a motivated qualitative counterexample to monotone-homogeneous intuition and a sharp tunable boundary. No claims about actual extinction or persistence are inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
