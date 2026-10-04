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
The exact replay source is `verify.cpp`.

Compile with a C++17 compiler and run the resulting executable. The program iterates through every exponent \(1\le n\le10^6\), maintaining \(2^n\) exactly as chunks in base \(3^{39}\). A 12-digit leading/trailing comparison is used only as a necessary filter; every survivor receives a complete exact ternary palindrome comparison.

The expected full hit set is
\[
\{1,2,3,4\}.
\]
The expected nontrivial filter-survivor list is
\[
\{41298,41299,41300,62318,377166,877495,918265\}.
\]
The program prints `VERIFY_OK` only after both lists match exactly.
