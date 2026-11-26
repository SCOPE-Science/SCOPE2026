---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

This is the coordinate volume of the real dual Lipschitz ball with one value fixed at zero. All distances are positive, so a small coordinate box gives full dimension. Basepoint change preserves the integer coordinate lattice and has determinant of absolute value one. With cross-class distance one and every t_i<=1, the unanchored constraints are exactly global range <=1 and the separate within-class ranges <=t_i. Translation by the anchored coordinate gives an affine cube-volume expression in the cube side L>=1 whose slope is the desired volume. Without the global constraint the cube integral factorizes; choosing the class minimum gives h_i(L)=t_i^(n_i-1)[n_i L-(n_i-1)t_i], with h_i(L)=L for a singleton. At L=1+epsilon the points lost to the global cutoff have one coordinate below epsilon and a different one above one, a union of slabs of total volume O(epsilon^2), so differentiating the product at one gives the heterogeneous formula, including t_i=1. Equivalently, partition the anchored ball by its unique global minimum, change the anchor to that point, and obtain a factor t_j^(n_j-1) for its class and h_i(1) for each other class; summing over minima yields the same formula. For common t, the formal product derivative gives the symmetric-polynomial expansion. A transfer a>=b+2 increases the degree-two product by a-b-1 and hence the volume strictly, since all higher elementary contributions are nonnegative and r>0. This proves the extrema up to permutation, with vacuous strictness when only one partition exists. At t=1 the volume is N. At fixed k,t along k|N, the balanced and concentrated bracketed terms after canceling t^(N-k) have leading terms (1-t)^(k-1)N^k/k^(k-1) and [k-(k-1)t]N; the stated coefficient follows. Three independent Ehrhart checks on sizes (2,1), (2,1,1), (2,2), at scale six with respective radii (1/2,1/3), (1/2,2/3,1/3), (2/3,1/2), gave volumes 7/4, 5/2, 17/9 from exact top differences 126, 3240, 2448. The supplied script was inspected, not executed; the finite tests corroborate only these cases, not the theorem.

## originality

PASS

The decisive same-family catalogue comparison is for within-class distance t>=1, sharing only the equilateral benchmark with the frozen regime. For 1<t<=2 it actually reverses the ordering of balanced and concentrated sizes. Its separate formula and asymptotics at t=2 do not determine the heterogeneous short-distance volume or the exact common-t maximizing/minimizing ratio. The published equilateral volume is credited; the inspected general polytope, primal-dual, and isomorphism results do not supply the exact short-distance formula. The distinct claim is assessed on this bounded evidence, not on a claim of publication priority.

## value

PASS

Anchored dual volume is a natural metric-sensitive convex-geometric invariant for these clustered spaces. The exact heterogeneous formula controls effects of individual radii, and the common-radius result gives a strict comparison of actual size profiles, reversed from the known other side of the equilateral regime. The sharp growth of the balanced-to-concentrated volume ratio quantifies the comparison beyond a qualitative bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
