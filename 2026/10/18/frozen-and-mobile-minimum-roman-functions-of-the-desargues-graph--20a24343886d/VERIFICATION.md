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

# Reproducibility and verification
The two checks require Python 3 with its standard library only; no external data, dependencies, connectivity or random seeds. With the package files in their relative positions, execute `python3 checks/verify_cyclic.py` and `python3 checks/verify_incidence.py`. Exact recorded stdout is in `checks/verify_cyclic_output.txt` and `checks/verify_incidence_output.txt`. The complete canonical `data/states_edges.json` lists every optimum Roman labeling and every permissible typed edge. Its SHA-256 is `579663ada37b90a8335fc3aa8e3b14b950f4a9288ab25e2a886816a7d31bfa81`.

The first program enumerates all \(2^{20}\) support masks for label \(2\), computes their forced one-labels, classifies minimum weight and all change operations, performs exhaustive breadth-first search, and checks a rotating automorphism permutes the five nontrivial components transitively. The second constructs the middle-level subset-incidence model independently, checks its explicit isomorphism to \(P(10,3)\), enumerates all relevant support sets with size at most six (all larger sets have weight at least fourteen), scans every unordered pair of optimal assignments for an allowed operation, and independently verifies graph distances and profiles. It also compares the complete resulting state and edge lists with the packaged certificate.

From the delivered JSONL package, all five standalone files were extracted and both programs were executed again from the extracted package paths. Both produced `VERIFY_OK` with output matching the recorded stdout byte-for-byte. The verification is an exhaustive finite computation for this specific graph; it supplies no infinite-family generalization. Public literature comparisons and the documented scientific self-review do not constitute independent audit or priority certification.
