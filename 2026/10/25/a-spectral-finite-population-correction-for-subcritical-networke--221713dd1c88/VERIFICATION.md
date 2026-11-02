---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The exact infection-intensity budget uses total infectious person-time E T_M to establish (1−R)E T_M=1−(R/M)J_M, J_M=E∫Σ_ij P_ij I_i C_j dt. A same-seed subcritical multitype birth-death process dominates SIR, has finite second moments, and finite genealogy collision probability O(1/M); integrated quadratic moments provide an integrable dominating variable so J_M→J∞. With D=I−RP, m′=−Dm, Y′=−DY−YD+diag((I+RP)m), X′=−DX+RYP+Rdiag(Pm). Symmetry/stochasticity and uniform seed solve ∫Y=D⁻¹/[n(1−R)] and ∫X=D⁻²/[n(1−R)]. Thus J∞=tr(PD⁻²)/[n(1−R)] and the coefficient follows. Neumann series K=[n(1−R)²]⁻¹ Σ_{k≥1} kR^k tr(P^k) positive (trace P²>0 if trace P=0). For Q symmetric stochastic, f′_R(x)=(1+Rx)/(1−Rx)³>0 on [-1,1], so K increases with identity-mixing θ. Independent exact-rational dynamic programming on finite SIR states, resolvent and integrated-moment matrix checks corroborate two-patch and one-patch examples without replacing the analytic coupling proof.

## originality

PASS

General subcritical branching epidemic approximations, message-passing bounds and network outbreak results are prior foundations. The assessed new component is the explicit first inverse-patch-size trace resolvent coefficient together with strict identity-mixing monotonicity for every symmetric stochastic P; no inspected predecessor directly implies that exact pair.

## value

PASS

The first nontrivial finite-size term of the minor-outbreak mean detects patch network topology while the infinite-population leading term is universal. Its spectral trace/closed-walk form and strict monotone mixing response provide a natural quantitative correction in a standard stochastic epidemic model; no critical-scale assertion is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
