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

# Finite exact verification record

The graph is the twelve-vertex two-pentagon model defined in `RESULT.md`. The two reproducible programs `verify_pairs.py` and `verify_cycles.py` use only Python 3 standard-library modules. They were executed from the package, and their compact JSON summary lines agree byte-for-byte. Their second lines are `ICOSAHEDRON_PAIRS_PASS` and `ICOSAHEDRON_CYCLES_PASS`, respectively.

`verify_pairs.py` recursively enumerates all complete vertex pairings along graph edges, tests the symmetric difference of each pair of distinct perfect matchings for exactly one alternating cycle, and breadth-first searches the resulting flip graphs. `verify_cycles.py` instead tests every six-element subset of the thirty graph edges, generates each short simple cycle, explicitly flips alternating edge parities, and repeats component and distance computations. Both independently certify the same three canonical SHA-256 digests of the complete matching, four-flip, and six-flip edge listings stored in the package.

The exhaustive conclusions are 125 perfect matchings, 300 four-flip edges, a 120-vertex four-flip component and five isolated states, 580 six-flip edges, connected six-flip graph of radius three and diameter four, and exactly five six-flip centers equal to those five isolated four-flip states. The four-flip large component has radius five and diameter six. The fixed labeled graph and the cycle-length restrictions are essential; graph-specific enumeration does not prove a general graph-family theorem. No independent external audit is asserted.
