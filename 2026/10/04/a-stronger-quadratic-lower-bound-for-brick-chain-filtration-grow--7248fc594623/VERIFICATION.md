---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The verifier `artifacts/verify.py` performs the following finite consistency checks:

- It computes the hook product of the \(2n\)-by-\(n\) rectangle directly from all cells and compares it with \(\prod_{j=0}^{n-1}(2n+j)!/j!\) for \(1\le n\le10\).
- It checks that \(q=7\), \(a=2n\), and \(b=n\) give dimension vector \((8n,3n)\) and composition length \(11n\) for \(1\le n\le20\).
- It evaluates \((4+8\log2-7\log3)/121\), compares it with the source endpoint, and reports exact finite-\(n\) lower-bound ratios using logarithms of factorials.
- The successful run ends with `CHECK_OK`.

The finite checks do not prove the infinite asymptotic claim. That claim uses the exact source inequality, the exact hook-product identity, Stirling's formula, and the displayed Riemann-sum estimate. No external or independent audit has been performed.
