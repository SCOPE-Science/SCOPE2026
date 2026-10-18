---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Pairwise error-ball disjointness equals exclusion of differences E+E. Every difference supported on the last four coordinates can be split into allowed burst patterns on {3,4} and {5,6}; first-two-coordinate projection is injective, proving code size<=4 even for nonlinear codes. Independently re-created all 64 error balls, graph adjacency and enumerated all four-cliques, obtaining exactly 192 and verifying closure under XOR after translating a chosen word; exactly 12 distinct direction subspaces and 16 cosets each. Translation-plus-reversal action has 7 orbits with sizes 16,16,32,32,32,32,32. Finite exhaustive enumeration is a complete proof for this specific 64-vertex problem, not a mere partial sample.

## originality

PASS

PASS best-of-knowledge: the Abramson SEC/DAEC model and linear constructions, later burst-distance bounds and perfect-code discussions are prior. Their accessible statements do not include the complete arbitrary (including nonlinear) length-six equality census, affine rigidity and specific seven subgroup orbits. Older 1958/1959 full text could not be accessed and priority risk remains.

## value

PASS

PASS: This is the first small nontrivial blocklength at which a sharp projection upper bound coexists with multiple optimal codes; classifying all nonlinear optima and proving unexpected affine rigidity is a mathematically natural exact finite boundary, not merely recomputing a known scalar capacity. The 12 direction planes and symmetry types provide benchmark structure for SEC-DAEC constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
