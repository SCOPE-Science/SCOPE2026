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
Run `python3 verify.py`.

The checker directly evaluates
\[
T_2(n)=\sum_{p^e\parallel n}ep^2
\]
on every prime-power and two-prime-support test case in a finite parameter grid. It confirms that the only fixed points found are
\[
16,\qquad27.
\]
It also checks the elementary inequalities used to close the two infinite proof branches over a finite regression range.

This finite replay is not the proof. The complete \(\omega(n)\le2\) classification is proved symbolically in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
