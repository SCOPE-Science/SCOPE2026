---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Projection matrices on the two orthogonal coordinate blocks give F_Q(t)=f1(t)/s1(t)+f2(t)/s2(t)=G(t)/(s1*s2) with s1=1+t^2+t^4 and s2=1+t^2+t^4+t^6, coprime, product L degree10. For any Q the derivative numerator H=G_prime*L-G*L_prime has degree at most 18 after the highest terms cancel. The explicit data Q0=diag(aa^T/14,bb^T/30), a=(1,2,3), b=(1,2,3,4), are genuine rank-one block idempotents and jointly rank2. Independent exact SymPy rational arithmetic confirmed H degree18, leading coefficient -58/35, gcd(G,L)=gcd(H,L)=gcd(H,H_prime)=gcd(H,p1*p2)=1. Thus there are 18 simple finite nonpole critical roots; the last gcd excludes the algebraic cut locus via rank(QP)=2 iff p1*p2 nonzero for this witness, and degree18 excludes criticality at infinity. Nonvanishing coefficient/resultant/discriminant conditions define a nonempty Zariski open subset of the irreducible projection Grassmannian, so generic constrained Q realizes 18. The known ED upper bound is attained, establishing GDdeg=EDdeg=18.

## originality

PASS

Friedman–Hoşten–Rosana arXiv:2610.02018 explicitly proves ED degree 18 for scroll ruling curves and defines GD degree for projection-constrained data, but its broad expected low-dimensional ED/GD equality is not a proved universal scroll theorem and does not itself certify an admissible Q with 18 off-cut-locus roots. The assessed added rank-two witness proves this special GD degree. Qualified PASS, acknowledging the known ED number and general framework.

## value

PASS

GD degree is a natural stationary-fitting invariant when both query and target are lines; it differs from unrestricted symmetric-matrix ED degree in known examples. The first asymmetric rational normal scroll S(2,3) is a nonarbitrary baseline, and an exact cut-locus-safe rank-two witness resolves whether constrained data loses complex critical points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
