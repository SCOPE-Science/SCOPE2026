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

For the fixed language of positive words {epsilon}∪a{a,b}*, the given binary transitions A=(a:00,b:10) and B=(a:002,b:120) produce strongly connected automata with strict f-positive distance corner 0. Product z=(0,0), q=(0,2) have exactly length-three positive routes z->q via abb and q->z via aba, while positive words shorter than three are just a,aa,ab and cannot traverse either pair; hence equality 3=3 defeats strict f-corner inheritance. aba nevertheless resets all six product states, so this does not contradict product synchronizability. The universal five-state minimum follows by classifying all two-state positive-corner automata (four Type I reset-a automata, one Type II identity-a/reset-b), verifying every 2x2 type pair retains its corner and singleton factors cannot create failure. Independently enumerated 16 two-state binary automata, found exactly 5 with corner 0 and all 25 two-by-two pairs good, and checked the 2x3 witness metrics and reset. The fixed alphabet and positivity-function restriction is essential.

## originality

PASS

Bradshaw–Clow–Stacho arXiv:2405.00826v3 states immediately before Theorem 6.1 that it is unclear whether f-corners remain corners in the product. Theorem 6.1 establishes that the product can be synchronized to the designated pair, which is strictly weaker. The explicit 2x3 counterexample both satisfies their synchronized-target theorem and disproves the proposed stronger inheritance, with complete sharp size minimum for this fixed f. The 2026 journal text was not directly compared page by page.

## value

PASS

Resolves an explicitly raised structural question in synchronizing automata by a minimal, strongly-connected and still synchronizable counterexample. The exhaustive lower bound (no total size <5 for this positivity language) makes the obstruction sharp and reusable for understanding product arguments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
