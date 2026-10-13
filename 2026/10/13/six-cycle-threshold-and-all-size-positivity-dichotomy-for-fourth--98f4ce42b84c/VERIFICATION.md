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

Run `python verify.py` from the extracted file set. The script uses Python's standard library only. It constructs the unit-rate cycle generators for sizes \(3\), \(4\), \(5\) and \(6\) and verifies the rational propagator numerator matrices by **coefficient identities over \(\mathbb Q[h]\)**, not by sampling finitely many values of the step size. It also verifies the polynomial row sums, the rational witness
\[
[T_6(7)]_{0,1}=-\frac{25354}{4790839},
\]
and the endpoint signs locating the unique quartic root between \(6\) and \(7\).

The all-\(n\) theorem uses the analytic discrete Green-function identity proved in `RESULT.md`. Auxiliary rational checks for a few cycle sizes are corroborative only and are not presented as an infinite proof. The sharp positivity statement is about the final rational matrix, not intermediate Runge–Kutta stages or floating-point implementation.
