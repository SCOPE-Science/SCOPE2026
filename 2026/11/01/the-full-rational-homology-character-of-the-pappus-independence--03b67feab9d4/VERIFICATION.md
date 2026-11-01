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

# Reproducibility

Run `python3 verify_pappus_full.py` in Python 3 using only its standard library. This reconstructs the Pappus graph, every independent simplex, an acyclic Forman matching on the full face poset, the exact automorphism group and conjugacy classes, and two independent fourth-homology character algorithms. The calculations are exhaustive for the one fixed graph. Expected output is in `verification_output.txt`.

The full cycle/centralizer table is the result. The earlier cyclic-subgroup character is reproduced as a consistency check, not independent certification. No outside theorem about this graph's specific character is assumed; standard simplicial Lefschetz and Forman discrete Morse results are used. No independent mathematical audit has been performed.
