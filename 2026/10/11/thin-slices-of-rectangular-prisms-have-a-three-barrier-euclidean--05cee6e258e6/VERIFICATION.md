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
- \(R_{k,\mathbf c}\) has affine hull \(\sum_i x_i=k\);
- the projection of \(e_i\) to its translation space has norm \(\sqrt{(n-1)/n}\);
- \(x_i=0\) is a facet exactly when \(k<C-c_i\), and \(x_i=c_i\) is a facet exactly when \(k>c_i\);
- if \(k/n\) is a smallest barrier, all lower coordinate facets occur;
- if \((C-k)/n\) is a smallest barrier, all upper coordinate facets occur;
- if \(c_{\min}/2\) is a smallest barrier, both opposite facets for a minimum-capacity coordinate occur;
- the interval-sum criterion constructs a center with coordinate clearance \(\delta_*\);
- the complete incenter set is exactly the shifted system for the actual facets.

`verify.py` independently formulates the coordinate-clearance Chebyshev linear program from the actual facet list and solves it by active-set enumeration for deterministic capacity vectors in dimensions three and four. It compares the LP optimum with \(\min\{k/n,(C-k)/n,c_{\min}/2\}\) and checks the facet classification. Finite computation is corroborative only and does not assess originality.
