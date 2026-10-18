---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For even b>=12, Q=b²-2, U=2b-1, V=2b-3, the exact digit expansions X=UQ=(1,b-2,b-4,2)_b and Y=VQ=(1,b-4,b-4,6)_b yield S_b(X)=V, S_b(Y)=U, so both distinct inputs map under H_b(n)=n S_b(n) to UVQ. The identities (2b-1)(2b+1)-4Q=7 and 4Q-(2b-3)(2b+3)=1 show gcd(Q,U)|7, gcd(Q,V)=1 and gcd(U,V)=1. Excluding b=4 mod7 makes Q,U,V pairwise coprime, so their separate squarefreeness implies both inputs squarefree. At the even-prime modulus 4 half of b classes qualify; at p=3 7/9; at p=7 precisely 40/49 (7 excluded classes for b mod7, plus one root lift of Q and one root lift of V). For odd p>=5, p!=7, the distinct p²-root sets of Q,U,V contain 3+(2/p) forbidden classes. The CRT finite-sieve densities converge to (1/2)(7/9)(40/49) times the convergent positive Euler product. The large-prime-squares union bound 4T sum_{p>P} p^{-2}+4 pi(T) has limsup_T/T tending to zero as P->infty and supplies the needed actual natural density, not a heuristic independence assumption. Independently verified expansions, exact squarefreeness equivalence for even bases 12..400, and residue-class counts for p=2,3,5,7,11,13,17,19,23,31,41,47. Found 106 qualifying even bases in 12..400, not used as an infinite proof.

## originality

PASS

The exact originating question is Question 30 of Noppakaew–Pongsriiam (Journal of Integer Sequences 26 (2023), 23.9.1), which establishes H_b noninjective on all N for all b>=2 and squarefree noninjectivity only for b=2..10. The present theorem neither pretends to settle every b>=11 nor repeats those finite examples: it supplies explicit quadratic-factor witnesses and an exact positive-density subset of even bases b>=12. No equivalent construction or complete parametric density is identified in its full 29-page primary text or scoped semantic search. Standard squarefree-sieve/local-density theorems underlie the density argument but do not already fix the specific digit-sum polynomial witnesses.

## value

PASS

Squarefree-input injectivity of H_b is an explicitly posed open-ended arithmetic-function problem. An explicit infinite family occupying positive natural density among bases, with the exact Euler-product density and valid squarefree digit witnesses, is a meaningful quantitative partial resolution, not simply a few computational collisions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
