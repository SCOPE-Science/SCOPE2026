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
# Verification

The supplied `verify.py` uses exact rational arithmetic in the affine-coordinate model of the regular simplex. Its construction does not use the theorem's energy formula when calculating pairwise distances: it forms the tree-edge points explicitly, subtracts their vectors, and sums the squared-coordinate differences.

It checks these independent invariants:

- For each tree, every cut weight is strictly between \(0\) and \(1\), and all \(n-1\) edge points have the claimed centroid.
- The all-pairs graph distance sum equals the sum of the tree-edge cut products.
- The directly computed squared-distance energy equals the displayed formula involving the Wiener index.
- The sharp star/path bounds and their equality classes hold for every enumerated tree.
- Distinct Prüfer sequences enumerate exactly \(n^{n-2}\) distinct labeled trees.

All Prüfer codes were tested for \(n=3,4,5,6\), corresponding to \(3,16,125,1296\) trees. At each of \(n=7,8,9,12,17,30\), 150 additional pseudorandom Prüfer codes were checked using a fixed seed. The actual run returned `VERIFY_OK`; all comparisons were exact rational equalities.

The theorem for arbitrarily large dimension relies on the algebraic proof in `RESULT.md`, not on bounded enumeration. No independent scientific validation has been performed.
