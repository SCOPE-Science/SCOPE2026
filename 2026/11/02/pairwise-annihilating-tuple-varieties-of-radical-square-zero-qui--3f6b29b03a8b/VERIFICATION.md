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

# Verification of pairwise-annihilating quiver tuples

Execute the accompanying standalone Python 3 script from the directory containing it:

```sh
python checker.py
```

The script uses the original vertex-and-arrow multiplication of the quotient quiver algebra, with all products of two arrows zero, and independently checks every tuple over each finite test field. Seventeen exhaustive cases cover fields of orders two, three and four, loops, parallel and opposing arrows, paths, cycles and arities one through four. The order-four field uses explicit finite-field multiplication via an irreducible polynomial. Every pair of distinct tuple indices is checked in both orders; no individual square-zero equation is imposed.

The expected output is included as `checker_output.txt`, ending with `ANNIHILATING_QUIVER_TUPLES_OK 17`. The individual reported totals can be compared directly. This is finite corroboration only: the universal formulas, geometric assertions and inverse reconstruction are proved algebraically in `RESULT.md` rather than inferred from testing. The review is not independent validation.
