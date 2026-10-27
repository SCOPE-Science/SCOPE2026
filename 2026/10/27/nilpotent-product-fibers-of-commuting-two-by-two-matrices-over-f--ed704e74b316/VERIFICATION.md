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

# Reproducibility and scope

Run `python check.py` with a recent standard-library Python 3 interpreter. The checker enumerates every ordered pair of \(2	imes2\) matrices over each of the fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). Its multiplication in \(\mathbb F_4\) uses \(\mathbb F_2[X]/(X^2+X+1)\), so the verification includes a nonprime field.

For each field, the program independently computes \(AB\), \(BA\), the nilpotence test (trace and determinant both zero), each individual nilpotent-product fiber, the commuting-pair denominator, and both aggregate counts. It asserts the claimed exact formulas and ends with `VERIFY_OK` on success.

Observed outputs: \(q=2\): 88 commuting, 52 qualifying, 40 zero fiber; \(q=3\): 945 commuting, 321 qualifying, 225 zero fiber; \(q=4\): 5056 commuting, 1096 qualifying, 736 zero fiber; \(q=5\): 18625 commuting, 2785 qualifying, 1825 zero fiber. All nonzero nilpotent fibers agree with \(2q(q-1)\).

The code is exhaustive for the four finite fields only. The uniform theorem for every prime power follows from the centralizer-and-orbit proof, not from extrapolating these tests. There is no independent audit certificate.
