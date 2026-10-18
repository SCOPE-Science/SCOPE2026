---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Differentiate z−x²/(2a): (xy−b)−x(y−x)=x²−b exactly; offset z->z+k only in the y equation does not affect this equality. Boundedness of x,z makes Q(T)-Q(0) O(1), establishing long-time mean x²=b. Compact stationarity gives ∫x²=b, ∫xy=b, means x=y=0 from integrating x and w equations when d≠0, and ∫y²=b+(1/a²)∫(xdot)². For b>0 equality would imply xdot=0 on invariant compact support, forcing y=x and wdot=−2dx there; boundedness of w forces x=0, contrary to ∫x²=b, so strict. These are analytic stationary/long-time proofs, not deductions from simulations.

## originality

PASS

The exact introducing 2020 article prints the model and its three coexisting chaotic attractors at (31,25,15,3.3), offset parameter k and controls, without a coboundary x²−b, invariant-measure moment theorem or branch-independent RMS. A superficially similar forcing-selected variance law exists for a sine-modified Sprott-B vector field but does not specialize, because the ODE differs. The exact coboundary and strict y-activity defect appear as independent, same-model structural constraints in the examined material.

## value

PASS

The exact x-RMS is directly motivated by the source’s central multistability and offset-boosting claims: all bounded coexisting branches, regardless of geometry or offset, have RMS(x)=5 at b=25. The sharp sign obstruction b<0 and stationary strict y-RMS defect are independently testable global constraints on recurrent statistical states, not arbitrary parameter slices or computed Lyapunov coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
