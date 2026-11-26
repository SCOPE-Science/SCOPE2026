---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Given the outcome permutation, at the arrival of label π_i the prior labels occupy exactly their designated spots by induction. The contiguous occupied run left of i gives precisely ℓ_i choices of preference, and every independent choice gives the desired outcome. At entry n in position j the left word must avoid 123 and 213, the suffix retains its own fiber weight because n blocks its leftward run, and the entry n contributes j. In the left word all factors are 1 or 2 and the 2s cannot be adjacent; descending-by-value increasing pairs attain 2^⌊(j−1)/2⌋. Placing all left labels above all suffix labels prevents forbidden cross-subwords, since the fourth entry of either forbidden pattern is its largest. This constructs equality in the composition recurrence on weights w_j=j·2^⌊(j−1)/2⌋. For j≥8 the split 5+(j−5) strictly dominates by the respective even/odd ratios 5(j−5)/j and 5(j−5)/(2j). The listed strict inequalities then eliminate 1 and 6, followed by 4, 2 and 7, whenever n≥8. All n≥8 are represented by 3 and 5 (start at 8, 9, 10 and add 3). Exchanging 5 threes for 3 fives increases the product, and b≡2n (mod 5) is unique with 0≤b≤4. Adding five increases a by one and bounded b gives the claimed root limit. Independent enumeration to n=9 used the equivalent test that an entry with a larger successor cannot have two smaller predecessors, and a monotone stack for nearest greater predecessors. The maxima were 1,2,6,8,20,36,56,120,216, with avoidance counts 1,2,6,22,90,394,1806,8558,41586. The bounded enumeration does not prove the unbounded formula. The frozen replay is verify.py, with the recorded run in verify_output.txt; the script was inspected, not executed.

## originality

PASS

The individual fiber formula and the aggregate enumeration for the class are established. The inspected literature and index results do not give the maximum individual fiber in this class, the weight-composition recurrence, or the eventual optimal 3-and-5 formula. This judgment is bounded to the comparisons below.

## value

PASS

The maximum determines the most likely single outcome conditional on belonging to this natural avoidance class, a statistic the established total does not give. The tight recurrence reduces a constrained permutation extremum to an exact optimization over part sizes, yields a maximizing construction for every order and identifies the eventual growth law. It is not merely a table of small orders or a reformulation of the known fiber product; it makes no claim to classify all maximizing permutations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
