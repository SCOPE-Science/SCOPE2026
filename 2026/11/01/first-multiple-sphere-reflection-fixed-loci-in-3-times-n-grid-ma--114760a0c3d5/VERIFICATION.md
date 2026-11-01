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

The executable `verify_reflection_homotopy.py` uses Python 3 alone. Run `python verify_reflection_homotopy.py` in the directory containing it.

The verifier constructs full reflected graph-edge orbits and checks the matching-compatibility graph against the explicitly specified whiskered half-grid for widths 2 through 10. It recursively enumerates every nonempty simplicial face, implements all Morse matching pairs, counts residual critical cells, and explicitly constructs and topologically sorts every directed Hasse cover. In order of half-width \(m=1,2,3,4,5\), the face counts are \(11,66,426,2635,16402\), the directed cover counts are \(13,144,1378,10976,83597\), and the critical-cell vectors are \(\{0:1\}\), \(\{0:1,2:1\}\), \(\{0:1,3:1\}\), \(\{0:1,4:4\}\), \(\{0:1,5:11\}\). Replayed computation terminates in `VERIFY_OK`.

The homeomorphism between fixed points of the realization and the orbit complex is proved in RESULT.md from barycentric coordinates. The wedge conclusions follow from the verified acyclic matching via the standard discrete-Morse CW theorem. The certificates prove only the five specified widths, and the full text of one recent matching-grid preprint remains inaccessible for comprehensive literature comparison.
