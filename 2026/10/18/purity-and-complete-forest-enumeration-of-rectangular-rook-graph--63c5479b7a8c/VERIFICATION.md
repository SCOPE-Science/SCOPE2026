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
# Verification notes

The source program `verification/verify_induced_forests.py` constructs every rook adjacency mask from row/column equality and tests induced subgraphs by an explicit depth-first cycle search. Its mathematical predictors separately recurse over alternating bipartite path components and uncolored linear forests, without using the direct graph test as an oracle.

Run with `python3 verification/verify_induced_forests.py` in any directory containing the `verification` folder. The resulting output is stored exactly in `verification/verification_output.txt` and ends with `VERIFICATION_OK profiles 10 total_subsets 370512`.

The checked profiles are \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4),(3,6)\); every subset is examined, including the empty subset. On all profiles the entire induced-forest polynomial and complete inclusion-maximal size distribution match the claimed enumerators. Additional third-party graph-library acyclicity checks agreed for all nonempty subsets of \((2,4),(3,3),(3,4)\). No computations are used to infer an infinite conclusion: the proof supplies the unrestricted case.
