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

Run `python3 verify.py` from the extracted package (Python 3, standard library only). A passing execution prints:

`TRANSITION_MATCHING_UNIVERSALITY_PASS direct_n<=10 words_n<=16 transfer_n<=90 means_m<=11`

The verifier compares the defining scattered-subsequence test, a greedy arch implementation, and a path-matching dynamic program through binary length ten. It checks exact joint histograms for every word through length sixteen, independently computes two-state generating-function coefficients through length ninety, and checks conditional means by every transition-position subset through eleven edges. All computations are finite; the infinite coefficient identities, structural graph theorem, and conditional convergence follow from the mathematical arguments in RESULT.md, not from enumeration. No independent audit is asserted.
