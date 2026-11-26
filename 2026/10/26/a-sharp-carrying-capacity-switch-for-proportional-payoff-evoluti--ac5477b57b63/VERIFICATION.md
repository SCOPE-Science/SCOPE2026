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

On the invariant interior the shared prefactor cancels from d log N/dx. Multiplying the proposed log-derivative of Φ by x(1−x)d(x) gives a quadratic with endpoint values P and R and quadratic coefficient b−a, exactly those of W; this check also covers a=b. Positive g and W give exponential convergence N→K. The increasing Φ has endpoint limits 0 and infinity, so the invariant gives a unique interior x∞, with x−x∞ exponentially small by local inversion. The resource log-odds derivative ε(1+θ)(x−x_c) integrates to the appropriate infinite limit unless x∞=x_c, when its integral is positive and finite. If x_0≤x_c, the terminal x is strictly below x_c even at initial equality. For K>K_c and x_0>x_c, strict monotonicity yields exactly one crossing and the invariant fixes its population coordinate at K_c, not its physical time or resource height. For the calibration, Φ(3/4)=36, Φ(1/2)=2, and cancelling 2x−1 leaves x/[(1−x)(1+(1−x)^2)]. With y=1−x the primitive is log y−(1/2)log(1+y²)−arctan y, yielding the stated J. Solving n/(1−n)²=2 exp(J) and evaluating gives 0.563817739263549, consistent with the stated interior limit. The supplied script and documented checks were read, not run.

## originality

PASS

The finite-capacity rescue phenomenon and its underlying model are prior work. The supported distinction is the exact fixed-payoff classification on the positive proportional subclass, including an explicit K_c, the unique turning population and the finite interior critical limit. The closest inspected exact resource-fate theorem varies the endpoint matrix and gives attainable final outcomes, which does not determine this fixed-matrix invariant or trajectory threshold.

## value

PASS

This gives a complete finite-capacity phase classification in a natural subclass that fixes the payoff order and isolates the role of population growth. It explains why a strictly declining cooperative fraction can still sustain the resource, gives a feedback-independent turning population and resolves the nonhyperbolic critical resource fate rather than just reproducing the known rescue phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
