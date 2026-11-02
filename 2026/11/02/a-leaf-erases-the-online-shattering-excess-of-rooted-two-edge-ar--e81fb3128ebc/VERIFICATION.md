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

Run `python3 verify_poset.py` and `python3 verify_product.py` with Python 3. Both programs require only the standard library and terminate with `POSET_ENUMERATION_ALL_PASS cases=20` and `ABSTRACT_ALL_PASS cases=20`, respectively. Both programs were executed and the announced output markers were observed before packaging. They use distinct representations of the hypothesis family and independently implement the complete binary split recurrence.

The direct program tests all possible fixed supports as well, not merely sample supports. The tested parameter set is all \(0\le t,s\le4\) with \(3^t2^s\le175\). These checks do not prove the theorem for unbounded parameters. The proof of that claim consists of the exact first-query case distinction and induction in `RESULT.md`.

The count \(1+3^t2^s\) is exact for every parameter by elementary independent arm choices. The only unproved topic noted here is whether any prior source gives an equivalent specialized family formula. No independent audit has been conducted.
