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

For a positive continuous P-periodic exogenous three-person share δ(t), averaging derivative of logit y proves ⟨δ⟩−1/3=⟨δ(2x−1)^2⟩ on every interior periodic orbit. Strict positivity gives mean>1/3 for nonconstant δ, and integrated inequality/per-period negative drift yields extinction for mean<1/3 and also equality with nonconstant δ. For δ≡1/3 the logit derivative −(1/2)tanh²(y/2) yields the claimed one-sided semistability. For δ=1/3+μ+η cosωt, reflection and ODE uniqueness give the phase-zero self-reflecting fold and reciprocal multipliers. Analytic IFT and quadratic expansion yield μ*(η)=3η²/(32ω²)+Oω(η⁴). Outside the fold neighborhood the return displacement stays negative; inside, D_ss<0, hence exactly 0/1/2 periodic interior trajectories and the prescribed basins. Applies only for fixed ω>0, sufficiently small |η|,|μ| and positive share, not large or slowly varying regimes.

## originality

PASS

Qualified PASS: Civilini and collaborators derive only the autonomous constant-three-person-share fold; the exact temporal-budget constraint, reversible harmonic fold shift and multiplier relation are not consequences of static equilibrium formulas. Other periodically varying games use different dynamical objects. Time-periodic scalar saddle-node normal forms are general prior theory; the exact coefficient and special reflection constraints in the identified game are the assessed contribution.

## value

PASS

Time-mixed higher-order interactions are a meaningful cooperative-game variant; the exact budget gives a global necessary condition for periodic cooperation independently of waveform, and the sharp second-order shift plus attracting/repelling pair quantifies how temporal variance changes the cooperation threshold. The reflection relation determines both Floquet multipliers without separate stability computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
