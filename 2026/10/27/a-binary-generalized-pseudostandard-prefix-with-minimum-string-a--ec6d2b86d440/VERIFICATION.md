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

I rebuilt the eight closures by testing candidate lengths in increasing order and imposing the reversal or reversed-complement relation on symmetric pairs, independent of the uploaded suffix-based implementation. The final word equals the stated length-182 word. All 12608 distinct nonempty factors have an occurrence meeting the six specified positions. For the lower bound I rebuilt the occurrence masks of the twelve displayed factors and iterated all ORs of positional masks. There are 29 distinct masks; the successive reachable-set cardinalities for one to six choices are 29, 281, 1067, 1879, 1935, 1936, and the full twelve-bit mask first appears at six. Repetition is allowed in this computation, so it includes all unions of at most five choices. Any attractor must cover these twelve factors. The finite directive can be continued indefinitely (for example, with any binary letters and consistently choosing an antimorphism giving continued growth, which here holds since a letter is appended each time).

## originality

PASS

The closest prior direct witness has exact attractor size five. The cited subclass theorems and the indexed exact smaller witnesses do not imply this size-six example or the failure of a universal size-five bound.

## value

PASS

After the natural published bound four failed at five, five was the next candidate uniform bound for the same structured class. This exact witness excludes it as well and gives a small independently checkable obstruction, providing a specific benchmark for any proposed uniform theorem. The mathematical threshold, not the arbitrary word length, is what makes the result useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
