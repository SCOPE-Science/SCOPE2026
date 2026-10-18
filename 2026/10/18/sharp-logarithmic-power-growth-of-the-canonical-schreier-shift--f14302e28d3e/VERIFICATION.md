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

# Verification and limits
The proof is analytic: (i) pull back each admissible image set, (ii) cover it by at most \(\lceil\log_2(n+2)\rceil\) admissible geometric-rank blocks, (iii) insert the finite harmonic test vector, and (iv) apply integral comparison and the harmonic-number expansion. A separate Baire argument gives residual unbounded-orbit behavior. The numerical checks are finite and do not establish any infinite statement on their own.

`check.py` uses Python's standard library. Run `python check.py` from a directory containing the extracted file. It performed 10,657 finite diagnostics, covering harmonic inequalities, geometric partition sizes and two-sided bound compatibility. It does not certify publication priority or provide independent scientific assessment.
