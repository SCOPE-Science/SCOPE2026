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

Read the *actual full author-posted primary PDF* and visually checked original model (1) on journal page 3495, F and V on page 3496, printed A_11,A_13,A_31,A_33 and R0 on page 3497, and direct local Jacobian and stability proof on pages 3497–3499. In original F, the Ia production row includes α_y I_y and Ie includes α_a I_a, while in V the same transfers remain with negative sign; therefore the displayed F−V contains 2α_y I_y and 2α_a I_a, but actual model (1) has one of each. The valid new-infection 3x3 F and triangular transition V give K by ordinary multiplication, with ρ(K)=max(ρ(B),β33/η5). Independent exact symbolic sympy arithmetic reconstructs the specified rational B=[[601/1000,6/5],[3/2000,1/1000]], det(I−B)=396801/1000000>0, while printed B[1,0]=1003/2000 and det(I−Bprinted)=−203199/1000000. Actual J youth-adult trace negative, det positive; elder eigenvalue negative. This is a concrete genuine model misclassification, not a statement about the paper’s fitted data.

## originality

PASS

General F/V next-generation construction and treatment of stage progression as transition, not new infection, are standard (van den Driessche–Watmough). But primary original specific model and published printed matrix visibly violate that reconstruction and display the wrong age-transfer factor A31; the explicit rational threshold reversal is source-specific rather than a generic reproduction-number theorem. No published correction was located under exact DOI/title and terms; unindexed erratum remains possible.

## value

PASS

Correcting a reproduction-number construction matters because it can reverse stability interpretation of the published exact mathematical model, shown with strictly positive rational parameters. Unlike a notation-only issue, the error materially misclassifies a threshold used by later analysis. The result has strictly mathematical scope, not medical/clinical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
