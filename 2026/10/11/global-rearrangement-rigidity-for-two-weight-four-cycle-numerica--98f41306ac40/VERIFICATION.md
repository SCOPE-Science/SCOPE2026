---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The exact claim is for each real 1<p<∞ and a>b>0 on real/complex ell_p^4, all six arrangements of (a,a,b,b). Duality map is |x_j|^{p-2}conj(x_j) with its continuous zero extension. Positive phases attain the triangle inequality, giving max Φ=Σw_j s_j^α s_{j+1}^β over the 4-simplex, α=(p−1)/p and β=1/p. Concavity of weighted geometric mean is strict up to proportional pairs; connected cyclic edges and mass normalization give unique maximizing positive simplex vector; a zero mass can be improved by transfer from an adjacent positive mass of order epsilon^α or epsilon^β versus O(epsilon) losses. For alternating (a,b,a,b), 2-step cyclic symmetry forces masses s1=s3,s2=s4, yielding H(t)=(a t^{p−1}+bt)/(1+t^p) with unique t>0. Its derivative at t=1 is (p−2)(a−b)/4, hence t>1 for p>2, t<1 for p<2, t=1 for p=2. For grouped (a,a,b,b), evaluating x=(t,t,1,1) for p>2 and (t,1,1,t) for p<2 yields exactly respective positive gaps (t−1)(a t^{p−1}−b)/(2(1+t^p)) and (1−t^{p−1})(a−bt)/(2(1+t^p)); all positive because a>b and t crosses 1 in the proved direction. For p=2, symmetric bipartite matrix singular values give grouped sqrt((a²+b²)/2), alternating (a+b)/2, strict by (a−b)^2>0. Four adjacent vs two alternating placements exhaust all six rotations, and at a=b all radii agree. Every quantifier follows from this analytic argument, not the finite verifier.

## originality

PASS

Best-of-knowledge only: multiple primary full-text comparisons show earlier sharp four-cycle permutation results in the classical p=2 Hilbert numerical radius and related local nonlinear Green-Hessian work, but neither gives the non-Hilbert all-exponent all-contrast strict ordering with certified witnesses. The n=4 p=2 slice is known and expressly excluded as new. Resultary published search found own record (not counted as prior) and local Hessian work, no dominating all-contrast Banach theorem. See structured comparisons and exact residual risks.

## value

PASS

The smallest directed cycle with two inequivalent repeated-two-weight arrangement orbits naturally asks which placement maximizes the Banach spatial numerical radius. The theorem gives a complete global (not perturbative) extremal classification for every weight ratio and every smooth l_p exponent, and explicit nonzero gap witnesses whose forms differ across p=2. This is a motivated structural operator-norm/duality-map ordering rather than a narrow arbitrary table. Unlike earlier local Hessian, no small-contrast restriction remains. It stops at four sites and does not claim exact non-Hilbert grouped radius or a general cycle rearrangement theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
