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

The standalone source file `verify.py` uses Python 3.9+ and only standard-library modules. Run `python3 verify.py` from the package directory.

Actual run checks: independent recursive vertex-mask enumeration of every perfect matching of \(K_{2m,2m,2m}\) for \(m\in\{1,2,3\}\), including those avoiding an explicitly constructed fixed perfect matching; exact integer inclusion–exclusion checks through \(m=12\); and exact sparse-polynomial verification of the first- and second-order formal moments for four symbolic evaluation parameters. The output ended in `VERIFY_OK`.

Observed direct count pairs (avoiding, total) were \((4,8)\), \((825,1728)\), and \((819242,1728000)\) for \(m=1,2,3\), respectively. Exact polynomial moment checks confirmed a zero first-order coefficient and a \(3/128\) second-order coefficient.

Finite checks cannot establish asymptotic error bounds: the analytical cutoff and factorial-tail estimates in `RESULT.md` carry the proof. No higher-order coefficient, effective remainder constant, or full-distribution quantitative limit is verified or claimed.
