---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For real SPD A with u!=0 and nonzero admissible update B=A+tau uu^T still SPD, define r as the number of distinct eigenspaces P_lambda u!=0. Sherman-Morrison gives (f(B)-f(A))/tau=b uu^T+sum_j c_j t_j v_tj v_tj^T/(1+tau*s_tj), all positive coefficients for the specified positive-pole/residue class; even for tau<0 the denominator is positive by the SPD downdate test and monotonicity s_t<s_0. Cauchy determinants for distinct active lambda and distinct positive shifts (including an optional constant column when b>0) give span dimension min(r,m+1_{b>0}). The Stieltjes integrals for x^p and x^-p, 0<p<1, are integrals of positive outer products v_t v_t^T; a nonzero vector in the active Krylov subspace has a nonidentically-zero rational partial-fraction pairing with v_t, giving strictly positive quadratic form and rank r. Outside the Krylov space all terms vanish. At exponent 1 direct Sherman-Morrison and B-A give rank one. Independent SymPy exact-rational matrices with 3 active eigenvalues and 4-dimensional A confirmed 12 independent cases including positive and negative tau, zero to three poles and optional linear term; finite tests do not prove arbitrary dimension or fractional continuum.

## originality

PASS

Best-of-knowledge PASS is for the exact active spectral grade equality in fractional powers and the positivity-based *lower bound* saturating the rational pole rank ceiling. Shmueli-Drineas-Avron recognize that square-root correction can be algebraically full rank and focus on fast numerical approximation; no inspected exact projective grade formula. Beckermann-Cortinovis-Kressner-Schweitzer and Bernstein-Van Loan already give general rational update rank upper bounds and Krylov exactness; an upper bound for arbitrary signs does not force exact saturation, which depends on strictly positive residues/Cauchy independence. Fasi-Higham-Liu covers scaled-identity active grade one. Original Bernstein–Van Loan full paper remained inaccessible despite permitted retrieval attempt; any hidden equivalent specialization remains an explicit material priority risk.

## value

PASS

The question is intrinsic in numerical linear algebra: a rank-one SPD change can induce an exactly full-rank square-root/inverse-square-root correction while still being numerically well approximated by low rank. The active grade identifies precisely which eigenvalues participate and the positive-residue pole budget gives a sharp dimension-independent algebraic criterion to distinguish exact representation from approximation; the exponent-one discontinuity and grade-one special case are natural boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
