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
The all-\(n\) proof is given in `RESULT.md`.

Critical checks:
- cycle vertices are exactly stable-set incidence vectors for even \(n\), and those vectors plus \(\mathbf1/2\) for odd \(n\);
- a stable-set vertex of size \(k\) has squared distance
  \[
  ns^2+k(1-2s)
  \]
  from \(s\mathbf1\);
- for even \(n\), the unique minimax center is \(\mathbf1/2\) with squared radius \(n/4\), and every stable-set vertex is tangent;
- for odd \(n\), with \(\alpha=(n-1)/2\), the unique minimax center is \(\alpha\mathbf1/n\) with squared radius \((n^2-1)/(4n)\);
- the \(n\) maximum stable sets average to the odd center, giving a global minimum-enclosing-ball certificate;
- the odd fractional vertex has squared distance \(1/(4n)\), hence is strictly interior;
- odd stable-set vertices lie on shells \((\alpha^2+k)/n\).

`verify.py` reconstructs the halfspace polytope for \(3\le n\le12\), checks the complete vertex list against direct halfspace intersection, verifies all closed formulas, and independently solves the full ambient minimum-enclosing-ball epigraph problem for \(3\le n\le9\). Finite computation is corroborative only and does not assess originality.
