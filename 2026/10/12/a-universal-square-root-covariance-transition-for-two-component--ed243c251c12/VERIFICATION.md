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

# Computational verification and analytic limits

`verify.py` is a standard-library-only independent enumerator of every Prüfer code for labeled trees on vertices \(0,1,\ldots,n\), which are bijective with rooted forests on \([n]\) after deleting the hub vertex \(0\). For all \(n=2,3,4,5,6\) and rational fugacities \(t=1/2,1,2\), it aggregates weights \(t^K\), computes each \(Z_k\) directly from connectivity, and checks the normalization, all expected component-size counts, and all distinct-size product moments against the derived formulas. These are exact fractions, not floating-point tolerances.

Recorded execution: `EXACT_ENUMERATION_PASS cases=15 checks=180 enumerated_weighted_tree_cases=54741`. Verification can be repeated with `python3 verify.py`; no third-party dependencies are needed. The analytic derivative gives the strict sign theorem and the trigamma expansion gives the infinite-size limit. The finite enumeration cannot certify those universal statements. No independent scientific audit has been performed.
