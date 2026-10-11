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
The arbitrary-graph proof is given in `RESULT.md`.

Critical checks:
- the source layer function satisfies \(\ell(h)-\ell(t)=1\) on every root vertex;
- connected semi-balanced root polytopes have affine dimension \(|V|-2\);
- the affine hull is therefore the intersection of the zero-sum hyperplane with \(\langle\ell,x\rangle=1\);
- \(c=\ell_0/\|\ell_0\|^2\) is the orthogonal projection of the ambient origin onto that affine hull;
- every root vertex has squared distance \(2-1/\|\ell_0\|^2\) from \(c\);
- a common vertex sphere is minimum enclosing exactly when its center lies in the convex hull of its contact vertices;
- root-polytope convex-hull membership of \(c\) is exactly the nonnegative edge-flow equation;
- in the standard bipartite orientation this is equivalent to uniform marginals and, by max-flow/min-cut, to the proportional Hall inequalities;
- uniform edge weights certify the condition for every biregular bipartite graph.

`verify.py` checks the projection and radius identities on several multi-layer semi-balanced examples and exhaustively checks every connected bipartite graph with part sizes at most four for equivalence between the proportional Hall inequalities and the corresponding integral max-flow feasibility after scaling. Finite computation is corroborative only and does not assess originality.
