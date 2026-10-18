---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Smooth Birkhoff orthogonality gives x=(t,1)/(1+t^4)^(1/4), y=±(1,-t³)/(1+t^12)^(1/4), 0<=t<=1. Directly expanded the two branch products; the stated exact factorization shows the positive branch dominates for 0<t<1. The constrained derivative along (1+t^12)r^4=1+t^4 has a resultant proportional to the displayed palindromic degree-14 Q(t^4). Inspected exact SymPy verifying script checking this identity and Sturm root counts; independently computed Q roots in (0,1) near 0.002416998 and 0.825586362 and optimized both branches, obtaining t*=0.9532144723 and T=2.070379018225525. Only the large root is compatible with the positive constrained derivative; endpoint values are lower. Numerical computation is corroboration, while exact resultant/root isolation is the proof.

## originality

PASS

Ahmad–Xie–Li (2022) define T_perp, derive universal bounds, the Hilbert value 10^(1/4) and ell_infinity squared endpoint, and explicitly leave further spaces open; their full primary 13-page paper does not compute ell_4². Published ell_3² T_perp and other ell_4² constants have different Birkhoff constraints or defining products and cannot imply the precise asymmetric two-chord optimization. Targeted Resultary and bibliographic searches did not locate the same constant in real ell_4².

## value

PASS

Provides a benchmark exact interior maximizing Birkhoff pair for a canonical smooth uniformly convex non-Hilbert space; the degree-14 isolated-algebraic extremum distinguishes it from endpoint and Hilbert benchmarks and can test sharp general inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
