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

# Reproduction

Using Python 3.9 or newer from the extracted directory, run `python verify_morse.py` and `python verify_chains.py`. Both programs are independent, stand-alone implementations requiring no third-party packages.

The first checks all 16383 nonempty labeled vertex subsets against the complete forbidden-triple description, reconstructs all 2256 faces, determines the dimension-wise face vector, reproduces 1121 elementary matching pairs, and checks all 10150 oriented Hasse incidences for acyclicity by a complete topological sort. It confirms the critical vector consisting of one zero-cell and thirteen five-cells, and the reduced Lefschetz numbers \((-13,1,1,1,1,1,1)\) of the seven powers of rotation. The homology character is their negative because degree five is the only nonzero reduced homological degree.

The second independently constructs the graph from translated Fano lines, tests each subset using connected-component enumeration rather than forbidden-triple lookup, and computes the six boundary ranks over three prime fields. For each field they are \((13,78,244,407,321,58)\), yielding reduced Betti number thirteen in degree five and zero otherwise. Its mod-prime results do not in themselves rule out integral torsion; that is ruled out by the perfect acyclic matching and resulting wedge decomposition.

Recorded output is supplied in `morse_output.txt` and `chains_output.txt`. The calculations are finite and exhaustive because every subset of a fourteen-vertex ground set is visited and every incidence in the finite face-poset Hasse diagram is checked. The proof does not claim an infinite-family census or results outside the stated graph.
