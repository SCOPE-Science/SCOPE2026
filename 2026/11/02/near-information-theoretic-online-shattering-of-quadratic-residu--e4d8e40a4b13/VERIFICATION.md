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

The proof establishes a uniform result for every odd prime-power field. `check_paley.py` and `check_output.txt` are standalone reproducibility supplements. To reproduce the finite checks, use Python 3.10+ and run `python3 check_paley.py` in this directory. No nonstandard Python modules are needed.

The checker enumerates actual finite-field nonzero square predicates, computes exact Littlestone depth via version-space recursion for all odd primes through 131 and for extension fields of order 9, 25 and 49, verifies the second-moment identity for all center subsets in the prime fields of orders 3, 5, 7 and 11 and deterministically selected subsets for larger prime orders, and tests the real threshold recurrence through 50 steps. These are finite checks only. The infinite bound follows from the independent algebraic proof given in `RESULT.md`.

The zero element is never classified as a quadratic residue. Character sums explicitly use the convention \(\chi(0)=0\) and adjust the Boolean incidence count by \(\mathbf1[x\in A]\). This is necessary for the exact split calculation. An independent external mathematical audit has not yet occurred.
