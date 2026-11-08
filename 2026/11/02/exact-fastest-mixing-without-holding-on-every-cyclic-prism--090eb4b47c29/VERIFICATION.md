---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. Dihedral and layer-swap averaging of arbitrary symmetric nonnegative zero-diagonal stochastic P on C_n□K2 reduces the optimum value to rim q and rung p=1-2q with q∈[0,1/2]. The exact Fourier branches θ_k+=1-qλ_k and θ_k-=-1+q(4-λ_k), λ_k=2-2cos(2πk/n), include all 2n modes. Every even prism is bipartite, so s with Ps=-s gives SLEM=1 for every admissible P. For odd n, ε=2-2cos(π/n), the necessary lower bound max(|4q-1|,1-q ε) is uniquely minimized at q=2/(4+ε), p=ε/(4+ε), μ=(4-ε)/(4+ε); inequalities ε≤δ,Λ≤4 bound all remaining symmetric/antisymmetric Fourier modes and prove attainment. The odd gap is π²/(2n²)+O(n^-4), one-quarter of the holding-permitted leading gap. Boundary n=3 is a triangular prism with distinct rim and rung edges; n even includes degenerate/disconnected walks.

## originality

PASS

PASS, qualified. Standard spectral FMMC symmetrization and Cartesian-product eigenvalues are established by Boyd and collaborators, and a related cyclic-prism problem allowing holding admits a different optimizer. Imposing zero diagonal is not a substitution in that solution: it forces period two for even n and a distinct two-mode balancing condition for odd n. The inspected primary work did not give the complete loopless all-n optimum; specialization under another name remains possible.

## value

PASS

PASS. A zero-diagonal transition constraint is a genuine protocol constraint in distributed averaging and changes feasibility qualitatively. The exact all-n formula, bipartite obstruction and factor-four asymptotic penalty provide a complete, directly usable design law on natural prisms—not simply a restriction of the unconstrained solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
