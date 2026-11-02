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

# Reproduction and limits

Run `python3 verify.py` in the directory containing this file. Python 3 standard library suffices. The program uses exact integers, a smallest-prime-factor sieve, Legendre factorial valuations, and cross-multiplication of rational ratios.

Observed output:

```
VERIFY_OK composite_pairs=1430 two_step_hits=60 prime_pair_hits=55 exceptional=[8, 15, 20, 25, 34] one_step=[4] independent_factorial_checks=2047 exact_integer=PASS
```

The script checks all composite consecutive argument pairs beginning at integers \(2\le m<2048\), not a sample. It does not test infinitely many parameters. The unbounded range is proved separately by the inequalities in `RESULT.md`, Step 3. Neither an external referee's review nor an independent audit has been performed.
