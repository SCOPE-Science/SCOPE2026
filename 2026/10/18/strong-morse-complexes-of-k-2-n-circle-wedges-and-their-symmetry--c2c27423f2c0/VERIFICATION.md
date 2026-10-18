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

# Verification of the mathematical claim

The full proof is in `RESULT.md`. Run `python3 verify_strong_k2n.py` from the extracted package directory. The program uses no network or third-party dependencies. It enumerates every strict vertex order for the bipartite graphs with two hubs and two through seven leaves, constructs the associated strong gradient, and takes all subfaces. It compares those exact simplicial face sets with the structural decomposition; computes mod-two simplicial homology; and checks the full signed simplicial Lefschetz character for all leaf permutations and both choices of hub exchange for up to five leaves. `verification_output.txt` is the recorded successful run.

The general homotopy equivalence and integral action are supplied by the structural proof, not by tests. The homology calculation is made using the finite CW quotient with two contractible regions and three transverse edges per leaf. The verifier therefore tests predictions rather than purporting to prove an infinite result.
