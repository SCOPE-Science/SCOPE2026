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

Feynman–Kac with resetting yields piecewise ODE Df″−(r+s+v 1_{x>a})f+rf(a)=0, f(0)=1 and bounded infinity. Occupation-density delta potential imposes interface jump D(f′(a+)−f′(a−))=u f(a). Explicit cosh/sinh left solution and decaying right solution give the quoted trivariate Laplace transform for all s,u,v≥0, not just marginals. At s=0 it equals [1+A(u+Φ(v))]⁻¹ with A=sinh(a√(r/D))/√(Dr), Φ(v)=√D v/√(r+v); its Lévy density is positive and integrable, hence independent Exp-time stopped subordinator. Differentiating gives conditional moments and exact increasing correlation. Independent exact algebra checked correlation at nine parameter combinations; inspected finite-difference program tests PDE consistency. Local time normalization explicitly occupation-density, not semimartingale local time.

## originality

PASS

Singh–Pal 2022 supplies separately evaluated first-passage, local-time, and residence-time marginal transforms, which do not determine their joint coupling. Colantoni et al. 2025 have the same inverse-local-time Lévy exponent in a reflected nonabsorbing model; that kernel is credited, not claimed new. Best-of-knowledge, not a guarantee of global historical priority.

## value

PASS

Joint stopped-search exposures and their correlation are important dependencies hidden by known marginals. Exact transform and strict reset-rate monotonicity are a natural quantitative refinement, not a formula obtained by simply multiplying marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
