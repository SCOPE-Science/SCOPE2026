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

The exact periodic matrix was independently instantiated from its displayed exponential entries. For each tested period, the sign groups were split and the minimum Gram eigenvalue was compared to one minus the largest singular value of the cross group. An explicit phase formula verified the positive Hilbert-corner entries; the finite Hilbert comparison was checked numerically with a tolerance allowing accumulated floating-point roundoff.

Run `python checker.py` with NumPy installed. The standalone checker passed 343 assertions on 49 periods: all integers from 4 through 48, then 64, 72, 96, and 128. It depends on no external files. It does not perform exhaustive pattern enumeration, and numeric success is not a proof for all periods.

The analytical proof consists of a finite geometric-sum identity, diagonal phase factorization, positivity/entrywise comparison, Gram-block spectral identity, and the known de Bruijn–Wilf Hilbert-matrix eigenvalue asymptotic. The independent audit has not been performed.
