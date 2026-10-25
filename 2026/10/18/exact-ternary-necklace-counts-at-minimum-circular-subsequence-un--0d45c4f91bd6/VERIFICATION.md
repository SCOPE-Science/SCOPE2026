---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For an alphabet of 3 letters, each constant length-k scattered subsequence forces >=k copies per letter so min length is 3k. Rich-block (arch) greedy decomposition forces k consecutive permutation triples at minimal length; circular rotation permits exactly three phase classes. Their sizes 6^k, pair intersections 3*2^k and triple intersection 6 yield L_k=3*6^k-9*2^k+6, and exactly one/two/three counts follow by inclusion-exclusion. A fixed nonmultiple-of-3 rotation would permute all phases and hence force a period-3 word, contradiction; rotations by 3j fix L_gcd(k,j) words. Burnside gives the stated N_k and Möbius inversion gives primitive necklaces. k=1 phase collapse is covered by formulas. Independent enumeration of all 3^(3k) words for k=1..4, explicit subsequence checks for k<=3, checked L_k, phase multiplicities, necklaces and primitive counts; general result proven structurally.

## originality

PASS

Best-of-knowledge scientific statement-and-implication comparison: known components properly credited; no inspected accessible stronger result decisively contains the precise final claim. Residual access and priority risks explicitly retained; lack of full access was not treated as independent proof of novelty.

## value

PASS

Closed-form exact necklace and primitive-necklace enumeration for a natural extremal circular subsequence-universality constraint. The three-phase intersection structure and rotation-fixed constraints are informative beyond a brute finite census, and exact counts at every k are usable in extremal word combinatorics, automata and sequence design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
