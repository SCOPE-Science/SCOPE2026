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
The theorem is proved symbolically in `RESULT.md`; finite computation is not used as an infinite proof.

Verified premises and steps:
- The standard \(n\)-stellohedron is the Minkowski sum of the coordinate simplices \(\Delta_{\{0\}\cup S}\) over all nonempty \(S\subseteq[n]\).
- Its facet set consists exactly of proper center-containing tubes together with leaf singletons.
- A tube of size \(k\) containing the center has offset \(2^{k-1}-1\); every singleton has offset \(0\).
- The projected singleton normal has squared norm \(n/(n+1)\), so summing all singleton radius constraints yields the sharp upper bound and forces the unique uniform center.
- A size-\(k\) tube normal has squared norm \(k(n+1-k)/(n+1)\).
- Monotonicity of \((2^{j-1}-1)/(j(j-1))\) proves every non-singleton facet is at least as far from the uniform center as a singleton facet.
- Equality is strict for all non-singleton facets when \(n\ge3\); when \(n=2\), the two size-\(2\) facets also attain equality.

`verify.py` checks the exact integer inequality and numerical distance identities for dimensions \(2\) through \(100\). It does not assess originality.
