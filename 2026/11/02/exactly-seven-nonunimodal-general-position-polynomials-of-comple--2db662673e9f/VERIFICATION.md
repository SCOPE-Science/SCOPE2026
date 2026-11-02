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

# Verification evidence and reproducibility

Use Python 3.10 or later and execute `python3 verify.py` from the directory containing the files. No third-party dependencies or network access are required.

The verifier reconstructs the complete bipartite graphs and finds each graph distance by breadth-first search, independently of the coefficient theorem. It enumerates every vertex subset, rejects those containing any triple with a vertex on a shortest path between the other two, and compares the resulting cardinality polynomial with the formula. It checks 36 graph instances and 530604 subsets. These instances include all seven anomalous part-size pairs and two balanced larger cases.

It also checks all 11325 unordered positive parameter pairs with the larger part at most 150, comparing the exceptional-case rule against every coefficient sequence, verifying log-concavity of the auxiliary binomial tail and directly evaluating the product factorization. The script outputs the exact small-parameter difference tables required by the proof, and ends with `VERIFY_OK` on success.

The finite checks do not certify every integer pair. Infinite correctness rests on the mathematical argument in `RESULT.md`: structural reduction, log-concave convolution, and exact inequalities for the three regimes of the larger part. All certificates here are same-authority computational checks; no independent audit has been carried out.
