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

Run `python3 check.py` in the directory containing this document, and compare the output to `check_output.txt`. Both are packaged alongside this report.

The checker evaluates exact and floating-point finite instances of the monomial moment inequalities and verifies root-of-unity angular orthogonality. Its reported successful finite assertions cannot establish the infinite-parameter claim. The proof in `RESULT.md` establishes the moment comparisons, dyadic exponential-peak lemma, positive lower bound, and uniform constructive upper bound for all stipulated parameters.

The sampling weights are positive, sites lie in the open unit disk in the construction, and the lower bound permits arbitrary angular layouts and positive point weights. No outside certificate or independent validation is asserted.
