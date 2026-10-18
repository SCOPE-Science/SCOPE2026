---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Connected trees of diameter<=3 are exhausted by stars and double stars. For D_(a,b), all three maximal independent sets and exact random-greedy probabilities are p_u=(n−1)/(n(a+1)), p_v=(n−1)/(n(b+1)), p_0=1−p_u−p_v; independent exhaustive permutation counts matched cases including D_(2,2) and D_(2,3). The three-coordinate TV bias is max_i|p_i−1/3|. Convexity/reciprocal comparison reduces a>=2 to a=2; exact difference against a=1 is (n²−8n+9)/(3n(n−3)(n−2)), negative at n6, positive at integer n>=7. Stars have bias (n−2)/(2n), strictly worse at n>=4. Boundary orders n3,4,5,6 give unique minimizers P3,D11,D12,D22 with biases 1/6,1/12,1/15,1/9; n>=7 unique D_(1,n−3) and bias 1/3−(n−1)/(n(n−2)). Independent rational fixed-order checks n=3..100 confirm examples only; displayed algebra proves all n.

## originality

PASS

Fairfax-Ball already gives exact mixed-spider probabilities including one-sided double stars D_{1,b}; that subcase is not new. The final assessment is the sharp optimization across ALL stars and two-sided D_{a,b} at each n with unique minimizers, plus the order-six transition and uniform positive gap for diameter<=3. Its fresh two-sided law and extremum comparison are not direct corollaries of the published mixed-spider expression.

## value

PASS

The smallest nontrivial diameter class with a positive uniform greedy-selection bias is a natural structural boundary given the known diameter-four family with bias tending to zero. An exact sharp value at every order, globally 1/15 at a uniquely characterized five-vertex fork, and the exceptional order-six minimizer constitute a complete, motivated optimization rather than an arbitrary small graph census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
