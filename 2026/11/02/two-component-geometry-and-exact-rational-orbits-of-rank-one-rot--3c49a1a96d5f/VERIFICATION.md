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

# Verification of rank-one Lie Rota–Baxter classification

The standalone file `check_rankone_sl2_rb.py` contains its complete finite-field arithmetic, Lie bracket, projective enumeration, direct Rota–Baxter identity test, and explicit conjugation action. It has no dependencies outside the Python standard library.

Reproduce with `python check_rankone_sl2_rb.py`. Expected exact stdout is provided in `check_rankone_sl2_rb.txt`. The checker ran successfully using those exact current files, and output bytes agreed with the embedded expected output.

For \(q=3,5,7,9\), all \((q^2+q+1)^2\) pairs of projective lines were examined. The direct original bracket identity was checked for every pair, both on and off the solution locus, and was found equivalent to the geometric incidence condition. The \(q=9\) implementation uses \(\mathbb F_3[t]/(t^2+1)\), which is a field because \(t^2+1\) is irreducible over \(\mathbb F_3\). The projective solution counts were \(25,61,113,181\); the exact nonzero rank-one map counts were \(50,244,678,1448\), agreeing with the formula. Explicit \(\operatorname{PGL}_2\) enumeration over \(\mathbb F_3\) and \(\mathbb F_5\) reproduced the full predicted orbit-size multisets.

Verification marker: `RANK_ONE_SL2_ROTA_BAXTER_GEOMETRY_OK 4_FINITE_FIELDS 2_EXACT_ORBIT_CHECKS`.

Finite enumeration does not prove the arbitrary-characteristic-not-two geometry or the all-odd-prime-power orbit spectrum. The proof is the trace-pairing reduction, the rational tangent-incidence parametrization, and the explicit stabilizer and square-class arguments in `RESULT.md`. No independent external mathematical audit has been performed.
