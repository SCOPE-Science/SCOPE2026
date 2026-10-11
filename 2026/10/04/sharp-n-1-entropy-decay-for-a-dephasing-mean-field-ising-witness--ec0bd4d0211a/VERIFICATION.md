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

The mean field vanishes because tr(m_t Z)=0, while local Z-dephasing commutes with every ZZ interaction term, giving rho_N=U_N m_t^{tensor N} U_N^*. Pairwise conjugation of X_i contributes one cosine factor per neighbor and all sine terms vanish in the product expectation. Since log(m_t)=alpha_t I+artanh(r_t)X and rho_N is unitarily conjugate to the product state, the many-body entropy difference reduces exactly to that one-site expectation. The fixed-time expansion of cos(2Jt/N)^(N-1) then yields the positive N-scaled limit. Fresh basis enumeration through N=8 reproduced the closed expectation exactly.

## originality

PASS

The source theorem proves a class-wide O(N^{-1}) normalized-relative-entropy upper bound but does not state optimality or an exact lower-bound witness. One-axis-twisting literature supplies related collective-spin expectations but not the faithful mixed-state Umegaki identity with local dephasing and the resulting sharpness conclusion. The audited witness therefore adds a genuine matching-order obstruction inside the exact hypotheses of the recent entropy theorem.

## value

PASS

A matching lower-order witness is a natural and useful sharpness result for a new quantitative propagation-of-chaos theorem. The example remains genuinely dissipative rather than reducing to a closed Hamiltonian special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
