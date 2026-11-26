---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The squared geometric coordinates sum to one, and summing the positive adjacent-coordinate products against the weights gives the claimed F. Independently, with b=(1,sq,q²,tq³), each monomial b_i z^i contributes b_i z^i[(2i+1)−(2i+3)z+q⁴z⁴((7−2i)+(2i−5)z)] to the cleared derivative; this gives all nine G coefficients and its endpoint signs. For G coefficients g_j in ascending order, the transformed coefficients are c_k=sum_{j≤k} binom(8−j,k−j)g_j. Independent symbolic expansion (python /workspace/review_checks.py, check 3) matches the entire printed list and all three differences. The differences are strictly negative using u²,u³≤u and x,v>0; therefore once c_3 through c_6 are nonpositive no positive coefficient can follow. The first three are positive and the last two negative. Descartes counts multiplicities and the Möbius substitution preserves them at positive y, so the sign change together with the opposite endpoint signs gives exactly one simple root. Termwise differentiation of the locally uniformly convergent positive series proves positivity up through 1/3 (at equality, all terms except n=0 give positive derivatives). This places the unique critical point strictly after 1/3; its change from positive to negative derivative yields the global maximum, and simplicity gives real-analytic parameter dependence locally, with branches agreeing by uniqueness. No assertion about boundary q=1 or about norming vectors for the true numerical radius is inferred.

## originality

PASS

The checked source poses this exact stationarity-root question outside its restricted regimes. The checked older same-shift results optimize a different invariant. The later modulation-response result reproduces the uniqueness proof and explicitly credits this exact frozen claim rather than being an earlier independent source of it. The supported distinct claim is unrestricted simple uniqueness and its maximizing-parameter consequence for the geometric profile, not the profile formula, lower exclusion bound, or actual numerical radius.

## value

PASS

It answers a specific published unrestricted open question for a natural weighted-shift test-vector family. The branch is uniquely selectable and simple throughout the admissible open region, making optimizations and sensitivity analysis unambiguous, without claiming global numerical conditioning or an exact operator-radius formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
