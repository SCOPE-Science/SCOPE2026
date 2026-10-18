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

For any odd n>=3, P_x,P_y,P_z are pairwise anticommuting Hermitian involutions, so B_w²=||w||²_2 I and its operator norm is ||w||_2. On a product state the Bloch-coordinate Cauchy–Schwarz bound gives expectation <=||w||_infty and product Pauli eigenstates achieve equality. For the actual product of rho marginals, trace duality bounds the positive witness gap by ||B_w||*||rho−rho_1⊗...⊗rho_n||_1. Quantum Pinsker with natural logs yields 1/2 times square; maximizing over w using the l1-ball support function ||w||_infty gives precisely 1/2 dist2(c,B1)^2. Local depolarizing c(t)=exp(-nt)c(0) makes the certificate positive iff its l1 sum >1, yielding the stated lifetime. The physical anticommuting-state witness rho_a is positive for a<=1/sqrt2, and gives the strict 3/2 factor versus fixed equal weights.

## originality

PASS

The source Tian preprint gives the general Pinsker witness mechanism and a fixed equally weighted three-Pauli example; Quensen et al. provide the octahedral separability criterion but not a quantitative total-correlation envelope. Combining anticommuting operator exact norm with duality produces the full REAL weight optimization; that projection formula and resulting best-bound/lifetime classification are absent from inspected source. General Pinsker and support-function duality are acknowledged as standard; originality is their sharp envelope for this specified physical three-parity family.

## value

PASS

This is an exact strongest certificate within an explicitly motivated experimentally accessible observable family, not a claim that the physical total correlation is determined by three numbers. It can strictly improve the anchor lower bound for positive physical states, supplies a closed soft-threshold formula and identifies the precise finite-noise horizon when this certificate ceases to detect correlation. The odd/even anticommutation boundary is mathematically essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
