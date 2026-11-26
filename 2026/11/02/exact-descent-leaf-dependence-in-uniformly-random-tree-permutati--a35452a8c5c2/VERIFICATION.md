---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Under the published bijective insertion code, I1 replaces the old last comparison by an ascent and then a descent; I2 leaves earlier comparisons unchanged and appends an ascent. Starting with the descent in (2,1), the extra descents are exactly the 01 transitions for the specified bit convention. Independently, each graph insertion keeps one of the current maximum/last vertices, replaces the other member of that active pair by a new leaf attached to the kept vertex, and leaves the old displaced vertex in the graph. After the first insertion the kept vertex has degree at least two and the new active vertex has degree one. Repeating an operation increases the leaf count by one; switching keeps it unchanged. This gives L=n−1−N01−N10 and agrees with the cited run formula. Hence 2D+L−n−1=b_last−b_first. The first bit and the change indicators form a bijective recoding into uniform independent bits; the first bit remains fair given the count T, giving exactly the displayed even/odd conditional law. The conditional mean is 1+T/2, the conditional variance is 1/4 on odd T and zero otherwise; fair parity for n≥4 gives the stated variance, covariance and correlation. For n=3 both variables are constant. The bounded endpoint error and the binomial CLT give the stated singular limit. The stated descent marginal follows also by adjoining an initial 1 and terminal 0: D=d then corresponds to choosing 2d−1 switch locations among n−1.

## originality

PASS

The insertion code, run formula for leaves and leaf marginal are established prior results. The inspected matching work does not state or give a formula for the joint law of adjacent descents and graph leaves. The supported distinct claim is the exact coupling, not the binomial leaf law or the code itself.

## value

PASS

Adjacent descents are a natural permutation statistic and leaves are a natural graph statistic for the same combinatorial object. The exact coupling relates permutation order to graph structure: for each leaf count, the descent count is fixed or supported on exactly two consecutive integers with equal mass. The bounded deterministic defect and the rank-one joint limit capture dependence that neither a marginal CLT nor the published leaf law provides.

The dated certificate retains the supplied scientific assessment, sources and limitations.
