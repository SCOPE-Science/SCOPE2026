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

## Reproduction

Execute `python3 verify_cubic_windows.py` in the same directory as this file, using Python 3 and its standard library. The checker was actually executed and reported PASS for all positive window lengths through 300, for 28 starts per length (8,400 window-sum computations in total), and for the difference-GCD reductions, initial telescoper, and fourth-order recurrence.

## Logical verification

The infinite conclusion is based on a symbolic recurrence reducing an infinite GCD to four differences, an elementary Fibonacci/Lucas GCD factorization, exact local valuations at two and three, and a polynomial telescoping identity. The complete proof is in `RESULT.md`. Computer enumeration alone would not establish the unrestricted conclusion.

## Scope and limitations

Only ordinary Fibonacci cubes are addressed. The finite calculation does not prove noncoverage in the literature or certify a formal proof. Independent audit is not performed.
