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

# Verification of exact ordered-clique-tree inverse law

The exact unweighted-star Schur complement and the actual one-tree sampling weights follow directly from the published algorithm normalization in [1, Algorithm 3]. The proof in `RESULT.md` uses no numerical approximations: an exact backwards pendant-edge resistance induction for every integer \(n\ge2\), followed by the standard resistance-matrix double-centering identity. The last-edge spectral consequence is an exact Rayleigh quotient.

Run `python3 verify.py` (Python 3 standard library, no external dependencies). For every \(2\le n\le8\), the checker enumerates all \((n-1)!\) possible increasing-parent maps, for 5,913 total weighted trees. Exact `Fraction` arithmetic verifies every mean edge coefficient equals \(1/n\), every mean pairwise resistance equals \(n\), the deterministic resistance of the final leaf pair, and every entry of the double-centered expected pseudoinverse equals \((n/2)P\). The checker was successfully executed from the same packaged path used for the artifact.

Finite exhaustive checks are finite evidence only; they do not establish the result for larger \(n\). The unbounded theorem rests on the published sampling law, series resistance of trees, independence of parent choices and the mathematical induction. This does not verify global solver accuracy or another sampling distribution. Independent scientific audit remains unperformed.
