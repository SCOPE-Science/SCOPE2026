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

# Reproducibility

Run `python3 verify.py` using the Python standard library. Its rational tests cover the cyclic inverse-Laplacian and unit-cell transfer identities for every cyclic order from \(3\) to \(60\), all contiguous-block energy formulas in that range, explicit exact real extremizers for all those orders, and an exhaustive sign-vector maximum for orders \(3\) through \(13\). It also compares the analytic complex and real constants numerically through order \(299\). The checker should print a single `VERIFY_OK` line. No external data are needed.

# Analytic dependencies and limits

The exhaustive finite search is corroboration, **not** the infinite all-order argument. Universality comes from the proved Green identities, exact unit-cell transfer to the continuous circle, the established circle Riesz rearrangement inequality, and a symbolic block sum. Standard Fourier diagonalization proves the complex result. Independent audit has not been performed.
