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

The accompanying `CHECK.py` was executed successfully with SymPy. It reconstructs the four-dimensional transfer matrix directly from inverse branches; independently verifies the normalized invariant-density vector and integral conservation; computes the exact resolvent and 11 Taylor coefficients; derives the characteristic polynomial, rational covariance function, summable Green--Kubo series, derivative, and nonzero cubic-pole coefficient; and checks exact rational specializations \(t=1/4,1/2,3/4\).

The analytic proof in `RESULT.md` covers all real \(0<t<1\) and the infinite-time central limit theorem via the classical spectral gap for a primitive piecewise-expanding Markov interval map. Symbolic computations do not independently certify this external functional-analytic theorem. The older and partially unavailable sources and the possibility of prior broader results remain the main novelty limitations. Independent audit: not performed.
