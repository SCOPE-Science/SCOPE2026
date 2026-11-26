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

Reconstructed RESULT.md lines 18–85 in time s=γt with h=γ₂/γ. The three faces of the symmetric physical triangle point inward or tangent. Z=u+3v/2 satisfies Z′=−v(u+2hv); on v=0 the vector field has v′=2u², so the origin is the only invariant subset where dissipation vanishes. Compactness and LaSalle give global clearance. For any nonzero initial state uniqueness gives Z>0 at finite times. The equation for q=v/Z has a forcing tending to zero and a coefficient tending to −2h, so q→0. The equation for v/Z² has forcing tending to 2 and coefficient tending to −2h, so v/Z²→1/h. Then (Z⁻²)′→2/h and sZ²→h/2. Returning to physical time gives the two amplitudes as stated, including t v→1/(2γ). The conclusion is on the symmetric triangle only; the zero orbit has no positive tail. Read the verification notes and checker as evidence descriptions, not as an independent execution or a proof; the limits are certified here by the analytic argument, not by a numerical run.

## originality

PASS

Credit the existing model, equality slice, generic cubic slowdown, and formally predicted amplitudes. The distinct supported claim is global clearance and the exact two tail limits for the unreduced deterministic equations from every nonzero point of the symmetric triangle; none of the closest inspected sources gives that implication.

## value

PASS

A local critical balance does not preclude another long-time state at finite prevalence. This theorem rules that out on the entire physical triangle and controls the distinct slow and fast compartment tails with exact physical-time normalizations. The recovery-independent double-infection coefficient is a meaningful benchmark for the reduced equations precisely because it is proved for the unreduced system. No value is assigned to the generic cubic exponent by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
