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
- the primary source gives
  \[
  \operatorname{Newton}(F)
  =
  \operatorname{conv}\bigcup_{i=0}^m
  \operatorname{Newton}(s_{\lambda^{(i)}});
  \]
- each Schur Newton polytope is the convex hull of the coordinate-permutation orbit of its partition;
- uniqueness plus \(S_m\)-invariance forces the minimum-enclosing center to \(c\mathbf1\);
- consecutive layer squared radii satisfy
  \[
  R_i(c)^2-R_{i-1}(c)^2
  =
  2(\beta_i-\alpha_i)(h_i-c);
  \]
- ordered partition midpoints imply
  \[
  \max_iR_i(c)^2
  =
  \sum_j\max\{(\alpha_j-c)^2,(\beta_j-c)^2\};
  \]
- the resulting scalar objective is strongly convex;
- on each interval \(h_{i+1}\le c\le h_i\), its unconstrained minimizer is the layer mean \(c_i\), giving the exact mean-or-boundary scan;
- boundary contacts are exactly the active source permutation orbits.

`verify.py` uses exact rational arithmetic for the scan. For deterministic examples it independently expands every distinct permutation of every source layer and solves the full ambient-space minimum-enclosing-ball problem numerically. The returned center and radius agree with the exact formula. Finite computation is corroborative only and does not assess originality.
