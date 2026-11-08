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

Finite p-heat ODE with p>1 is the gradient flow of convex edge energy, globally well-posed and order preserving. For a tight oriented edge x-y with u_x-u_y=L=1, normalization x=1,y=0 and complete-multipartite adjacency constraints reduce exact maximal difference derivative to -2+max_{0<=h<=1}{|a-b| h^(p-1)-(N-a-b)H_p(h)}, H_p(h)=min_{z in[h,1]}(z^(p-1)+(1-z)^(p-1)). The proof supplies feasible configurations attaining the bound. For 1<p<=2, H_p=1 on optimum and the maximum is |a-b|-(N-a-b). For p>2 convexity yields a balanced z=1/2 or endpoint, giving the stated negative power-harmonic expression when 2s<N; maximizing over part pairs picks the two largest. The sharp rate has nonpositive sign iff 2s<=N+2, and a Dini derivative comparison gives contraction for each input while a positive-rate witness disproves it. Independent direct original-edge-flow computation on K_(6,1,1), p=2, u=[0,2,2,2,2,2,1,1] has L=1 and tight-edge derivative 2=2s-N-2, proving noncontraction there; this sample is not the general proof.

## originality

PASS

Mugnolo establishes variational p-heat dynamics and order/norm comparison, Lin--Liu--Yang estimates gradients of positive functions, and Münch--Wojciechowski relates linear graph heat to curvature. They do not give exact one-input edge-Lipschitz Dini rates over every multipartite part profile and all 1<p<infty. The linear p=2 special case is credited, not claimed original.

## value

PASS

The sharp p-independent contraction phase boundary alongside p-dependent optimal instantaneous dissipation is a meaningful nonlinear graph flow classification. The nontrivial dependence on the top two part sizes for p>2 is useful for exact regularity analysis, not a scalar renaming of linear theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
