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

For the center-started 1D telegraph process with left sticky wall, right absorbing wall, Poisson reversal rate alpha/2, b=alpha R/v>0, the backward moment equations and sticky waiting-time boundary conditions are explicitly solved in pinned RESULT.md. The first two moment polynomials give M(b)=3+3b/2+1/b, V(b)=5b^2/2+10b+12+8/b+3/b^2 and Q(b)=V/M^2. Independently differentiated the exact rational expressions and checked M_second=2/b^3>0, V_second=5+16/b^3+18/b^4>0 and Q_derivative=16(2b^3-3b^2-9b-5)/(3b^2+6b+2)^3. The quartic 5b^4+10b^3-8b-6 and the cubic 2b^3-3b^2-9b-5 each have one positive root by Descartes; b_M=sqrt(2/3)<b_V≈0.975331842868198<1<3<b_Q≈3.16896685513906. On [b_M,b_V], M strictly increases while V strictly decreases, so the full nondominated mean/variance frontier is exactly this interval, all points supported by unique positive weights. Q decreases then increases and its minimum b_Q lies outside, dominated in M,V by b_V. Q-1=(b^4+4b^3+8b+8)/(3b^2+6b+2)^2>0; inf Q≈1.099983697266. The source exact Laplace transform provides independent moment cross-check, but these raw moments and the mean optimizer were prior known.

## originality

PASS

Angelani, Optimal escapes in active matter, gives precisely the same sticky-wall stochastic model, exact first-passage transform and mean optimum; all raw moments are implied by that stronger transform. These are explicitly acknowledged prior components. Inspected closest primary papers do not directly state the triple global optimizer ordering, full mean–variance Pareto frontier or the dominated relative-risk optimum. Newness is confined to their joint extremal classification, not differentiating known transform by itself.

## value

PASS

The global selection of reversal rate for three competing natural risk objectives (mean, absolute variance, relative variance), and a complete supported Pareto frontier with the surprising fact that the relative-risk optimizer is inferior in both absolute objectives, is a motivated qualitative design boundary. It is mathematically more informative than routine raw-moment differentiation, while making no larger model generality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
