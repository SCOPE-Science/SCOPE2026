---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

From e^2=f, ef=f, fe=0, f^2=f over F_2 obtain (a,b)(c,d)=(0,ac+ad+bd). All products are f-only. If (0,P) is a product-sum, right multiply by x_i to get Pb_i and left multiply to get P(a_i+b_i); adding gives Pa_i. Hence f-only product space W is an ideal in the full Boolean function algebra on A^n. Its diagonal generators q_ii=a_i+a_ib_i+b_i jointly vanish only at the zero tuple, so finite-function-algebra pointwise interpolation gives W={functions vanishing at 0} of dimension 4^n-1. The variable projections have linearly independent e-coordinate forms of dimension n, disjoint from W, proving dim_F2(F_n)=4^n+n-1, |F_n|=2^(4^n+n-1), and potential 4. Independent Boolean-ideal rank calculations gave 3,15,63 for n=1,2,3; the unrestricted claim follows from the ideal proof.

## originality

PASS

Exact clone/term-function dimension formula for Olshanskii’s concrete prime nonassociative ring. Olshanskii proved growth potential/maximality and a general two-sided exponential-scale bound, not this exact finite-n dimension. Published affine Lie free-growth formula concerns a genuinely different multiplication and identity signature. Best-of-knowledge originality with older polynomial clone theory risk.

## value

PASS

The full term-function description and exact growth in every free rank for an explicitly exhibited *prime but nonsimple* finite nonassociative ring sharpen the originating maximal-potential theorem. Clone dimensions and exact relatively-free algebra orders are natural structural invariants; the Boolean ideal proof makes the formula independent of numerical tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
