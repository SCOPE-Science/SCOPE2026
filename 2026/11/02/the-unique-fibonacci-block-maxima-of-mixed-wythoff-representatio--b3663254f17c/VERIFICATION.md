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
# Verification and reproducibility

The attached `verify.py` uses only Python's standard library. Execute `python3 verify.py` from the package directory. The observed output was:

```
VERIFY_OK fibonacci_blocks=13 F_m_range=4..16 largest_endpoint=1597 complement_up_to=1597
```

The program uses \(\lfloor k\varphi\rfloor=\lfloor(k+\sqrt{5k^2})/2\rfloor\), evaluated using `math.isqrt` and integer arithmetic; the irrational input ensures no borderline equality. It separately enumerates all ordered positive lower-plus-upper representations through 1597, checks Beatty complementarity, checks exclusion from the upper-plus-upper sumset at Fibonacci indices five through seventeen, and checks every block's claimed maximum and unique location for indices four through sixteen. This is only finite corroboration. The general result is proved from exact Beatty and Fibonacci identities, the no-carry argument, and the previously established mixed-sum complement theorem. No independent audit has been performed.
