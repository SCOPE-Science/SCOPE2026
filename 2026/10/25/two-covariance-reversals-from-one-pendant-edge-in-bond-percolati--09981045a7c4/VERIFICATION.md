---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For any connected unicyclic original graph, open bridges B=M-LZ where M counts retained edges and Z indicates all L cycle edges are open. Indicator covariance gives Cov(M,I)=-p sum_v d_v q^(d_v), and Cov(Z,I)=-p^L sum_{cycle}q^(d_v), so Cov(B,I)=-p sum d_v q^d+L p^L sum_{cycle}q^d. In the single-leaf case degrees are one 1, one 3 and L-1 twos, resulting in pq times Phi_L=-1-2(L-1)q-3q² +L p^(L-1)q(L-1+q). Under odds u=p/q, multiplication by (1+u)^(L+1) yields F_L=L u^(L-1)((L-1)u+L) -(1+u)^(L-1)(u²+2Lu+2(L+1)). All coefficients below u^(L-1) negative, with higher signs -,+,- for L>=4: Descartes gives at most two positive roots counted with multiplicity. For L<=6 the bounding quadratic has negative discriminants -44,-83,-96,-23, establishing no roots. Exact L7 witness Phi_7(13/14)=15515949/210827008>0; for all L>=8 q=1/(2L) and the explicit exponential lower bound give positive witnesses, while Phi(0)<0 and Phi(1)<0. Therefore precisely two simple zeros for L>=7, and one on bare C_L. Independently checked odds-polynomial identities L3..9, exact rational positive witnesses L7..100, and inspected complete exhaustive subset verifier for L3..8. All-L result is analytic, not extrapolation.

## originality

PASS

Best-of-knowledge PASS for the exact sharp L=7 reentrant bridge–isolation covariance threshold. Prior independent-percolation bridge identities concern bridge number, density or covariance with *component count*, and published component-triangle covariance concerns another pair of statistics. Formula for B=M-LZ is elementary, so the claimed new fact is the two-root phase theorem, not generic covariance algebra.

## value

PASS

A one-edge structural perturbation of a natural unicyclic network changes the bridge–isolation covariance from one sign switch to a sharp two-switch pattern at L=7. The exact global root-count transition is motivated by interacting topological connectivity and local isolation observables, and distinguishes a small natural graph family from its leafless base.

The dated certificate retains the supplied scientific assessment, sources and limitations.
