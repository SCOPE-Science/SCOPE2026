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

Run `python3 verify_binary_evolution_symmetry.py` using standard Python 3. The script enumerates all binary \(n\times n\) matrices for \(n=2,3,4\), selects invertible matrices by an independent bitwise Gaussian elimination implementation, checks all natural-basis permutations directly, and confirms the exact centralizer count of each transposition. The actual run produced:

```text
n=2: GL=6; transposition fixed=2 each; nontrivial=2; exactly-C2-transposition=2; asymptotic main count=2
n=3: GL=168; transposition fixed=8 each; nontrivial=24; exactly-C2-transposition=21; asymptotic main count=24
n=4: GL=20160; transposition fixed=192 each; nontrivial=1344; exactly-C2-transposition=1008; asymptotic main count=1152
VERIFY_OK
```

The program tests finite cases; the all-dimensions centralizer formula and probability asymptotic are proved separately in `RESULT.md`. No external computational certificate or independent verification has been claimed.
