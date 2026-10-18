---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

N_lambda has polytope unit ball with 8 vertices obtained by signed permutations of (1,a), a=lambda^−1−1 in [0,1]. The arithmetic endpoint (||x+y||+||x−y||)/2 is convex on the product ball, so its maximum is attained on vertex pairs. Symmetry reduces to four orbit values 1, 2lambda, 1/lambda, max(1/lambda,2lambda); the explicit pair (1,a),(-a,1) has both chord norms equal m=max(1/lambda,2lambda). Scalar Heinz ≤ arithmetic mean gives H_nu≤m and equality for this pair gives >=m uniformly 0<=nu<=1. Monotonic branches intersect only at lambda=1/sqrt(2), min sqrt(2); degenerate boundary lambda=1/2,1 checked. Independent exhaustive 64-vertex-pair evaluations at representative lambdas are corroborative; vertex reduction is proof.

## originality

PASS

Best-of-knowledge: the actually inspected Example 4.10 of Zuo–Huang for the same max(l_p,lambda l_q) norm gives formulas only when q<p<=2 or 2<=q<p; the mixed endpoint q=1<2<p=infinity is omitted from both printed cases, notwithstanding an imprecise subsequent claim of full generality. Their general comparison bounds and a conditional theorem do not state or immediately force the full lambda-dependent max(1/lambda,2lambda) profile. Other indexed octagonal-plane records use different invariants, and no stronger exact mixed-endpoint Heinz formula was located.

## value

PASS

Filling a genuinely omitted mixed endpoint of the natural max-of-two-lp family resolves an exact two-dimensional Banach geometric invariant for every Heinz parameter, not just the symmetric/arithmetic endpoints. The sharp phase transition at lambda=1/sqrt(2) and the shared extremizing chords are intrinsic to the octagon/square degeneration family, with plausible use in characterizing nonsquareness and geometrical comparisons, rather than arbitrary case selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
