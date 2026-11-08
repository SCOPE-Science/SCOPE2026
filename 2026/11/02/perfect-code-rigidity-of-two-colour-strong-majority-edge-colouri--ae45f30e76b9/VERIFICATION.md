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

For a red edge uv, exactly two of its four adjacent edges must be red, giving a_u+a_v=4 for red incidence degrees a_v; for a blue edge the count gives a_u+a_v=2. All edges stay inside the profile classes {1,3} or {0,2}, and connectedness forces one class. Each profile-3 vertex is adjacent only to profile-1 vertices, each profile-1 vertex has exactly one such neighbor: D of profile-3 vertices is an efficient dominating set. The other class is its color swap. Conversely any efficient dominating set yields precisely two strong-majority assignments, so b=2p and |V| divisible by four for existence. The 2-power vertex-transitive and Möbius cases use the explicitly quoted previously published Knor–Potočnik Theorem 1.2 and Lemma 2.2; an even Hamiltonian-cycle/chord proper 3-edge coloring supplies index 3 when no code. Independent brute-force graph checks verified K4 (4 codes,8 assignments), K3,3 (0,0), square prism (4,8), directly applying the original edge-neighbor condition.

## originality

PASS

Kalinowski et al and Pękała–Przybyło introduce and bound strong-majority edge coloring without this cubic two-color perfect-code bijection. The powerful Knor–Potočnik 2012 perfect-code classification is clearly credited and, by itself, does not assert edge-color assignments. Earlier exact prism cases are recognized as covered corollaries, not novel standalone discoveries.

## value

PASS

An exact global structural equivalence for a newly studied edge-coloring invariant across all connected cubic graphs, including exact labeled multiplicity, transfers substantial older perfect-code classifications and exposes the Möbius obstruction. It is more than recomputing known prism counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
