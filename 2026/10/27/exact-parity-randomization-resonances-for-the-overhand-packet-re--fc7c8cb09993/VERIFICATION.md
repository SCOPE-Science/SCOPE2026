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

A packet reversal has sign (-1)^(length choose 2); the ordered composition weights are p^(m-1)(1-p)^(n-m), so multiplying the signed single-packet series and summing the geometric series gives the stated denominator and initial conditions. With r=sqrt(1-p) the oscillatory solution has numerator sin(nθ)-r sin((n-1)θ), where p=2r cos θ. The argument shift of 1-r exp(-iθ) is arctan(sin θ/sqrt(1+cos²θ)), strictly increasing with positive derivative for 0<θ<π/2, with endpoint limits 0 and π/4. The increasing total phase runs strictly between 0 and nπ/2+π/4, giving exactly floor(n/2) positive integer multiples of π; the phase and parameter derivatives are nonzero at each crossing. At the repeated-root endpoint the formula limits to r^(n-1)[n-(n-1)r]>0. Above it both characteristic roots lie in (q,1); x^(n-1)(x-q) is strictly increasing there, giving positivity by the difference quotient. The zeros in θ differ from jπ/n by less than π/(4n), so the empirical law is the pushforward of the uniform θ law. Differentiating the inverse cosine gives precisely the stated density; the radicand has a simple endpoint zero. Below p* irrational rotations give both signs, and rational rotations form a repeated orbit of at least five equally spaced angles, which cannot stay in either closed semicircle. Multiplicativity of sign gives the exact parity distance; full reversal is a fixed sign factor under the alternate convention.

## originality

PASS

The shuffle model, the general sign-character time law, and second-order recurrence methods are established. The substantive distinct claim supported by the searches is the exact finite-deck set of parity-uniform cut probabilities, its cardinality and simplicity, and its limiting parameter distribution. Agreement about the model or about sign expectations for another shuffle is not coverage of this claim.

## value

PASS

Parity is the canonical two-point quotient of the walk. Determining all parameter values for one-step stationary parity at every deck size, and resolving their density and endpoint concentration, answers a natural exact randomization question not captured by the full-deck mixing scale. The novelty-bearing part is the root classification in the physical cut parameter rather than just a recurrence evaluation or a standard TV projection formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
