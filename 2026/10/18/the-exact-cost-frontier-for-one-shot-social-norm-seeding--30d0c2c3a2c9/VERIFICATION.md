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

For x<1 and y>0, dividing the ODE gives a linear equation with integrating factor (1−x)^(−β). Its solution through (r,0) is g(x)=(1−x)^β ∫_x^r β(r−u)/(1−u)^(β+1) du; evaluating the integral verifies both branches of g and makes the sign of y−g(x) invariant until x reaches r. For x∞<1, the time integral of y is finite and y is uniformly continuous; hence y→0 and x∞≤r, since otherwise the per-capita rate of y would eventually be positive. Below the curve the orbit cannot reach r and its limit lies strictly below r; on it the limit is r; above it no such non-outbreak limit is possible. With x→1, logistic upper and lower comparisons give y→1−r; x=1 follows directly, while y=0 is invariant. On the feasible arc [a,r], g''=β(1−r)^(1−β)(1−x)^(β−2)>0, g'(r)=0 and g(a)=a uniquely. Thus the right endpoint cannot minimize c_s x+c_v g(x), and the sign of λ+g'(a) yields exactly the stated transition, including equality. For β<1 the base of the interior power is positive because it equals ((1−x*)/(1−r))^(β−1) at the unique derivative root. Every successful seed lies strictly above the minimum, but perturbations to larger x at fixed positive y approach it even at (a,a). For β=1, t log t=r/(1−r) yields the claimed principal W, and substitution gives the mixed cost formula. The numerical package evidence is supplemental; the result is established by these analytical checks. The term ‘critical saddle’ is informal: (r,0) has a double-zero linearization and is not a hyperbolic saddle. Success is defined unambiguously elsewhere and no conclusion uses hyperbolicity.

## originality

PASS

The distinct supported claim is the one-time two-cost optimization frontier, not the phase portrait or its exact separation of basins. The closest statement supplies the full feasible separatrix, which makes the new calculation short, but does not pose or solve the weighted price allocation. No equivalent cost theorem was found in the inspected sources; this is not a priority certificate.

## value

PASS

The exact frontier answers whether a hard budget can work and how relatively costly supporter recruitment changes the optimal composition, not just whether a given seed spreads. The mixed-to-corner transition and the distinction between equality and strict budget slack are useful even though strict convexity makes the proof short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
