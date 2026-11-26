---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Conditional independence and the four environment states give the exact failure law. With both single-good masses positive, one single-good term at any integer k is at least min(q10,q01)e^(−λN), according to the side of θN; rounding θN to within 1/2 gives the stated upper bound, hence the optimizer window. The real second derivative is positive, so inspecting the floor and ceiling of the clipped minimizer suffices. With k=θN+t, the scaled failure is G(t)+q11 e^(−λN)e^((B−A)t). A minimizing lattice point for G lies within one unit of t0 and is feasible at the stated threshold; testing it gives the explicit upper error and positivity of the remainder gives the lower error. G(t+1)−G(t) changes sign at tc, so each phase has its minimizing coordinate in [tc,tc+1], the endpoint values coincide, and strict convexity puts t0 in the interior. The resulting continuous periodic envelope has the stated full range, and the irrational orbit visits arbitrarily close to every phase infinitely often; rational phases have a finite orbit. On q10=0<q01 comparison with k=0 directly yields k≤log(1+q11/q01)/B for every optimizer; interchanging seasons gives the other boundary. When both masses vanish the product or constant cases apply, including ties; the introductory endpoint statement is qualified by these cases. Independent bounded floating-point enumeration corroborated 6000 finite-budget cases and 4357 eligible phase bounds and sampled the example's predicted interval; the infinite result rests on the analysis. The supplied checker was inspected but not executed.

## originality

PASS

The distinct contribution supported here is the explicit lattice-phase prefactor, range and error bound together with the change at the single-good support boundary for the specified two-season failure objective. Dormancy, correlated environments, convex redundancy allocation, and ordinary exponential balancing are not credited as new. Available neighboring statements do not establish this phase-resolved claim. Some related papers were not available in full text, so this is not a priority finding.

## value

PASS

The exponential rate alone is an elementary balance. The explicit, generally nonconverging order-one factor resolves the reliability loss from the indivisibility of seeds, gives both limiting extrema, and distinguishes rational periodic effects from an entire irrational accumulation interval. The support boundary explains how an environment event of any fixed positive mass can maintain an interior large-cohort allocation whereas its disappearance changes the limiting fraction. This is useful for the specified finite-cohort reliability objective without implying an evolutionary prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
