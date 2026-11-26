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

The digit recurrence maintains the identity between truncated summand columns and the target prefix, with the excess represented by the carry times the next place value. Both summands are nonnegative and at most the target, so no higher summand bits need be guessed past its canonical length; zero final carry is both necessary and sufficient. An independently written replay checked the frozen table's root, both successors of every row, the carry-zero and exception flags, complete reachability and opposite acceptance after every final-one edge. The frozen row counts were 4,6,18,9,41,29. An additional most-significant-bit-first check reversed the carry relation and used separately written exception recognizers, reaching 2,5,14,10,39,27 states after a leading one with no mismatch. Zero was checked separately in both directions. This checks all canonical lengths, not just the frozen script's bounded census. In ordinary bit order the sixth complement is 11 or (10)+011, giving 3 and the recurrence n -> 4n+7 on the sequence starting at 3, equivalently (4^k-7)/3 for k >= 2. Counting 4^k <= 3X+7 includes equality and handles X below 3, and logarithmic growth implies density zero. An infinite eventually periodic set would have positive density, so nonperiodicity follows.

## originality

PASS

The pass is for the substantive first-six classification, particularly the precise exceptional sets for d=5 and d=6, not for introducing fibbinary integers, the d=1 identity, or the carry-automaton method. Closest inspected statements did not supply those higher-dilation complements. This is a bounded best-of-knowledge judgment, not historical-priority certification.

## value

PASS

The initial consecutive dilations of a standard sparse digit set give a natural comparison. The precise d=6 exceptional sequence determines membership at all scales and a logarithmic, not modular, obstruction immediately after the singleton at d=5. The theorem therefore supplies concrete structure beyond generic decidability or a finite list of observed misses; the elementary or already-known low cases chiefly provide context.

The dated certificate retains the supplied scientific assessment, sources and limitations.
