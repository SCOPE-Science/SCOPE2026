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

# Verification evidence

## Independent-of-proof finite tests
Run `python3 verify_matroid.py` in a directory containing the accompanying standalone program. It has no external dependencies. The program enumerates every nonempty family of equicardinal subsets on ground sets of sizes at most five, and tests the basis-exchange axiom to retain every labeled matroid. It independently evaluates the VC dimension by projections, the Littlestone dimension by exact version-space recursion, the primal/dual common-independent-set maximum, and the dual-rank subset minimum. It also checks the exact minor split for each nonconstant coordinate. It performs additional seeded GF(2)-linear-matroid checks up to ten elements.

The captured `verification_output.txt` reports 498 complete small matroids (1, 2, 5, 16, 68, 406 by ground size) and 336 reproducible seeded binary-representable instances. It ends with `ALL_MATROID_IDENTITY_CHECKS_PASS`. Re-running the program should reproduce every output line. These tests are finite, not a proof for all finite matroids.

## Mathematical dependencies and limits
The unrestricted theorem depends on the standard matroid-intersection min–max theorem (explicitly stated in Chakrabarty et al., arXiv:1911.10765v1), the elementary dual-rank identity, and induction on the size of the ground set. An actual query of a nonloop/noncoloop corresponds to deletion or contraction, while a loop/coloop is a constant query. The key exact algebraic identity is the split of the subset minimum over whether the queried element belongs to the minimizing subset. The result does not apply to arbitrary constant-weight set systems or to noisy or infinite settings. No independent scientific audit has been performed.
