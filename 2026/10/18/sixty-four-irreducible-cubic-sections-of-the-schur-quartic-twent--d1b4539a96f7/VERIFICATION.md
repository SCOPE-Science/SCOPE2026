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

# Exact verification
The accompanying Python 3 standard-library script `verify_schur_cubics.py` accepts no inputs and uses the explicit 24 line parametrizations and 32 triple incidences from the published source. Run `python3 verify_schur_cubics.py` in a directory containing this file.

The script recomputes the five quartic-restriction coefficients for each line, all 276 pairwise determinants in \(\mathbb Q(\sqrt{-3})\), 32 genuine concurrent and distinct triple points, all four-vertex clique exclusions, the Gram determinant and Smith invariants, exact integral spanning relations, the index-three hyperplane class, and every binary choice on the eight free coordinates. It confirms 64 valid solutions and 32 complement pairs, without statistical inference or floating point.

Logical ingredients not reducible to finite computation are the Hodge index theorem on smooth complex K3 surfaces, coincidence of linear with numerical divisor equivalence there, the quartic restriction sequence for cubic sections, and the elementary fact that a reducible cubic hypersurface over an algebraically closed field has a linear factor. The published line table specifies the objects; the script independently checks the nontrivial incidence premises.

No claim is made about singularities of the 64 cubic surfaces, all cubic sections of the Schur quartic, or primitivity in the full Néron--Severi group. Literature overlap remains subject to the access limitations explained in the accompanying review. Independent audit has not been performed.
