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
# Verification and reproducibility

Run `python verify.py` with Python 3 (standard library only). The verifier uses exact `fractions.Fraction` arithmetic and independently rebuilds the projector onto the signed-zero degree subspace for even \(N=6,8,10\). It enumerates all perfect matchings, reconstructs the first and second moments, checks their normalized contact identities, verifies all odd-cut supporting-plane distances, all coordinate facet contact points, and a fractional counterexample to odd-cut integrality. Expected final line: `ALL_EXACT_TESTS_OK`.

Expected size-specific data: \(N=6\): 15 edges, dimension 9, 15 matchings, 20 nontrivial odd subsets, squared radii \(1/15\) and \(12/5\). \(N=8\): 28 edges, dimension 20, 105 matchings, 112 odd subsets, squared radii \(1/35\) and \(24/7\). \(N=10\): 45 edges, dimension 35, 945 matchings, 492 odd subsets, squared radii \(1/63\) and \(40/9\). The odd-subset counts include complementary duplicate cuts.

The all-\(N\) correctness certificate is the *analytic* argument in `RESULT.md`, using the exact finite-dimensional projection, blossom-distance inequality, and the positive John and Löwner moment decompositions. Finite enumeration is **not** an exhaustive proof over all even orders. No outside implementation, publication-priority certification, or independent proof audit is represented.
