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

Every nonempty subsequence occurrence corresponds to a unique nonzero bitmask; OR-ing masks by candidate word detects coverage exactly (OR=all position bits). Restricted-growth canonicalization represents each ternary word up to letter relabeling once. The reviewed C++ direct verifier iterates every canonical word length 1..11 and every nonempty position mask; a second verifier checks every labeled word using greedy prefix/suffix embeddings. Newly written independent integer-encoded C++ full enumeration (distinct storage/encoding) rechecked all 44,292 canonical words, 72,517,166 occurrence masks, the 29,525 canonical length-11 words, the unique exception and both minimizers; Its three distinct symbols have a trivial relabeling stabilizer, so the orbit has precisely 3!=6 labeled words. This is exact finite exhaustive proof of the stated bounded theorem, not a claim for length >=12.

## originality

PASS

The primary 2022 and expanded 2025 subsequence-cover papers introduce the definition, γ(3)=8, algorithms and a length-15 ambiguity with four symbols, but do not state the first ternary ambiguous length or six labeled exceptions. The finite threshold requires a complete census and is not merely the earlier γ(3) table.

## value

PASS

For a natural recently introduced notion of cover, the first possible failure of shortest-cover uniqueness and its complete equality classification is a mathematically natural boundary, not an arbitrary slice or only a sample; code supplies a short exhaustive certificate usable as an exact reference instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
