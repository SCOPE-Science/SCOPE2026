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

# Reproduction

Run `python3 verify.py` using the Python standard library. The program prints `PASS: 1559 independent rational and root checks`. It independently solves all the finite-state backward equations with exact fractions, checks three-state directed formulas and the four-state continuum of rational test rates, tests the renewal/resolvent formulation, verifies the derivative polynomial, and enumerates a family of hazard-maximal undirected weighted graphs.

# Logical scope

Finite enumeration does not prove a universal theorem. The infinite graph-parameter claims are proved by Feynman–Kac domination, a finite-state killed-resolvent expansion, exact symbolic elimination, and derivative signs in RESULT.md. The radical root and optimum were also checked with standard floating-point arithmetic. No formal verification or independent scientific audit has been conducted.
