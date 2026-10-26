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

The standalone file `verify.py` constructs the open-neighbour adjacency of each labelled lollipop graph independently of the symbolic proof. It computes each configuration's unique orbit depth and primitive eventual period by following the finite functional graph, then tests the predicted maximum depth, number of extremal configurations, exact characterization of each extremal configuration and exact classification of primitive two-cycle states.

Execute `python3 verify.py` with a standard Python 3 installation. The recorded `verification_output.txt` must conclude with `LOLLIPOP_MAJORITY_VERIFY_OK`. The finite test range is \(3\le m\le8\), \(2\le\ell\le10\) and \(m+\ell\le17\), giving 53 graph instances and 768,032 labelled configurations, including boundary \(m=3,\ell=2\).

The graph-state enumeration is exhaustive only for the stated finite parameter range, not for all clique sizes or tail lengths. The all-size result instead follows from the full analytical proof in `RESULT.md`. The comparison to published literature is bounded to sources and sections actually inspected, not a claim of complete historical precedence screening.
