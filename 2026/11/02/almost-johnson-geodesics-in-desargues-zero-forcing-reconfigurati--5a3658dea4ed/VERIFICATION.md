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

Minimum ordinary zero forcing sets of the 20-vertex GP(10,3) are exactly the 13,520 eight-vertex masks (none of 77,520 seven-vertex subsets forces). The exact closure algorithm exhausts all C(20,8)=125,970 masks. Exchanging one chosen and one unchosen site builds a simple graph with 178,560 undirected edges. All-source BFS across 13,520 vertices exhaustively visits 91,388,440 unordered pairs, comparing exact d with j=8−|A∩B|: 47,380 have excess1 and none have excess>=2; by j counts 2:16080,3:25080,4:5730,5:360,6:130; radius7 diameter8, eccentricities 7:980 and 8:12540. I inspected the original C++ checker including loop bounds and forcing closure, then independently wrote and executed a separate C++ all-source BFS / mask enumeration reproducing all numbers; finite exhaustive proof, not inference from samples. Strictness witness masks 255 and 999 have j2 but graph distance3.

## originality

PASS

Butler–Grout–Hall Z(D)=8 and Geneson–Haas–Hogben general exchange-reconfiguration definitions and algorithms are prior. Inspected full latter paper does not specify the Desargues all-pairs distance-defect histogram/radius. A generic enumerator capable of computing numbers does not already state the exact results. No covering Resultary Desargues metric record identified.

## value

PASS

Desargues GP(10,3) is a canonical symmetric graph; exact near-isometry of its minimum zero-forcing exchange graph within Johnson J(20,8), unique small detours and complete eccentricity census are natural reconfiguration invariants. The finite classification is informative beyond knowing Z(D) or connectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
