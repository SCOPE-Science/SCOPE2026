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

The graph is precisely the Cayley model on Z4² with degree six and its complement cyclic Latin-square model. Every independent 4-set is among 4 rows,4 columns,4 cyclic symbols,4 parity blocks; checking all C(16,4)=1820 and C(16,5)=4368 possibilities proves maximum independence number 4 and exact 16 classes. Enumerating all exact covers yields ten partitions and 10·4!=240 named colourings. Both actual independent source algorithms construct ALL legal one-component two-colour switches, one via component generation and another by 28,680 pairwise recognition, and BFS all 240 starts; they assert 1008 edges, eccentricities 168 at4 and 72 at5, complete distances (1008,5400,13416,8280,576), and quotient three squares with common parity-block vertex. This exhaustive finite certificate supports the entire specific graph claim; inspected exact algorithms, not merely their PASS logs. Independent reexecution of code not performed during this run.

## originality

PASS

240 named four-colourings are known OEIS A158792 and are excluded. Brouwer/Cameron graph models and degree parameters are prior art. Wanless (2004) cycle switches on Latin-square isotopy/main classes are not Kempe moves among proper colourings of the complementary Latin-square graph. Chakraborty–Feghali–Mahmoud (2024) list-Kempe general theorem requires palette at least six for degree six and does not settle four colours. Resultary search found no same 10-vertex three-square quotient or full named metric, though an older unindexed enumeration remains possible.

## value

PASS

Complete naturally motivated reconfiguration graph at the chromatic threshold of the well-studied non-rook (16,6,2,2) strongly regular Shrikhande graph. The quotient three quadrangles meeting at one hub explains mobility and exact named-state distances beyond the known raw colouring count; the object/invariant are not arbitrary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
