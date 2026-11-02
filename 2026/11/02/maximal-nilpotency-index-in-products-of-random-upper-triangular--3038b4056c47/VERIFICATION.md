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
# Finite verification

The independently implemented `verify.cpp` runs direct enumeration of ordered upper triangular pairs, verifying nilpotence from the product diagonal and maximal index from its first superdiagonal. Exhaustive instances are \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\), with respectively \((36,10),(225,96),(2025,1120),(1728,112),(91125,14256),(331776,4608)\) as the nilpotent-pair and maximal-index-pair counts. It separately enumerates all three-letter-type words for sizes \(2\) through \(8\) and numerical field sizes \(2,3,4,5,7\), verifying the weighted word polynomial.

To repeat: `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. Successful output ends with `VERIFY_OK`.

These computations do not establish the general result. The general argument is the exact diagonal-word classification and independence of first-superdiagonal coordinates in `RESULT.md`. The field-size-four and field-size-seven word checks require no finite-field arithmetic and check only the integer combinatorial factor; all direct matrix enumerations use prime fields. Independent mathematical auditing has not been performed.
