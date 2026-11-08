---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For continuous positive T-periodic environmental forcing w and strictly interior T-periodic orbit (x,r) of Jiang et al. Eq.(9), with a,b payoff symbols A=rP_N−1,B=r_d Q_N>0, differentiate H=−log(1−x)+[epsilon(beta−alpha)]^(−1)log((r−alpha)/(beta−r)). The A terms cancel and dot H=B[theta−(1+theta)x], hence over a full period E(xB)/E(B)=theta/(1+theta) for every N>=2. When N=2, Q_2=x/2 even at w=1, hence E x²=theta/(1+theta)E x and Var x=bar x(theta/(1+theta)−bar x); for nonconstant x the unweighted mean is strictly less than the static equilibrium. At N=2 theta=r_d=1, alpha=3/2,beta=9/5,epsilon=12,w=1+eta cos t, unforced equilibrium (1/2,5/3) has Jacobian [[1/12,3/16],[-8/45,-1/10]], trace −1/60, determinant 1/40. Its period map is locally invertible in initial state, giving an attracting interior analytic periodic branch. First harmonic from (iI−J)z=(5/48,−1/18) gives |z_x|²=625/54772; time-shift eta→−eta gives even mean, so bar x=1/2−(625/54772)eta²+O(eta⁴). Independently rederived symbolic Jacobian and amplitude. The exact identity, not bounded shooting, establishes unbounded parameter claim.

## originality

PASS

Jiang et al. 2023 establishes governing ODE, static equilibrium and periodic response examples; the exact payoff-weighted mean identity, N=2 finite-amplitude variance penalty and local perturbation coefficient are not stated in its inspected Eq.(9)/periodic sections. Other environmental-feedback mean laws in indexed records use different ODEs, so do not imply this one by renaming variables.

## value

PASS

An exact integration law for every interior periodic orbit of a physically motivated nonlinear feedback game, with a strict measurable fluctuation cost in pairwise groups and an analytically constructed stable forced example. The result goes beyond observing trajectories or a static equilibrium fraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
