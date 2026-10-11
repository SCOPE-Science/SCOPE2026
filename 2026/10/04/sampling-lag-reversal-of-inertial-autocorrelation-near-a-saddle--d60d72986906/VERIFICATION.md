---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact comparison is correct. In the overdamped regime, using r_-r_+=alpha and r_-+r_+=eta rewrites the derivative of the ratio-difference as a difference of two decaying exponentials with exactly one zero; the sign function starts at zero with positive slope and tends to a negative limit, so it has exactly one positive crossing. At critical damping the log ratio log(1+s/2)-s/4 rises then decreases to minus infinity, giving one positive root. In the underdamped regime the second-order bracket equals -1 at every odd half-period while the matched first-order autocorrelation stays positive.

## originality

PASS

Best-of-knowledge originality passes narrowly for the exact lag-domain classification. Classical damped-oscillator literature supplies the autocorrelation formula, and the accessible Ditlevsen source broadly notes that inertia/damping may enhance or reduce warning signatures. The audited theorem proves the sharper exact comparator result: a unique positive crossover in the overdamped and critical regimes and explicit infinitely many negative intervals in the underdamped regime. Resultary found no prior exact theorem.

## value

PASS

Fixed-lag autocorrelation is a standard early-warning statistic. The unique crossover and explicit negative lag bands precisely identify how sampling lag can reverse the comparison between first- and second-order linearized saddle-node models, turning a broad qualitative issue into an exact boundary theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
