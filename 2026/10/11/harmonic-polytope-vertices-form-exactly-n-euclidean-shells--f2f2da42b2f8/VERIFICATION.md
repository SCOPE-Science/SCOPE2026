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
- the published vertex is \(e_k+f_k+(\pi_1^{-1},0)+(0,\pi_2^{-1})\);
- the source's three classes \(a,b,c\) satisfy \(a+b+c=n-1\);
- the distinguished positions satisfy \(p+q=n+1+b\);
- a permutation of \(1,\ldots,n\) has centered squared norm \(n(n^2-1)/12\);
- shell \(b\) has squared radius \(n(n^2-1)/6+2(n-1)/n+2b\);
- every \(b=0,\ldots,n-1\) occurs and shell squares differ by \(2\);
- grouping the source enumeration at fixed \(b\) gives the displayed multiplicity;
- the outer shell is exactly \(b=n-1\), with \(n((n-1)!)^2\) vertices;
- the outer-shell barycenter is the uniform affine point;
- the parallel-axis average proves the exact minimum enclosing radius and center uniqueness.

`verify.py` enumerates all fine harmonic triples for \(2\le n\le5\) and checks the shell index, exact squared radius, shell multiplicities, total source vertex count, outer contact count, and outer-shell barycenter. Finite computation is corroborative only and does not assess originality.
