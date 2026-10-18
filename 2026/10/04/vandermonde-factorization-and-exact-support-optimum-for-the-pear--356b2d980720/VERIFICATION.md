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

PASS: For positive masses a,b,c and three distinct ordered support points, the standardized moment Gram determinant det E[(1,Y,Y²)^T(1,Y,Y²)] = kappa-gamma²-1. Determinant of W^T diag(a,b,c)W gives abc times squared three-point Vandermonde divided by variance³, proving exact positive gap. Pairwise variance identity gives V(r)=ab r²+ac(1+r)²+bc, with r>0. I independently symbolically differentiated G=abc r²(1+r)²/V³ and verified G'=-2abc r(1+r)P/V⁴ with published cubic P=a(b+c)r³+a(2b+c)r²-c(a+2b)r-c(a+b). Its signs +,+,-,- and limits P(0)<0, P(infinity)>0 imply exactly one positive root and unique global maximum; endpoint gap tends zero but never attained. For a=b=c=1/3, P=(r-1)(r+2)(2r+1)/9 and G(1)=1/2, hence 1<kappa-gamma²<=3/2. Source checker performs exact rational finite checks, but infinite conclusion is algebraic, not experimentally inferred.

## originality

PASS

PASS, qualified: Pearson equality and the general skewness-kurtosis feasibility region are classical, as is the Gram determinant method; none is claimed novel in isolation. The fixed-positive-masses support-shape maximization, uniqueness and exact cubic boundary are not supplied by the materially inspected general-moment source; its three-valued construction varies masses. A nearby published fixed-mass three-point kurtosis phase diagram optimizes kappa alone, not kappa-gamma², and cannot imply the stated range without separate derivation. Searches revealed no independent stronger table/formula, but older moment-problem literature and incompletely accessible Rohatgi--Szekely article remain priority risks.

## value

PASS

PASS: Prescribed atom masses are a natural constrained moment-family parameter. The result identifies a sharp attainable upper boundary for the *Pearson gap* and unique extremizing support shape, including an exact equal-mass endpoint and quadratic degenerations. Determinant factorization alone is standard algebra; complete sharp support optimization is the independently useful component, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
