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

For the stated strip and a<1 the angular increment for F(z)=S(z) is exactly 1/2, forcing I=±ρ; each prime two-cycle has exactly one +ρ representative. Then b g(θ)=(2−γ)ρ and g=4 sin(2πθ) cos²(2πθ). On the positive half of the circle each interior root t=sin(2πθ) of 4t(1−t²)=(2−γ)ρ/b gives a reflected pair. This cubic peaks nondegenerately at t=1/√3, with nonzero angular second derivative and nonzero forcing derivative, proving both symmetry-class folds and the orbit counts. Independently, the derivative T of S∘F at a representative has trace γ−k and determinant −q, where k=2abρg′(θ). Since (S∘F)²=F² the return has trace (γ−k)²+2q and determinant q². Thus it is exponentially attracting exactly for 0<k<2γ, a saddle outside the closed interval, and has multipliers 1,q² at either endpoint. The reflected phase choices give opposite signs of k. On the positive branches k=2π(2a−1)(2−γ)|1−3s|/√(s(1−s)), s=t². Differentiating the square gives the sign of 3s−1, so each branch reaches 2γ exactly once; the two roots of the resulting quadratic give the stated thresholds. At the same b>b₀ the cubic roots x<y obey x²+xy+y²=1. For r=y/x>1, the square of the ratio of their positive k values is r(r+2)²/(2r+1)², which exceeds 1 because the numerator minus the denominator is r³−1. The low-t branch therefore crosses first, with the table including the boundary counts. A separate direct return-map differentiation and bisection at three parameter pairs corroborated the crossing values (replay: python /workspace/branches/review05_direct_return.py); the symbolic argument covers the entire range. The unit multipliers exclude exponential attraction at the boundaries, not all possible nonlinear attraction.

## originality

PASS

The odd-harmonic symmetry, dissipative map and numerical periodic regimes are prior work. The exact counts and strictly ordered thresholds within the specified symmetry strip do not occur in the closest inspected same-map passages or Resultary comparisons. This is a bounded comparison, not a historical priority certificate.

## value

PASS

The symmetry picks out a natural class of periodic attractors of the studied map. A simultaneous birth does not imply a simultaneous later loss: the strict analytical separation gives a genuine one-sink regime for every admitted a and γ, even where a numerical period diagram would barely resolve the two crossings. The formulas and exact census are useful independently of global basin or bifurcation classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
