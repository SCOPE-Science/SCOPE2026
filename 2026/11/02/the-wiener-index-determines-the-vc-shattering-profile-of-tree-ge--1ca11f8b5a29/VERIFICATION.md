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

# Verification and limits

The proof in `RESULT.md` establishes the statements for every finite nonempty tree; this is not a finite-extrapolation result. The critical logical steps are the exact classification of complementary convex subsets by single edges, the equivalence between triple shattering and noncollinearity, the impossibility of crossing tree splits on four labeled vertices, and the unique middle-vertex enumeration of collinear triples.

Run the standalone Python-standard-library checker with `python3 VERIFY.py`. It uses breadth-first search for distances and explicitly reconstructs convex subsets and their complementary convexity, independently of oriented edge cuts. It then enumerates traces on every support and checks all coefficients, the triple median condition, and the distance/cut formula. Prüfer words enumerate every labeled tree through order six (1,442 total), followed by 120 reproducible test trees of orders seven through ten. Star and path equalities are also checked through order ten.

The local execution completed with `ALL_TREE_HALFSPACE_WIENER_CHECKS_PASS`. Finite verification does not certify an infinite theorem, establish historical originality, or constitute an independent scientific audit. No exhaustive search beyond six vertices is claimed.
