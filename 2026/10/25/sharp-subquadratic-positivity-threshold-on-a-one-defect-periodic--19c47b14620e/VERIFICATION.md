---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Assembling element matrices for lengths (h,1,1,1,1) gives P=(M+tK)^(-1)M; the pinned exact symbolic verifier computes det(6h(M+tK)) with positive factors for h>=1,t>=0, all 20 directed off-diagonal numerators and five positive diagonal numerators. In the 10 reflection orbits every entry for t>=1/6 except positions (0,2),(1,4) has a positive sign; those two have factor t F_h(t), while (0,3) forces negativity for 0<t<1/6. The cubic F has one positive zero by Descartes sign changes, with F(1/6)=-36(h-1)(h+1) and F(h²/6)=h(h-1)²(h+1)³(h+2). Thus t=0 or t>=rho(h), rho(1)=1/6, strict bound for h>1; expansion F(h/6+c)=6(c-3)h³+O_c(h²) proves rho=h/6+3+o(1). Separate exact-rational assembled-matrix checks verified five ratios (1,1.5,2,5,20), eight timesteps per ratio. The independent finite checks alone do not prove polynomial identities for all h,t.

## originality

PASS

Statement- and implication-level primary-source and mathematical-index comparisons found no directly covering result in the material actually inspected; related ingredients and covered special cases are credited. Best-of-knowledge originality is qualified by the explicit residual risks; a negative search result is not novelty proof.

## value

PASS

Sharp positivity threshold for a consistent-mass numerical heat propagator is a natural time-step invariant. One anomalously long periodic element allows a cyclic bypass that changes threshold growth from the conventional sufficient h²/6 to actual h/6+3+o(1), an asymptotically unbounded improvement, so exact five-cycle root is structurally motivated rather than arbitrary symbolic arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
