---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For each integer p>=2 the rational orbit u_j=2^(p-1-j)/(2^p-1) has p distinct states. Selected vs excluded ordinary-to-stubborn distances are integer multiples of 1/(2^p-1), disjoint by parity and strict spacing; symmetric unions of open intervals radius 1/[100(2^p-1)] ensure the required left-trust-only itinerary for p-1 steps and right-trust-only for the last. Actual averaging gives u_(j+1)=u_j/2 and final (u_(p-1)+1)/2=u_0. In a uniform small neighborhood each affine step has slope 1/2, so the return map contracts exactly 2^-p and yields open local basin; no one-/two-agent symmetric self-confident system can cycle because ordinary distances to sole stubborn opinions cannot increase. Independent exact rational itinerary and contraction checks for p=2..24 support all-p proof.

## originality

PASS

Original source gives one period-three example for the same three-agent SCOD model and convergence with IDENTICAL stubborn opinions; neither determines arbitrary prescribed prime p with open attraction under two DISTINCT anchors. Broader piecewise-affine contraction constructions may exist but do not necessarily satisfy the model’s symmetric set-confidence incidence constraints.

## value

PASS

Shows optimal agent count does not bound prime-period length even with reciprocal open confidence, while guaranteeing a rigorous attracting neighborhood, a substantive dynamical construction addressing published oscillation questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
