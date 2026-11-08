---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read frozen RESULT.md blob a4f0c10... . Odd and twice-odd cases follow isolating k=1 and k=2 terms modulo 4/8. For n∈4Z₂, use Li₂(2)=0 from Li₂(z)+Li₂(z/(z−1))=−log²(1−z)/2, expand binom(n,j)^2=n²P_j(n)/j² and divide by n³. The unique odd linear contribution is j=4 coefficient −11/3; nonlinear potentially odd j=4 and j=8 quadratic terms cancel modulo2, while sorted valuation bound E(j,m) and B(j) prove all remaining terms even, uniformly in the 2-adic tail. Independent exact Delannoy recurrence checks reproduced valuation for n=1..2499, and checked the exceptional rational coefficients and j≤31 bounds. This is a genuine infinite p-adic proof, not exhaustive finite enumeration.

## originality

PASS

Lengyel (2021) gives a lower bound for 4|n and explicitly conjectures the sharp equality, while providing the easy odd/twice-odd cases. Inspected more recent related Legendre p-adic and weighted Delannoy sum literature with mathematically different targets; no stronger theorem checked that implies ν₂(P_n(3)−1) exact.

## value

PASS

Resolves an explicit sharp published valuation conjecture for a classical special-function/combinatorial sequence over every positive index and identifies exact cubic order of 2-adic proximity of D_n to one; natural nontrivial p-adic arithmetic result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
