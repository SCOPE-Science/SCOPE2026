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

The self-contained Python file `verify.py` was executed using its exact input as packaged, with its output retained in `verification_output.txt`. The checks exhaust all directed arc patterns on cycles of orders 3 through 6 (5,440 configurations) and establish exact-rational finite probability identities at two distinct retention parameters for orders 3 through 5. All 5,482 exact assertions passed. Additional limiting-formula sanity checks at four parameter values were run and do not constitute proof of distributional convergence.

The infinite-window weak convergence, Dirichlet spacing reduction, and Gumbel limit are justified by the arguments in RESULT.md, not by finite experiments. No proof assistant or external mathematical certification was used; independent auditing has not been performed.
