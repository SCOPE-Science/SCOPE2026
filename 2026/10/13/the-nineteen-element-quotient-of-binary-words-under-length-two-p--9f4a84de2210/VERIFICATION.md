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
# Reproducing checks

Execute `python3 verify.py` using a standard Python 3 interpreter. The program constructs each 2-letter palindrome insertion using literal word concatenation and checks both forward derivations yielding the same 11-letter word. It tests signature preservation for every 2- through 13-letter binary word under every possible single insertion; enumerates the undirected duplication graph of words of lengths 2 through 14; compares connected components against signatures on every length slice 2 through 9; and checks all 19 displayed signature types and class counts through length 9.

The program prints `VERIFY_OK` only after all assertions succeed. The exact output for the inspected package was:

`VERIFY_OK primitive_join_paths=4 prefix_signatures_preserved_through_length=13 graph_limit=14 graph_vertices=32764 graph_edges=81924 exact_component_slices=2..9 quotient_size=19`

Finite enumeration is not an infinite proof. The uniform canonical reduction and the local identity, with its two explicit forward chains, provide the mathematical proof in `RESULT.md`. No independent audit or validation is represented.
