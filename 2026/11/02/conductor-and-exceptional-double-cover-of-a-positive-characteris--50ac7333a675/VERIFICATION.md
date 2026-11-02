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

The local calculations in `RESULT.md` show that the ordinary Nash blowup charts have equation \(x^2t=z^{2m}\), while normalization adjoins \(w=z^m/x\) with \(w^2=t\). The conductor calculation is purely algebraic: \(S_x=R_x+R_xw\), \(xS_x=(x,z^m)\), and the quotient inclusion \(k[z,w^2]/(z^m)\subset k[z,w]/(z^m)\) has zero conductor. These identities suffice for all \(m\).

Run `python3 verify_conductor.py` using the Python standard library to reproduce the finite semigroup check for \(1\le m\le16\). Observed output: `NASH_CONDUCTOR_SEMIGROUP_16_CASES_OK`. The finite test is not an all-\(m\) certificate and does not assess scientific originality. External independent audit is not performed.
