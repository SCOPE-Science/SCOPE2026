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

Order-five de Bruijn cycles are in bijection with Euler tours of the 4-bit overlap digraph, normalized at the unique 00000 edge. The provided checker enumerates rooted full edge tours; a second independently described 2^16 local-edge-order traversal is consistent. I independently wrote a fresh DFS over all 32 directed 5-bit edges and enumerated all 2048 canonical cycles, then computed distinct literal cyclic palindrome strings by scanning each of 32 starts and lengths 1..32. Independently recovered exact P frequencies {22:32,23:32,24:200,27:192,28:920,29:544,30:128}, longest L frequencies {7:200,8:192,9:856,10:128,11:392,12:32,13:200,15:48}, 23 joint (P,L) values and 51 lengthwise profiles. The complete finite exhaustive bijection, not a sample, proves the stated finite domain.

## originality

PASS

Best-of-knowledge originality of the precise final claim, not novelty of definitions or known partial results: A rooted Euler tour of the 4-bit binary de Bruijn graph is equivalent to a rotation class of order-five de Bruijn cycles; counts of distinct literal palindrome strings differ from occurrence-based palindromic complexity. General circular palindrome upper bounds imply a weaker L/P ceiling and cannot imply which lengths 25/26 counts are absent or joint cells frequencies. Existing de Bruijn cycle count specifies universe size only. The accessible primary statements do not logically cover the claimed full classification; inaccessible plausible documents remain explicitly risky.

## value

PASS

The complete joint palindromic spectrum for a canonical constrained word class is a natural exact finite invariant not deducible from the classical 2048 cycle count or generic circular-palindrome upper bounds; joint lengths and profile frequencies are potentially useful for designing and classifying de Bruijn sequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
