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

Edge differences form the zero-sum hyperplane and the Lipschitz norm is precisely the maximum of edge slopes, since paths bound all pairwise slopes and every edge is shortest. Changing coordinates gives max(|u|+|w|,(|v|+|w|)/t). Duality preserves the real Euclidean distance, and swapping u,v with a scalar realizes inversion of t. For t≥1 sign averaging preserves the quadratic sandwich and removes off-diagonal entries without raising distortion. On the unit norm body the maximal diagonal energy occurs at |w|=0 or 1: the upper corner energy a(1-z)^2+b(t-z)^2+cz^2 is convex. The reverse squared norm has exact Cauchy–Schwarz maxima 1/a+1/c and (1/b+1/c)/t². Normalize the reverse maximum to 1; at each h=1/c in (0,1) the smallest feasible a=1/(1-h), b=1/(t²-h) minimize the forward maximum. The two branches then strictly increase and decrease respectively. Their difference has numerator −(2t+1)(h−t)(h−t/(2t+1)) over h(1−h)(t²−h); only the second root is admissible, also at t=1. It follows that the displayed Q is optimal and the squared distance is 3−2(t−1)/((t+1)(2t−1)). Its derivative has sign t−2, giving the two reciprocal unique minima with squared value 25/9 and the uniform and degenerate limits 3. The displayed Q is in dual coordinates for t≥1, with t<1 handled by the swap/scaling. Frozen check.py is an exact rational finite check, not a continuum proof; independently verified contact candidates and off-optimum controls at five ratios with Fraction, replay python3 /workspace/branches/independent_finite_checks.py (check 2).

## originality

PASS

The edge-quotient model and t=1 cube endpoint are known. The prior one-defect family already realizes the same numerical minimum, but does not give this alternating profile or its isolated minimizers. Strong same-object catalogue overlaps give volumes and a later Minkowski decomposition, not an exact Euclidean distortion solution. The verdict is for the alternating profile and its sharp ratio characterization, not for transport duality, sign averaging, or the number 5/3 in isolation.

## value

PASS

The four-cycle is the first cyclic transport example beyond trees and the alternating weights are a natural one-parameter deformation retaining opposite-edge symmetry. The exact optimum supplies a nonmonotone contrast with the cube endpoint and a one-defect plateau, identifies the precise best deformation, and produces the sharp quadratic comparison. General norm equivalences do not answer these questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
