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

The full binary branch coding of the piecewise slope-2 map is a fair Bernoulli itinerary. Exactly the two length-m cylinders flanking 1/2 form the hole; adjacent-symbol equality bits give a 2-to-1 reduction to avoiding the single word 1 followed by m-2 zeros. Last-one decomposition yields b_{r,l}=1+sum_{j=1}^r b_{r,l-j}, including r=0; from t+m-1 cylinders derive P(tau>=t)=b_{r,t+r}/2^(t+r), r=m-2. Generating function at 1/2 and subtraction of first r+1 unconstrained lengths yields E tau=2^(m-1)-m+1. Perron root gives escape log(2/lambda_m), entropy log(lambda_m) and dimension log(lambda_m)/log2 for m>=4; r<=1 has entropy zero. Small-hole expansion follows (2-lambda)*lambda^r=1. Null precritical boundary points do not change Lebesgue results. Finite independent direct counts for m=2..7,t=1..6 corroborated but did not supply the infinite proof.

## originality

PASS

Closest dynamical papers address entropy/dimension or periodic/zeta changes; general finite-state waiting-time algorithms could compute any fixed forbidden list but the inspected results did not state the explicit simultaneous all-m recurrence and first-hitting mean. This is a qualified best-of-knowledge assessment, not a claim of novelty of finite-state methods, Perron entropy or Hausdorff formula.

## value

PASS

Symmetric dyadic neighborhoods are the canonical critical-hole refinements of this map. The closed all-resolution finite-time survival distribution and exact expected escape time are natural probabilistic invariants; the first positive-entropy scale m=4 gives a substantive boundary beyond routine fixed-parameter counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
