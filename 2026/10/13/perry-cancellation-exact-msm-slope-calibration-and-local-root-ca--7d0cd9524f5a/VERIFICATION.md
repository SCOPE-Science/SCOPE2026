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

For the displayed specialization, the scalar orthogonal Perry correction is identically zero when E(y) is nonzero. With E(z) nonzero the projection multiplier times E(z) equals y-z, so zero inertia gives s=gamma*tau*d and p=a*s. The stated raw quotient simplifies to -Gamma*s/(tau*zeta*y)=gamma*a. A nonterminal k=1 update therefore first locks Gamma_2 under the strict retention condition; k=0 is not covered. In the locked map with first trial 1, 1<=zeta<=5/4<gamma; for y nonzero one can divide the sufficient acceptance inequality by the positive a*zeta*y^2*(1-zeta/gamma)/gamma. Since the right-hand minimum is at most nu*|E(z)|, it suffices that |y|<=gamma/(sigma*nu*zeta). The first unit update reduces |y| by at least a factor of four (or already hits zero) and resets zeta to 1, so another accepted unit update hits zero. The state recurrence, not the line search globally, is slope-free: outside the sufficient basin acceptance can still depend on a. My exact rational replay (branches/independent_small_replays.py perry) gives Gamma=28/15, states 1,-1/4,0 and nonzero trial points 3/28,-1/14. This checks the stated equations, not a reconstruction of the complete implementation. The PASS is for the stated mathematical specialization, with defined quotients and stopping caveat; the external primary text could not be independently transcribed, and no additional source guarantees are inferred.

## originality

PASS

The supported distinction is the exact scalar lock combined with a quantified two-unit-step basin for the specified Perry/MSM/relaxed-projection recurrence. Scalar Perry cancellation in isolation is immediate algebra and is not credited as an independent novelty. The accessible nearest algorithm and indexed neighboring result have materially different directions and no state identity or capture implication matching this claim. Limited by unavailable primary full text.

## value

PASS

The scalar affine mode is a natural diagnostic for a spectral projection method. The lock separates the projected Perry correction from what the spectral loop does, and the explicit basin explains exactly when the unit trial switches the recurrence into finite capture. This gives a parameterized check that is stronger than merely observing descent on sample runs, without claiming a multivariate result or global finite termination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
