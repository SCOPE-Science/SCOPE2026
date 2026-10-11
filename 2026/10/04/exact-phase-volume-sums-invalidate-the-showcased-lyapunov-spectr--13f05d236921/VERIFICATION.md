---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The printed uncontrolled Jacobian has constant trace \(c-a-b\), so Liouville fixes the finite-time determinant growth and hence the sum of finite-time singular-value growth rates; any asymptotic Lyapunov spectrum must have the same sum. At \(a=40,b=2,c=22\) the exact sum is \(-20\). Exact decimal addition reproduces source sums \(20.5159,22.3152,24.3169\). Adding diagonal feedback shifts the trace by \(r_1+r_2+r_3+r_4\), giving required sums \(-120\) and \(-140\), versus the printed \(-62.6296\) and \(-82.0194\). The finite QR replay is supporting evidence only.

## originality

PASS

The primary 2023 article contains the equations and all five exponent vectors but does not perform the constant-divergence Lyapunov-sum check. Exact-number, DOI/title, correction, divergence and Liouville searches surfaced the source and later citations but no prior publication stating the five-case inconsistency. The Liouville determinant theorem is classical background, but no inspected source had already combined it with these published numerical vectors.

## value

PASS

Although the decisive test is a standard trace/Liouville identity, it is substantively motivated: all five spectra are central quantitative diagnostics for the source’s hyperchaos/control discussion and every one is impossible for the printed equations, with very large sum discrepancies. This is a meaningful published-data consistency correction, not an arbitrary normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
