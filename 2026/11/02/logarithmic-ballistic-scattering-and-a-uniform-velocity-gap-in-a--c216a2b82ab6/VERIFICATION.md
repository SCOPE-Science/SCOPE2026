---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Verified the exact substitution s=sign(cx0), z=s y, w=|c x| to z_next=z+w, w_next=w(1+a/(1+z^2)). Because w≥w0, z≥z0+n w0, the increments are summable and w increases to W>0; ∑_{k≥n} a w_k/(1+z_k²)=a/(W n)+O(log n/n²). Summing w−W establishes the logarithmic z correction with finite renormalized constant. At the first crossing z_N≥z0+1, the pre-crossing multipliers ≥r=1+a/(1+R²) and ∑_{k<N}w_k≤w_N/(r−1) force W≥r−1 independent of x0. Nonfixed points escape every compact set, hence Poincare recurrence yields the stated classification of invariant probabilities. Tested signed coordinate identities and velocity bound for five numerical orbits, including x0=10^−12; source script read, not executed.

## originality

PASS

The same positive-feedback equilibrium-line branch of Zhang et al. is the relevant object, but their inspected full article treats existence/stability and mostly a<0 numerical attractors, not all-orbit scattering or the uniform transverse-displacement-independent velocity bound. Related published planar escape laws concern other maps; statement-level coverage is not established by their similar terminology.

## value

PASS

The exact logarithmic correction and especially a nonzero velocity gap uniform as a nonfixed point approaches an entire equilibrium line are natural dynamical boundary properties. The complete invariant-probability classification makes the exact asymptotic globally meaningful; these are not merely a fixed-point computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
