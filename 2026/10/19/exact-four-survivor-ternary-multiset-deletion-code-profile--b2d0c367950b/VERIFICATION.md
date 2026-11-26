---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Two words can share a four-symbol receiver exactly when their componentwise minimum has sum at least four; any shared longer receiver also contains a four-symbol one. A heavy word contains a pure four-symbol receiver, and distinct selected heavy words cannot share a heavy coordinate, giving at most three heavy words. At n≥10 no light word exists, and the three pure words attain the bound. For 7≤n≤9 two light words intersect in at least 2n−9≥5; the three pure words and (n−6,3,3) are compatible. At n=6 each light word has two coordinates at least two, hence contains one of three distinct pair-type receivers; at most three light words coexist. The three pure and three (3,3,0)-type words attain six. At n=5 the nine displayed incompatible triples cover each of the twelve light vectors at least twice; counting incidences bounds selected light words by floor(9/2)=4, and the seven-word witness attains the total. In a separate exact finite check, I enumerated triples summing to n and represented each by the 15-bit mask of its four-symbol receivers. With words indexed in order, memoizing F(i,used) as the larger of skipping word i and taking it if its receiver mask is disjoint from used (terminate with F=0 after the last word) gave 7,6,4,4,4,3 for n=5,…,10. This corroborates all short cases independently of the recorded clique search; the unlimited tail is proved by the heavy-coordinate argument. RESULT.md, VERIFICATION.md, check.py and check_output.txt were inspected, not executed. The recorded script uses int.bit_count(), so Python 3.10 or later is the safe replay version despite its docstring's Python ≥3.9.

## originality

PASS

The known n=5 endpoint is explicitly credited and is not accepted as new. The validated distinct contribution is the full four-survivor ternary profile for n≥6, especially the exact six-word case, the four-word plateau and the exact threshold for the pure code. No exact or mechanically dominating result for the full contribution was identified after comparison of the closest indexed and primary-source formulas.

## value

PASS

This is the next natural fixed-survivor profile beyond three symbols, with an operational ability to distinguish unordered ternary messages from just four remaining symbols. The six-word instance reaches a qualitatively different packing of light words, and the exact four-word interval and sharp onset of pure-code optimality determine the usable message alphabet at all lengths. The local receiver certificates explain both exceptions and are more useful than a table of small enumerations alone. The already known single-deletion endpoint is not counted as added value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
