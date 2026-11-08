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

Schoenberg coefficient characterization of zonal PD on S^d gives the correct cone. EGF of n-th centered difference, (2sinh(z/n))^n, computes exact top Bernstein coefficient for t^n and t^{n+2}; combined with leading Gegenbauer terms and C_m^lambda(1) normalization gives [Q_n] B_n Q_(n+2)=(n!/n^n)(n+lambda)(d+1-n)/(3n)*(n+1)(n+2)/((n+d-1)(n+d)), negative for n>=d+2. For S2, explicit n=1,2,3 Legendre expansions are positive; odd n=3 samples m>=7 controlled by published sharp |P_m(1/3)| Bernstein inequality and the low m=1,3,5 calculated separately. Independent exact symbolic reconstruction confirmed 60 (d,n) top coefficients and P5(1/3)=1/3. Prior n=4 S2 coefficient -9/256 is explicitly credited, not claimed new. Full quantifiers rely on the proof, not 60 tests.

## originality

PASS

Best-of-knowledge original contribution limited to complete claimed classification and quantitative threshold; classical ingredients and exact previously known special cases credited. Primary comparisons distinguish same mathematical objects from similar names; remaining equivalence risk explicitly documented.

## value

PASS

The shape-preservation question for zonal spherical covariance kernels is natural: ordinary affine Bernstein approximation preserves positivity for exactly three degrees on S², and a dimension-dependent obstruction applies to all larger spheres. This converts a known single-degree counterexample into a complete sharp degree frontier and general closed obstruction, a useful exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
