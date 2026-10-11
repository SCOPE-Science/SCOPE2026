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
- the published stack-sorting iteration formula gives exactly the vertices \(v_k\);
- the vectors \(d_k=v_k-v_1\) have pairwise zero dot products and squared norms \(k(k-1)\);
- the simplex becomes \(t_k\ge0\), \(\sum t_k/\sqrt{k(k-1)}\le1\) in an orthonormal basis;
- \(\sum_{k=2}^n1/(k(k-1))=(n-1)/n\), yielding the exact inradius;
- the all-vertex sphere has squared radius \(n(n^2-1)/12\);
- the integer \(q\) is characterized by \(q(q-1)<2n\le q(q+1)\);
- the minimum-sphere weights are positive and sum to \(1\);
- active vertices are equidistant and every inactive vertex lies weakly inside;
- the positive contact weights certify global minimum-enclosing optimality and uniqueness;
- the predecessor becomes an additional contact exactly when \(2n=q(q+1)\).

`verify.py` checks \(3\le n\le100\) using exact integer and rational arithmetic for the edge and minimum-sphere identities, together with floating evaluation only for the radical inradius clearances. Finite computation is corroborative only and does not assess originality.
