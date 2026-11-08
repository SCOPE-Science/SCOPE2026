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

For symmetric numerical semigroup S of multiplicity m≥4, reflection about Frobenius F identifies gaps f of H=S/3 with elements x=F−3f in residue r=F mod3; f is pseudo-Frobenius exactly when x is minimal under subtraction of positive S∩3Z. If r=0 then H is symmetric and PF(H)={F/3}. If r=1 or 2, any factorization of a source element in class r contains a generator of class r or a pair of generators of opposite class 3−r, so the residue module equals (G_r ∪ pair sums of G_{3−r}) + S0. Taking its minimal candidates c<F gives the exact PF list (F−c)/3 and the binomial generator-count bound. Apéry calculation for S=<m,m+d,...,m+(m−2)d> with 3|d and gcd(m,d)=1 gives PF(H)={d/3,...,(m−1)d/3} and type m−1, unboundedly sharp. Independent Apéry/member DP matches seven admissible parameter pairs. The universal claim rests on module duality and Apéry proof, not bounded enumeration.

## originality

PASS

Known all-divisor pseudo-Frobenius formulas for two-generated source semigroups, and divisor-two half quotients, cover some special cases or different dimensions. Feihu Liu 2026 treats particular quotient Apéry/Frobenius/genus, not this all-embedding-dimension ternary symmetric-source residue generator candidate theorem as checked. The general generator computation may be derivable via other older quotient algorithms, retained as priority risk.

## value

PASS

Entire PF(H) and type of a natural quotient of any symmetric source can be reduced to finitely many source generators and pairs, with a sharp size bound in unbounded families. It is a structural bridge between symmetry, Apéry module minimal elements and pseudo-Frobenius invariants, not a narrow recomputation of known two-generator tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
