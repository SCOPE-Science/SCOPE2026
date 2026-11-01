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

Read the full frozen RESULT.md theorem, boundary and Legendre proof. With I_n(c)=integral_0^pi exp(-ct)P_n(cos t)sin(t)dt, the integration-by-parts identity gives I_(n+2)(c)=[c^2+n^2]/[c^2+(n+3)^2] I_n(c) and strictly positive I_0=(1+exp(-pi c))/(1+c^2), I_1=(1-exp(-pi c))/(4+c^2). Hence each parity ratio I_n(a)/I_n(b) is strictly increasing (a>b) or decreasing (a<b). Comparison of base ratios shows min n=0 for a>b; Euler products/Wallis yield the smaller limiting EVEN-parity ratio a(1-exp(-pi a))/[b(1-exp(-pi b))] for a<b, not attained by finite n. Schoenberg coefficient nonnegativity is necessary/sufficient for all finite site matrices; infinitely many strictly positive coefficients in each parity give strict PD on S2 at a!=b. Equal scales reduce to (1-lambda) times strictly PD exponential. Independent high-precision Legendre integrations and exact recurrence/coefficient-ratio checks corroborate but do not prove the infinite criterion.

## originality

PASS

The new comparison concerns a signed difference of two geodesic exponential scales, not the known positive definiteness of each scale. Schoenberg diagonalization and single-scale positivity are historical inputs; the exact three-case endpoint lambda frontier, which parity/degree controls it, and strict positivity at the threshold are the surviving claim. Relevant Resultary records returned other spherical and covariance spectral work, no implication to this two-scale ratio.

## value

PASS

The exact largest admissible subtraction weight of two natural isotropic geodesic covariance models is a meaningful nonstandard covariance-design/positive-definite-kernel invariant; identifying low-degree versus high-frequency obstruction and strictness at boundary is more than a textbook restatement of Schoenberg positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
