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

With Python 3, SymPy, and mpmath installed, run:

```sh
python tools/check_period.py
```

The script checks a symbolic conservation cancellation, a symbolic comparison-function derivative, and the strictly positive algebraic factor supporting monotonicity. It also numerically evaluates the original physical-time period integral at 18 combinations of turning amplitude, positive velocity feedback and positive restoring strength, including near-zero and very large restoring strengths. All numerical two-term residuals obeyed \(A^4\lvert T/T_{\mathrm{two\,term}}-1\rvert<17.634\) on the selected cases. Additional small-amplitude and monotone-sequence checks passed.

The universal \(O_\beta(A^{-4})\) assertion, the global period range, and strict period monotonicity are **analytic claims** proved in RESULT.md; no finite numerical test or symbolic identity alone certifies them. The independent mathematical audit remains unperformed. The two-term estimate excludes the singular limit \(\beta\downarrow0\), and originality does not include the previously studied \(\gamma=0\) axis.
