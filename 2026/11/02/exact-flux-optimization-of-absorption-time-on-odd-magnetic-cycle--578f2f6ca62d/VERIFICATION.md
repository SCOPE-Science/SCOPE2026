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

For odd N and sin(phi)≠0, the twisted ring Hamiltonian has simple plane-wave eigenvalues and no eigenvector orthogonal to the site-0 sink. Dissipative identity implies A=-iH−kappa P0/2 strictly stable, so the integrated no-jump survival solves a Lyapunov equation. Spectral row sums reduce the trace to N/kappa, an oriented roots-of-unity term sigma_j/(2J sin(phi)), and a positive even term; Chebyshev characteristic-polynomial residues and the discrete Fourier interval identity sum_q sin²(jπq/N)/sin²(πq/N)=j(N-j) give the latter kappa*j(N-j)/(8J² sin²(phi)). The j=0 formula follows separately. At optimal sin sign opposite sigma_j, writing x=1/|sin(phi)|≥1 reduces global minimization to a strictly convex quadratic with unconstrained x*=2J/(kappa L). This proves the two-solution weak-sink regime, the unique quarter-flux strong regime, and coalescence at kappa=2J/L. An independent complex Lyapunov solver checked all nonzero sources on N=3,5,7,9 for four fluxes, two sink strengths and J=1.7 (160 numerical comparisons), including both flux orientations; the proof, not these finite tests, covers all odd N.

## originality

PASS

The 2014 Krapivsky–Luck–Mallick primary full text studies a quantum ring with a local trap but **without magnetic flux**, and shows dark/avoiding states and decay rates; its continuous sink model is a close antecedent and this distinction is material. Bose–Jin–Korepin study unitary twisted spin-ring state transfer, Zimborás et al chiral network transport, and Finocchiaro et al a discretely monitored chiral ring. None of the inspected mathematical claims computes the full flux-dependent continuous-sink integrated survival nor the all-kappa global flux bifurcation. Earlier combinations of these methods or a missing exact Green-function treatment remain priority risks.

## value

PASS

Mean integrated survival is an exact physically motivated transport observable. The theorem classifies it for all odd ring lengths, all source distances and sink strengths, with a qualitative design transition at kappa=2J/L from two interior optimal fluxes to one quarter flux. It differs from unitary transfer fidelity, asymptotic decay rates, or stroboscopic detection, and supplies an independent natural closed-form benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
