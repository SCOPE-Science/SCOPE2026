---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In one-based ruler indices the letter is 1+v2(j); two occurrences of a maximal valuation in a linear interval would have a higher valuation between them. Thus any circular square crosses the original cut. Palindromicity gives the square starting at N-d. For an off-center square, reflection puts the cut inside the second half: with x>0 letters of that half before the cut and y>0 after it, equality of the two Parikh vectors forces P(y+2x)-P(y)=2P(x). The contiguous factor on the left contains an index divisible by 2^r for r=floor(log2 x)+1, since its length is 2x; the prefix on the right has no such letter. This excludes off-center squares. A square survives exactly the cuts d<=c<=N-d, including its endpoints; a cube would give two distinct square starts at the same half-length. The base order has no admissible square. An independent carry-free integer encoding with doubled-word prefix sums verified exact occurrence pairs, all cut counts and absence of cubes through order 9, plus the length-21 counterexample. Replay: python3 /workspace/review-evidence/check_frozen.py (zimin). This is bounded corroboration, not the all-order proof.

## originality

PASS

Credit the standard linear avoidance and the related seam-palindrome construction. The supported distinct claim is uniqueness among all indexed circular Abelian-square starts at every admissible half-length, with the exact rotation and higher-power consequences; no inspected source establishes that uniqueness.

## value

PASS

This resolves the boundary dependence of a canonical linear Abelian-squarefree word: it locates every cyclic obstruction, gives a complete cut-by-cut count, and separates Zimin rigidity from general palindrome symmetry by a verified counterexample. It is an all-order structural classification, not just a count for a selected small rotation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
