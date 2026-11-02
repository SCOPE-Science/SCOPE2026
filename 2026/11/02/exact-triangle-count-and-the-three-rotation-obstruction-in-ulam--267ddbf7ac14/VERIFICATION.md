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

# Verification

The proof is contained in RESULT.md and is not delegated to a finite experiment. The core identity is that the disagreement-edge set of any two permutations connected by a labeled single deletion is a nonempty star. Symmetric differences of three such stars admit only the common-center configuration or the three-edge exceptional configuration. This gives the exhaustive classification.

For a finite independent check, run `python3 verify.py` in a directory containing the provided script. It uses explicit symbol-deletion reads to test adjacency, rather than relying on the inversion-star proof. It enumerates all vertices for lengths 2 to 6 and checks the identity neighborhood for lengths 7 to 14. Expected output ends in `VERIFY_OK full_vertices=872 local_orders=7..14`.

Observed triangle totals for lengths 2 through 6: `0, 8, 112, 1320, 15360`. The script checks unique classification into shared-read and triple-rotation types, as well as vertex degree and the exact formula. No experiments at greater lengths, external formal proof or independent audit are claimed.
