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

# Reproduction and limits

Run `python3 verify_desargues_homotopy.py` with Python 3.10 or later. No third-party libraries or downloads are required. The verifier reconstructs the graph from subset incidence, verifies an explicit graph isomorphism to \(GP(10,3)\), and exhaustively enumerates all \(113{,}192\) matchings including the empty set. It applies the declared staged face pairing, removes its single empty-face pair to produce an ordinary discrete Morse matching, and topologically sorts all \(680{,}370\) oriented face incidences to prove acyclicity. It derives the full signed integral Morse differential by memoized gradient-path expansion and asserts an exact rank-three primitive image, with three explicit unit columns.

The successful test prints `DESARGUES_HOMOTOPY_VERIFY_OK faces_with_empty=113192 matched_pairs=56567 critical=1x0+8x5+48x6 oriented_incidences=680370 integer_d6=3_unit_pivots homotopy=5xS5+45xS6 gradient_expansions=19573`.

The numerical certificate is finite and exhaustive for this graph. The mathematical final step also uses the standard discrete-Morse CW theorem and the classification of maps \(S^5\to\bigvee^8S^5\) by their integral degrees; the verifier does not implement those general theorems. This package provides no external independent audit.
