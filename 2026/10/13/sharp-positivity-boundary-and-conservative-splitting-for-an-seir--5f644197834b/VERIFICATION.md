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

Summing the four printed living updates cancels transmission, progression and recovery and gives d^+-d=h*mu*i^++alpha*h*(r^+-r). Substituting r^+-r=h*(gamma*i^+-alpha*r)/(1+alpha*h) proves the one-step nonnegativity condition with equality allowed, and separately the condition for nondecreasing deaths. The living updates are nonnegative and at least one stays positive for finite h whenever the current living fraction is positive. For alpha=0 the mortality increment is nonnegative. For any fixed positive h, alpha and other stated rates, start with e=i=d=0 and 0<r<1: the exact death residual is -alpha^2*h^2*r/(1+alpha*h). Perturb e,i,d upwards while reducing s; continuity gives strictly interior counterexamples for this same h and rates. In the balanced update the waning transfer is bounded by r; the subsequent four nonnegative transfers occur with opposite signs in donor and recipient, giving zero net mass change and nondecreasing deaths. Expanding each transfer to first order at fixed 1-d>0 gives the continuous SEIRSD vector field and O(k^2) local defect for h=k+O(k^2). Setting alpha=0 makes the updates coincide exactly. The stated domain excludes d=1 where q is not defined; the balanced state map can be extended there by fixing the all-deceased vertex since q is bounded by beta on the punctured simplex and all updated living coordinates tend to zero. Independent exact replay `python3 /workspace/review_replay.py 1` reproduces both vectors, including deaths -58583/161600 and 243/161600. The frozen checker was inspected, not executed.

## originality

PASS

The unmatched mortality correction is closely anticipated by the earlier SIRSD paper and general paired-transfer positivity methods are established. The supported distinct contribution is the exact equivalence for the particular published five-coordinate SEIRSD recurrence, including the obstruction for every positive h at every positive immunity-loss rate, and a sequential replacement retaining the original permanent-immunity update. The source's numerical experiments with alpha=0 are outside the negative-death cases.

## value

PASS

Population-simplex feasibility is a meaningful structural requirement of the printed numerical method. Its failure is not just normalization error or a single large-step artifact; the exact frontier distinguishes feasible inputs, and for each step there are valid strictly interior states that return negative deaths. The matched variant preserves the established permanent-immunity use case and corrects temporary-immunity feasibility without claiming higher accuracy, universal stability, or an improvement in epidemiological inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
