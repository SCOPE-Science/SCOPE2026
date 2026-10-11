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
The all-parameter proof is given in `RESULT.md`.

Critical checks:
- Euclidean diameter endpoints are vertices;
- a source vertex with \(k\) nonzero coordinates uses exactly \(n,n-1,\ldots,n-k+1\);
- coordinatewise,
  \[
  (u_i-v_i)^2\le\max\{u_i^2,v_i^2\};
  \]
- therefore every squared diameter is bounded by the sum of the largest \(s=\min\{m,2n\}\) entries of two copies of
  \[
  n^2,(n-1)^2,\ldots,1;
  \]
- balancing the two prefix lengths gives \(a=\lfloor s/2\rfloor\) and \(b=\lceil s/2\rceil\);
- disjoint supports attain the bound;
- equality in the coordinate inequality forces disjoint supports, and equality in the doubled-spectrum bound forces exactly the stated value sets;
- for \(m\ge2n\), both endpoints use every positive value and the diameter is independent of further coordinates.

`verify.py` exhaustively generates all source vertices for \(1\le m,n\le5\), checks every pair, confirms the closed formula, and verifies the equality classification for every maximizing pair. Finite enumeration is corroborative only and does not assess originality.
