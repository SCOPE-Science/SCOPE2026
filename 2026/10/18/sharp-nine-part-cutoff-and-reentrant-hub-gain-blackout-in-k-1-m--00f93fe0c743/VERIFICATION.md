---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Connectedness and B>0 make the pinned Laplacian positive definite on the whole compact feasible simplex. Along each nonzero diagonal direction the second derivative is twice the squared Frobenius norm given in the proof, so existence, uniqueness and automorphism symmetry justify reducing all allocations to x=B-2my. The peripheral differences split into the two stated eigenfamilies, and the remaining block has off-diagonal -sqrt(2m). For k=2m, a=k+x and b=1+y, the derivative of its inverse trace along the budget line is [k(b^2+k)-(a^2+k)]/(ab-k)^2. This gives the strictly negative derivative at y=0 and, with the two peripheral terms, P_m(B/(2m))/B at the other endpoint. A zero endpoint derivative selects that endpoint uniquely. For m<=8, the first subtracted term is maximized at m=8 and the factor 2m/(2m+1+y)^2 is bounded by 1/[4(1+y)]; the positive Bernstein and shifted-power coefficients certify the resulting quartic on all y>=0. For m>=9 the cleared polynomial has two sign changes and P_m(m/3)<0, while P_m(0)>0 and P_m is eventually positive. This gives exactly two distinct roots and the stated closed interval. The witness separator m/3 identifies each root when bracketing near y=2/3 and near y/m=1 in the two respective limits, giving B_-/m -> 4/3 and B_+/m^2 -> 2.

## originality

PASS

The closest source on a nearly identical tripartite graph imposes a fixed pair of equal-gain leaders, while the closest statements on the same continuous objective concern different graphs and sign laws. The general inverse-trace design objective and selection tools are prior work. The evidence supports the specific K_{1,m,m} support criterion, exact m=9 onset and two distinct scales as the contribution, not novelty of reentrance in general.

## value

PASS

The unit-edge graph has a distinguished universal vertex, yet adding budget can make its optimal gain go from positive to zero before becoming positive again. The exact integer onset, closed switching interval and different linear and quadratic budget scales quantify this effect across a natural family, rather than recording a numerical exception or a routine optimality condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
