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

## Reproducibility
Install the specified symbolic dependency from `requirements.txt` and run `python verify.py`. The script reconstructs the scalar RandProx-LC steps, verifies symbolic moment factors, differentiates the exact cumulative risk, checks the algebraic optimizer and compares fully enumerated rational Bernoulli trees with the closed-form moments over 96 parameter/horizon tuples. All assertions must pass and it prints a success marker.

## Mathematical evidence boundaries
Exact rational enumeration through six iterations does not prove the result at arbitrary iteration counts. The analytical proof in `RESULT.md` uses iid conditional expectation, a geometric series, a strictly increasing derivative numerator and asymptotic radical expansions. The admissibility conclusion beyond \(\gamma\tau\le p\) is specific to the displayed quadratic; no general-purpose numerical stability guarantee follows.

## Independent status
No independent audit, third-party verification or priority certification has been performed.
