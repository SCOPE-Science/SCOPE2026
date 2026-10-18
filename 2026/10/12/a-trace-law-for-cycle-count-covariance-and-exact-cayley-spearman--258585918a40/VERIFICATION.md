---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Condition on Pi(i)=j. If j=i there is a fixed-point cycle and a uniform S_(n-1) complement, yielding 1+H_(n-1); if j!=i contract the forced directed edge, preserving cycle count and giving H_(n-1). Thus Cov(C,1_{Pi(i)=j})=(n-1)/n^2 on the diagonal, -1/n^2 off it. Summing proves the universal trace law. Plugging a_ij=(i-j)^2 gives Cov(C,D)=-(n^2-1)/6; Bernoulli-cycle variance H_n-H_n^(2) and permutation Spearman variance 1/(n-1) give exact correlation and decay. Independently enumerated all permutations n=2..6 for a non-symmetric polynomial array and D.

## originality

PASS

The elementary indicator contraction identity supplies a universal finite-array covariance and exact Cayley–Spearman coefficient; the inspected Jiang article gives a broader asymptotic independence framework but not these finite values. A general Ewens/permutation character identity may imply the trace formula and is a specific novelty risk.

## value

PASS

A finite-sample, arbitrary-array covariance functional is a useful exact structural statement for ranking and matching statistics, and the full Cayley–Spearman correlation quantifies the rate only suggested by asymptotic metric-independence theory. This is more than repeating a one-variable expectation or reporting a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
