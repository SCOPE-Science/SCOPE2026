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
# Verification details

`checker.py` independently computes every centered real supremum-norm row by enumerating the 70 balanced sign vectors on eight states, for 343 triples of rational eigenmultipliers. An exact rational tie case is also checked. A separate numerical loop evaluates independently constructed Markov rows for 24 parameter/time combinations. Three small-time tests compare the derived quadratic coefficient with a finite difference, for 371 grouped cases in total; all pass.

The exact proof relies on finite likelihood ordering and the strictly decreasing positive integral \(J(u)=h(u)\sinh(2u)/(2u)\), with \(h(u)=\log\coth u\). Checking finitely many parameters is not a proof of strict monotonicity, uniqueness at every rate triple, or complex-space norm equality; these follow from the analytic argument in `RESULT.md`.

The independent-audit channel was not performed.
