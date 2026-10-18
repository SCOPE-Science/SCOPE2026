---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Direct substitution u=alpha/y splits ∫_0^t F(y)dy into alpha∫_{alpha/t}^∞ e^(-u)u^-2 du plus alpha/[2(1+alpha)]∫ e^(-u)u^-1 du, so its second term is +E1(z)=-Ei(-z). Standard E1 and upper-incomplete-gamma asymptotics at z=alpha/t→∞ yield corrected mean-inactivity +t²/alpha and printed-sign result −t²/alpha. Independent mpmath evaluation at alpha=1,t=1/10: corrected/direct integral 0.0089507141557596967408421823, source-sign −0.00412976212135288638431065. These computations verify the analytic derivation, not a substitute for it.

## originality

PASS

The original model-specific Eq(15) states the wrong sign, and the complete corrected model-specific mean inactivity and reversed small-time asymptotics have not been identified in inspected correction records. The special-function identity is old and explicitly credited; the claim is the identification and mathematically consequential correction of a particular published result.

## value

PASS

Mean inactivity is a physical reliability descriptor emphasized by the original distribution paper and is a conditional expectation of nonnegative t−Y. The source formula predicts a negative value for all sufficiently small positive times, violating that fundamental interpretation, and reverses its leading t² coefficient. Correcting an analytically published distribution formula with such an impossible behavior has concrete mathematical and interpretational value; this is not a mere typographic notation variant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
