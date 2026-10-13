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
# Verification

The theorem was checked from the p-morphism axioms rather than inferred from enumeration.

For a p-morphism \(f:\mathbf A_n\to\mathbf A_1\), maximal source points must map to maximal target points because the back condition would otherwise demand a strict source extension. Monotonicity forces every point mapped to a maximal target value to have all maximal completions of that color. Conversely, if all maximal completions have one color, the back condition excludes the root and monotonicity excludes the opposite maximal value. Mixed colors force the root. These implications prove uniqueness.

For the converse construction, extension of partial functions replaces \(M(x)\) by a subset, which proves monotonicity. In the mixed case, maximal completions of both colors explicitly witness the two nontrivial back-condition demands. Therefore every coloring produces a p-morphism.

The standalone checker `verify_p_morphisms.py` exhaustively tests all maps for \(n=1\) and \(n=2\) from the definitions. Its recorded output is:

`n=1: total=4, surjective=2`

`n=2: total=16, surjective=14`

`all finite sanity checks passed`

The finite check is not used to infer the theorem for arbitrary \(n\). No claim is made for target \(\mathbf A_m\) with \(m>1\).
