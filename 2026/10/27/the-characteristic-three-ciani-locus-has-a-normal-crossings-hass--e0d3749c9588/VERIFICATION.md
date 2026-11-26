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

The partial derivatives factor as x(x^2-r y^2-t z^2) and cyclic analogues. On a coordinate line, a critical point is equivalent to the corresponding coefficient being ±1; off those excluded parameter planes, the 2-by-2 principal minors of the system in x^2,y^2,z^2 are nonzero. Thus its determinant vanishes precisely when its kernel yields an all-nonzero critical point over the algebraic closure. This verifies the stated smooth open. In F^2 the three adjoint diagonal coefficients are 2(s+rt), 2(t+rs), 2(r+st), and off-diagonal coefficients have odd exponents and vanish. The determinant therefore defines the nonordinary divisor with multiplicity one on each branch, and stable rank and nullity give the asserted 3-rank and a-number. Completing the square in x^2 gives the stated even quartic for the x-involution elliptic quotient; its middle coefficient is -(s+rt) in characteristic three and tests ordinarity. The two cyclic quotients give the other factors, and the degree-eight splitting isogeny is prime to three, yielding exactly the stated Newton polygons. On the graph s=-rt, the last smoothness factor becomes -(r^2-1)(t^2-1); the remaining exclusion is rt=±1. Two graph equations yield (1-r^2)t=0 in one cyclic case, hence the r-axis with r≠±1 and a transverse normal determinant 1-r^2. The three branch gradients are independent at the origin. For the census one surface has (q-2)^2-2(q-3) points, each pair has q-2, and the triple intersection has one. For the total, the discriminant in t is (r^2-1)(s^2-1); over r,s≠±1 the number of roots summed over t is (q-2)^2+1, because the one-variable quadratic-character sum is -1 (factor r^2-v^2=1 and count q-1 solutions). For t=1 and t=-1 the excluded roots satisfy s=-r and s=r respectively, leaving (q-3)^2 forbidden triples after all coordinate exclusions. The resulting total (q-2)^3-(q-3)^2 and branch inclusion-exclusion give all four stated counts, including (1,0,0,0) at q=3.

## originality

PASS

Existing splitting and explicit Hasse tests already account for much of the rank and Newton description. The supported distinct contribution is their joint simple-normal-crossings geometry on the full smooth marked three-parameter open and the exact all-extension-field census there. Three later-dated Resultary records cover exact portions or all of that result, including the same count polynomials; they are documented material overlap, not demonstrated earlier priority. The earlier finite-field Resultary census has a different family, equivalence convention and range.

## value

PASS

The full marked standard form is a natural parameter space; the claim describes its entire nonordinary divisor and distribution across all extensions, not coefficients chosen after a point search. The intersection pattern and exact counts give a baseline for comparing Newton strata and for enumerating or sampling smooth Ciani quartics, provided one does not confuse parameters with moduli. The splitting and individual ordinarity tests are known ingredients, not the source of this value by themselves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
