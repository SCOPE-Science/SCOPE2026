---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed the exact finite Fock/Kraus representation W_eta=(2/pi)e^(-2|beta|^2) sum_l (-q)^l|f^(l)(2sqrt(eta)beta)|^2/l!, where q=2eta-1, and the exact Jacobian to z=2sqrt(eta)beta. For q>0 sufficiently small, polynomial nonzero away from its finitely many zeros and derivative bounds confine all negative support to disks radius R sqrt(q) about stellar zeros (including tails at infinity). Near an m-fold zero z_j, z=z_j+sqrt(q)w yields q^-m P_q -> |a_j|^2 (-1)^m m! L_m(|w|^2). Fixed-support dominated convergence plus d²w=pi dx gives coefficient m! C_m exp(-|z_j|²)|a_j|² at order q^(m+1); lowest multiplicity governs. The Laguerre sign intervals give C_m>0. Normalization uses half L1 excess convention and fixed finite nonvacuum state; not uniform in coalescing roots.

## originality

PASS

Best-of-knowledge implication comparison of assigned exact claim against primary literature and semantic Resultary search. Pointwise minimum negativity (area-free) is not equivalent to the integrated negative volume: the region of negative Wigner values shrinks on scale sqrt(q) and contributes q. The submitted integral-coefficient theorem strictly refines pointwise survival. It does not deny the known half-loss positivity boundary, and the references do not logically give the coefficient without local asymptotic analysis.

## value

PASS

This gives a quantitative critical exponent and positive coefficient for a natural operational nonclassicality measure at the known sharp 50-percent pure-loss boundary. Distinguishing smallest local stellar multiplicity from total stellar degree matters, and shrinking negative regions add one exponent beyond pointwise negativity. The all-finite-polynomial local-to-global asymptotic is a motivated structural theorem rather than an illustrative Fock-number calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
