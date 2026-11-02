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

Orthogonal monomials in normalized disk Bergman space have squared norm 1/(k+1); adding τ|f^(m)(0)|² modifies only coefficient m, so the exact kernel is (1-t)^(-2)-q t^m with q=τ(m+1)²(m!)²/[1+τ(m+1)(m!)²]∈[0,m+1). The disk zeros are the zeros of P_q(t)=1-q t^m(1-t)². For |t|=1 the factor t^m(1-t)² is -4 sin²(θ/2) exp(i(m+1)θ), and all positive-q boundary crossings occur exactly at θ=(2j+1)π/(m+1), q=1/[4sin²((2j+1)π/(2(m+1)))]. At each crossing Re[tF′/F]=m+1>0, giving strictly inward root motion as q increases, including multiple simultaneous crossings. A multiple root could only occur at t=m/(m+2), q*=(m+2)^(m+2)/(4m^m)>m+1, outside finite penalties. Hence the staircase counts all interior products with strict > thresholds; equality is boundary and excluded. The first threshold is 1/4 for even m and [4cos²(π/(2(m+1)))]^-1 for odd m; the q-to-τ inverse yields τ1=1/6 and τ2=1/132. Independent polynomial companion roots tested m=1..12 over admissible noncritical strengths, and checked physical thresholds. All claims are finite τ≥0 and m≥1; no multiple-jet norm.

## originality

PASS

General Lu Qi-Keng/Bergman kernel zero phenomena, radial weight perturbations and Sobolev derivative inner products are prior work. The complete discrete all-order zero-entry staircase for the inverse-norm Bergman RKHS with a single centered m-th derivative penalty is different from canonical jet-evaluation Gram kernels, zeros of finite-degree Sobolev orthogonal polynomials, and radial weighted Bergman kernels. Broader specialized RKHS classification could cover it but was not found in the inspected primary text.

## value

PASS

The exact number of interior reproducing-kernel zeros as a function of a physically meaningful positive derivative regularization parameter is a natural complete Lu Qi-Keng phase classification, not an arbitrary low-order census. The strict boundary equality, root simplicity for every finite penalty, and unreachable formal thresholds are mathematically useful precise facts for derivative-regularized analytic spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
