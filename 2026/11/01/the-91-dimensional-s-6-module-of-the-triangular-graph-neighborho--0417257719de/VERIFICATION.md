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

Run `python3 verify.py` with standard Python 3 (no external packages). `verification_output.txt` is the recorded output from a successful full replay.

The verifier reconstructs every face and the integral simplicial incidence signs; it checks all chain-complex compositions, performs exact rational boundary reduction, computes Lefschetz traces by fixed oriented faces for the eleven partitions of six, checks every irreducible character inner product and reconstruction, and independently checks that all fifteen seven-cut facets are the open neighborhoods.

The proof establishes ordinary reduced rational homology and its natural symmetric-group module only; it does not certify integral torsion, equivariant generalized cohomology, or homotopy equivalence. The finite-group quotient conclusions use rational transfer after barycentric subdivision. No independent mathematical audit has been performed.
