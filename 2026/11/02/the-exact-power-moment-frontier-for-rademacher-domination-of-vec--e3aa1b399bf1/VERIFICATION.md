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

The universal comparison uses the same deterministic step bounds on both sides. Martingale orthogonality proves p=2; the cited planar comparison for even convex C² functions with convex second derivative applies to |t|^p for p≥3, and the cited norm-preserving planar reduction handles every finite Euclidean dimension. For two steps, with previous vector v, s=|v| and increment bound r, the affine chord of (s²+r²+2sr u)^(p/2), u in [-1,1], majorizes the boundary values when p≥2. Subtracting that affine function leaves a convex difference, extending the bound to the ball. Conditional mean zero removes the affine term and the average of (s+r)^p and |s-r|^p increases in s, so substitution of the initial bound is valid. Zero step bounds and the one-step case are immediate. For p<2 the orthogonal two-step witness gives 2^(p/2)>2^(p-1). In the three-step witness the first two orthogonal increments give deterministic norm sqrt(2)δ; the last signed increment is radial and is mean zero given the past. In the reference sum the first two signs have magnitude 0 or 2δ with probability 1/2 each. The even power series cancel through order two; at every order 2k≥4 the multipliers 2^k-2^(2k-1) and binom(p,2k) are both strictly negative for 2<p<3. The first coefficient is p(p-1)(p-2)(3-p)/6, and absolute convergence holds for every 0<δ<1/2. Thus a strict failure occurs at horizon three for the whole subcubic gap and not before.

## originality

PASS

The supported distinct result is the explicit strict planar three-step obstruction for every 2<p<3, giving the sharp frontier and, with the two-step comparison, the first failure horizon. The positive all-horizon range is established prior work. The two-step lemma's method and its monotonicity mechanism are already present in the proof of Juškevičius–Šileikis Lemma 6 after weakening its input from convexity of f'' to monotonicity of f'(x)/x; this auxiliary part is not an independent broad novelty claim.

## value

PASS

The counterexample identifies precisely where a natural sharp Rademacher comparison fails, and the two-step upper bound identifies the minimum failure horizon. A conditionally symmetric planar example of length three distinguishes adaptation from deterministic-direction comparisons; the proof shows that neither a large dimension nor an asymptotic construction is needed. The already known positive theorem and the auxiliary two-step argument do not alone carry this assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
