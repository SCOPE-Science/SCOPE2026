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

This is the specified Lebesgue-stationary three-coordinate map and only the observable c-1/2. The four affine images have disjoint interiors covering the cube and unit Jacobian. The full-branch u-map supplies independent itinerary choices of weights (1/4,1/4,1/2) independently of the initial c; splitting the last branch by c simply gives doubling mod 1. This yields the stated central operator. The binary digits are independent fair bits under Lebesgue measure; doubling shifts the Rademacher index up, while the two half maps average to a down shift except at index 1 where they cancel. Thus the walk is killed, not reflected, at 0. Solving the resolvent recurrence with geometric forcing and zero boundary gives the difference of the (1/2)^j and eta^j modes, yielding the stated sum. Substituting z=2 eta/(1+eta^2) simplifies the sum to (1+eta^2)/(3(2-eta)^2), verifying cancellation at 4/5 and giving square-root coefficients -2 sqrt(2) and -2 sqrt(2)/81 at the two edges. Independently, the sine transform diagonalizes the killed half-line transition at cos(t) and gives C_n=(1/(8 pi)) times the integral on [0,pi] of cos(t)^n sin(t)^2/(5/4-cos(t))^2. Laplace expansion at the two ends gives the quoted leading coefficient: the endpoint denominators before squaring are 1/4 and 9/4, hence the ratio 1/81 with sign (-1)^n. The quadratic vanishing and next even Taylor terms give O(n^-5/2); the interior is exponentially small. Exact direct dyadic-cell integration of the branch dynamics (/workspace/review_work/baker.py) produced lags 0..7: 1/12, 1/24, 7/192, 5/192, 73/3072, 115/6144, 859/49152, 355/24576. This diagnostic does not substitute for the analytic proof.

## originality

PASS

The known decay exponent, exact reduced operator, and killed-walk transition kernel are fully credited. The distinct earlier contribution assessed is the evaluated algebraic center covariance and its two sharp stationary constants. Later Resultary records demonstrably cover the same formula and stronger families; their overlap is recorded explicitly, not claimed to be new relative to those later statements. No earlier exact evaluation or parity constants were found in the strongest inspected sources.

## value

PASS

The simplest nonconstant smooth central coordinate is a natural test observable for a neutral baker model. A closed all-lag covariance and unequal amplitudes resolve what the optimal order bound cannot: simultaneous contributions from two spectral edges with a measurable parity effect. The scope is a concrete benchmark, not a claim for arbitrary observables or parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
