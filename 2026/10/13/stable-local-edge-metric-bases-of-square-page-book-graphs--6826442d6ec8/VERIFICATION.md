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

The computed vertex-to-edge distinction sets for adjacent edge pairs are P_i union P_j for two page-spoke edges of matching type, and {y,a_i} union {b_j:j != i} or its symmetric {x,b_i} union {a_j:j != i} for common-spine or within-page pairs. These are all adjacent-edge pair types. Hitting every P_i union P_j requires selected non-spine vertices on all but at most one page, so at least r-1. At equality no spine vertices occur, exactly one page is empty and one non-spine vertex chosen on every other page. Orientation witnesses force counts A>=2,B>=2; these are also sufficient for hitting both oriented families. This is realizable precisely r>=5, and binary strings with at least two of each orientation give 2^(r-1)-2r choices per omitted page, hence r(2^(r-1)-2r). Independent exact breadth-first distance and edge-pair enumeration verified all candidate sets through size r-1 for r=5,6,7, yielding 30,120,350 bases. This does not replace the general proof.

## originality

PASS

Best-of-knowledge complete basis classification for local EDGE metric dimension of quadrilateral book K_{1,r} square K_2. The 2020 defining paper gives this invariant for paths, ladders, stars, cycles and wheels but does not prove book graph classification. The 2024 Amini-Henning-Tavakoli paper describes corona and edge-corona operations, not the Cartesian product book; only its abstract/metadata was accessible, so this remains a named bibliographic risk. Resultary related book/crown work computes different invariants.

## value

PASS

Exact minimum, all extremal configurations and a closed enumerator for a natural well-studied graph family, with a structural threshold at five pages. The full optimizer classification is useful for combinatorial design and contrasts with the already-studied global edge metric parameter. This is not a numerical convenience example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
