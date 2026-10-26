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

## Scope of checks

The accompanying Python 3 program `verify.py` uses elementary field arithmetic, direct generator-column construction, and complete enumeration of the \(180\) invertible two-by-two matrices over \(\mathbb F_4\). Every resulting map is evaluated on representative projective nonzero codewords. This is equivalent to checking all nonzero codewords because multiplication by a nonzero field scalar preserves Hamming weight.

For \(t=0,1,2,3,7,20\), the program independently verifies equal enumerators and computes exact rational minimal distortions. It verifies the projective group orders for \(q=2,3,4\) and the parity of each quaternary projective permutation; and it enumerates multiplicity tuples to check that all-distinct nonnegative quintuples have total at least ten. Its exact output is in `verify_output.txt`.

Run with `python3 verify.py` from a directory containing this package's files. Expected last line: `VERIFY_OK`.

## Limits of machine checks

Finite enumeration of selected \(t\) values alone cannot prove the theorem for every \(t\ge0\). The general proof uses the projective-weight dictionary, the exact \(A_5\) action, the five-distinct-multiplicity obstruction, and the strict ratio bound for every odd permutation. No Lean, external certification, or independent mathematical audit was used.
