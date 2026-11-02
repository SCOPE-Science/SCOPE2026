---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The self-adjoint point-interaction Schrödinger operator on circumference 2π has free-arc transfer P(k) and jump J(q), with det=1 and tr[J(β)P(k)J(α)P(k)]/2=cos(2πk)+((α+β)/(2k))sin(2πk)+(αβ/(2k²))sin²(πk). At half flux cos θ=−1 this factorizes into (R(k)+α)(R(k)+β)=0, R(k)=2k cot(πk), strictly decreasing from 0 to −∞ on each (n+1/2,n+1); positive barriers yield one k_n(q) per interval and no other levels. For equal q the one-arc matrix has trace 0 and determinant 1, hence its square is −I and geometric multiplicity exactly two; unequal strengths give distinct simple levels. Implicit differentiation gives dE_n/dq=2k_n/D_n(q) with D_n=2πk_n+q/k_n+πq²/(2k_n), so 0<dE_n/dq<1/π; integration yields a sharp energy-splitting upper bound |α−β|/π approached as n→∞. Expanding the exact squared relation (R+g)²=d²+[2k cos(θ/2)/sinπk]² near (k_n(g),g,g,π) gives gap (4k_n/D_n)√(d²+(k_n²+g²/4)ε²)+O(d²+ε²); nonuniformity in n is acknowledged. Independently multiplied transfer matrices, finite root brackets and coupling derivatives agreed. Numerical tests are corroboration, not the infinite-level proof.

## originality

PASS

Best-of-knowledge original contribution as delimited by the final assigned theorem, not novelty of its foundational method. Direct original statements and implications were compared against the checked primary results and the published-finding search. Highly relevant inaccessible works remain named as residual priority risks; no failed search or abstract alone proves whole-document noncoverage.

## value

PASS

The natural antipodal two-point-barrier magnetic ring exhibits a symmetry-protected exact doublet at half flux. The all-level sharp imbalance ceiling and two-parameter cone give quantitative sensitivity information that is not reduced to a qualitative avoided-crossing observation; those exact inequalities are meaningful invariants of an analytically tractable quantum ring model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
