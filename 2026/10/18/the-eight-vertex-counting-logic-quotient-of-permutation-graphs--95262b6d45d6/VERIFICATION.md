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

# Reproduction

Install the exact dependency pinned in `requirements.txt` and run `python3 verify_permutation.py`; compare standard output to `verify_output.txt`. It exhausts \(n!\) inversion-graph presentations at every order \(1\le n\le8\), interns every colour-refinement tuple across all graphs with *no hashes*, checks the class partitions agree after \(n\) and \(2n\) rounds, and compares adjacency-preserving bijections with NetworkX's exact graph-isomorphism decision. It finishes `EXACT_PERMUTATION_VERIFY_OK`.

Run `python3 verify_independent.py` and compare standard output to `independent_output.txt`. Its generator and refinement are separately coded, and graph-isomorphism comparisons are again exact, but its WL signature uses a cryptographic digest: therefore this run is supporting corroboration, not the proof certificate.

Exact coverage proves the finite class counts and multiplicities, not any beyond-eight formula or independent validation. The underlying correspondence with \(C^2\) is established theory; independent expert review and an exhaustive priority check have not been performed.
