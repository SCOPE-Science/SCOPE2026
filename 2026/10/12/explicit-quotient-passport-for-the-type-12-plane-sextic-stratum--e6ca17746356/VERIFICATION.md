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

Taking affine t=Y/Z and x=X/Z gives Kummer extension x^6=-t(t^4+beta t²+1). The cited Badr–Bars theorem supplies full G=C3×D8 of order24 and N=<sigma²> of order6. With residual V4 action t→-t and t→1/t, the invariant fixed field is C(t²+t^-2); degree is 6×4=24. Kummer ramification index6 at t=0,∞ and 4 roots of t^4+beta t²+1; the degree4 base map has index2 at t=0,∞ and ±1,±i. For beta≠±2, combined inertia orders at u=∞,-beta,2,-2 are (12,6,2,2); orbit sizes 24/e=(2,4,12,12). Calculated discriminant of quartic as 16(beta-2)²(beta+2)² and tame Riemann–Hurwitz 24(-2+11/12+5/6+1)=18=2g-2 for g=10. Independent sympy validation of branch-polynomial identities and Riemann–Hurwitz; this is symbolic in beta, not finite sampling. Exceptional beta loci excluded exactly as stated.

## originality

PASS

Badr–Bars arXiv:2208.12749v1 Proposition 6.1 is acknowledged as prior source of full group, family and N. The novelty-bearing datum is the actual quotient rational function and the labeled beta-dependent branch divisor; it is not the group identity or unordered abstract signature. Broughton–Shaska–Wootton arXiv:1807.02742 describes Breuer genus≤48 signature tables and hence broader coverage of generic abstract signature. Searches for explicit t²+t^-2/plane model and group/signature did not locate a stronger labeled quotient, but an old equivalent Mobius-transformed superelliptic model remains possible.

## value

PASS

The quotient by the full automorphism group is a natural invariant of this genus10 plane-sextic family. Providing its rational coordinate and varying branch location makes explicit a degree24 Hurwitz cover and parametrized four-point configuration useful in moduli studies; the result does not rely for value on claiming the abstract inertia multiset itself was previously unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
