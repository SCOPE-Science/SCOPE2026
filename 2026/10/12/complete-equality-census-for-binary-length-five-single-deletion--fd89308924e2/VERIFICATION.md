---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Built compatibility graph of all 32 length-five binary words by pairwise disjoint deletion shadows; it has 305 edges. Independently enumerated maximal cliques by Bron–Kerbosch and obtained size histogram 3:12,4:300,5:288,6:6, with exactly source six listed size-six codebooks, proving maximum<=6 without relying on size-seven sample. Directly recomputed three complement/reversal orbits and received-shadow coverage 16 for precisely the two matching VT syndromes 0,3 and 14 for other four. Original verifier also exhausts all C(32,6)=906192 and C(32,7)=3365856 subsets and compares LCS adjacency.

## originality

PASS

Sloane 2002 arXiv math/0207197 survey covers A(5,1)=6, one canonical VT construction, and small-block optimality, not six-code equality census or nonperfect maxima. Kulkarni–Kiyavash 2012 establishes hypergraph packing/bounds but not complete n=5 optimizer families. Resultary returned the nearby published n=6 single-deletion census (nine maxima), logically a different length with no reduction to n=5 equality cases. Exact finite historical census remains an explicit risk.

## value

PASS

This is the first nonlinear classical VT length-five regime and identifies *all* equality cases, showing optimality does not imply perfect deletion coverage (4/6 fail it). Natural complete finite extremal classification and precise symmetry types, not isolated arbitrary string examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
