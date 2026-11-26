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

Using the rRKN position formula with the second force at q+Vhξ+(Vh)²F(q)/2 gives Q'=AQ+Bξ with A=1−z/2+Vz²/12 and B=h(1−z/6). Independent exact integration against 2v gives 1−E[A²]=zD(z); D strictly decreases since 3z²−32z+104 is everywhere positive. Synchronous coupling gives W₂ contraction precisely while E[A²]<1, an invariant law there, and zero stationary mean. For z≥ρ, the stationary identity for the raw second moment rules out finite second moments since E[A²]≥1 and B≠0. Within the interval the scaled variance is (1−z/6)²/D; the difference from 1 factors as z(z²−8z+8)/(288D), giving both roots and the bias signs. At both roots E[A²]=(z+1)/9<1; B=0 only at z=6, giving δ₀. At all other stable steps a hypothetical stationary Gaussian yields a nonconstant mixture of centered Gaussian variances because A² is not constant. Strict Jensen for its characteristic function rules out that Gaussian. At the two calibration roots the exact remainder of E[A⁴]−1 is (318z−1516)/1215, negative at the smaller and positive at the larger. W₄ contraction gives a finite fourth moment at the smaller root; at the larger a finite fourth moment would violate the fourth-moment identity, whose forcing is strictly positive. No limiting simulation is needed for these statements.

## originality

PASS

Neither the integrator nor the conditionally Gaussian random-affine mechanism is new. The decisive distinct claim is the exact calculation for one rRKN 2.5 substep with triangular stage randomization, including both target-variance roots and their opposite fourth-moment behavior. The defining paper and the closest indexed moment-splitting precedent do not supply these rRKN-specific quantities.

## value

PASS

Stationary variance is an especially natural accuracy diagnostic on the harmonic Gaussian test problem. For a published unadjusted sampler the exact cancellation of variance bias at two step sizes, one with infinite fourth moment, demonstrates concretely why a second-moment check can fail even in the simplest target. The closed-form stability range and roots make the diagnostic reproducible and interpretable without relying on a finite simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
