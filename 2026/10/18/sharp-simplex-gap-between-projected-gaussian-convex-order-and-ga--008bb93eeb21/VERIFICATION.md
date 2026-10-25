---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The scalar Gaussian-mixture convex-order criterion is exactly t≤E R, by Jensen plus |x| test. The regular-simplex frame identifies zero-sum projected vectors, and the sharp norm inequality sum |a_i|≥sqrt(2 sum a_i²) attained on two entries proves projected threshold sqrt[2/d(d+1)]. Any jointly Gaussian rank-one coupling has scalar correlation C PSD diag1; the trace bound tr Cov(mean)=(n²-1^T C 1)/(d n²)≤1/d forces s≤1/d. Correlation C=V^T V attains I/d², and trace equality plus Gram projectors gives rigidity. Verified exact rational Gram, trace, projection identities d=2..10. It does NOT claim that actual multivariate convex order fails.

## originality

PASS

Jourdain–Pagès provides the general projection necessary criterion and Gaussian-block sufficient coupling idea; Guéant proves a two-component equivalence and highlights larger-mixture difficulty. Those frameworks do not give this all-d regular-simplex exact pair of thresholds and rigidity. The later three-component asymmetric example tests full multivariate order, which is explicitly not the assertion assessed here.

## value

PASS

A sharp quantified separation between necessary projected tests and a natural sufficient joint Gaussian coupling is a motivated benchmark for multi-component Gaussian-mixture convex comparison; exact rigidity of the endpoint coupling is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
