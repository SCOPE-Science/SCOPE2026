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

For H=Z×N and Q=N² with Dirichlet diagonal 4, normalized sine/Fourier point-mass weights are N_H=1-cos(2jk2) and N_Q=(1-cos(2ak1))(1-cos(2bk2)), over omega=4-2cos k1-2cos k2. Their rank-one diagonal resolvent F(ε) is continuous, strictly decreasing, finite at zero, and tends to zero, so Birman–Schwinger gives exactly one simple negative eigenvalue iff lambda>1/F(0). For a critical zero vector, Fourier amplitude is δhat/omega and its norm squared is integral N/omega². Near zero, N_H~2j²k2² yields logarithmic divergence (no ℓ² zero mode), while N_Q~4a²b²k1²k2² yields integrability (one-dimensional ℓ² eigenspace). Polar integration for fixed j gives F_H(0)-F_H(ε)=j²ε log(1/ε)/(4π)+O_j(ε). Dominated convergence gives F_Q(0)-F_Q(ε)=εB_ab+o(ε). Since F(0)-F(ε)=F(0)²(λ-λc)+o(λ-λc), the two claimed coefficients follow. Fourier normalization, multiplicity, positivity, and boundary j,a,b>=1 were checked explicitly. Independent Gauss-Legendre and one-dimensional Green-integral calculations confirm F_H,1=0.3633802276324186; F_Q,1,1=0.30234727368645, B_1,1~0.13661977237 and corner slope~0.669111596, and edge log ratios approach j²/(4π).

## originality

PASS

Best-of-knowledge surviving finding is the sharp fixed-site half-plane-versus-quadrant near-threshold exponent and coefficient comparison jointly with their different ℓ² threshold types. Molina 2006 already gives Green image kernels and existence equation; Resultary and Hiroshima et al. cover related critical constants, especially j=1. These older parts explicitly do not count as novel. The inspected primary theorem statements do not supply the complete sharp all-site logarithmic-vs-linear detachment dichotomy. Limited access to Molina 2021 and the indexed multipole report creates substantial, recorded priority risk, not an automatic science fail.

## value

PASS

An exact point-defect spectral threshold in a two-dimensional lattice is a natural object; determining whether the critical state is an ℓ² eigenvector or a resonance and measuring the binding rate is a substantive question not settled by knowing merely the critical coupling. One Dirichlet wall yields marginal dipole decay and ε log(1/ε), while two perpendicular walls yield quadrupole ℓ² decay and linear detachment, with precise universally quantified fixed-site coefficients. This structurally distinguishes edge from corner and supplies numbers useful for spectral asymptotics, not a small arbitrary slice or routine reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
