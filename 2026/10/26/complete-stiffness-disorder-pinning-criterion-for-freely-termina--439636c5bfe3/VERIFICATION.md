---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For N>=2 and all positive masses, internal springs and independently varying inter-dimer stiffnesses, M^(-1/2) K M^(-1/2) is an irreducible Jacobi matrix, so positive eigenvalues are simple and smoothly ordered. Hellmann-Feynman gives partial lambda_j / partial b_i=(u_(B_i)-u_(A_(i+1)))^2 (mass-normalized). Thus joint stationarity forces all inter-dimer elongations zero; restricting every internal dimer to its local optical eigenproblem and connectivity of the free path shows all local squared optical frequencies coincide. Conversely an explicit recurrence u_(B_i)=-(alpha_i/beta_i) u_(A_i), u_(A_(i+1))=u_(B_i) constructs an exact b-independent vector for all b_i>0, with eigenvalue Lambda. N sign changes across internal bonds yield simple ordinal N+1 by Jacobi Sturm oscillation. Independently assembled and mass-normalized 36 randomly heterogeneous chains N=2,3,5 and verified residuals and correct sorted eigenvalue index. No claim of uniform spectral gap or invariance under mass/internal-spring changes.

## originality

PASS

Wallis 1957 already studies free-end alternating mass edge modes; Allein et al 2023 analyze mass-dimer strain topology; Vishwakarma et al 2025 investigate protected edge modes under *constrained symmetry-respecting* disorder. These works cover important uniform or constrained special cases. The exact necessity AND sufficiency for arbitrary heterogeneous positive masses and in-cell springs under all independent inter-dimer stiffness variations, including fixed index N+1 and full zero-strain mode profile, was not found in the checked primary material. General Jacobi eigenvalue sensitivity is standard and not new. A recent 2026 dimer-phonon preprint and uninspected historical full article are priority risks.

## value

PASS

The iff pinning criterion characterizes when a free mechanical chain has an exactly robust eigenfrequency and mode shape under an (N-1)-parameter family of independent positive spring perturbations, identifying its exact spectral order. It is a natural structural invariant and design boundary, not a small numerical improvement; it clearly separates robustness to intercell stiffness from mass and intracell detuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
