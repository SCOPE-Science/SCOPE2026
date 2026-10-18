---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

With fixed m,r,k,lambda>0, fixed inoculum one, c>0 co-scaling saturation and disease mortality, the implicit horizon T solves mT+c integral_0^T[x V/(1+lambda cV)]dt=1 uniquely since derivative m+cF>0. The ODE bound d(log V)/dt<=g(x)=9/2-(x-10)^2/20 gives V<=exp(g(x)t) and T<=1/m, hence Kc<=K0 uniformly all x>=0,p in [0,1]. K0 uniquely maximizes at x=10 with strict sign and uniform negative curvature. Uniform C2 compact perturbation and derivative signs make one critical maximizer on any fixed [0,R], while the global K0(R)<K0(10) gap excludes unbounded tails. This yields unique global x_c(p)=10+O(c), q_c(x_c(p))/c=10m J(9/2,1/m)+O(c), and optimized Kc=K0(10,p)+O(c), all uniform p including endpoints.

## originality

PASS

PASS, best of knowledge: Barril-Vegué’s 2026 source defines the exact coupled within-host/evolution model and exhibits multiple finite-c fitness peaks depending on host mixture. It does not establish a uniformly unique global optimum under joint vanishing crowding and mortality coupling. Older heterogeneous-host virulence evolution studies use different infection-age structures and cannot be substituted for this parameter-specific singular perturbation theorem.

## value

PASS

PASS: the theorem proves that a biologically meaningful two-peak/hysteresis mechanism disappears under a precise weak-competition limit, uniformly over host proportions, and gives exact limiting selected phenotype and induced mortality. A motivated global bifurcation/selection boundary, not just the elementary peak of initial growth g(x).

The dated certificate retains the supplied scientific assessment, sources and limitations.
