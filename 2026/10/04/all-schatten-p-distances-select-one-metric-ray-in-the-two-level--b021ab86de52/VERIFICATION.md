---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Writing \(t=(C_1+C_2)/2\) and \(u=(C_1-C_2)/(C_1+C_2)\) gives metric eigenvalues \(t(1\pm r)\), where \(r=\sqrt{s^2+(1-s^2)u^2}\ge s\), with equality exactly at \(C_1=C_2\). For fixed \(r\), strict convexity for \(1<p<\infty\) gives the stated unique \(t_p(r)\), and substitution gives \(m_p(r)=2r/((1+r)^q+(1-r)^q)^{1/q}\). Its logarithmic derivative reduces to a strictly positive numerator, so the global optimum is uniquely at \(r=s\). The piecewise-linear \(p=1\) case and equioscillation \(p=\infty\) case similarly have unique fixed-\(r\) optima and increasing minima. The \(s=0\) boundary is included and still yields the unique identity metric. Independent numerical rechecks reproduced the formulas on representative \(s,p\) values.

## originality

PASS

The 2018 primary paper was inspected in full. It solves the Hilbert--Schmidt criterion, gives the two-level equal-coefficient optimizer there, and explicitly suggests analogous minimizations in other Schatten classes, including operator norm, but does not give the all-\(p\) formulas or ray-invariance theorem. Searches for the same two-vector/Schatten approximation statement found no prior equivalent theorem.

## value

PASS

The theorem closes an explicit family of alternative metric-selection problems raised by the motivating paper and reveals a structural invariant—the selected positive ray is independent of Schatten index—even though the normalization changes. This is a natural complete two-level classification rather than a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
