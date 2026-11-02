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

Putting u_n=-log x_n gives u_(n+1)=p u_n-log c+O(exp(-delta u_n)); summing the normalized affine recurrence gives u_n=C p^n+(log c)/(p-1)+o(1), C>0 from u_n->infinity. Algebraic flight durations satisfy tau_n~a exp(q C p^n), so t_n is dominated by the last term and log log t_n=n log p+O(1); logarithmic flights have tau_n~a C p^n, hence t_n~const p^n and log t_n=n log p+O(1). Bracketing T between consecutive returns gives matching N(T) asymptotics. Summing b_n by Cesàro and bounding incomplete-cycle outside-time gives L(T)~b0 N(T). The cited piecewise example gives r(x)=sqrt(1+x^2)-1, return r/(1+r-r²)=x²/2-3x^4/8+O(x^6), tau~2/x² and b0=1-2epsilon. Independent symbolic expansion and recurrence checks corroborated constants.

## originality

PASS

Best-of-knowledge source/implication comparison: Qualitative density-one attraction or return-map asymptotics alone do not state the two alternative explicit L(T) leading-coefficient laws. The combined two-flight-time conditional conclusion is not covered by the inspected source statements. All specific risks are retained; inaccessible literature alone did not determine the outcome.

## value

PASS

Physically motivated quantitative refinement of statistical attraction: the same superattracting return-map order yields different observable occupation decay depending on algebraic versus saddle-logarithmic flight times; gives universal leading coefficients for each.

The dated certificate retains the supplied scientific assessment, sources and limitations.
