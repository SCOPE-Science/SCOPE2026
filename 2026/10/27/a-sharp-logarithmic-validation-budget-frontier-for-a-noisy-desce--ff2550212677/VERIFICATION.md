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

At zero the empirical loss change is 3/2−2J/B, giving the strict integer cutoff floor(3B/4)+1. The unit-step proposal is always ±1 regardless of the current iterate, so zero cannot be revisited after acceptance. Fresh draws give the asserted conditional hazard and multiply survival; after departure the gap is exactly 1/2. For every B the exterior tail is positive and at most 1/2, so permanent survival is positive iff the hazards are summable. For large B the consecutive binomial mass ratio from the first accepted count is <1/3, so the tail and its first mass are comparable; Stirling at 3B/4+θ, 0<θ≤1, gives B^(-1/2) exp(−BI) up to bounded factors since the entropy shift is θ log 3+O(1/B). For c>0 the floors are bounded perturbations and summation reduces to k^(-cI)(log k)^(-1/2), or to 1/[k(log k)^(a+1/2)] at critical scale. The two equality cases diverge; if c≤0 is allowed, B stays at one and departure is immediate in the almost-sure eventual sense. An additive B offset bounds the union of departure events via a summable envelope. A flip after departure instead requires a strict majority for the opposite endpoint and an opposite proposal; the resulting symmetric chain contracts by |1−2q_B| for fixed B. The supplied finite enumeration and output were read as corroboration only, not as proof of the thresholds.

## originality

PASS

The covered ingredients are the independently sampled null-step rule, exact lattice-tail methods and the product/summability test. The distinct finding is the exact pathwise failure frontier of this specific noninterpolating, fixed-step repeated safeguard, including irreversibility and the sharply divergent equality at a=1/2. It is not a claim about full adaptive scaling or priority for any of the ingredients.

## value

PASS

The model isolates how a shared but independently sampled validation batch can fail to protect even an exact global optimum. It distinguishes arbitrary finite fixed budgets, a sharp log slope, and the separate log-log refinement that a Chernoff exponent alone misses. It also gives an explicit way to control the probability of ever accepting a worse point in the regime where retention is possible, without claiming applicability to other step rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
