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
# Reproducibility and limits

`verify_periods.py` uses exact rational arithmetic to enumerate binary branch words, solve the affine fixed-point equation for each word, verify branch consistency at all iterates, enforce the **open** symmetric hole, and compare with the theorem's fixed-point formula. It checks all periods \(1\le n\le13\) at four rational choices of \(a\), including the two sharp parameter boundaries. Run with `python3 verify_periods.py` using the standard library. No numerical tolerance, timeout inference, or floating-point approximation enters these finite checks.

The main argument proves that every survivor for every real \(0<a\le2/5\) eventually reaches one of the identified periodic cycles. The finite checker cannot establish that universal quantifier or exclude periodic points of larger periods; the proof does that via the irreversible same-side transition inequalities and their exact equality case.
