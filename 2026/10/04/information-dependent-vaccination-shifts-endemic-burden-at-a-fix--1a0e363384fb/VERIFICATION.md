---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The submitted endemic-equilibrium equation has the form of a strictly increasing scalar function of the infected coordinate when all stated parameters are positive and the invasion threshold exceeds one. Its value is negative at zero and diverges positively, so the endemic root is unique and positive. Implicit differentiation gives strict decrease with the information-dependent vaccination coefficient and the information growth rate, and strict increase with the saturation coefficient and information decay rate. For large vaccination response, monotonicity and the fixed equilibrium identity force the root to zero; multiplying by the response coefficient and passing to the limit yields the submitted inverse-response scaling. An independent numerical reconstruction at the stated baseline reproduced all four one-at-a-time sign directions and convergence of the scaled infected coordinate to the analytic limit. The finite numerical check is only a transcription guard; the proof is the monotone scalar equation and its exact derivatives.

## originality

PASS

The accessible primary article material for Fang--Liu--Du states the same model, the invasion-threshold formula, existence of an endemic equilibrium and numerical effects of the information-response parameters, but no exact theorem giving all four comparative-static signs plus the large-response asymptotic was located. Earlier behavioral-vaccination work establishes the broader qualitative fact that information can change endemic behavior, so that general principle is not claimed as new. The accepted originality is narrow: the exact four-parameter theorem and asymptotic for this specific equilibrium, which clarifies why independence of the invasion threshold from those parameters does not imply independence of endemic burden. Open-access routes did not yield a complete verified PDF of the exact 2026 source and the permitted institutional retrieval likewise did not produce one; this is recorded as a residual source-access risk rather than converted into a scientific failure.

## value

PASS

Separating invasion-threshold invariance from endemic-burden invariance is mathematically and epidemiologically meaningful. The theorem gives exact directions for four information-response parameters and a quantitative large-response law showing that endemic burden can become arbitrarily small while the invasion threshold remains supercritical. This directly clarifies a source-specific interpretation and is more substantive than a numerical sensitivity check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
