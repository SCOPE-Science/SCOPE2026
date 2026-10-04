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

The structural reduction was checked independently by `verify.py` on a finite range. The script factors each tested integer, computes its arithmetic derivative exactly, and compares the equation `D(n)=k*n` with the exponent criterion `a_p=p*c_p` and `sum(c_p)=k`.

The infinite asymptotic is established in `RESULT.md`; finite enumeration is not used as proof of the limit. The analytic dependencies are the prime number theorem and elementary weak convergence of regularly varying counting measures.
