---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The source correctly encodes Rule54 pair transitions T0=(1,8,0,12) and T1=(2,4,3,0). I independently reconstructed the 13 forbidden-pattern proper prefixes and their suffix transitions and exhaustively closed all reachable (prefix, Boolean 4x4 relation, min(length,2)) triples for each of 13 origins; their state counts matched the source. Each closed length>=2 state had a nonzero relation diagonal; forbidden patterns have zero relation product. The integer prefix adjacency determinant factorizes to (1+z^2)(1-2z+z^3-z^4), and direct periodic images through n=14 matched the avoiding words with singleton correction. The finite automaton closure, unlike sampled enumerations, covers all lengths.

## originality

PASS

Jen 1989 Proposition 2 proves the four finite forbidden words for finite blocks; this is not claimed new. Martínez–Adamatzky–McIntosh Rule54 subset diagrams and periodic examples are also established. The remaining exact same-period cyclic-lifting theorem and generating function are not stated in those focused inspected results; a different finite automaton census could overlap.

## value

PASS

It closes the natural distinction between locally permissible outputs and same-period ring preimages for a canonical cellular automaton, including an explicit all-n count and topological growth rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
