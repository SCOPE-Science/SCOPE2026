---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Positivity forces both integer exponents ≤t=N−1, and this condition is sufficient even on the diagonal where equal powers carry to one bit. There are ts labeled pairs. A two-bit value determines its unordered exponent positions uniquely, and a second labeling is available exactly when both distinct positions are r-th powers. One-bit values do not collide with two-bit values or with each other, so subtracting binom(s,2) gives the exact count for all allowed cutoffs, including t=1. Algebra gives Z=−{t^(1/r)}−s(s−1)/(2t); the extra term is a shift by −1/2 plus O(t^(−1/2)) for r=2 and O_r(t^(−1/r)) for r≥3. In a full block [k^r,(k+1)^r), count the corresponding integer interval [(k+α)^r,(k+β)^r); relative to its uniform target the error is O_r(k^(r−2)+1), uniformly in endpoints. The sum of these errors is O_r(K^(1−1/r)), and the single unfinished block is of that order at most. On a dyadic index block of size T, a threshold comparison can change only in a fractional-root interval of length O_r(T^(−1/r)); the difference of two prefix bounds gives O_r(T^(1−1/r)) exceptional indices. Summing these bounds proves the uniform-in-threshold rate and the shifts stated. Boundedness of Z gives an O(N) error, and its nondegenerate limiting law rules out convergence to any constant and hence a constant linear correction with o(N) remainder.

## originality

PASS

Credit Yan's cited Chen lemma for the first-order count and do not claim novelty for fractional-root equidistribution as a proof ingredient. The distinct finding is the exact dyadic count and label collisions coupled to the quantitative distribution of the normalized secondary remainder, including the collision-induced shift at r=2 and failure of every constant linear correction. Inspected prior statements cover the leading scale or a different counting problem; Chen's inaccessible full text remains a real implication risk.

## value

PASS

The value is identifying the exact size and distribution of the leading asymptotic's fluctuations in a natural subfamily of the general Romanoff set, not the routine binary-encoding argument alone. The square case has a different secondary law because collisions survive at linear scale; higher powers have no such shift. The nondegenerate law settles the natural question of whether a deterministic second coefficient exists at dyadic cutoffs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
