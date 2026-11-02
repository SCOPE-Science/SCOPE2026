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
# Verification of the finite Cantor circular Abelian spectrum

The exact mathematical claim and complete proof are in `RESULT.md`. To reproduce the finite checks, execute `python3 checker.py` from a directory containing these files, using Python 3 and only the standard library. The checker constructs independent cyclic spans and one counts and compares all lengths and all thresholds with the symbolic formula for ranks one through seven. Replayed result: `ALL CHECKS PASSED`. The rankwise complete totals were 5, 23, 113, 599, 3353, 19391, 114161.

The proof of the unrestricted theorem requires no external computational certificates: its critical parts are the exact gap identity, the strict comparison of all gap windows containing versus avoiding the wrap gap, the optimal realizable carry pattern, and the threshold-sum evaluation. Finite enumerations alone do not establish the result at arbitrary rank, and source searches alone do not establish novelty. Historical priority remains non-exhaustively checked. Independent mathematical auditing has not been performed.
