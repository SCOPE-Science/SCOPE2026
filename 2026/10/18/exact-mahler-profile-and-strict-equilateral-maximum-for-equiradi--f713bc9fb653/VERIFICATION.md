---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The proof reduces the primal unit-ball volume to a finite binomial sum using complete signed-orthant integration, and the polar volume to the exact range-density integral. The closed polynomial derivative has strictly positive coefficients after removing the factor \(1-s\). Those arguments cover **all integers** \(n\ge2\) and **all real parameters** \(s\ge\frac12\).

Run `python VERIFY.py`. The script independently compares the collapsed and uncollapsed orthant volume formulas using rational arithmetic for every integer \(2\le n\le14\) at seven exact radii; verifies the derivative identity coefficient by coefficient and checks both endpoint identities. When NumPy and SciPy are installed it independently builds the primal hull and the polar halfspace-intersection polytope for \(2\le n\le5\) at six radii and compares geometric volumes numerically. Both verification stages completed successfully during self-review. The floating geometric tolerance is \(5\cdot10^{-8}\) relative, and finite tests do not certify the infinite quantifiers independently.

The basepoint is the hub, dimensions refer to the \(n\) leaf coordinates, and the origin is interior to both convex bodies. The full signed-orthant decomposition covers all domain strata except measure-zero boundaries. This record does not constitute an independent external audit.
