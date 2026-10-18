---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: For split finite-dimensional locals B,C, the tensor radical is JB⊗C+B⊗JC (nilpotent, quotient F); quotient by its square canonically gives JB/JB² ⊕ JC/JC². Thus e is additive. A nontrivial local split algebra has e>=1 because J=J² and nilpotence imply J=0. e(P)=1 implies every radical layer is at most one-dimensional, with x^k spanning it; stationary nonzero filtration layers impossible, so P=F[x]/(x^m). Converse follows from e-additivity. Sakurai unique factorization is the explicit external premise for uniqueness of exponent multiset. Scope: finite-dimensional split local F-algebras over arbitrary fields; no assertion for nonsplit or nonlocal rings.

## originality

PASS

Best-of-knowledge original as precise final theorem, after distinguishing stronger priors and genuine access limitations. Failed search is not proof of novelty; see mathematical implication checks and source inspections.

## value

PASS

PASS: This is a natural structural limit on the number of tensor factors of a split Artinian local algebra using its elementary cotangent dimension. Equality gives a complete maximal-factorability classification and unique nilpotency exponents, rather than an arbitrary instance or a numerical substitution. It does not determine subextremal factorization patterns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
