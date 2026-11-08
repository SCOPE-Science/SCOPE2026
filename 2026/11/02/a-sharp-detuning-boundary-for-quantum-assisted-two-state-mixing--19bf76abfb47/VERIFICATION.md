---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Pauli commutators give the 3x3 Bloch generator M with initial z=1. At b=0 the y,z-plane is damped rotation and at a=0 z obeys the classical scalar equation. For ab≠0 the symmetric part of N=M+2γI is diag(4γ,0,0), and its eigenvector equations force first component nonzero; all eigenvalues of N have positive real part. Analogously M has strictly negative real spectrum. Hence e^(2γt)z(t), a nonzero exponential polynomial with all exponents of positive real parts, is unbounded in absolute value; its leading finite trigonometric polynomial has positive mean square. Taylor gives z(t)-e^(-2γt)=-2a²t²+O(t³). The exact Laplace resolvent P_b(s),Q_b(s) and simple pole at zero at b=0 give λ_s=-2γb²/(γ²+a²)+O(b⁴) and A_s=a²b²/(γ²+a²)²+O(b⁴). Independently checked numerical matrix exponentials for several real a,b,γ and eigenspectrum in the off-axis case; finite tests corroborate rather than prove universal spectral argument.

## originality

PASS

The central/permutation-group algebra quantum-stochastic-walk two-state acceleration formula is prior work. The b σ_z detuning is outside that commuting Hamiltonian family; the all-time iff classification and quadratic, nonzero late-time pole residue are not implied by that theorem or the general Lindblad formalism. Best-of-knowledge PASS with primary-paper full-text access limitation.

## value

PASS

This sharply locates the loss of all-time output-mixing improvement under an arbitrarily small physically natural diagonal energy detuning, including the singularly slow late-time relaxation with small spectral weight. The small amplitude prevents conflation with first-hitting mixing-time deterioration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
