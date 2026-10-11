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
# Verification and proof dependencies

The accompanying `verify_monge_square.py` is a standalone Python standard-library checker. Running `python3 verify_monge_square.py` enumerates all vertices of the claimed \(n-1\)-cube for \(2\le n\le10\), checks exact integer/rational slacks, masses, and contact zeros, and compares assignment costs for all permutations when \(n\le6\). The expected output begins `VERIFY_OK square-monge n=2..10`.

The optional `verify_lp.py` requires Python 3 with NumPy and SciPy. Running `python3 verify_lp.py` independently solves the full exact-facet-normalized inball linear program numerically for all \(2\le n\le11\); it additionally tests optimal-face superdiagonal extrema through \(n=7\). The program asserts agreement within \(2\cdot10^{-8}\) (or tighter local bounds); the LP floating-point calculations are corroborative, not rigorous infinite-dimensional certificates.

The proof used to establish all-dimensional validity, rather than only the tests, is in `RESULT.md`. Its critical nonstandard lemma is the minimum-total-mass inequality for nonnegative arrays with adjacent Monge slacks at least one. Its proof uses permutation exchanges, their average, and equality in all permutation assignments; it includes an explicit feasible family attaining equality. The published Monge-polytope facet theorem is used to identify the tangent facet counts. The 2026 same-family paper's abstract was available, not its full text, and independent external audit has not occurred.
