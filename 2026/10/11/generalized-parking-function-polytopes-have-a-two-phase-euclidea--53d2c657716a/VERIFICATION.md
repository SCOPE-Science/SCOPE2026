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
- the source facet offsets for a size-\(k\) subset are \(U_k=k(a+b(n-(k+1)/2))\);
- a size-\(k\) facet normal has Euclidean norm \(\sqrt k\);
- symmetry averaging reduces global feasibility to diagonal centers;
- the lower/upper intersection value is \(r_k=(U_k-k)/(k+\sqrt k)\);
- the continuous \(k\)-profile has a strictly decreasing derivative numerator after \(y=\sqrt k\), hence only endpoint sizes can minimize;
- comparing the two endpoints gives the phase boundary \(a-1=b(\sqrt n+1)\);
- the active shifted facets force the unique center \((1+r)\mathbf1\);
- strict unimodality away from the endpoints gives the exact tangent-facet classes.

`verify.py` checks many parameter triples by evaluating every facet-size threshold and, in small dimensions, independently solving the full Chebyshev linear program containing every source facet with `scipy.optimize.linprog`. Finite computation is corroborative only and does not assess originality.
