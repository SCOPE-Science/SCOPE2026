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

# Verification notes

The claimed statement is an analytic theorem about exact ultimate capture probabilities, not a Monte Carlo estimate. With the precise delta-sink normalization in RESULT.md, solve the two-equation killed resolvent for one Poisson-reset interval, then divide the two local capture fluxes. Cross multiplication leads to the scalar positive-denominator inequality \(A<H_B(t)\). The no-reset limit is \(B(1+A)/[A(1+2B)]\). The strict global inequality for \(B\le1\) follows from affinity of \(K(B,t)\) in \(B\), its negative endpoint values, and \(t<\sinh t\). For \(B>1\), the strictly positive Taylor slope at zero and decay to zero ensure a nonempty reentrant \(A\)-window.

Run `python3 check.py` to reproduce numeric checks of independent two-sink matrix solving against the exact odds formula at 175 parameter cases, representative envelope signs, and two brackets for \(A=11/10\), \(B=100\). The checker is an auxiliary calculation and cannot certify the universal inequalities. Its executable uses only the Python standard library.

Reviewed limits: the theorem proves at least two crossings, not exactly two; no general claim about other target placements; the shape of the maximizer \(C(B)\) is left as a variational characterization; no independent audit has been conducted. Literature-priority uncertainty persists because generic two-defect resolvents exist and some specialized sources may have been overlooked.
