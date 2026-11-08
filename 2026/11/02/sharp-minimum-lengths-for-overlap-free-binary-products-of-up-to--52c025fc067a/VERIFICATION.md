---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The claim is finite and exactly quantified for binary words, 1<=k<=9 nonempty ordered square factors. A binary word contains an overlap axaxa of period p iff the two length-p+1 substrings starting p apart agree; when adding a letter to a previously overlap-free word, a new overlap must end at the new letter. Inductively this append-one-letter test enumerates every overlap-free word of each length through 48, not just a sample. The DP F_k(w) counts all k-square decompositions by their final square cut and is exact. An independently written implementation enumerated all overlap-free binary words through 48 (416 at length 48), independently checked square-cuts and found 122 square words <=48. It reproduced (m_1..m_9)=(2,4,6,8,14,16,18,24,48), (c_1..c_9)=(2,2,2,2,6,4,2,8,2), with total cut counts equal to minimizer counts at each k. At k=9, only 001001101001011010011001011001101001011010011011 and its bitwise complement qualify, each with exactly one nine-square decomposition. The included verifier uses an additional independent complete square-block breadth-first check; it was read, not treated as an unexplained log. The exhaustive length<=48 reduction plus a known length-48 witness proves each finite minimum; nothing beyond length 48 or more than 9 squares is asserted.

## originality

PASS

Shallit, Ten Squares Force an Overlap (2026), already proves that ten binary squares force an overlap and exhibits precisely the displayed 48-character nine-square witness. These are expressly prior art. His finite Lemma 7 search restricts factors to a four-block alphabet, so does not prove that no unrestricted nine-square product is shorter, that there are exactly two minimum products, unique cuts, or the full k<=9 table. Full original paper comparison and Resultary queries found no matching unrestricted enumeration, with residual risk from unindexed tables.

## value

PASS

The minimum total word length at the maximal feasible nine-square count, and the exact number and rigidity of minimizers, are natural structural extremal invariants at the sharp nine-versus-ten transition. An exhaustive finite cutoff can be worthwhile here: it answers a precise open numerical extremal question not implied by the published existence witness or ten-square impossibility theorem. The five preceding minima are included as a coherent full spectrum rather than arbitrary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
