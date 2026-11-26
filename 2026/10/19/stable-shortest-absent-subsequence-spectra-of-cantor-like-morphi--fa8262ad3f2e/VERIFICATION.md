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

The claim is over the binary alphabet, for full iterates only, r>=1 and k>=2. The iteration doubles the count of ones and inserts r(r+2)^k zeros between the two identical copies. Splitting any word of length 2m into two length-m words proves universality inductively; the all-one word of length 2m+1 precludes more. An absent word of length 2m+1 must have both its length-(m+1) prefix and suffix absent from the previous iterate, since otherwise the other m letters embed in the other copy. For r>=2 the overlap is a single letter; if it is zero it fits in the middle, and if it is one the endpoint zeros, if present, skip the respective endpoint ones. In every such case one more one is needed than remains. For r=1 the allowable overlap triples are exactly 000, 001, 100, 101, 111. The first four admit a central zero run with at most m letters on either side. For 111 the endpoints 00,01,11 and their reversals omit respectively 2,1,0 of the two adjacent boundary ones, by the prefix and suffix 101. The boundary ones are disjoint and this again leaves exactly one too few. The nine and four parameter choices give distinct words. At k=2 in the r>=2 case every occurring pattern for r=2 persists by zero-gap inclusion, and the endpoint argument keeps the four exceptions absent. The two finite bases were independently reproduced by collecting all obtainable strings of length at most five by append-or-skip (python3 /workspace/branches/frozen_math_replay.py 2): both have all sixteen length-four words and the exact reported nine/four missing lists at length five. The inspected frozen checker instead uses digital and morphic constructions and an earliest-occurrence automaton; its reported sampled runs corroborate but do not establish the induction.

## originality

PASS

Two distinct indexed findings cover the ordinary Cantor case exactly; credit that coverage without inferring priority from directory dates. The supported distinction is the larger-gap r>=2 regime and the uniform parameter transition between the exact languages, not the r=1 formula in isolation or the general SAS framework. No inspected statement supplies or mechanically implies that full distinction.

## value

PASS

The exact forbidden language is a finer invariant than the universality index or a numerical search. The natural Cantor-morphic family has a sharp change of forbidden pattern shape and cardinality when the smallest zero blocks grow from one to at least two, and the precise result holds at every generation. This supplies a useful test family for exact subsequence-language theory, independently of the already covered ordinary Cantor slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
