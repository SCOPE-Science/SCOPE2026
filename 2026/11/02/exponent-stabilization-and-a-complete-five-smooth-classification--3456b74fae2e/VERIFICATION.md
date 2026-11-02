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
# Reproducible verification

Run `python3 verify_unit_generation.py` from this folder. The program uses only integer modular multiplication, gcd and Euler-totient counts, and compares incremental subgroup closure with a separate breadth-first closure. It checks all \(36\) clipped prime-power moduli and verifies each claimed threshold by checking both its generating property and its predecessor's failure, except for the trivial minimum \(1\). It also checks the reduction identity at each modulus \(1\le n\le2000\).

Actual output:

```
VERIFY_OK table_cases=36 stability_cases=2000 subgroup_methods=2 exact_integer=yes
CASE 4 G= 3
CASE 8 G= 5
CASE 42 G= 11
CASE 126 G= 13
CASE 30 G= 11
CASE 60 G= 13
CASE 120 G= 17
```

The finite audit is exact for its stated input range. Infinite exponent stabilization rests on a separately written Frattini-kernel proof; the finite all-parameter classification follows because only the 36 stated reduced cases can occur. Re-running the code does not constitute independent mathematical validation of the proof or historical priority.
