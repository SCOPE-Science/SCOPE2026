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

For two scalar positive-curvature quadratics and complete averaging W=(11^T)/2, the local gradient secant equals h_i whenever defined; initialized adaptive alpha_i=q/h_i remains constant under the specified local-gradient step rule. The tracking invariant sum y_i=sum grad_i and primal consensus after the first averaging step give error recurrence e_(k+1)=(1-q)e_k-q*xi*e_(k-1), xi=(h1-h2)^2/(4*h1*h2). Its characteristic polynomial r²+(q-1)r+qxi is strictly Schur stable iff qxi<1 and q(1-xi)<2; the active bound changes at xi=1/3: qcrit=2/(1-xi) below and 1/xi above. The full 4x4 state has factors r(r-1) times this quadratic; r=1 is excluded on the legitimate gradient-tracking invariant subspace. Independently reconstructed symbolic 4x4 update characteristic polynomial and tested eight rational stable/unstable parameter cases spanning both branches; exactly reproduced source algebra, not relying on standalone verifier status. Unit roots on the boundary are not asymptotically stable.

## originality

PASS

The original AdGT work develops the adaptive local-gradient update and proves sufficient global-network convergence conditions. Qu–Li classical gradient tracking uses homogeneous fixed common steps, and the nearest published exact graph-tuning record addresses homogeneous scalar quadratics. These do not directly entail a heterogeneous reciprocal-curvature two-agent necessary-and-sufficient Schur boundary. The most relevant AdGT full article could not be obtained: OA preprint/PDF links were blocked in this run and authorized Oxford retrieval attempt was stopped by a safety check; only its available abstract and metadata were read. This is a material best-of-knowledge priority risk, not automatic scientific rejection.

## value

PASS

The two-agent complete-averaging quadratic specialization is the minimal nontrivial model of curvature heterogeneity for adaptive gradient tracking. Its exact stability frontier and flip-versus-unit-circle transition show how reciprocal-curvature steps can fail despite scalar local smoothness control, sharpening conservative general network tuning without pretending to be a general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
