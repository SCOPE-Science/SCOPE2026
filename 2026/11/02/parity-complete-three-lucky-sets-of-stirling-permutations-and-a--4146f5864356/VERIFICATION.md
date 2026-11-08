---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For each n>=3 and 2<=i<j<=2n-1 with at least one index odd, the four explicit Stirling-permutation constructions show existence of exact lucky set {1,i,j} iff i is odd or i<n. Necessary obstruction for even i>=n with odd j uses original source Proposition 3.8 and Lemma 4.3(a); odd-odd case uses the proven two-lucky input and the rank-lifting operation, odd-even and even-odd use explicit nested block insertions, with inserted 1 at a block boundary preserving Stirling nesting and parking luck. Both-even i+j<=2n is sufficient via explicit block word only, not a complete classification. Counting disjoint parity cases gives (n-1)(n-2)+h*n-h(h+1)/2, h=floor((n-1)/2). Independently implemented every case from mathematical word formulas and directly checked duplicate-label nesting, exact lucky parking indices and admissible labels for 7,694 eligible pairs over n=3..25. Frozen verify.py further describes 112,520 construction checks n3..60 and exact exhaustivity n<=8; these finite results supplement, not replace, the case proofs.

## originality

PASS

Colmenarejo et al. (arXiv:2403.03280; journal JIS 2024) give complete two-lucky sets, operations preserving lucky sets, and selected three-lucky examples, plus necessary obstructions, but the inspected Section 4 does not establish the entire parity sector or the broad both-even sufficient construction. Some odd-odd triples are straightforward consequences of earlier results and not separately claimed. Harris–Martinez on arbitrary parking functions has a larger object class and its every-subset theorem does not imply the duplicate nested-word case. The newly constructed mixed-parity range is the assessed remainder.

## value

PASS

The source paper poses the exact three-lucky-set admissibility question for Stirling permutations. A necessary-and-sufficient characterization for the entire large odd-containing parity sector, exact count, and natural both-even positive region make measurable progress on a specific open enumerative classification. It does not pretend to settle the remaining both-even sector.

The dated certificate retains the supplied scientific assessment, sources and limitations.
