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

# Exact-arithmetic verification

Run `python barbell_phase_verify.py` with SymPy; `DEPENDENCIES.txt` identifies the only external Python dependency. On the reviewed package the program returned:

`VERIFIED: 7 symbolic orbit formulas, 6 symbolic exact differences, 224 direct rational inverse checks, 32 exhaustive orbit minima.`

The independent matrix construction uses graph vertices indexed \(0,1\) for the two-vertex clique and \(2,\ldots,q+1\) for the larger clique; bridge endpoints are \(0,2\). The program compares each of seven leader-pair orbit formulas against exact rational inverses for sizes \(3\le q\le10\) and bridge weights \(1/7\), \(3/2\), \((q+2)/(q-2)\), and \(13/2\). It also symbolically verifies six algebraic difference factorizations.

These finite tests alone do not prove the universal theorem. The proof uses the exact symmetry decomposition plus positivity of factored polynomial coefficients on the entire parameter domain. No floating-point inference, external theorem prover or independent human audit was used. The general case of arbitrary clique sizes is not claimed.
