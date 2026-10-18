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
# Exact checks
Compile with `g++ -std=c++17 -O3 verify.cpp -o verify` and run `./verify`. The source exhaustively evaluates the determinant in the integral cyclotomic basis for every triple pair at prime orders \(p\in\{5,7,11\}\). It independently computes rank-one status from nine size-two minors and compares every pair to the claimed residue criterion and every count to the closed formulas. The exact output is embedded as `verification_output.txt`.

# Limits
All-prime validity requires the proof in `RESULT.md`; finite enumeration alone cannot establish it. Comparisons of publication implications remain best-knowledge and are not independently certified.
