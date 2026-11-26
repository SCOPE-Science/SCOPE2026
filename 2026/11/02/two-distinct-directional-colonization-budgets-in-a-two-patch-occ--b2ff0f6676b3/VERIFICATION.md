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

The stationary weights satisfy all four master equations by direct symbolic multiplication with the specified generator; positivity and irreducibility give the unique normalized law. Quotient differentiation gives W_E=δL²−4Lht+4δt² and W_P=δL(L+g)−4Ljt+4δt² with t=u−B/2. Reflection excludes negative t when δ>0. In the repaired proof, both numerators decrease on [0,L/2], start positive and end negative: W_E(L/2)=−2(h−δ)L² and W_P(L/2)=−2(j−δ)L²+δLg<0 since j−δ=2e+g and δ<L. Thus each has exactly one root in that interval and the feasible optimizers are obtained by clipping at B/2. Evaluating there yields the stated thresholds. Since W_P−W_E=δLg+4Lgt>0 on the root interval, the P root is strictly farther right, which also gives B_P>B_E at B=B_E. At each threshold the corresponding optimizer is still at the endpoint, and δ=0 gives unique midpoint optima. The uploaded verification script was inspected, not executed: it had the wrong quadratic sign in W_E and used the wrong radical for the sample u_E. The supplied replacement verifier corrects both and passed 405 exact stationary comparisons plus exact derivative and optimizer checks for the example. The replacement RESULT.md makes the root choice explicit and documents the corrected finite checks. The theorem and scope are unchanged.

## originality

PASS

The supported distinct claim is the comparison between expected occupied-patch count and joint occupancy: their separate exact endpoint thresholds and strict ordering. Do not credit as distinct the joint-occupancy optimization in isolation if the parameters match the closely related Resultary record. The corrected proof and verification preserve the exact objectives, thresholds and boundary cases, so the statement-level comparison still applies.

## value

PASS

The two commonplace conservation metrics favor different allocations in a natural minimal occupancy model. The proof identifies a nonempty interval in which one objective keeps the full endpoint allocation while the other requires splitting capacity, and orders the allocations once both split. This decision-relevant contrast is stronger than a numerical example or substituting stationary probabilities; it remains valid with the corrected evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
