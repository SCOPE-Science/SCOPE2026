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

For a fixed d-dimensional density matrix rho and independent Haar-uniform diagonal phases, let P=Tr rho^2>0 and S=sum_i rho_ii^2. Expanding Tr(Re(UrhoU*)^2)=(P+Tr(rho_theta rho_theta^T))/2 and balancing torus characters gives mean (P+S)/(2P), variance sum_{i<j}|rho_ij|^4/(2P^2), and central third moment 3 sum_{i<j<k} Re(rho_ij^2 rho_jk^2 rho_ki^2)/(2P^3). Balanced ordered pairs are reverse edges and balanced ordered triples are directed triangles, with combinatorial factor 12. The d=2 sum is empty. For all d>=3, rho=I/d+epsilon H with 0<epsilon<1/(2d) and three nonzero edges yields strict positive definiteness, fixed diagonals/entry magnitudes and opposite cubic signs as the triangular phase flips. Independently formed Re(UrhoU*) matrices over 343 seventh-root grids for two qutrit witnesses and matched mean, variance and third moment at 1e-12 tolerance. The character proof, not finite grids, covers arbitrary d and continuously uniform phase.

## originality

PASS

Best-of-knowledge originality comparison by actual statement and implication, with historical and unavailable-material risks recorded; no priority certification. Inspected closest prior statements use different scopes/estimands or do not directly entail this final exact claim.

## value

PASS

The first phase-sensitive higher moment of a normalized real-sector coherence/imaginarity statistic is a natural quantum-resource question; finding the triangle-cycle invariant and sharp d=3 onset separates magnitude-dependent variance from phase-dependent skewness. The witness realizes both signs at equal moduli in physical positive-definite states, giving a usable structural diagnostic rather than a cosmetic Fourier rewriting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
