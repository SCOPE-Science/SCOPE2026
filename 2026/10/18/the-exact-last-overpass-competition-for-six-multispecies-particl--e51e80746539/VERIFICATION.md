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

Dividing by a leaves rates 1,x,1+x. An adjacent inversion swap removes exactly one inversion, so the finite embedded chain is acyclic with only one absorbing state. The two penultimate arrangements are obtained by swapping either of the two unlike neighbors in 001122; consequently only (1,0) and (2,1) can be last. First-step exponential races establish the recurrence with the appropriate terminal payoff. I independently implemented the recurrence with integer polynomials: at each inversion level multiply the previous common denominator by one copy of each distinct total-rate polynomial at that level, and for each state sum move-weighted child numerators times all level factors other than its own rate. This establishes the rational representation by induction without cancellation or numerical interpolation. Exact cross-multiplication matched the frozen Q on the full 90-state/89-nonterminal/180-transition graph. Exact polynomial differentiation matched the reported numerator B with strictly positive coefficients; reciprocal numerator reversal, leading and constant coefficients and substitution x=2 verified symmetry, limits and the example. Reflection of sites plus reversal of labels supplies the probabilistic explanation of the reciprocal identity. Fresh replay passed: python3 /workspace/review-checks/last_swap.py (standard library only).

## originality

PASS

The supported distinct content is the exact finite rational last-type probability and its all-rate strict increase; the Markov recurrence, reflection idea, and large-population last-type selection are not claimed as new. No compared exact source or applicable stronger theorem supplies this finite joint event.

## value

PASS

The invariant tests which of two dependent species boundaries actually completes last, a finite counterpart to established cut-selection results whose marginal cut laws cannot answer it. Two particles per species give the first balanced repetition of all three species, with many different accessible orders of same-type crossings, in contrast to a single copy per species. The exact gap-ratio dependence, steep small-gap tail and strict ordering for every rate ratio give a usable benchmark for finite joint-cut theory, rather than a single enumerated instance or an absorption-time proxy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
