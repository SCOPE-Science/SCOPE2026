---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Dual distance at least 2 excludes exactly the zero columns. An admissible generator's projective column multiplicities give its class up to the projective-linear permutations: row operations give the projective action, and coordinate scaling and permutation account for column representatives and ordering. Hermitian Cauchy–Binet evaluates the Gram determinant as ∑_{i<j}m_i m_j modulo 2, because a pair from different projective classes contributes the norm 1 and a pair from the same class contributes zero. With t odd entries, the result is binom(t,2) modulo 2; among t=0,…,5 it is nonzero only at t=2,3, the even- and odd-length cases respectively. Nonsingularity also gives rank two. Flipping entries by +1 for even and −1 for odd entries is nonnegative, changes the length n to n+1, and maps parity weight 2 to 3. The odd side has d=(n+1)−max m′; d=1 would force multiplicities (n,1,0,0,0) up to order, of parity weight 1. The same update reverses the map and commutes with every projective permutation, proving the bijection on classes. The source convention 1≤k≤n−1 gives even n≥4 here. Independent arithmetic checked all 32 parity patterns and the 60 projective permutations, with a direct n=4 to 5 test of 50 admissible vectors and two orbits on each side. The supplied finite verifier was examined, not executed.

## originality

PASS

The primary paper explicitly poses this exact all-even-length question. Its projective multiplicities and finite counts are prior; the supported new part is the parity involution proving the first identity on the stated equivalence classes for all even n≥4. No prior statement or implication supplying that involution or the resulting general identity was found in the checked sources.

## value

PASS

This closes an explicitly posed classification question for all even lengths in scope. An involution on projective multiplicities explains the count equality and yields matching equivalence classes, rather than simply extending the finite tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
