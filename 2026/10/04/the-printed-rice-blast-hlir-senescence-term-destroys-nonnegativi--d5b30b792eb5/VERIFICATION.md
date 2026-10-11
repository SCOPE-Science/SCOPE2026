---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The counterexample is exact. Disease-free spatially constant data keep u,L,I,R equal to zero up to the switch, while H remains strictly positive by the logistic equation. The source convention changes the Heaviside factor to one for t>t_s, so the right derivative of R at the boundary is -r_s H(t_s)<0 and R immediately becomes negative. A fresh numerical replay using the source values gives H(95)=5.5239951658751245 and right derivative -0.5689715020851378. The source's explicit update has the identical sign defect, and summing the printed component equations reproduces the doubled senescence loss in its total-density equation.

## originality

PASS

Originality passes. The complete primary PDF explicitly declares nonnegative initial states, defines the senescence switch, and prints a removed-compartment equation whose vector field points strictly outward from the nonnegative cone on a simple disease-free boundary state. The immediate predecessor does not contain an HLIR removed compartment, and the bounded searches found no correction of this source-specific sign obstruction.

## value

PASS

The removed density is part of the modeled nonnegative state and enters the paper's disease-severity denominator. An admissible trajectory that is forced negative by the printed senescence mechanism invalidates the claimed compartment interpretation and identifies a necessary correction target. That is a substantive model-consistency result even though more than one biological repair is possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
