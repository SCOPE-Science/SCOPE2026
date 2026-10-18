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

At a=−1/2 and b≠0, direct derivatives give H=y−x²/(2b), H_dot=−H and global invertible map (x,y,z)→(x,v=−x/2+bz,h=H) with Jacobian −b. Exact transformed system x_dot=v, v_dot=−v/2−bx+x²/2+bh, h_dot=−h. Bounded complete trajectories require h=0 by backward exponential blow-up. On h=0, E=v²/2+b x²/2−x³/6 gives E_dot=−v²/2; planar saddles/sinks at x=0,2b identified by determinants b and −b. For bounded forward-complete h≠0, E_dot≤−v²/4+b²h² and h∈L² yield v∈L², v→0, v_dot→0 and x(x−2b)→0, hence convergence to one equilibrium. The left-going saddle unstable branch is trapped and tends to sink; right-going branch cannot remain bounded. All nonconstant bounded complete orbits therefore lie on its unique heteroclinic up to translation; ∫v² dt=2ΔU=4|b|³/3. Invariant measures supported on equilibria by invariance of h and E. b=0 solved x=e^(−t/2)x0; linear Volterra/Gronwall gives global forward boundedness, y→0 and z-limit, while bounded complete implies x=y=0. Exact symbolic checker polynomial identities inspected (it alone does not prove global dynamics).

## originality

PASS

Sprott case G itself is known, chaotic parameter plots and equilibrium spectra have extensive prior coverage. The special a=−1/2 exact polynomial Darboux contraction, global planar damped conjugacy, complete classification for every real b (including b=0), unique heteroclinic/action and all invariant compactly supported measures are not implied by the inspected chaotic-regime atlas or positive-a linearization results. Best-of-knowledge priority risk persists for unindexed negative-a classifications.

## value

PASS

A rigorous complete bounded-dynamics theorem on a precisely distinguished codimension-one model parameter plane replaces numerical chaos-region diagrams with a global invariant manifold, a unique connecting orbit and exact dissipation. This is structurally significant within a standard chaotic-flow benchmark; the b=0 degeneracy is a natural boundary of the conjugacy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
