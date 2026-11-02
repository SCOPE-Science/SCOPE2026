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

# Computational verification and proof boundaries

The script `verify_extraspecial_involution_orbits.py` uses only the Python 3 standard library. Execute `python3 verify_extraspecial_involution_orbits.py`. It constructs explicit group multiplication tables from the class-two quadratic central-extension law for each of the plus/minus extraspecial groups at \(m=1,2\). It enumerates all commuting involution tuples of lengths \(r=1,2,3\), and independently enumerates all quotient quadratic isometries and applies lifted automorphism actions and central twists.

It checks full orbit decompositions using union-find, directly re-evaluates orbit invariants, and matches the symbolic formulas for both homomorphism and orbit counts. The following checks passed:

| \(m\) | Type | \(r=1\) orbits | \(r=2\) orbits | \(r=3\) orbits |
|---|---|---:|---:|---:|
| 1 | plus | 3 | 10 | 36 |
| 1 | minus | 2 | 4 | 8 |
| 2 | plus | 3 | 11 | 50 |
| 2 | minus | 3 | 10 | 36 |

The final script status is `VERIFY_OK` (twelve parameter cases). The small parameter computations neither verify the general Witt extension theorem nor constitute an infinite proof. The mathematical proof in `RESULT.md` establishes the general statement, using the classical finite quadratic-space extension theorem and a direct presentation/lifting argument for extraspecial groups. No independent external audit was conducted.
