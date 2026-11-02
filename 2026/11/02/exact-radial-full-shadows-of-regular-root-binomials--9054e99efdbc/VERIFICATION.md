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

## Analytic checks

The derivative identity for \(z^rQ(z^d)\) is exact, and the recurrence counts every degree and zero. The root-preservation argument uses Rolle's theorem for \(Q'\) and for \(y^{r/d}Q\) on the positive axis. The last step uses the published connectedness theorem for the limiting core of an arbitrary polynomial.

## Reproducibility

Run `python CHECK.py` with SymPy installed. The program uses exact polynomial expansion and rational isolating intervals, not floating-point zero plotting. It independently checks 560 finite descendants and prints `CHECK_OK: 560 exact symbolic descendant identities and rational isolating intervals`. The check is finite and does not certify the arbitrary-degree or all-power assertion; the proof handles those quantifiers.

## Limits and audit status

No computer algebra system was used as a substitute for the connectedness theorem. The inspected literature covers the quadratic case and a selected Rodrigues derivative order, so neither is claimed as novel. Historical priority and proof correctness have not been independently audited.
