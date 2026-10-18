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

The formula is proved for all integers \(d\ge3\) by reducing every row type to a two- or three-dimensional character cube and counting lifts. The finite exact-arithmetic program `CHECK.cpp` was compiled and executed with g++ -std=c++17 -O3, and completely enumerated all \(4\)-row, \(4\)-column pairs for dimensions three and four. Its observed ranks and determinant multiplicities agree exactly with the formulas. For dimension four the enumeration involved \(\binom{16}{4}^2=3{,}312{,}400\) minors. The program is corroboration, not a substitute for the arbitrary-dimension argument. No independent audit has been performed. The classification is restricted to elementary binary groups and four-row/four-column restrictions.
