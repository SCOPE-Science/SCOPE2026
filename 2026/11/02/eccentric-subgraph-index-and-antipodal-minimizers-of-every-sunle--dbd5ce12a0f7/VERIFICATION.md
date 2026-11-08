---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: RESULT.md counts connected edge-selected subgraphs through any two distinct leaf indices via their unique cycle path (or spanning path/full cycle), with a_j(d)=2j-n+max(d-j,0)+max(n-d-j,0) allowable j-vertex arcs. Optional other leaf edges contribute 2^(j-2), and the n spanning paths plus cycle contribute (n+1)2^(n-2). The a_j(d) expression decreases strictly toward antipodal cyclic distance, giving unique minimizing index distance. Evaluating even and odd geometric sums gives L_n, while same-index and diagonal T_n=(2n-1)2^(n-1)+1>2L_n remove alternate minima. Core/leaf endpoint factors are 2 and 4 for distinct indices, with the stated minimum. Independent exhaustive edge-subgraph connectivity enumeration for n=3..7 confirmed leaf/core minima, ES=81,288,930,2736,7644 and every antipodal witness. The path counting, not the finite enumeration, supplies general n.

## originality

PASS

PASS, qualified. De--Patra 2026 introduces exactly f(u,v) and ES and considers unicyclic extremal graphs; accessible abstract and detailed research overview do not establish all individual sunlet vertex profiles. Critically the full primary text could not be obtained, including through authorized institutional access (VPN disconnected), so a stronger coverage cannot be excluded. Inaccessibility alone does not negate the independently proved and motivated all-n claim.

## value

PASS

PASS: S_n is the canonical uniform pendant-leaf unicyclic graph, and the recently defined eccentric-subgraph index naturally asks for pairwise minimum counts. An exact all-n two-type profile, center and parity-dependent opposite-leaf minimizers is independently useful for comparisons with known unicyclic extrema; it is not merely a remapping of distance eccentricity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
