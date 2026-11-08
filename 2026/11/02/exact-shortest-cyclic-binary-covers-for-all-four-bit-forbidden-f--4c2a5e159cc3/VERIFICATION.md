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

PASS. For each of 72 representative cases (six forbidden-four patterns, n=4,...,15), independently parsed the actual 1,146,591-byte certificates.json blob and generated every mandatory n-bit word by ordinary nonwrapping forbidden-factor testing. Independently reconstructed required de Bruijn arc imbalances, all supplementary integer flow changes and cost, verified every vertex balance is zero, every directed arc satisfies potential(head)-potential(tail)<=1, exact primal-dual objective equality, strong connectivity of active directed graph in both orientations, and every printed table value. The 72 distinct certificates had 193,330 required arcs, 89,657 supplementary multiplicities and maximum 16,384 vertices; zero validation errors. Euler existence and one-circle coverage follow from balanced strongly connected directed multigraph containing each required arc. Reversal/complementation gives all 16 forbidden patterns. This proves only orders n<=15.

## originality

PASS

PASS, best of knowledge. A complete 72-value optimum table for one cyclic word covering every ordinary finite forbidden-factor-avoiding n-word is neither the exactly-once restricted-language de Bruijn construction of Moreno–Matamala nor directly the optimal collection of cycles of Cazaux–Rivals. The integer Chinese-postman reduction is classical; the explicit certified enumerative optima are the claimed addition. Primary Cazaux–Rivals accepted manuscript and Moreno–Matamala paper formulations were inspected; historical unindexed computed tables and algorithm specializations remain risks.

## value

PASS

PASS. A natural finite but extensive, fully specified covering optimization with 72 independently certifiable optima, contrasting forbidden-subword language size with supplementary Eulerian augmentation. The exact nonmonotone class ordering and certificates support reuse as benchmarks. No infinite-order formula or full census of optimal circles is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
