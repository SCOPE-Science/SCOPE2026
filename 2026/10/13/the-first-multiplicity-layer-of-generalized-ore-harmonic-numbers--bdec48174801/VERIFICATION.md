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

For k≥1 and n>1 the Ω≤2 factorizations are p, p² and distinct pq. For x=p^k, the prime and prime-square denominators x+1 and x²+x+1 are coprime to x, so integrality requires them to divide 2 and 3, respectively, impossible already at x=2. For x=p^k and y=q^k, 1<4xy/((x+1)(y+1))<4, leaving 2 or 3. The first gives (x−1)(y−1)=2 and therefore {x,y}={2,3}, k=1 and n=6; the ratio at 6 is 2. The second gives (x−3)(y−3)=12: zero factors cannot occur and if both factors were negative they would both equal −1 since x,y≥2, giving product 1. Thus the three unordered positive-factor pairs give (x,y)=(4,15),(5,9),(6,7). The first and last have a non-prime-power member; in (5,9) the exponents 1 and 2 differ. This proves the exact unbounded classification and the necessary Ω≥3 consequence for proper k. The uploaded checker was inspected but not run; its finite sweep is not needed for this proof.

## originality

PASS

The harmonic exception 6, the generalized definition, the earlier finite negative search and the earlier even two-prime support exclusion are not new. The distinct part is the uniform exact multiplicity-two classification, including exclusion of odd squarefree semiprimes for every k≥2. No inspected result establishes that missing branch for unbounded primes. The unavailable original generalized Ore paper remains a substantive access risk.

## value

PASS

Generalized Ore harmonicity has an open existence question for proper k; the two smallest nontrivial multiplicity layers are natural to exhaust. Closing the odd semiprime case uniformly gives an exact unconditional restriction on the prime factorizations of any hypothetical examples, complementing a stronger prior bound that applies only to even two-prime support. This is a modest structural classification, not a numerical search extension or a new existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
