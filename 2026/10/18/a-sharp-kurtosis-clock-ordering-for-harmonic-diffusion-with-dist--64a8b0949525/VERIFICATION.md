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

The accompanying `verify.py` is standalone and requires Python 3, SymPy and mpmath. Run `python3 verify.py` alongside this file. Its current run gave `PASS: 428 independent arithmetic, quadrature, root and order assertions`.

The program recomputes stationary second/fourth moments by independent high-precision quadratures of their conditional formulas, compares them with the cumulant decomposition, checks the exact polynomial factorization, and checks root values and signs. The mathematical argument for all positive periods and all admissible reset laws is given in `RESULT.md`; numerical tests are not used as proof of parameter-uniform inequalities.

Scientific boundaries: the sign protocol ordering is after division by positive survival factor \(L_2\), the reset distribution must be centered with a finite fourth moment, and periodic stationarity means uniform equilibrium phase. Independent mathematical validation and external priority audit have not been performed.
