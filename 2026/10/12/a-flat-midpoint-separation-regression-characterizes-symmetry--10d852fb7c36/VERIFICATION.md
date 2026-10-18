---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Center iid X1,X2 at mean μ and write Z1,Z2 with mgf M. Conditional mean zero given |Z1-Z2| annihilates (Z1+Z2)cosh(t(Z2-Z1)); exchangeability independently annihilates the sinh part. Factoring expectation of (Z1+Z2)e^{t(Z2-Z1)} using independence yields M'(-t)M(t)+M(-t)M'(t)=0. Thus for K=log M, K'(t)+K'(-t)=0 and K(t)=K(-t) near zero. MGF uniqueness forces central symmetry. Conversely global sign reversal leaves separation invariant and flips midpoint, proving conditional mean constant. Exponential integrability justifies differentiation on smaller neighborhood. Independent exhaustive exact fractions confirmed 9072 support-weight laws, 396 equivalent cases; enumeration is not the universal proof.

## originality

PASS

Best-of-knowledge PASS after reading complete particularly relevant older midrange paper via authorized institutional access, reading relevant open author preprint on adjacent-order regressions, and checking related independence and covariance results. Older characterization corpus remains large, and 2015 Huang--Su full article not fully examined.

## value

PASS

Mean independence of two-observation midpoint and separation is a canonical and weaker dependence constraint than full independence. The theorem gives a complete symmetry characterization under a transparent local mgf assumption and includes atomic, mixed and continuous parents, sharply separating symmetry tests from classical sample-mean/range normality independence theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
