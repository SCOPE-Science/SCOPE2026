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

A CC density operator is diagonal in some product basis, and that basis refines eigenspaces of its two marginals; conversely a rank-one marginal spectral-refinement product resolution commuting with the state forces product-basis diagonality. For universal commutation, all rank-one product projectors inside each P_alpha tensor Q_beta block generate its full matrix algebra, whose commutant consists of scalars; cross-block terms vanish, giving rho=sum c_ab P_a tensor Q_b with nonnegative coefficients and the stated marginal trace constraints. Conversely that block scalar form commutes with all refinements. Two-qubit rho_cc=0.5(|00><00|+|11><11|) has both marginals I/2 but X-basis dephasing yields I/4; checked the exact matrix witness independently.

## originality

PASS

Luo 2008 Theorems 1-2 and Section III were read in the authorized full text: the classicality/spectral criterion is stated using eigenprojectors without resolving the all-versus-exists degeneracy quantifier. Wu–Poulsen–Mølmer and Girolami et al. acknowledge degenerate-basis measurement ambiguity. The exact iff block-scalar characterization for every rank-one refinement is not stated in the inspected primary material. Its elementary commutant proof could be folklore and this remains a risk.

## value

PASS

A classically correlated state with degenerate marginals can be misclassified by an arbitrary spectral eigenbasis. The theorem repairs a precise logical gap and exactly identifies when marginal degeneracy is harmless, a motivated reusable classification of quantum-correlation measurements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
