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

The 24-edge explicitly specified Chvátal graph gives the ordinary independence complex with f=(12,42,52,20) and 126 nonempty faces. Independent reconstruction of all face posets and Hasse orientations gave acyclic matching profiles K:(62 pairs, critical 0+2), D_0:(49 pairs, critical 0), D_2:(48 pairs, critical 0+2), L_0:(12 pairs, critical 0+1), L_2:(13 pairs, critical 0), with directed incidence counts 320,243,239,44,47 and complete topological sorts. The actual verify_chvatal.py additionally tests legal 49/13-step elementary collapse sequences for D_0 and L_2 and exhaustive 4+8 graph-automorphism orbit transfer; edge-preserving generators and independent-set deletion counts distinguish the two orbits. Forman matching implies S2, point, S2, S1, point, respectively; link-cone gluing makes D_v→K a homotopy equivalence in the B orbit. The chromatic backtracking in the actual package verifies chi(G)=4 and chi(G-v)=3 for all v. Exact finite graph, not infinite family.

## originality

PASS

The previously published Chvátal equivariant-collapse result already gives the whole independence-complex S2 type and cannot be counted as novel; the substantive final additional theorem is the exact two-orbit vertex-deletion and link homotopy dichotomy. No checked source implies that deletion classification. Barmak supplies a suspension principle for triangle-free graphs but not these individual vertex-deletion types.

## value

PASS

The Chvátal graph is a canonical 4-chromatic vertex-critical triangle-free graph. A full, exact two-orbit classification of its independence-complex deletion/link behavior is a motivated natural graph-complex invariant: all 12 graph vertex deletions reduce chromatic number, while only four eliminate the independence-complex S2 homotopy. Complete 12-vertex finite classification is a substantive topological/chromatic contrast independent of the previously known global S2 claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
