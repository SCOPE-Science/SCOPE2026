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

# Verification of the rook-graph general-position polynomial

The proof in `RESULT.md` is exact and valid for every integer \(m,n\geq1\). The executable checker `verify.py` (Python 3 standard library only) independently constructs forbidden geodesic triples, enumerates all selected vertex sets for 50 positive-side boards with at most 16 cells, tests selected-edge-component star structure separately, and compares the resulting coefficient sequences with the formal recurrence. The test covers exactly 576,650 vertex subsets. It then tests 484 ordered positive parameter pairs through side lengths 22 for symmetry, degrees, leading multiplicities and the first three coefficients. A captured output file `verification_output.txt` is included; the final line is `VERIFY_OK`.

Run `python3 verify.py` from the extracted artifact directory. An end-of-run marker is a reproducibility check of the executable, not a certificate of infinite validity, originality, independence, or correctness. The core proof relies only on the geodesic/P4 equivalence, the component structure lemma for bipartite graphs, and the standard labeled exponential formula. A computer is not necessary to establish those three arguments. No external files, private resources or network operations are required.
