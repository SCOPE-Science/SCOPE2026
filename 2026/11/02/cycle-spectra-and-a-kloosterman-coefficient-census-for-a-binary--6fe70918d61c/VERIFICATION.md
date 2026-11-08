---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

With u=x^(q-1) in the norm-one subgroup over F_(q^2), the exact identity F_t(x)=x^q[t+u+u^{-1}] inverts u and F_t^2(x)=[t+u+u^{-1}]^2 x. Admissible Tr(1/t)=0 excludes zero multipliers. The paired nontrivial norm-one fibers correspond one-to-one to z in F_q^× with Tr(1/z)=1 and each yield (q-1)/ord(t+z) cycles of length 2ord(t+z), while F_q^× has (q-1)/ord(t) cycles. Character orthogonality and w=1/(1+v) give T_q=(q-1-K_q)/4 admissible coefficients with 2cycles; Hasse bound and q=4 evaluation give positivity iff q>=8. Independently computed all admissible maps over F_8 by direct finite-field arithmetic: 3 coefficients, K_8=-5, each with q-1 two-cycles. The all-q result rests on field identities and the elliptic Hasse bound, not this finite test.

## originality

PASS

Best-knowledge PASS for full cycle spectrum and exact Kloosterman parameter census. Hou proves the permutation criterion and the norm-one semilinear factorization, which is credited. That factorization does not itself enumerate orbits, count coefficients having two-cycles, or establish the Kloosterman/Hasse threshold. Other inspected cycle papers concern different polynomial families. The cycle decomposition is an elementary extension of Hou and may have appeared independently; no priority certification.

## value

PASS

A complete orbit-count formula for a natural published characteristic-two permutation polynomial family and an exact Kloosterman-controlled cycle-statistic census (with sharp first base-field size) are useful finite-field dynamical invariants, not arbitrary small-field recomputations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
