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
The arbitrary-\(n\) proof is given in `RESULT.md`.

Critical checks:
- the primary source gives the complete vertex set \(e_i-e_j\) for arrows \(i\to j\);
- for the transitive tournament, all vertices are \(e_i-e_j\) with \(i<j\);
- \(S_n=\sum_{i=1}^{n-1}i(n-i)=n(n^2-1)/6\);
- the weights \(i(n-i)/S_n\) are positive, sum to \(1\), and their simple-root barycenter is exactly
  \[
  c_n=S_n^{-1}(n-1,n-3,\ldots,1-n);
  \]
- \(\|c_n\|^2=2/S_n\);
- a vertex of gap \(d=j-i\) has squared distance
  \[
  2-\frac{4d-2}{S_n};
  \]
- the shell radius is strictly decreasing with \(d\), so the simple roots are exactly the contacts;
- the positive contact barycenter proves that no translated center can attain the same radius.

`verify.py` checks all algebraic identities exactly for \(3\le n\le100\). For \(3\le n\le9\), it independently solves the full ambient minimum-enclosing-ball epigraph problem over every vertex and compares the numerical center and radius with the exact formulas. Finite computation is corroborative only and does not assess originality.
