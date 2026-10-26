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

# Verification record

Reproduce the small-prime-field checks with `python3 verify.py` from the unpacked finding. The program enumerates each adjacent-block pair, independently builds the full linear commutator matrix from basis inputs, computes its rank and the product rank, and compares the resulting complete joint frequency table with the closed Gaussian-binomial formula. It multiplies by the number of free far-off-diagonal blocks, and checks that total counts equal the group order. Eleven configurations over prime fields of orders \(2,3,5\) passed, including a \(3\)-field example with group order \(531441\). It also checks that for field order \(2\) and block sizes \((2,2,2)\), the three square-rank counts at class size \(16\) are \((192,1728,576)\).

A separate exact-integer evaluation of the formula for seven field orders \(2,3,4,5,7,8,9\), each with six block triples, checked total group-size normalization and integrality of the resulting class counts. Those evaluations are finite algebraic checks, not an exhaustive proof or independent audit. The proof applies to all prime powers, including extension fields not exhaustively enumerated in the standalone program.

The verification code uses the Python standard library only. No external datasets, hidden paths, or precomputed verification logs are required. The source inspections and remaining publication-priority uncertainty are detailed in the scientific review.
