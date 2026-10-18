---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n>=3 crowns, only deleted-matching endpoints are at distance three. Any selected set with at least three vertices therefore automatically provides a distinct selected distance<=2 witness to each chosen vertex. The dominating sets are precisely all of A or B, selections with >=2 from each shore, and singleton shore selections whose matching mate is among >=2 vertices on opposite shore. Two-vertex dominating sets fail the witness condition. Thus S_n(z)=2z^n+((1+z)^n-1-nz)^2+2n z²((1+z)^(n-1)-1). Single-vertex deletion classifies minimal sets as exactly both shores, 2n(n-1) matched triples, and C(n,2)C(n-2,2) two-plus-two disjoint-index sets, giving minimal polynomial 2z^n+2n(n-1)z³+C(n,2)C(n-2,2)z⁴. Lower optimum 3 and upper minimal n. Independently verified all subsets and minimal status n3..6; universal claim analytic.

## originality

PASS

The 2017 regular graph bound already implies the scalar upper semitotal domination number n (attained by either whole shore), and this part is explicitly excluded from novelty credit. The assessed original contribution is the full all-set polynomial and exact inclusion-minimal family distribution; a prior scalar bound does not imply these.

## value

PASS

The complete coefficient distribution and inclusion-minimal set structure give exact natural invariants of a standard nontrivial graph family, with a meaningful distinction between global domination witnesses and minimality. This is substantially more information than a previously known scalar upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
