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

# Finite verification

The complete adjacency matrices have vertices indexed by all binary words of the tested length. An edge represents at most four shared distinct deletion-plus-at-most-one-substitution outputs. The maximum permissible codebook is the exact clique number.

Run `python3 verify.py`. Expected result: optimum values 5, 5, 6, 8, 12 and final `VERIFY_OK`. Its error balls are constructed both by deletion followed by at-most-one substitution and by substitution followed by deletion, with equality asserted for every word. Every witness pair is also checked directly.

An independent integer-bit-mask implementation is provided as `independent_check.cpp`, to be compiled with `g++ -O2 -std=c++17 independent_check.cpp -o independent_check` and executed with `./independent_check`; expect the same five clique numbers and `VERIFY_OK`. Both exhaustive solvers use a sound greedy-coloring upper bound in a complete maximum-clique backtrack; the C++ program independently builds all channel outputs.

The computed numbers of admissible unordered vertex pairs for lengths 4 through 8 are 38, 115, 552, 2917, 15194. These are diagnostic totals, not standalone upper-bound proofs. The exact bounds rely on the supplied exhaustive search and its monotone coloring-bound argument.

This finite verification does not check any other length, alphabet, or error model. It is not an independent scientific audit.
