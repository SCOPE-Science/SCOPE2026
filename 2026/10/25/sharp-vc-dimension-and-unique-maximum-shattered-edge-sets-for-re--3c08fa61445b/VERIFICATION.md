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

# Reproducibility and verification scope

Run `python3 verify.py` using Python 3 standard library. The expected complete output is preserved in `verification_output.txt`. The program constructs all regular orientations of \(K_3\) and \(K_5\), enumerates every candidate edge-query support, computes its actual projection patterns, and confirms equivalence with the all-cut criterion. It confirms that each largest shattered support equals an internal-edge union of cliques on parts of sizes \(m\) and \(m+1\), and that the exhaustive counts of maximum supports are three and ten, respectively.

For odd orders three through eleven, it independently verifies the general cut inequalities for the explicit two-clique construction, over all nontrivial cuts. It does not enumerate all regular tournaments beyond order five, nor check all edge subsets for larger orders. These bounded calculations do not by themselves certify the general theorem. The proof in `RESULT.md` establishes the all-order cut lemma, the inequality and extremal rigidity without relying on software.

No independent scientific audit has been conducted. Historical-priority claims are limited to the source comparisons recorded in `REVIEW.md` and `AUDIT.json`.
