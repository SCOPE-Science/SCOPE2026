---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Nathanson greedy interval criterion (or three explicit successive remainder inequalities) applies because a<b<c and denominator growth b>=a²-a+1, c>=b²-b+1 and 0<θ-S<1/(c(c-1)). For any equal-sum triple ordered x<=y<=z, rational magnitude gives a<=x<3a and x<=y<2b; setting R=qxy<6qab and N=2xy-q(x+y), the formula z=Rc/(Nc+R) and c=(6qab)²+1 force N=0 by positive denominator or rational denominator-integrality contradictions (R²<c), hence z=c and (2x-q)(2y-q)=q². Divisor pairing classifies exactly. Any supposed S<T<θ gives a nonzero rational gap >=1/(Qxy), or, if H=1/x+1/y<S, derives z<6Qab and then T-S>=1/(Qxyz)>1/(36Q²a²b²)=2(θ-S); both impossible. Exact Fraction independent checks for q=3,5,7,9,11,15 checked greedy, all divisor ties, and bounded no-improving intervals; infinite q follows from rational inequalities, not enumeration. Note the standard two-term factorization itself is classical.

## originality

PASS

Nathanson open question on equality of greedy Egyptian n-term best underapproximations motivates the general target. Earlier two-term optimal equalities and divisor identities do not provide unbounded best 3-term fiber. Kovač and Kovač–Tang eventually greedy approximation for almost all/rational targets concern long prefixes and not exactly three terms, so quantifiers do not dominate.

## value

PASS

Gives a complete explicit fiber of optimal triples and proves unbounded multiplicity, including strict denominator variant, directly addressing a named published finite Egyptian best approximation question; the small rational perturbation and no-better-gap proof are substantive beyond classical divisor enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
