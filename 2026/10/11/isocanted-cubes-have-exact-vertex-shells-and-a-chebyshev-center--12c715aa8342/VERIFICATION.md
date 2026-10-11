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
The arbitrary-parameter proof is given in `RESULT.md`.

Critical checks:
- the centered source inequalities are \(|x_i|\le\ell/2\) and \(|x_i-x_j|\le\ell-a\);
- every source-labeled vertex translates to \(k\) coordinates \(\ell/2\) and \(d-k\) coordinates \(a-\ell/2\), or its antipode;
- shell \(k\) has squared radius \(k\ell^2/4+(d-k)(\ell/2-a)^2\) and multiplicity \(2\binom dk\);
- adjacent shell squares differ by \(a(\ell-a)>0\);
- the two pole vertices uniquely certify minimum-enclosing radius \(\ell\sqrt d/2\);
- coordinate-facet clearance is \(\ell/2-|z_i|\);
- difference-facet clearance is \((\ell-a-|z_i-z_j|)/\sqrt2\);
- the two centered clearances cross exactly at \(a=\ell(1-1/\sqrt2)\);
- below and at the threshold the optimum center is uniquely \(0\);
- above the threshold the entire optimal-center set is the stated diagonal segment.

`verify.py` enumerates all source-labeled vertices for \(2\le d\le8\) at several rational parameter pairs. It verifies the defining inequalities, all shell formulas and multiplicities, strict shell ordering, and tightness of every facet family. It also checks the threshold and center-regime identities exactly with symbolic radicals. Finite computation is corroborative only and does not assess originality.
