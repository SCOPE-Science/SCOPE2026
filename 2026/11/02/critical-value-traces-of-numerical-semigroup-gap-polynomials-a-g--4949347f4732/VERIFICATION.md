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

# Reproducible exact checks

Run `python3 verification/critical_trace_verify.py` with Python 3 and its standard library. The program uses exact integer and rational arithmetic and contains no external dependencies.

```text
VERIFY_OK semigroups=276 trace_companion_vs_log=828 Hessian_entry_checks=207 symmetric=24 pseudosymmetric=10 other=242 exact_rational=yes
CASE F=2 genus=2 rank=1 trace=-1/4
CASE F=5 genus=4 rank=2 trace=-6/5
CASE F=6 genus=4 rank=1 trace=-3/4
CASE F=11 genus=6 rank=0 trace=0
```

The checker enumerates semigroups with \(1\le F\le13\), compares two independently implemented trace evaluations at three coefficient vectors per semigroup, and reconstructs the low-F Hessian by exact interpolation from companion-matrix traces. All 828 trace comparisons and all 207 Hessian-entry comparisons passed. Neither these finite checks nor matrix computations replace the all-F proof. The source's general Newton relations and the Frobenius reflection count are derived explicitly in `RESULT.md`.
