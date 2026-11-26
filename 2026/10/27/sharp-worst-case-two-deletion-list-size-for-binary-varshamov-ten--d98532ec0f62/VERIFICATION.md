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

Independently reconstructed the bound. For each inserted bit, the identical insertion gaps are exactly those joined by successive copies of that bit, giving n distinct one-insertion descendants of the receiver in total. Inserting a bit into a fixed length-(n−1) word gives checksum increments in [0,n]; same-bit equal increments mean identical words, and opposite-bit increments are separated (zero insertions at most the word's weight, one insertions at least weight plus one). Thus shadows of distinct words in a syndrome are disjoint. A singleton shadow forces the two removed symbols of any witness embedding to be in one constant run, so the word is obtained by inserting a repeated pair. For the pair 00 the integer increment is twice the suffix weight; for 11 it is twice the total weight plus twice the prefix zero count plus three. For a fixed pair equal increments imply the insertion gaps are separated by copies of its symbol and hence give the same word; the two pairs give opposite parities. All increments are in [0,2n−1], so at most two such words per syndrome are possible. The shadow budget gives 2L≤n+2. For the zero receiver, syndrome zero includes the zero word and exactly the pairs of 1-positions with sum n+1; no weight-one word contributes. At n=2, the checksum residues of 00, 01, 10 and 11 are 0, 2, 1 and 0. The frozen script and saved output corroborate the theorem but are not its proof.

## originality

PASS

The inspected sources have the same intermediate-layer technique, a weaker worst-case upper bound, an average-size lower bound, or a different deletion-list problem. None gives the sharp pointwise VT upper bound plus attainment.

## value

PASS

Gives the exact worst-case ambiguity of a classical single-deletion-correcting code just beyond its unique-decoding radius. It nearly halves the known n candidate bound, proves an all-length witness and identifies the singleton-shadow obstruction rather than just computing small cases. The distinction from average list size matters for worst-case list budgets. No decoding-time gain is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
