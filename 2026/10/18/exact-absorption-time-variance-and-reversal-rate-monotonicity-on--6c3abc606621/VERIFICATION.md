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

The transient killed chain has finite moments for each allowed n, λ and κ, since from any state there is positive probability of a bounded-time path of unreversed hops to 0 followed by killing; the minimum of these probabilities over the finite states is positive. The first-hit Poisson equations require the two incoming endpoint boundary values, not both headings at both endpoints. Reflection exchanges the headings at site zero, so the residual lifetime has one law regardless of the arrival heading, and the strong Markov property yields independence of the first-arrival history. At zero the flip terms cancel by reflection, giving κE[A]=1+f_+(1)=n and κE[A²]=2E[A]+2E[A]f_+(1)+g_+(1). Independently checked the proposed moments by substitution into the full killed-ring generator equations, including the boundary and the zero-site equations, and checked the fair-heading average of second moments minus the square of the fair-heading mean and both derivatives: /workspace/branches/replay4.py, 10 exact symbolic identities passed. Reflection gives the other heading. Uniqueness then yields the closed forms. For R′, n−1≤b≤n²/4 gives the lower bounds n³−5n²/2+n and n³−3n²+11n−18 for the two numerator brackets; both are positive for n≥3. The zero-site derivative is positive for the same n and κ>0. Thus strict monotonicity holds on λ≥0, with positive right derivative at zero. The frozen numerical verifier was read without execution; the rational-identity check and analytic inequalities establish the general result.

## originality

PASS

The supported distinct claim is the explicit absolute variance and strict reversal-rate monotonicity for every fair-heading starting site in the fixed continuous-time ring with finite local killing. The closest inspected published generating-function treatment models discrete steps, direction of arrival and imperfect per-step detection. Other close results are first moments only or continuous-space boundary and gating models. None of the strongest checked statements establishes the submitted joint result. This is a bounded judgment, not a priority guarantee.

## value

PASS

For a natural finite-reactivity ring model, the result provides an exactly usable fluctuation invariant, not only an algorithm to invert a generator. The target-start case is particularly informative: its mean is n/κ independently of λ, yet its variance strictly increases with λ. The decomposition separates the effect of excursions after arrival from first arrival, and a strict sign for every site, including the initially ballistic endpoint λ=0, goes beyond a small-parameter example or a restatement of the means. It makes no claim about other geometries or stochastic ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
