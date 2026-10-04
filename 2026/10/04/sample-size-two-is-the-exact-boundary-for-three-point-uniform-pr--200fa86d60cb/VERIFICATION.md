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
The proof was checked from the exact three-point distribution. The formulas for the first two moments of the maximum and for the product of the minimum and maximum follow from exhaustive event partitions. Differentiating the resulting rational correlation at the uniform mass vector reduces its sign to \(D_k\). The initial values \(D_2=6\) and \(D_3=248/9\) are exact; for \(k\ge4\), the analytic recurrence bound on \(E_k\) proves \(D_k>0\).

`verify.py` independently enumerates finite samples for selected small sizes with exact rational arithmetic and checks the symbolic derivative identity and finite stress values. It is a consistency check, not the proof of the universal quantifier. No global maximizing probability vector is asserted.
