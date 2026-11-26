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

The sign marginal is uniform, and the positive-rate joint chain is irreducible. Independently set p to the charged marginal and d to half the difference of the two conditional charged probabilities. Adding the conditional balance equations gives p-p_eq=(Bs/G)d because the sum and difference of the relaxation rates are 4kG and -4kBs and the ratio of the summed up rates to the summed relaxation rates is p_eq. Subtracting the equations then gives 4(ν+H/G)d=2ks/C, so d=ksc/[2(H+νG)] and the oriented flip current is νd. Conservation gives the same current on the other three edges; the summed log rate ratio is 2α and all stationary mass ratios cancel. This gives the stated σ and both normalized fractions H/(H+νG) and νG/(H+νG). Since ks²<H+νG, the charge is strictly between p_eq and 1/2. The fractions give strict monotonicity and the one-sided limits; the Bernoulli divergence has positive first derivative for p>p_eq and second derivative 1/[p(1-p)], yielding the decreasing strictly convex free-energy frontier.

## originality

PASS

The bounded comparison supports the specific biased-battery marginal versus full-chain dissipation identity and its switching frontier, not novelty of four-state telegraph models, the free-energy convention, or cycle entropy production. The closest examined telegraph model computes a different observable with symmetric wells.

## value

PASS

For fixed battery and affinity parameters the identity gives an exact way to infer full-chain dissipation from the storage marginal when switching is the only parameter varied. The positive fast-switching dissipation limit despite a thermal storage marginal and the opposite slow-switching endpoint quantify what a marginal-only model misses. This is a useful restricted benchmark rather than a general battery efficiency or optimal-control claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
