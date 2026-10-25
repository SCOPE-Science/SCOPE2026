---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The scalar activation is finitely piecewise affine, hence each image cell has linear part DW/(2rho), rank at most rank W; a small open input cell near zero activates all slopes, giving matching lower image dimension. If F(X) is on the Perron ray, differentiating at zero along every input coordinate forces each column W e_j into span v, so rank W=1. Conversely rank-one positive W= rho v q^T/(q^T v) gives F(x)=v ~tilde g(q^T x/(q^T v)), and on the ray F(tv)=v g(t). Original Gaivao--Pires Lemma 6 gives monotone semiconjugacy h with irrational rotation T and singleton discontinuity preimage; the branch indicator agrees pointwise. Subtract g(t)=t/2+delta-I(t), h(g(t))=h(t)+alpha-I(t) to obtain t-2(delta-alpha)=H(t)-H(g(t)), H=2(t-h(t)), osc H<=2 by monotonicity. All rank-one network sums telescope. Irrationality excludes periodic points; a.e.-one-to-one monotone semiconjugacy plus uniquely ergodic rotation gives one invariant probability. Analytic checks do not depend on finite checker.

## originality

PASS

Pires proves persistence of a Cantor set on an invariant Perron ray for arbitrary positive W, not a criterion for universal one-step collapse or equality of image dimension and rank; Gaivao--Pires supplies the scalar semiconjugacy. These results are incorporated explicitly, not rebranded. The exact network-wide rank criterion and uniform all-initial-data population discrepancy combine the old scalar dynamics with a nontrivial global coupling classification.

## value

PASS

The rank-vs-image dimension and exact synchronization threshold classify how much of the full n-dimensional state survives the first network step, a structural question not settled by invariant-ray existence. The global bounded total-activation discrepancy at rank one supplies a sharp strong quantitative trajectory consequence. Though the scalar coboundary identity is short once the semiconjugacy is known, the complete network-level boundary has independent interpretive use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
