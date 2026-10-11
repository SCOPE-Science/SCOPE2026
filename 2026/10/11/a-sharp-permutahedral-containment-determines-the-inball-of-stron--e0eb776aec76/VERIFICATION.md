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
The theorem is proved symbolically in `RESULT.md`; finite enumeration is corroborative only.

Critical checks:
- Theorem 3 of the primary source supplies the affine equation and every nonempty proper subset-facet height.
- The interval-pair count has the exact run-length form
\[
2T_n-\sum_j\Phi_n(\ell_j)+\sum_j\ell_j\ell_{j+1}.
\]
- The merge identity
\[
\Phi_n(u+v)-\Phi_n(u)-\Phi_n(v)
=
\frac{uv(2n-2-u-v)}2
\]
proves the sharp cardinality lower bound and equality only for two-run words.
- The intrinsic normal of a cardinality-\(k\) subset facet has norm \(\sqrt{k(n-k)/n}\).
- The centered distance minimum is attained exactly by the four endpoint prefix/suffix facets.
- Opposite endpoint facets give the same radius as a universal upper bound.
- At the optimal radius they force center coordinates \(c_1=c_n=0\); all other facets have strict slack at the origin, so the incenter set has affine dimension \(n-3\).

`verify.py` checks every nonempty proper subset for \(3\le n\le14\). It directly recounts the source interval-pair formula, verifies the run identity, the sharp lower bound, all equality cases, and the four centered contact facets. It does not replace the arbitrary-rank proof and does not assess originality.
