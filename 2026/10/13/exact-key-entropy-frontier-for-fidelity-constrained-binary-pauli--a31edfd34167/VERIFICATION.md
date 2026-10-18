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

For two distinct pure qubit Bloch vectors, C=cos²(θ/2), V=sin²(θ/2)>0 and τ=2η−1, the source contractions give utility (1+Cλ_z+Vλ_x)/2 and fidelity divergence −log(1−Vλ_x²). Every channel has λ_z≤1; |λ_x|≤t makes τ≤C+tV necessary, and I/Z mixing with λ_x=t, λ_z=1 attains it. Group Pauli outcomes into {I,X} and {Y,Z}: q=p_Y+p_Z=(1−λ_x)/2. Entropy chain rule H(Pauli)≥h₂(q)≥h₂((1−t)/2); the two-gate distribution attains equality. This proves feasibility and exact entropy for every θ∈(0,π], t∈[0,1], η∈[0,1], including η and θ boundary cases. At t=1, θ=π, the permitted divergence bound is +infinity; no finite bound is implied. The source optimal contraction a* gives the privacy-optimal specialization. Independent exact 1/10-grid test covers 286 probability vectors and corroborates, but the unrestricted assertion uses the entropy grouping proof.

## originality

PASS

The Shannon-key extremal frontier is an exact constrained resource theorem for a fixed pure binary ensemble, not just the previously known one-bit perfect-privacy endpoint or the source optimal fidelity contraction; the primary 2026 preprint discusses key budgets without a Shannon optimum. The result is mathematically simple once the Pauli sign partition is recognized, so implicit-corroIary and folklore risks remain.

## value

PASS

Shannon key entropy directly measures the classical randomness resource for Pauli concealment. Optimizing it across all four Pauli gates at every pair-specific fidelity/utility cap, with explicit feasibility and two-gate achievers, resolves a motivated joint resource frontier; it does not claim a non-Pauli optimum or physical fractional single-use key.

The dated certificate retains the supplied scientific assessment, sources and limitations.
