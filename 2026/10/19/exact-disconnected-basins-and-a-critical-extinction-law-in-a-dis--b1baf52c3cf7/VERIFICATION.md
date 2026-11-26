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

The sign reduces to the sign of x−a for x>0, with H(a)=a. Since r_+>μ and μ<2, 4a/r_+<4(μ−1)/μ²<1; the upper quadratic takes value a(1+ε)>a at a, so the smaller crossing of level a lies below a and the larger is b>1/2. At b the actual image is a, and (b,1) maps into (0,a). The lower branch is increasing on (0,a) and its limiting value at a is a(1−ε), so that interval is invariant. For r_->1 its unique positive fixed point is in (0,a); increasingness prevents overshoot and the sign of f(x)−x gives monotone convergence from either side. For r_-<1 geometric contraction makes the product of the factors (1−x_j) positive, including for an orbit entering the interval in one step after b; this yields the positive exponential prefactor. At r_-=1 the positive orbit decreases to zero and 1/x_(j+1)−1/x_j=1/(1−x_j)→1, hence nx_n→1. Neither rate claim is for the exceptional endpoints 0 and 1. On (a,b) the right quadratic exceeds a and its maximum r_+/4 is below b: for r_+≤2 use b>1/2; otherwise f(r_+/4)=r_+²(4−r_+)/16≥1/2>a. The continuous logistic self-map of [0,1] at r=r_+ has f²(x)−x=−x(rx−r+1)[r²x²−r(r+1)x+r+1]; the quadratic discriminant is r²(r+1)(r−3), and at r=3 its double root is the positive fixed point. Coppel convergence then applies, and the invariant interval's lower bound a>0 excludes convergence to zero. At r=3 the upper fixed point attracts but is not hyperbolic; locally f² is increasing and its displacement has sign opposite x−p_+, which also gives local stability at this endpoint. The equilibrium at a and its single preimage b, and 0,1, are accounted for separately. Their zero measures leave basin lengths b−a and 1−b+a. At zero dispersal the larger crossing tends to 1/μ while the equilibria merge at a, giving the one-sided limiting selection fraction 2/μ−1. The critical value ε=1−1/μ lies in the stated strip because r_+=2μ−1<3 there. The analytical proof supports all limits; checker.py was read, not executed. It checks symbolic identities and sampled terminal states, not the inverse-time law directly, despite the broader verification note.

## originality

PASS

The scalar map, positive equilibrium branches and strict stability thresholds predate the 2023 source: Singh, Parham and Hu derive the same autonomous resident recurrence in 2011. The frozen Relationship to prior work should credit that antecedent rather than saying the 2023 paper introduced the map. The retained mathematical finding is the exact all-initial-state partition and uniform selection law on the specified weak-growth strip, including the critical trajectories and positive limiting selection fraction, not a newly introduced map or a new general logistic extinction mechanism. The strongest inspected prior results do not give that partition. This is a bounded assessment with the access risks below.

## value

PASS

Exact coexistence ranges do not by themselves say which attractor a given initial density reaches. The discontinuity produces a disconnected lower basin and exact, physically interpretable population outcomes under uniform initialization across the full weak-growth strip. The positive limiting selection fraction despite equilibrium coalescence and the distinction between inverse-time and exponential extinction add precise quantitative conclusions beyond earlier local thresholds and samples. The result is useful for this model even though the underlying logistic convergence and decay mechanisms are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
