---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS — For uniform k-subset A and complement B on each unrooted unit-edge binary tree, PD(U)=|U|+sum_{e internal} 1_{U crosses split e}; pendant contribution deterministic, so exact covariance reduces to split-crossing indicator moments. Verified full leaf-insertion completeness under canonical center-root encodings. An independent, separately written exact hypergeometric inclusion-exclusion covariance evaluator (rather than the package subset enumerator) generated exactly [1,1,2,2,4,6,11,18,37,66,135] nonisomorphic shapes for n=4..14, and reproduced the strictly positive minimum values for n=4..13: 2/9, 6/25, 2/9, 88/441, 5/28, 82/567, 13/126, 25/363, 107/3234, 53/11154. At n=14 and k=6 only one shape has negative covariance, exactly -122/7007; independent canonical form equals the caterpillar. The source verifier additionally has two distinct checks of the witness moments N=3003, sums X=47619, Y=55627, XY=882033. Exhaustive finite theorem checked as such, not an assertion beyond n=14.

## originality

PASS

PASS, qualified. Nipperess–Matsen 2013 gives mean and variance formulas for ONE phylogenetic diversity under rarefaction using edge snips, and includes edge-indicator covariances; does not claim a joint complementary-A/B sign threshold or the n=14 unique caterpillar witness. Hardy–Senterre 2007 studies community phylogenetic structure and additive partitions, not the exact covariance of complementary random subtree lengths. No indexed published finding or exact n14 table matched. General split-moment methods give a route to computation but not the numerical finite classification without enumeration.

## value

PASS

PASS — A sharp, exhaustive first sign-change threshold in the intrinsic covariance of complementary subsample subtree lengths on natural unrooted binary phylogenies answers a motivated rarefaction/partition question. The certificate is complete across all tree shapes and partitions through n13 and exactly n14 k6, not merely one found negative example. Unit-length finite scope is clear and self-contained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
