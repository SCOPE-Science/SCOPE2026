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

The numerical verification is reproduced by `artifacts/verify_m826.py`. It checks the Brill--Noether number, expected dimension, sextic node count, Severi quotient dimension, trigonal Hurwitz dimension, all factorizations of degree six with nontrivial cover degree, the dimension exclusion of the double-cover case, and the Coppens--Kato numerical threshold.

Recorded output:

`VERIFY_OK rho=-4 expected=17 delta=2 severi=17 trigonal=17 only_nonbirational_k=3 gonality_severi=4`

The checker does not substitute for the cited geometric theorems: irreducibility of the Severi and Hurwitz spaces and the cover/gonality theorems are literature inputs.
