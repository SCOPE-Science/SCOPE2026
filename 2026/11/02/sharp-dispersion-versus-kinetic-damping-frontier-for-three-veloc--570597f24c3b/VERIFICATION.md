---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For 0<|c|<1, 0<s_v,s_w<2, and a=1/s_v-1/2,b=1/s_w-1/2, the adopted published stability boundary F(v,w)<=0 transforms by direct rational algebra into Phi=8a²b+4ab²-a-b>=0. With p=ab, Phi=a(8p-1)+b(4p-1), implying p>1/8. A collision damping cap q0<=q<1 imposes a,b∈[ell,1/(4ell)], ell=(1-q)/(2(1+q)). The lower chain when p<1/4 yields 8p²+(4ell²-1)p-ell²>=0, hence p>=P(ell); also p>=ell². Both branches attain and uniquely minimize via (a,b)=(ell,ell) if ell>=1/sqrt6, else (P(ell)/ell,ell), transition q*=5-2sqrt6. Third-order physical log-eigenvalue phase expansion then yields coefficient |c|(1-c²)(p-1/12) and strict infimum |c|(1-c²)/24 as q↑1. Independently checked symbolic F/Phi identity and twenty damping-cap designs.

## originality

PASS

Known exact LBM stability region and physical eigen-expansion are credited, not claimed as new. The additional mathematical claim is the closed two-branch damping-constrained sharp optimization, transition and unique minimizers; no covering formula was evidenced in available primary abstracts or related papers. The uninspected full same-model paper makes the originality judgment qualified.

## value

PASS

A sharp two-regime tradeoff between low-wavenumber phase dispersion and the magnitude of zero-frequency kinetic eigenvalues is a motivated numerical-stability design question. The transition identifies exact optimal relaxation choices and a nonattainable universal dispersion floor, materially beyond the known qualitative no-third-order-stable observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
