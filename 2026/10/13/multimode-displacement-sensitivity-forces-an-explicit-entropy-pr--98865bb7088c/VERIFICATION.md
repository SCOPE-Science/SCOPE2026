---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Assuming the *specified uniform thermal Lindblad Gaussian steady-state model* identities from Yoshimura–Hamazaki, tr(V^-1)=2N/nu and Σdot/γ=arcoth(2nu)(||rbar||²+tr V−2Nnu), and displacement QFI u^T V^-1 u, put d=2N and x_i=nu λ_i(V^-1)>0. Then sum x_i=d and their max R∈[1,d). For an index with x1=R, Cauchy–Schwarz/Jensen yields sum_{i>=2} 1/x_i >= (d−1)^2/(d−R); this is exact and yields tr V≥nu[1/R+(d−1)^2/(d−R)]. Removing nonnegative ||rbar||² and simplifying gives Σdot/γ≥d nu arcoth(2nu)(R−1)^2/[R(d−R)]. Independent symbolic algebra verified the identity for arbitrary d and R and finite positive spectra corroborate Jensen. For R=rho N with 0<rho<2, dividing by N and taking limit yields the stated 2rho nu arcoth(2nu)/(2−rho). Important boundary: for N=1 physical attainable R has tighter restrictions and R=1 equality; no claim of realizability/saturation for N>1. Source Gaussian thermodynamic identities could not be independently checked against the full primary because of access; proof is therefore conditional on these precisely cited premises, not certified from finite spectral checks.

## originality

PASS

The prior Yoshimura–Hamazaki paper establishes source multimode trace/entropy identities and a single-mode sensitivity tradeoff, per accessible abstract and assigned package, but the accessible material does not display the full N-dependent best-displacement-direction profile. The new derivation applies a sharp trace-constrained reciprocal-eigenvalue inequality to those identities. Best-of-knowledge PASS with prominent high priority risk: full source End Matter unavailable and may already imply or state this profile.

## value

PASS

The rational gain-dependent lower bound quantifies unavoidable entropy-production growth for extensive best-direction multimode displacement sensitivity, with explicit near-ceiling divergence and linear-in-N necessary cost. This supplies a motivated scalable measurement/dissipation obstruction even though spectral extremizers need not obey physical symplectic constraints, and no equality over physical steady states is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
