---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The exact formula agrees with the convention in Jiao–Luo–Wu (3.2). At A=0 the two products inside the real part are adjoints. On the span of u,v, put H=B−C, h=a−b and k=2ab(1−r²)/q. For 0<r<1 the signed eigenvalues (h±q)/2 give |H|=(h/q)H+kI. Expanding det(kI+(1+h/q)B+(1−h/q)C) gives k(a+b+q); in coordinates u=e1, v=(r,s) the adjugate numerator in u*D⁻¹v is rk. The result with complex phases follows by undoing the rephasing. The phase-normalized u±v diagonalize the symmetrized product, giving r(r±1) before scaling. Orthogonal ranges give zero and coincident ranges give min(a,b)P by direct pseudoinversion. In dimension one the formula gives the scalar median (sort by permutation invariance). The half-angle substitution gives derivative with sign (t−1)(t³+t²+3t−1), with the cubic strictly increasing; common scalar translation leaves D fixed and shifts the spectrum. Thus the algebraic threshold and the strict-positive witness are correct for the stated families. The last displayed decimal digits of κ are slightly off: κ≈0.06744224886812295177; the exact formula and the threshold are unaffected.

## originality

PASS

The defining operation, symmetry and trace-norm estimate are prior. Neither that estimate, the different optimization-defined median, nor the checked Resultary positivity results supply the sharp signed spectrum and common shift for this map. The distinct claim passes on the inspected evidence, not as a priority guarantee.

## value

PASS

For a symmetric scalar-median extension defined algebraically on Hermitian matrices, positivity is a natural structural question. Dimension two already disproves it even in the interior of the positive cone. The whole rank-one overlap classification identifies exactly where the negative direction occurs and supplies a dimension-free optimal remedy on the equal-amplitude projection family, not just a numerical negative witness. It neither weakens the published trace-norm theorem nor claims a remedy for arbitrary matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
