---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction and scope

Execute `python verify.py` after installing the dependency in `requirements.txt`. This independently performs the **new endpoint and residence-time interval calculations** using rigorous outward-rounded `mpmath.iv` arithmetic. It constructs high-precision switching-time guesses only to select rational enclosures; the acceptance of every switching interval, the crossing-direction signs, and the return displacement signs comes from interval calculations, not from point estimates.

Verified new rational initial conditions, in order: -0.569204, -0.569203, -0.55677, -0.55675, -0.55517, -0.55514. Certified return-displacement signs: positive, negative, negative, positive, positive, negative. Guaranteed exterior residence bounds: first interval above 0.8984045, second below 0.861155, third above 1.000965. These strictly separate the three intervals from the critical residence time 2π/7 between 0.8975979 and 0.8975980.

The program does not independently redo the previous paper's whole-interval first-hit and no-grazing certificates. Those fully inspected existing lemmas are explicitly imported as mathematical premises, not presented as new calculations. The original preprint's central-cycle multiplier bound is also a prior premise. The full seven-cycle proof is a mathematical combination of these premises, certified new interval bounds and scalar crossing monotonicity.

No independent audit has been performed. The interval checks are mathematical computational evidence, not proof of global uniqueness of all periodic orbits outside the prescribed intervals.
