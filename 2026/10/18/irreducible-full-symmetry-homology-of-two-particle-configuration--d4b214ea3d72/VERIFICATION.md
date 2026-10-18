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

Run `python3 verify.py` with standard Python 3. This file is a complete implementation of signed cellular matrices for unordered two-point configurations of complete bipartite graphs. No third-party libraries or external data are required. It checks integer boundary-composition zero on every square and computes modular ranks and actual signed kernel-action traces modulo 1009. It does not infer a rational theorem from finite-field data: the all-sizes proof is in `RESULT.md`.

The test dimensions and computed \(\beta_2\) values are \((3,3):0\), \((3,4):2\), \((3,5):5\), \((4,4):12\), \((4,5):27\), \((5,5):60\), and \((5,6):104\). Direct signed cycle-trace comparisons for all side permutations were performed on \((3,3),(3,4),(4,4),(4,5)\). All side-exchange elements of the balanced examples \((3,3),(4,4)\) were checked too, for 4,248 comparisons in total. The code checks the exact chain relation before computing any ranks, and explicitly compares predicted traces to those induced on the degree-two cycle kernel.

Limitations: computations modulo a prime do not prove characteristic-zero rank in general, rational semisimplicity in arbitrary size, or novelty. Those claims instead rely on the mathematical argument and primary literature comparison. The degree-two group character does not itself specify an integral lattice. No independent audit has been performed.
