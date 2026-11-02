---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The potential-coordinate polar constraints |x_i-y_j|<=1 and connected tight-edge incidence at vertices give lattice integrality. For dilation n, fixing the p-side potentials with x1=0 and range r leaves exactly (2n+1-r)^q independent second-side choices; the number of first-side vectors of range r is (r+1)^p-2r^p+(r-1)^p for r>=1. This proves the universal lattice count including p=1 and n=0. Ehrhart degree d=p+q-1 plus d+1 exact Newton samples completely determines each coefficient. A fresh independently coded Fraction finite-difference interpolator enumerated all 49 unordered classes d<=13, checked the leading volume 2^d p!q!, and found only (7,7), dimension13, c1=-7184/715 nonpositive. Independent small direct lattice counts matched. This is an exhaustive finite cutoff statement, not extrapolation beyond dimension13.

## originality

PASS

Best-of-knowledge originality PASS: Magic positivity implies ordinary positivity, but the converse fails: Konoike already exhibits ordinary-positive yet magic-negative classes such as K3,7. Therefore a table of magic failures is insufficient to imply which is the first ordinary failure. The nonpolar h* source concerns another lattice polytope. Neither is proof of the precise K7,7 boundary. Material comparisons distinguish actual mathematical implication from common terminology. Relevant uninspected sources and residual priority risks remain explicit.

## value

PASS

Ehrhart positivity in the ordinary monomial basis is a natural exact invariant distinct from magic-basis positivity. The complete 49-class cutoff establishes a sharp first counterexample and uniqueness at the first dimension in this canonical graph-polar family, as well as a uniform exact counting and volume formula; a finite but complete and motivated classification is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
