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

The proof reduces liar domination on \(K_{n_1,\ldots,n_r}\) to a part-capacity test. The accompanying `verify.py` reimplements the original definition directly from graph neighborhoods and compares it against that test for every ordered positive multipartite profile through total order \(9\).

The replay also forms the predicted cardinality polynomial by truncated binomial products, compares every coefficient with direct subset enumeration, and checks the minimum-cardinality feasibility formula.

Expected replay output:

`VERIFY_OK profiles=501 subset_checks=173736 coefficient_checks=4551 gamma_checks=501 max_order=9`

The verification is finite and does not establish the theorem for unbounded order; the structural proof in `RESULT.md` does that. The primary full text of Roden and Slater (2009) was not available in the inspected lawful sources, so the originality review treats its reported complete-bipartite scalar results as prior-covered and records the remaining bibliographic risk.
