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
- the vectors \(e_i-e_{i+1}\) form a basis of the zero-sum hyperplane;
- each facet sign vector \(\varepsilon\) has the unique normal satisfying
  \[
  x_i^\varepsilon-x_{i+1}^\varepsilon=\varepsilon_i;
  \]
- the zero-sum variance identity gives
  \[
  \|x^\varepsilon\|^2
  =
  \frac1n\sum_{p<q}
  \left(\sum_{k=p}^{q-1}\varepsilon_k\right)^2;
  \]
- every signed interval sum has absolute value at most its length;
- summing the squared interval lengths gives
  \[
  \frac{n(n^2-1)}{12};
  \]
- equality occurs exactly for the two constant sign vectors;
- their opposite supporting hyperplanes force every inscribed ball to have radius at most
  \[
  \sqrt{\frac{12}{n(n^2-1)}};
  \]
- strict slack for all other facets gives a relative neighborhood of incenter locations in a subspace of dimension \(n-2\);
- every vertex has norm \(\sqrt2\), and averaging squared distances over each opposite vertex pair proves the unique minimum enclosing sphere.

`verify.py` exhaustively enumerates every facet sign vector for \(2\le n\le11\), reconstructs the exact rational facet normals, checks the variance identity and equality cases, verifies the closed inner and outer radius formulas, and checks the expected codimension-one affine constraint. Finite computation is corroborative only and does not assess originality.
