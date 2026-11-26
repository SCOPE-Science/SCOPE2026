---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The three spokes on each inner triangle have distinct colours. For an all-distinct incoming outer triple, the spoke permutation relative to it is a 3-cycle, so the outgoing triple is also distinct. For an incoming triple with repeated a, singleton b, absent c, the spoke at b must have colour a, making c repeated, b singleton and a absent on the outgoing triple. The seam is a row rotation and cannot reconcile an odd number of these swaps. Thus for odd k all cut triples are distinct. For any omitted colour, a column's two retained paths cover all six column vertices: one stays on the omitted-spoke row, and the other joins the remaining two outer vertices through all three inner vertices. Each changes the cyclic ordering of the active pair by one swap, whereas the seam preserves the order. The odd return transposition gives one spanning cycle for each omitted colour. This argument also works at k=1, with only the twisted seam. For even k, contracting each triangle preserves each bicoloured component count and yields a cubic bipartite graph with parts of size 2k. If all unions were Hamiltonian, the three cyclic relative permutations of the matchings would each be a 2k-cycle of negative sign but would compose to the identity, a contradiction. The published factorization count supplies existence and counts; a Kempe switch on the only bicoloured component merely permutes the names. Both bundled verifier sources and their finite outputs were inspected, not executed. The recorded finite agreement through k=8 and k=10 is not the proof of the all-k claim.

## originality

PASS

The novelty credited is the all-factorization Hamiltonicity for odd k and the exclusion for even k in this family, with Kempe rigidity a consequence. Not credited as novel are odd existence, the Jacobsthal counts of all factorizations, the all-distinct cut description for odd k, or the general permutation-sign argument. The closest verified structural result describes all colourings, but obtaining Hamiltonicity of every two-colour subgraph requires tracking how its paths connect across each column and the twisted seam, which the enumeration does not calculate. The 2011 paper is a material unresolved access risk; the strongest statements actually inspected support the decision without making a historical priority claim.

## value

PASS

The parity classification resolves the perfection question for every colouring of a natural cubic graph family, not just the existence of one construction or the number of colourings. Tracking the bicoloured pairings and the triangle-contraction obstruction explains why the known odd and even enumeration classes behave differently, and gives exact Kempe rigidity even when multiple unlabelled factorizations exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
