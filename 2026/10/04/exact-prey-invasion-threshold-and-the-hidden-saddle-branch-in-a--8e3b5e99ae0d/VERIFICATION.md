---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Adding the predator equation to the prey equation after multiplying the latter by the assimilation coefficient cancels predation and yields a quadratic with exactly one positive predator root. Substitution into the prey equilibrium equation gives the attack-rate branch. Its limit at zero prey is exactly the predator-only invasion threshold. The small-prey expansion has a positive first correction and the Jacobian determinant has the corresponding negative leading term, so the nearby coexistence equilibrium is a saddle. Fresh numerical reconstruction at the source parameters gives threshold 0.208, coexistence equilibria near (8.3358197853,54.8152125587) and (32.0797287675,54.6492858751) at attack rate 0.8, with determinants approximately −0.04513 and 0.06983 respectively; the small branch expansion tends to the predicted unit coefficient.

## originality

PASS

The primary paper gives the exact predator-only stability threshold and nevertheless reports a numerical transcritical event at a larger, initial-condition-dependent value. It does not give the audited exact coexistence parameterization, prove that any boundary collision must occur at the invasion threshold, or identify the small-prey coexistence branch as a saddle. The audited theorem therefore corrects a scientifically material bifurcation interpretation and adds the missing local branch geometry rather than restating the source threshold.

## value

PASS

Correctly locating and typing a boundary bifurcation in a published bistability model is scientifically consequential: it separates the true invasion threshold from a trajectory-dependent numerical transition and exposes a hidden saddle branch that organizes coexistence. The result is a structural correction, not a cosmetic numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
