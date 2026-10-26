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

# Reproducibility and proof limits

Run `python3 verify_minimal_forts.py` from this directory. It uses only Python standard-library modules. The script constructs \(T_n\) adjacency directly from edge incidence in \(K_n\), enumerates all \(2^{\binom n2}\) vertex subsets for \(n=3,4,5,6\), checks every nonempty candidate against the original fort definition, and extracts inclusion-minimal forts by inclusion comparisons. It then compares the exact sets with the two structural families and compares size histograms against an independently computed labeled star-component recurrence.

Actual output from execution of the delivered script is in `VERIFY_OUTPUT.txt` and ends in `VERIFY_OK`. For \(n=6\), the script checks all \(32768\) subsets and finds exactly \(308\) inclusion-minimal forts with cardinality profile \(35,195,78\) at sizes \(3,4,5\). The direct finite experiments are sanity checks, not proofs for arbitrary \(n\). The infinite statement is derived from the edge-incidence lemma, the minimal-edge-cover characterization, and the labeled exponential formula in `RESULT.md`.

The literature comparison identifies a published minimum-fort-size consequence for Johnson graphs, but does not assume that minimum-size information proves the all-size classification. Source access and bibliographic priority limitations are set out in `RESULT.md` and `REVIEW.md`. Independent audit: not performed.
