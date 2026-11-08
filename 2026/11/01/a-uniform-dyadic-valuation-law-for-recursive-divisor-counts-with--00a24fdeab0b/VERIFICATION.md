---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Formal Dirichlet convolution identity from κ0 recursion gives ζ/(2−ζ). Labelled-cofactor coefficient extraction gives G_r(t)=2^r e^t/(2−e^t)^{r+1}; with u=e^t−1, 2^-r κ0(N)=Σ_{j=0}^k [binom(r+j,j)+binom(r+j−1,j−1)]j!S(k,j). For k=0,1 this equals 1 and r+2. For k≥2 and odd r, j=1 term r+2 is odd, others even; for even r, j≥3 vanish mod4, and j=1,2 sum ≡2 mod4 because S(k,2)=2^{k−1}−1 odd. Thus the claimed four-case v2 formula for all r≥1 k≥0. Independently recomputed κ0 from proper-divisor exponent-vector recurrence for r=1..14,k=0..7 (112 integer cases); tests corroborate but do not prove unbounded r,k.

## originality

PASS

Best-of-knowledge PASS: derives a sharp uniform dyadic valuation classification for exponent vectors (r,1,…,1), including exceptional k=1 and stabilization at k≥2. Known Dirichlet series itself is not new. A highly relevant Fink companion full text remains a genuine residual risk, not an automatic failure.

## value

PASS

The first non-squarefree exponent-vector family p^r times an arbitrarily long squarefree cofactor is a natural arithmetic structural class. The sharp, uniform v2 law detects exceptional unbounded k=1 growth and stabilization after two cofactor primes, answering a genuine exact invariant beyond small-count tables; no claim for two repeated primes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
