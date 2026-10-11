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
The arbitrary-arc proof is given in `RESULT.md`.

Critical checks:
- the source vertices are alternating matching vectors with the same number of \(+1\) and \(-1\) coordinates;
- the canonical center has coordinate \(q/m\) on \(U\) and \(-p/m\) on \(D\);
- exact expansion gives common squared radius \(pq/m\);
- orthogonal projection of a common-sphere center onto the convex hull gives squared minimum radius \(R_0^2-d^2\);
- the source H-description and all-prefix consequence give \(c_\alpha\in\mathrm{SP}(\alpha)\) exactly when \(0\le q u_j-p d_j\le m\) for every proper prefix;
- after translation by \(\mathbf1_D\), every active vertex is a \(0/1\) vector of weight \(q\);
- the uniform-density theorem identifies constant-coordinate membership with uniform density of the active shard matroid.

`verify.py` exhaustively checks all ordinary arc words of lengths \(2\) through \(10\). It enumerates all alternating matchings, verifies the common-sphere identity with exact rational arithmetic, checks equivalence between the all-prefix strip and the source rise/fall facet conditions for the canonical center, verifies translated weight \(q\), and checks the monotone-word criterion. Finite computation is corroborative only and does not assess originality.
