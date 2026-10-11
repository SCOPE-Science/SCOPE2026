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

# Reproducibility and limits

Run `python3 verify_morse.py` and `python3 verify_independent.py` in a directory containing the two supplied programs. Only the Python 3 standard library is required.

The first program reconstructs the 20-vertex, 30-edge dodecahedral graph and its 111376 matching masks including the empty mask, constructs an explicit acyclic Morse matching on the ordinary 111375 nonempty faces, counts 55626 pairs, and verifies all 666330 codimension-one incidences by topological sort. It checks the complete critical vector, including the one vertex, the five five-cells and the 117 six-cells, and calculates the zero signed Morse boundary matrix \(\partial_6\) of size \(5\times117\). Each cancellation is chosen only after counting unique directed gradient paths.

The second program uses a distinct vertex-deletion recurrence for the matching polynomial and an independent full augmented mod-two simplicial boundary computation. The resulting reduced homology ranks are 5 in degree 5 and 117 in degree 6. The mod-two computation alone does not certify integral torsion-freeness or the homotopy type; those follow from the explicit acyclic matching plus signed boundary analysis.

The computation and conclusion concern this fixed finite graph and the ordinary matching complex only. The bibliography search is not a proof of uniqueness, and an indexed prior mod-two source could not be read in full through the attempted retrieval paths. No independent audit or external certification is asserted.
