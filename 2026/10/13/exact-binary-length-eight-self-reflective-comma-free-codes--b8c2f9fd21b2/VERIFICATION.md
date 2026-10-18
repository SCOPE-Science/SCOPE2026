---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Every length-8 reversal-invariant binary dictionary is a union of reversal orbits. The 256 words form 136 orbits, of which 56 are individually comma-free (12 singleton,44 size-two). Pairwise orbit compatibility yields a 56-vertex 929-edge graph; any valid dictionary corresponds to a weighted clique. Independently enumerated ALL 2107 maximal cliques by bitset Bron–Kerbosch; largest weight is 18 with 16 pairwise-eligible maxima. Pairwise compatibility is not sufficient, so every candidate maximum was checked against every proper splice of all ordered codeword pairs. Exactly 12 genuine size-18 dictionaries survive, with 6 palindromes and six reversal pairs each, exchanged in 6 distinct complement pairs. Finite domain is exhaustively covered, not a timeout heuristic; independently computed witness fingerprints match bundled list.

## originality

PASS

Churchill 2009 introduces W_r(k,n) for reversal-closed comma-free words, gives general upper bounds, including even k, and constructions at other parameters. Its full article does not report all twelve labeled size-18 binary length-8 codes. Fimmel et al 2023 full paper counts length-two and length-three codes and investigates alphabet self-complementation, a different involution. Wang–Tonchev 2009 addresses generic comma-free searches, but only its abstract was accessible; its possible table is explicitly unresolved. No stronger known theorem inspected determines these equality cases.

## value

PASS

Exact maximum plus a complete, exhaustive optimizer census is a natural finite extremal code invariant directly tied to frame-synchronizing reversal-closed dictionaries; full equality classification and complement pairing are mathematically useful independent of a general n theorem. Twelve explicit witnesses and exhaustive correctness provide a replayable complete classification, not an arbitrary random slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
