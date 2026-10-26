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

# Reproducibility and limits

Execute `python3 verify.py` from a directory containing the standalone script. It uses only the Python standard library.

The script enumerates surjections through independently constructed repeated-pair/permutation data for \(2\le n\le7\). For \(2\le n\le6\), it additionally enumerates all coordinate words directly and compares the complete sets. For \(2\le n\le5\), it separately constructs the star-transposition network and compares every edge of the surjective-word exchange graph with pairwise incidence in the network, checking the canonical bijection and exact edge/triangle counts. For \(2\le n\le7\), a complete breadth-first search from a representative vertex checks connectedness and the predicted maximum distance. The theorem's proved vertex-transitivity permits a single-source eccentricity check to certify the finite instance's diameter. The run ends with `ALL_VERIFY_OK`.

The unbounded-parameter theorem does not depend on finite search. Its correctness rests on the bijection, the split/merge metric calculation, and an explicit diameter-realizing pair of root edges. No independent validation or external certificate is asserted.
