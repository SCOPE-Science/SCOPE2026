---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and computational checks

Run `python3 verify.py` using Python 3 and its standard library. The program constructs the collision-free two-particle cubical deleted-product model directly from \(K_{p,q}\), for ten displayed parameter pairs between \((3,3)\) and \((6,6)\). It calculates the chain counts and mod-two boundary ranks, compares the resulting Betti numbers with the theorem, and independently enumerates all conjugacy-class pairs of part permutations to test the signed fixed-cell traces both with and without particle exchange. Small cases also check dimensions of the particle-exchange eigenspaces in second homology by exact modular arithmetic. All 880 character checks pass.

An expected final output line is:

`COMPLETE_BIPARTITE_TWO_POINT_CHARACTERS_VERIFIED 880`

For example, \((p,q)=(3,3)\) gives \((b_1,b_2)=(8,1)\) with degree-two exchange eigenspace ranks \((0,1)\); \((4,4)\) gives \((18,25)\) with ranks \((12,13)\); \((5,5)\) gives \((32,121)\) with ranks \((60,61)\).

These finite calculations are independent computational spot checks, *not* a proof for unbounded parameters. The mathematical argument uses the published mature-graph theorem, a natural first-homology identification, an exact equivariant Euler–Poincaré calculation valid for all \(p,q\ge3\), and rational symmetric-group character identities. No external proof assistant or independent audit has been used.
