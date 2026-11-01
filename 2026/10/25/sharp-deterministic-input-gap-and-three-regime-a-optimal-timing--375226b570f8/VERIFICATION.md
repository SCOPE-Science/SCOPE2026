---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For x0=0, x1=b u0+w with centered independent variance-s noise, put h=b^2>0, q=E u0^2,p=E u1^2,c=E x1u1. The information covariance is [[s+hq,c],[c,q+p]], with c²<=(s+hq)p and total budget s+(1+h)q+p<=beta. The inverse trace is minimized at c=0 (feasible via independent centered open-loop controls), with full budget used. With S=s+hq in [s,(s+h beta)/(1+h)], the strictly convex symmetric function 1/(eta+S)+1/(eta+beta-S) is minimized at S*=clamp(beta/2,s,(s+h beta)/(1+h)), yielding unique optimal covariance and late/mixed/early timing regimes. For fixed deterministic controls, c²=h q p and full-budget branch determinant D(q)=(eta+s)(eta+beta-s)+h q(q-s), strictly convex, so maximum occurs only at pure-stage endpoints; switching beta=s(2+h). Randomized gap strictly positive iff optimal q*,p*>0; h>1, beta->infty ratio (1+h)^2/(4h). Independent exact rational checks of 3030 mixed deterministic splits and rational witness h=4,s=eta=1,beta=3 reproduce F*=4/5,F_det=5/6. Scope excludes deterministic state-feedback, which is more expressive than fixed deterministic open loop.

## originality

PASS

Bencherki--Lee--Matni--Rantzer arXiv:2609.08751 gives the general nonlinear weighted trace-inverse covariance design, convexity and Frank--Wolfe linear oracle via Riccati recursion, including finite-horizon causal feasible covariances. Its Sections 2–4 and Appendix 8.1 do not explicitly classify the present two-stage scalar isotropic criterion, three timing phases, or fixed deterministic open-loop separation. Ordinary A-optimal balancing of two positive diagonal entries is standard; novelty is specifically the exact dynamical realization and gap.

## value

PASS

The exact three regimes and sharp deterministic-vs-randomized gap in a natural smallest dynamic A-optimal design are a meaningful classification of when randomization/correlation control is necessary for optimal information, with an unbounded gain-dependent approximation loss. The nonlinear inverse-trace objective matters; replacing it by linear Frank-Wolfe subproblems changes the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
