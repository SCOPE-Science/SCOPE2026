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

# Reproduction and scope

Run `python3 verify_cubic_windows.py` with Python 3 (standard library only). Successful execution prints exactly one line beginning `VERIFY_OK` and confirms the values recorded below. The checker calculates the gcd of twelve consecutive length-\(2m\) windows independently for both standard Fibonacci and Lucas sequences and every \(1\le m\le160\); it compares the result against the closed formulas. It also tests the exact cubic-sum identity and normalized half-length reductions at 1,600 explicit pairs, four-term normalized gcd formulas at 1,001 integer parameters, and the fourth-order recurrence for both normalized sequences at six indices for each parameter. All computations are exact integers, not floating point.

Observed output:

```
VERIFY_OK windows=320 signed_sum_checks=1600 linear_parameter_cases=1001 k6_F_actual=2_proposed=4 k6_L_actual=2_cube_difference_gcd=28
```

The infinite theorem is proved algebraically in `RESULT.md`. The program provides independent finite consistency checks and reproduces illustrative counterexamples; no finite range is used to infer an unbounded conclusion. Source comparisons were literature searches, not an independent referee validation. There is no external independent audit evidence.
