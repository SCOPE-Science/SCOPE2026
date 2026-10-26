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
# Reproduction of finite checks

Run `python3 verify.py` with a standard Python 3 interpreter. No external packages are required.

The script computes every pair \((g,h)\) in \(UT_4(\mathbb F_q)^2\) for \(q=2\) and \(q=3\), using independently defined group-coordinate multiplication and inversion, and checks all three target fiber strata. It then checks \(q=4\) through finite-field outer-sextuple counts using \(\mathbb F_2[T]/(T^2+T+1)\). The expected terminal line is `VERIFY_OK_UT4_COMMUTATOR_FIBERS`. Actual observed checks: `FULL_UT4_GROUP_ENUMERATION 2 PASS 4096 pairs`, `FULL_UT4_GROUP_ENUMERATION 3 PASS 531441 pairs`, and `GF4_OUTER_SEXTUPLE_ENUMERATION PASS 16777216 pairs`.

These are finite corroborations. The general proof uses the displayed determinant and linear functional counts, valid in every characteristic. No independent mathematical audit has been performed.
