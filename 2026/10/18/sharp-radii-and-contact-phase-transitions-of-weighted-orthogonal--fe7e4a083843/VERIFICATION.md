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

Support additivity yields h(u)=Σ a_i√(1−u_i²). Central symmetry permits a largest inball centered at zero by the support constraints in opposite directions. If an enclosing ball is centered at c, averaging the squared distances from c to a farthest pair ±x gives ||x||²+||c||², so the minimum enclosing center is uniquely zero. Write s_i=u_i². Since √(1−s_i)≥1−s_i with equality only for s_i=0 or 1, the minimum support is W−max a_i with exactly the stated axis normals. A common support at a point of the centered inball must be its unique tangent support there; this gives exactly the stated inner contact points. For the maximum one can independently set y_i=√(1−s_i), so 0≤y_i≤1 and ||y||²=d−1. Choose y_i*=min{a_i/τ,1}, with τ chosen by Σ[1−(a_i/τ)²]_+=1. That sum is continuous and strictly increasing after min a_i and tends to d; at least two entries are positive at its root because no individual term reaches 1. The decomposition a=τ y*+(a−τ)_+ bounds a·y by τ(d−1)+Σ(a_i−τ)_+ using Cauchy–Schwarz and y_i≤1. Equality is attained uniquely at y*. This proves the threshold rule and its uniqueness, the radius formula, and the strict active inequality even when a weight equals τ. All maximizing normals are independent sign choices on the nonzero coordinates; a support point at maximum support must be Ru by equality in Cauchy–Schwarz, and every outer contact conversely has such a normal. The proposed all-phase examples follow by taking the smallest k weights equal and the remaining weights strictly above the threshold. The d=3 threshold compares the largest weight with the Euclidean norm of the two smaller weights. At fixed sum the inradius bound follows from max a_i≥W/d. Testing equal squared coordinates gives the circumradius lower bound and is globally optimal only for equal weights by the unique y* formula. This also fixes equality for the ratio. Finally u_i² is Beta(1/2,(d−1)/2), whose moment of (1−u_i²)^(1/2) gives the stated gamma quotient for twice the mean support.

## originality

PASS

The distinct contribution is the full weighted, all-dimensional Euclidean phase and contact classification including equality surfaces, with simultaneous sharp fixed-mean-width extremality. The discotope object, support function and standard optimization methods are established ingredients. Individual radius and fixed-sum inequalities have direct short derivations once the simplex problem is formulated; novelty is not credited to those ingredients or asserted to be historical priority. Checked mentions of the unit dice and later exact subfamily matches do not contain a prior covering phase theorem.

## value

PASS

The motivating question is how the nearest and farthest boundary points of an established family of convex bodies change as radii vary. The main payoff is not just an exact number for the unit dice: one scalar threshold resolves every outer contact set and gives all attainable counts and the correct counts on the transition surfaces, where a numerical optimizer or a radius formula alone would not distinguish zero coordinates. It also shows precisely how mean width can stay fixed while Euclidean roundness changes. This is a natural complete phase classification using elementary tools, with a sharp fixed-width comparison, not a new general KKT method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
