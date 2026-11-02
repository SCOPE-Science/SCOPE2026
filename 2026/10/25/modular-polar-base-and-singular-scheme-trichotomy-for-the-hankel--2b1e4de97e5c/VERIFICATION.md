---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Exact integral triangular coordinates on a=1, t=b, U=c+b², W=d+bc and V=e+U²-4b²U+5b⁴ give F=W²+UV-2t^6; reversing coordinates treats e=1. Differentiation produces (U,V,W,t^5) for p!=2,3 and (U,V,W,t^6) as intrinsic singular ideal in p=3; in p=3 gradients alone give a reduced line/C_- plus isolated reduced Q off cubic, and F restricts to -2s^6t^6 on C_- (thus 6Pa+6Pe). In p=2, global gradients are three quadrics, complete intersection (2,2,2) with local k[t,W]/W², Hilbert 8m-4, genus5. No geometric singular point with a=e=0; hypersurface is irreducible/normal by gcd and R1+S2. Independent SymPy expansion verified exact integral identity, quartic restriction and both Groebner ideal inclusions in p=2,3,5,7; finite checks cannot certify all characteristics or scheme support, which follow from proofs.

## originality

PASS

Compared actual invariant and mathematical implications rather than names. Examined closest primary materials, cited known premises/special cases, and preserved priority risks; no decisive equivalent or dominating all-scope theorem found within checked sources.

## value

PASS

The permanent of the smallest nontrivial Hankel 3x3 matrix is a canonical cubic threefold; polar base versus intrinsic singular scheme is geometrically fundamental exactly when characteristic divides degree. The p=3 reduced polar quartic largely outside the cubic and its length-six intersections are substantive structural degeneration and full characteristic boundary classification, not merely a textbook Jacobian calculation or arbitrary coordinate example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
