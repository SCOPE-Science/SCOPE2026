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
# Verification instructions and limits

Execute `python3 verify_hexagon.py` in any Python 3 environment. Only standard-library modules are required. It enumerates the exact outward support halfplanes corresponding to all vertex-chord directions for the displayed integral affine-regular hexagon. For every subset of three and four distinct halfplanes, it calculates the intersection with the fixed enclosing rational square using exact fractions. Of the 715 cases, the least intersection area is exactly \(4\). Any chord triangle or quadrilateral can be tightened onto these supporting lines, and clipping cannot increase area. Thus the exact finite check supplies a valid exhaustive lower bound for this **one** reference polygon, independent of the symbolic general-hexagon proof.

The main theorem for the continuum of all centrally symmetric hexagons follows analytically from the three-generator zonotope area decomposition, the two-dimensional coordinate-width formula, and the sorted-determinant inequality. It is not inferred from random finite sampling. Reproducible arithmetic checks do not establish novelty or independent review. Independent audit is not performed.
