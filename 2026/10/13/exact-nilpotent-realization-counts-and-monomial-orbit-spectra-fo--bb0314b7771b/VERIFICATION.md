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

Run `python3 verify.py` using a standard Python 3 installation; no external packages are required. The script checks finite-field arithmetic with explicit prime and irreducible-polynomial extension tables, enumerates every admissible diagonal word and nonzero cycle product in its finite test range, constructs a representative sparse matrix for every candidate with the required characteristic polynomial, and checks its nilpotency and maximal index by direct multiplication. It then forms cyclic-word orbit representatives and compares the exact periods against the Möbius formula.

Verified field orders are \(2,3,4,5,7,9\), including extension fields of orders \(4\) and \(9\). Dimensions \(3,4,6\) include cases with zero solutions and cases with characteristic dividing the dimension. In the \(q=4,n=6\) case, it verifies \(21{,}870\) labelled solutions, two period-three orbits, and fourteen period-six orbits. The script ends with `VERIFY_OK` on success.

The finite instances do not certify the theorem for arbitrary parameters. General validity depends on the characteristic-polynomial identity, the splitting criterion for \(t^m+\beta\), the elementary edge-weight gauge argument, and Burnside/Möbius enumeration proved in `RESULT.md`. Literature priority has not been independently certified.
