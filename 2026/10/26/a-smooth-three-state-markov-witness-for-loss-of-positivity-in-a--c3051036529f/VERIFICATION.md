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

The analytic verification is in `RESULT.md`. It checks: (1) each generator pulse has nonnegative off-diagonal entries and zero column sums; (2) the pulse amplitudes and widths give a bounded \(C^3\) matrix function; (3) the eight sampling fractions for formula (3.19) are distinct and only the two intended nodes are nonzero for each \(h_n\); (4) the two remaining matrix exponentials give the stated exact coordinates; and (5) strict negativity follows from \(g'(s)>0\) for \(s>0\). The included `verify.py` checks the exact closed form at three decreasing step sizes with high-precision decimal arithmetic. Finite checks supplement but do not replace the analytic proof. Independent audit and independent validation remain unperformed.
