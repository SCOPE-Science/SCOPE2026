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
# Verification record

The attached standalone `check_pal_mean.py` uses Python 3, SymPy, exact rational arithmetic and exact integer determinants. It exhaustively enumerates all binary order-four cyclic de Bruijn words and chooses the canonical rotation beginning at the unique factor `0000`. It finds exactly 16 cycles, eight with zero length-five palindromes and eight with two. Each of the eight ordered binary triples is compared with its predicted palindrome-event probability.

The checker separately constructs the order-four de Bruijn row Laplacian on length-three vertices, removes and adds edges according to the two-edge contraction, and computes ordinary directed-tree cofactors for each applicable equality type at alphabet sizes two and three. This tests the critical nonstandard determinant/contraction identity. It also performs exact rational checks of the summed formula through alphabet size fifteen. Run: `python3 check_pal_mean.py`.

The output is expected to end in `ALL_PALINDROME_MEAN_CHECKS_PASSED`. For binary cycles the full check reports `BINARY_EXHAUSTIVE_OK 16 {2: 8, 0: 8}`; the three ternary equalities yield respectively `5/18`, `13/54`, `13/54`, and all-distinct `8/27`.

The finite checks do not prove arbitrary-alphabet assertions: the all-alphabet proof is in `RESULT.md`. No external validation or independent audit is claimed.
