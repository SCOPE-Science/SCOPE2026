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

# Exact verification instructions

From a directory containing the embedded files, execute:

```text
python3 certificate.py
python3 independent_check.py
```

Both programs use only exact integers, standard-library fractions, primality by full trial division, and integer divisor enumeration. The first prints \(21\) prefixes and \(6\) live residuals at length seven; \(18564\) prefixes and \(74\) live residuals at length eight; and zero valid completions for both. The second checks the same nonexistence by a separate depth-first denominator-bound recursion and reports terminal-node counts \(6\) and \(74\). Exact evaluation also verifies the displayed nine-term identity. The proof's finite-reduction step, not a computer timeout or imposed maximum on the last denominators, makes the output exhaustive.

The ordinary arithmetic checks were executed successfully. No independent audit has been performed, and no machine-checked proof formalization is claimed.
