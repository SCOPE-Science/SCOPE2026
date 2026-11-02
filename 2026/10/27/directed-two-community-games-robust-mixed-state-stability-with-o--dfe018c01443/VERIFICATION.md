---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For strictly positive 2×2 game payoffs with interior ESS p (K=−(r_A−r_B)' >0), positive directed contacts W and action-independent positive constant migration α,β, mass equilibrium e=β/(α+β), f=α/(α+β) and mixed masses (pe,pf) is interior. The η equation decouples with eigenvalue −(α+β). Differentiating the precise source ODE yields L=C−κg1^T with positive κ=p(1−p)K, C=[[-(Rfu+α),(Reu+β)],[(Rfv+α),−(Rev+β)]], g positive and C(e,f)=0. Thus det C=0, trace L=−A−B−κ(g1+g2)<0 and det L=κ[(B+Y)g1+(A+X)g2]>0: 2D Hurwitz, so full physical Jacobian strictly Hurwitz, implying local exponential stability but no global theorem. Independent symbolic differentiation of original nonlinear ODE at G=[[1/2,3/2],[3/2,1/2]], W=[[10,1],[5,1]], α=β=1/20 gives characteristic polynomial (λ+1/10)(λ²+209λ/40+627/80) and damped nonreal pair −209/80±i√6479/80. Fresh symbolic checks confirm sign identities and witness; exact algebra, not extrapolation, proves universality.

## originality

PASS

Best-of-knowledge original versus closest accessible statements, with real Resultary and primary-source comparisons; failed search is not novelty proof and uninspected plausible literature is recorded, not declared noncovering.

## value

PASS

The natural smallest directed extension of a symmetric-network ESS stability theorem resolves whether reciprocity is essential for *local* stability over all positive directed contacts and migration rates. The exact nonreal-mode witness further distinguishes stable relaxation from monotone decay; it is a mathematically meaningful robustness boundary in a specified dynamical model, without inflated global claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
