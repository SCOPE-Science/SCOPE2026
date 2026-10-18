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

The executable `verify.py` uses only the Python 3 standard library. Run `python3 verify.py` from the directory containing this file. The direct Euler-graph census enumerates all distinct binary de Bruijn cycles of orders 3, 4 and 5, verifies uniqueness of every length-order cyclic factor, and checks the complete per-cut greedy-arch histogram and the repeat-event gap formulas. Separate Fredricksen–Kessler–Maiorana and randomized Eulerian generators test additional orders. For orders 3 and 4, a separate scattered-subsequence membership routine exhaustively checks the indices without using the arch scanner.

Successful execution on the packaged program printed:

`VERIFY_OK complete_binary_debruijn_cycles_n3_to5=2066 rooted_rotations_n3_to5=65808 random_derived_cycles_n6_to8= 105 FKM_orders_3_to10=8 explicit_subsequence_crosscheck_n3_to4=272`

The finite computations are supporting checks only. The theorem for every order and every de Bruijn cycle is justified by the explicit repeat-gap enumeration and scanner coupling proof, not by extrapolating these computations. Independent scientific audit has not been performed.
