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

For each integer k>=1, x=(1,t on left; -1,-t on right), t=1+sqrt2, has x⊥1, ||x||²=2[1+k(3+2sqrt2)]=2D, and x^TLx=2(A+C)+4b≤4 by hub row budgets. Thus algebraic connectivity α≤2/D for EVERY feasible symmetric P, regardless of edge orbit invariance. Candidate a=(2+sqrt2)/D, b=(1+k(1+sqrt2))/D gives ka+b=1, is nonnegative, and Lx=(2/D)x. Full orthogonal eigenvalue decomposition: 0,a (2k-2 copies),(k+1)a,η± where q(z)=z²-[(k+1)a+2b]z+2ab. Signs q(a)=-ka² and q((k+1)a)=-2kab place η-=2/D as smallest positive eigenvalue and η+≤2-η- since a+b≤1, giving SLEM 1-2/D. Equal SLEM forces both hub budgets saturated, x as eigenvector and every individual leaf edge a, hence bridge b: global unique optimum. Distinct heuristic a=b=1/(k+1) has gap [k+3-sqrt((k+3)²-8)]/[2(k+1)], worse for k>=2 and order k^-2. Independent symbolic residuals in free k and twelve matrix spectra reproduced; finite tests are support, not unrestricted proof.

## originality

PASS

Best-of-knowledge original for k>=2 in the uniformly stationary balanced bistar. Crucially, the 2020 Jafarizadeh source already addresses exactly the bistar topology but its formula requires conditions (60), violated for all k>=2 with uniform masses; its candidate even breaches hub stochasticity. General FMMC SDP and clique-bridge block theory do not entail a closed-form constrained optimizer or uniqueness. k=1 is known path, explicitly credited. Strong exact-object prior merits ongoing specialist check.

## value

PASS

Balanced double stars are a natural diameter-three cut-bottleneck family for discrete-time fastest mixing with uniform equilibrium. A single sharp non-symmetrized Rayleigh dual vector, optimizer on a hub-loop-saturation boundary, and individual-edge uniqueness resolve a nontrivial family of SDPs in closed form. The exact comparison proves order-k improvement in spectral gap over standard maximum-degree/Metropolis heuristics; not merely a parameter renaming, known table entry, or tiny sample computation. Natural limits are balanced sizes and reversible nonnegative stochastic transitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
