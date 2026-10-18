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
# Verification

Execute `python check_friedman.py` with Python 3.9 or later. All dependencies are in the standard library. It reports 889 finite assertions (rational identities are checked exactly; square-root upper bounds are checked numerically): rational transition probabilities and killed-survivor first moments through twenty time updates; independent histories enumerated by urn counts; the binomial reflection formula; and finite conditional domination inequalities. The output also prints short exact tables of first-return masses and survival probabilities.

**All-time proof checks.** The essential analytic identities are the killed recurrence \((n+1)a_{n+1}=na_n+s_n\), the symmetric reflection estimate \(Q_m(x)\le2x/\sqrt m\) for integer \(m\ge1\), and the resulting bootstrap inequality \(s_{2n}\le2n^{-3/2}(1+\sum_{k<n}s_k)\). Each is proved for all admissible states/times in the result, not inferred from the checker. Successive improved bounds yield summability of the survival sequence and then the stated tail. The precise tail constant and endpoint moments are unproved.
