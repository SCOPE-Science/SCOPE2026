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
The arbitrary-dimensional proof is given in `RESULT.md`.

Critical checks:
- the affine equation is \(\sum_i x_i=3^{n+1}\);
- every source facet has coefficient pattern \(1,2,\ldots,k-1,k,\ldots,k\);
- the source support value is the stated \(\kappa(k,l)\);
- intrinsic projected-normal squared norm is \(Q-W^2/(n+1)\);
- the singleton facets have exact distance \(\bigl(3^{n+1}-3(n+1)\bigr)/\sqrt{n(n+1)}\);
- every non-singleton facet is strictly farther;
- only five small ambient/support pairs escape the uniform coarse inequality, and their exact rational squared-distance certificates are positive;
- singleton constraints give a matching universal radius upper bound and force the center uniquely.

`verify.py` reproduces the five exact finite certificates and exhaustively checks every facet parameter for \(2\le n\le60\) using exact rational squared-distance comparisons. The finite replay is corroborative only and does not replace the arbitrary-dimensional proof or assess originality.
