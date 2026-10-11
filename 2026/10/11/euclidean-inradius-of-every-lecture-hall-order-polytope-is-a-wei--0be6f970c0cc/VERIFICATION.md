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
The theorem is proved symbolically in `RESULT.md`; finite computation is corroborative only.

Critical checks:
- The diagonal lecture-hall scaling takes the polytope to an ordinary order polytope, so the irredundant halfspaces are indexed by minimal elements, maximal elements, and covers.
- A cover \(i\prec j\) has Euclidean normal \(s_j e_i-s_i e_j\), and dividing its norm by \(s_is_j\) gives the edge weight \(\sqrt{s_i^{-2}+s_j^{-2}}\).
- Summing ball-distance inequalities along any augmented maximal chain telescopes exactly to \(1\ge r\ell(\gamma)\).
- The longest-prefix construction satisfies every forward edge inequality and every maximal-element upper boundary.
- The longest-suffix construction satisfies every reverse edge inequality and every minimal-element lower boundary.
- Every optimal center lies between the prefix and suffix path bounds coordinatewise, so equality for every element is equivalent to uniqueness.
- Setting every \(s_i=1\) recovers the ordinary-order formula \(1/(2+(h-1)\sqrt2)\).
- Taking \(P\) to be a chain gives the displayed lecture-hall-simplex formula.

`verify.py` enumerates maximal chains for representative weighted Hasse diagrams, compares enumeration with dynamic programming, and checks both explicit center constructions against every facet-distance constraint. It does not assess originality.
