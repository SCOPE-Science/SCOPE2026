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
# Reproducibility

Run `python3 verify_frucht_ind2_morse.py` and `python3 verify_frucht_ind2_homology.py` with Python 3 and the standard library only. The first run confirms exact integer boundary cancellation, all 25 complete topological sorts, critical cells, and complete homotopy types. The second run independently uses connected induced triples and mod-two simplicial matrices to obtain the entire reduced homology table, and checks the graph's LCF isomorphism. Expected terminal lines are `MORSE_ALL_25_OK` and `INDEPENDENT_ALL_25_OK`; the adjacent output text files record all printed observations.

The graph and all simplices are enumerated exhaustively, but this proof does not claim a theorem for arbitrary cubic graphs. An integer unit-pivot Morse boundary, rather than finite random testing or mod-two ranks alone, is used to establish the asserted integral homotopy types. Independent scientific validation is not available.
