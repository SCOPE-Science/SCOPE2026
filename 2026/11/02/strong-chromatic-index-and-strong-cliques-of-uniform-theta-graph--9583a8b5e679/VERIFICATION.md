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

# Reproduction and limits

Run `python3 verify_theta.py` in a standard Python 3 installation. There are no optional packages or external data files.

The script constructs the simple graph adjacency and then the conflict relation from the four possible endpoint-neighbor comparisons. It checks every distinct conflicting edge pair against the explicit coloring. Its separate backtracking decision procedure tries the proposed optimum and one fewer color for small instances; its maximal-clique search computes the clique number independently for other small instances.

Verified execution:

`VERIFY_OK constructive_graphs=464 exact_chromatic_instances=30 exact_clique_instances=50`

The 464 direct checks range over \(3\le k\le18\) and \(2\le\ell\le30\). Exact chromatic tests cover \(3\le k\le5\), \(2\le\ell\le11\); exact clique tests cover \(3\le k\le7\), \(2\le\ell\le11\).

These are finite calculations. The stated theorem for all \(k\) and \(\ell\) relies on the proof in RESULT.md. The comparisons with prior literature constitute a bounded source review, not an independently confirmed priority certificate.
