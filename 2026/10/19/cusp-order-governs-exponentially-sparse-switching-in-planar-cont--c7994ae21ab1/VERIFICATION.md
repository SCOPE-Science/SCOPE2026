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

The strict separation condition resets each upper visit below the switch; in a lower run the positive ratio y/x^p grows by lambda^(1-p), so visits recur. For q=1/lambda and a=1-lambda*x_tau, the first upper iterate after the reset is the least integer m with (p-1)m>tau+1+log_q(a^p/y0). The resulting tau'=(p/(p-1))*tau+O(1) is uniform along the fixed orbit. Dividing by successive powers of R=p/(p-1) and summing the bounded-error tail gives a limit and an O(1) unscaled error. The limit is positive since tau tends to infinity and the remaining tail from any visit in units of that visit is bounded by K/(R-1). Inversion gives the log count. At p=2, a tends to 1 strictly from below after the first visit, so floor(log_q(a^2/y0)) is eventually ceil(log_q(1/y0))-1, including at integer log heights. This argument applies only with positive initial height and without equality hits under the stated separation condition.

## originality

PASS

Credit the antecedent for the parabolic map, infinitely many upper visits and the ghost-orbit/omega-limit analysis. The supported distinct result is the quantitative actual-time law for general p and the eventual integer-affine clock at p=2. No equivalent statement or stronger result supplying this law was identified in the checked material.

## value

PASS

This assigns a precise time scale to a known recurrent, nonperiodic switching example whose limit set does not specify visitation frequency. It isolates the cusp order from the contraction strength at leading order, gives a bounded counting error for every admitted orbit, and resolves the integer-height resonance rather than discarding it as exceptional.

The dated certificate retains the supplied scientific assessment, sources and limitations.
