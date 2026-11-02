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

# Verification and reproducibility

This package includes `verify_support.py`, `verify_support.txt`, `verify_logic.py`, and `verify_logic.txt`.
Run the programs with Python 3, without external packages, in the directory containing the files. Each program uses exact deterministic finite computations and assertions.

- `verify_support.py` generates 15 mixed-factor products with alphabet sizes 2, 3, 4, and 5. It enumerates all third vertices above every ordered anchor pair (5,670 pairs) and compares the complete four-component colored-distance profile to a separately constructed coordinate-option dynamic program. Every comparison passes. These checks exercise equal anchors, nonadjacent anchors, binary factors, and nonbinary factors.
- `verify_logic.py` constructs unlabelled graphs and computes stabilized noncounting three-variable logical types on ordered triples. At each refinement step it records the *set*, not the multiset, of possible colors obtained by quantifying each variable, and canonicalizes colors across both structures in a comparison. All 12 predicted equivalent/inequivalent comparisons pass. The largest graph in these paired comparisons has 24 vertices.

These finite checks corroborate the local extension lemma and fixed-point logical consequence. The universal quantification over all finite parameter vectors is established by the proof's coordinate-independence and permanent three-pebble strategy, not finite enumeration. The four-variable separation uses the explicit four-clique formula and needs no numerical experiment. No independent mathematical review has been performed.
