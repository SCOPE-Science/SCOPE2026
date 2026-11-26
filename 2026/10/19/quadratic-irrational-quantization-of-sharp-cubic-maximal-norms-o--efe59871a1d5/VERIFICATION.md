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

The two slack factorizations follow from (Λ−1)y²=Λz² and Λz²(3−2z)=1, with 2y=3. On averaging at mean one in L³, the affine term drops out and each zero must be z or y, giving high mass α. Nonconstant finite vectors give quotient above one; Jensen equalization of each group at fixed means improves the quotient unless both groups are constant (a threshold tie may be placed in the upper group). For a fixed mass, differentiation gives the displayed bracket, and dividing by t² gives a strictly decreasing expression with strictly negative derivative at its unique root. Thus the optimal t is smooth and interior. For a→0, write m=a+(1−a)t: m³−t³≤3a(t+a)²; splitting at t=a^(1/3) bounds F−1 uniformly by O(a^(2/3)); the other endpoint follows from F−1≤(1−a)/a. This verifies global maximum separation. The mean-one second variation minimizes 3α(Λ−1)y u²+3(1−α)Λz v² under αu+(1−α)v=−(y−z); every feasible linear slope is realized by a smooth mean-one path. Its reciprocal weight sum simplifies to 1/(3Λz²) by the mean constraint. Consequently κ=3(y−z)/(2D)=1−√7/14 with D=(322−31√7)/162. For the grid, the nearest point yields an O(n^−2) upper bound on the deficit and the maximizing point is then within O(n^−1). The local multiplicative bounds apply to both and squeeze the optimal deficit relative to the squared distance to the nearest point, without assuming the optimizer is always that point. The quadratic integer polynomial gives the lower rational-approximation bound, continued fractions attain the matching order infinitely often, and density gives the n^−2 subsequence. Irrational mass excludes equality on every finite uniform space; atomlessness gives equality of exactly the stated two-level distributions.

## originality

PASS

The complete-graph operator and two-value extremizer theorem are prior. The supported distinct result is the exact fixed-cubic, large-n quantization, including the irrational limiting mass, nonzero curvature, and uniform relative asymptotic on near-integral subsequences. The inspected two-level theorem is a starting point rather than an implication of this arithmetic statement.

## value

PASS

This identifies the sharp norm gap of a natural complete-graph operator, not just a uniform upper bound. Equal atom weights grid the extremizing mass, and identifying the resulting exact arithmetic factor explains why there need not be a single convergence rate. The pointwise certificate and constrained curvature tie the atomless equality problem to the finite-grid behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
