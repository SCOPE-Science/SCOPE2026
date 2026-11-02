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

From the artifact root run `python3 verification/verify_tripartite.py certificates/tripartite_signatures.csv`. It independently computes both the nine-cohort factor dynamics and explicitly labelled vertex dynamics on the minimal representative of every one of the \(17{,}576\) capped initial-color signatures. It asserts the complete tail/period histogram, the period-existence and maximum-tail predicates on the \(84\) sorted size classes, and exactly matches all labelled configurations on four further graph triples. The script generates the certificate CSV and prints `ALL_QUOTIENT_AND_MICROSCOPIC_CHECKS_PASSED`. A recorded successful local run is provided in `verification/run_output.txt`.

# Limits

The finite enumerator is a proof only together with the exact cohort-size truncation lemma and the all-size feasibility cutoff at shore size seven in RESULT.md. It establishes no claims about other graph families, larger thresholds, or randomness. Independent audit has not been performed.
