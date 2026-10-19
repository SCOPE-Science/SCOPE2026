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
# Verification record

Run `python3 verify.py` in this extracted folder. The standard-library-only verification compares the block spectral trace with direct numerical inversion of full pinned Laplacian matrices, tests exact rational signs of the cubic for the reentrant \(K_{6,2}\) example, checks boundary derivatives, budget conservation, marginal equalities and random asymmetric feasible alternatives. The run reported `PASS 2302 finite cross-checks` and switch budgets approximately `3.34679965326` and `10.3824948581`. These are independently coded numerical cross-checks, **not** an independent scientific audit. The finite checks do not prove the all-parameter theorem; the analytical proof is in `RESULT.md`. No formal verification or external expert evaluation was performed.
