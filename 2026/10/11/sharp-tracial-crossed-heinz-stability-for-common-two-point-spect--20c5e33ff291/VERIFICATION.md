---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Reconstructed the proof over all finite tracial von Neumann algebras with faithful normal finite trace, a>b>0, 0<t<1 and arbitrary projections. Projection identities R^2=X(2-X) and R(X-1)=-(X-1)R yield self-adjoint C_t=s(X)-d_tu(X). The polar sign U=sgn(P-Q) conjugates X to 2-X on E=supp u(X); faithful finite trace supplies spectral reflection even for continuous spectra. Pairing h(x)+h(2-x) establishes the EXACT trace-deficit functional-calculus minimum min(d_tu(x),a+b-delta|x-1|). The polynomial-square identity 2s(x)-Lu(x)=((sqrt(a)+sqrt(b))x-2sqrt(b))^2>=0 proves the uniform coefficient min(d_t,L/2)/delta^2. For d_t<=L/2 complementary rank-one M2 projections attain d_t/delta^2; for d_t>L/2 rank-one P,Q with overlap r*=(sqrt(a)-sqrt(b))/(sqrt(a)+sqrt(b)) attain L/(2delta^2). Independently computed 2x2 rational witness a=100,b=1,t=1/2, r*=9/11: C eigenvalues -820/121,18782/121, trace deficit 40, distance squared 6480, quotient 1/162. All seven frozen files and current identical Git blobs were read/checked. These explicit finite checks corroborate, but do not replace, the analytic infinite-dimensional proof.

## originality

PASS

Best-of-knowledge PASS for the genuinely new high-contrast sharp tracial constant, not for the already-covered low-contrast case. Sababheh--Bourin arXiv:2610.04567v1 Theorem 6.1 proves the sharp Loewner-order coefficient min(d_t,L-d_t)/(a-b)^2 and Corollary 6.2 its trace consequence, while Remark 6.3 explicitly declines a claim of trace optimality. The submitted tracial coefficient min(d_t,L/2)/(a-b)^2 agrees when d_t<=L/2 but is strictly higher for d_t>L/2, with rank-one noncommuting sharpness. The trace-optimal phase is not implied by the earlier Loewner inequality. Fresh broader norm, Heinz, and published-record searches found no decisive mathematically covering result. Gaps in older full-text access and possible implicit projection-angle identities are retained as priority risks, not treated as proof of novelty.

## value

PASS

The natural trace-optimal quadratic stability question arises directly because the closest sharp Loewner predecessor expressly leaves trace optimality unclaimed. The result determines a complete exact sharp universal constant over a natural projection-pair family, including a nontrivial high-contrast phase and an unbounded asymptotic separation between order and trace coefficients. The polar-sign spectral reflection extends the extremal calculation to continuous-spectrum projection pairs in finite tracial vN algebras; both phases have exact low-dimensional sharp witnesses. Unlike a routine renaming of the known Loewner bound, the high-contrast coefficient is strictly stronger and mathematically motivated; no generalization to unconstrained positive operators or unrelated symmetric norms is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
