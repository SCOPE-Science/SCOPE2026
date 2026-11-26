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

On the clockwise shift eigenvalues 1,−1,i,−i the generator eigenvalues are 0, −2(a+b), and −(a+b)±i(a−b). None hits the Padé denominator poles 3±i√3 after scaling by h≥0. To check the decisive numerator identities without the uploaded checker or a Fourier inversion, I put Z=h(ax+bx³−a−b) in the polynomial ring with x⁴=1 and verified exactly that the proposed numerator N=ΣN_j x^j satisfies (12−6Z+Z²)N=D(12+6Z+Z²), and N(1)=D. Thus the four coefficients divided by D are the actual four row entries with the stated orientation. The common denominator and diagonal numerator are positive on h≥0; the opposite entry is positive for h>0. Both nearest-neighbor quartics have positive coefficients at degrees zero through three. Their leading coefficients have the signs of 3b²−a² and 3a²−b², respectively. This gives strict positivity for finite h>0 in the closed rate interval. Outside, exactly one leading coefficient is negative, and its F(h)/h⁴ decreases strictly from +∞ to that negative coefficient. It has exactly one positive root, simple, with the necessary sign on both sides. The other entries stay positive. At h=0 the update is the identity; at the horizon precisely the affected entry type is zero. These calculations establish every h, including both bias endpoints.

## originality

PASS

The distinct supported result is the exact drift ratio and complete finite-step positivity horizon for positive unequal rates on the homogeneous bidirectional four-cycle. The earlier symmetric cycle result supplies a=b, and the later one-way result agrees with b=0 after scaling. The most relevant Padé positivity literature gives general sufficient conditions and failure examples, not this sharp two-way classification. A targeted primary search returned no results and does not establish absence.

## value

PASS

A bidirectional homogeneous four-cycle is a natural small conservative transport model where drift can vary independently of overall time scale. The criterion gives the precise drift tolerance of a standard fourth-order integrator, and the unique horizon beyond it exactly determines the permitted step range. It resolves both an all-step boundary and the finite-step behavior across the full positive two-rate family, rather than tabulating isolated parameter choices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
