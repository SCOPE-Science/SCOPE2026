---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The source equations have one shared exposed class E. At the disease-free equilibrium only the incidence term entering E creates newly infected individuals; the flows alpha*varphi_j E into I_j and (1-alpha)phi E into C are transfers. The resulting F has only its first row nonzero, V is lower triangular, and the unique possible nonzero eigenvalue of FV^{-1} is the displayed additive R*. The infected Jacobian yields the same threshold because its real characteristic function is strictly increasing and has g(0)=a_E(1-R*). For the exact two-strain witness the printed quantity satisfies R_print^2=5/6<1 while R*=10/9>1, and a fresh symbolic calculation gives characteristic polynomial (z+3)^2((z+3)^2-10), hence positive eigenvalue -3+sqrt(10).

## originality

PASS

The complete primary 2026 paper was inspected at the model equations and reproduction-number section. It places progression terms out of the common exposed class inside its new-infection matrix, obtains a maximum of square-root branch expressions in equation (3.8), and states local stability in terms of that quantity. Standard next-generation literature explicitly defines F using production of genuinely new infections, not transfers between infected states. Current Resultary search found no source-specific correction with the additive shared-exposure formula or the exact false-stability witness. Separate-exposed-class multistrain models are architecturally different. Originality therefore passes.

## value

PASS

The result repairs a published local-stability criterion and gives an admissible parameter point where the printed rule predicts stability while the actual linearization is unstable. Correcting a threshold that changes the qualitative epidemiological verdict is a substantive and reusable model-analysis contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
