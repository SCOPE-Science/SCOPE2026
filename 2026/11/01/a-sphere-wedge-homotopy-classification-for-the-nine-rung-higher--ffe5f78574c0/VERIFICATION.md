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

# Direct reproducibility

Execute `python3 verify_ladder_homotopy.py` using a standard Python 3 interpreter. The checker relies only on the standard library and does not download any data. Its recorded successful stdout is `ladder_verification_output.txt`.

The script exhaustively tests all \(262,143\) nonempty subsets of the graph, matching a second column-based enumerator to obtain \(22,692\) nonempty simplices. It checks \(11,343\) acyclic pairs over \(132,988\) incidences and the precise critical cell dimensions. It computes a nonzero mod-two degree-five cocycle supported on masks `73875`, `73878`, `74386`, `75922`, confirms its coboundary is zero and its pairing with a closed five-cycle is one. Its explicit eighteen-term degree-seven cup-three diagonal computes an identically zero square. Four independently lifted critical 7-cycles are verified closed.

# Mathematical limits

Finite enumeration is a complete proof only for this particular finite graph, not for other ladder lengths. The CW-attachment argument uses standard published results: discrete Morse matching, \(\pi_6(S^5)=\mathbb Z/2\), the Steenrod-square detection of the suspended Hopf attaching class, and the specified simplicial cup-i formula. No independent external audit is asserted.
