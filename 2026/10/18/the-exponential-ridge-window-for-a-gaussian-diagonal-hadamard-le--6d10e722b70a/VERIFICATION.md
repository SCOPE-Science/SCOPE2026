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

Independent analytic reconstruction. Orthogonality makes the two row-sign classes equally large and x*=0. The scalar normal equation gives (g²−h²)/(g²+h²+2ρgh+η), with an almost surely positive denominator even in the two rank-one sign classes. For |ρ|<1 and below the support endpoint, the upper tail of cos φ/(1+ρ sin φ) is the angular fraction on which cos φ−tρ sin φ>t, namely arccos(t/√(1+ρ²t²))/π. Symmetry, followed by differentiation, gives the stated absolute CDF and signed density. Orthogonal sums/differences give a standard Cauchy at |ρ|=1. Counting fair signs or the two size-N/2 populations gives all the weights, including the exact without-replacement cutoff; the largest nonextreme |ρ| is at most 1−2/m for m≥2, proving the stated support and tail separation. At the extremes the ridge squared risk is Q(η)=E[U²/(U²+η/2)²]. Scaling U=√(η/2)t gives √η Q(η)→√π/2, because the remaining integral of t²/(1+t²)² is π/2. The Gaussian-exponential error in the scaled integral is O(√η) by splitting at η^(-1/2), so the unscaled error is O(1). Away from extremes ridge only decreases squared magnitude. On |R_m|≤1/2 that magnitude is bounded by 4/3, while the nonextreme complement has contribution bounded by B_m² times the exponentially small fair-sign concentration tail. In the prefix coupling R_m→0 and η_m→0 give the arcsine variable of squared mean 1/2. Adding the exact extreme mass times Q(η_m) gives the arbitrary-sequence expansion and all three regimes, with errors governed by m and η_m, not their relative speed. The supplied script was inspected, not executed; the analytic verification does not rely on its numerical tests.

## originality

PASS

The Gaussian/Hadamard ratio and its basic high-probability counterexample are prior work. A later distinct indexed record also gives the with-replacement unregularized law and exact rare-Cauchy tail. Credit here is for the exact regularized risk law, sharp simultaneous ridge constant and sampling-without-replacement classification, not for those shared ingredients. No inspected statement covers that substantive extension. The frozen source's reference to Section 3 of Song–Zhang is imprecise: the PDF locator is §2.2.3, Eq. (3).

## value

PASS

The example is motivated by a specific proposed Gaussian substitution. The exact result explains why the visible typical behavior is not evidence of finite squared risk and gives the regularization scale and constant that balance rare singular sketches against the ordinary sector. It also shows exactly when changing the sampling design removes the pathology, rather than just bounding its probability. These facts are useful for evaluating this sketch on its motivating obstruction even without a general regression theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
