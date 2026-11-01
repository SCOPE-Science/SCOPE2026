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

# Reproduction checks

Run `python3 toroidal_cut_checker.py` using only the Python standard library. The program independently generates the graph and all Alexander-dual faces for parameter pairs \((5,5)\), \((5,6)\), and \((6,6)\). It confirms the complete face counts, checks every tetrahedron is an elementary square, replays and verifies the freeness of the proposed elementary-collapse pairs, checks that the remaining filled two-complex is precisely the chosen torus triangulation, and separately computes all mod-two boundary ranks.

Expected dual face vectors: \((25,300,150,25)\), \((30,435,180,30)\), and \((36,630,216,36)\). Expected boundary ranks: \((24,124,25)\), \((29,149,30)\), and \((35,179,36)\). Expected reduced dual Betti numbers: \((152,1)\), \((257,1)\), and \((416,1)\) in degrees one and two. The final output marker is `TOROIDAL_THREE_CUT_DUAL_CHAIN_CHECKS_OK`.

These checks are finite corroboration only. The universal proof is the face classification, free-face collapse and integral Alexander-duality calculation in `RESULT.md`. The proof excludes cycle factors of length four; neither an equivariant classification nor a homotopy classification of the original cut complex is verified. Independent audit has not been performed.
