---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS: Strict convexity of constrained unweighted L2 fit fixes a0=-lambda x and gives kappa(z)=3/z^3[z^2/2-1+(1+z)e^-z], strictly decreasing from 1 to 0 by an integral argument. Exact normalized plant/error polynomials X=1-s+k s^2/2 and E=s(k-1+k s/2) lead to negative/positive first-contact rational boundaries L_theta,U_theta. The unique tangent maximum of L at a_theta yields k_theta and an earlier equality-trigger at criticality. For k>k_theta, only later positive contact fires. Taking k down to k_theta gives unattained S_theta>a_theta. Precontact differential inequalities imply positive homogeneous contraction and uniform non-Zeno interevent intervals. Fresh independent theta=1/2 calculation reproduced kcritical=.572949016875, a=1.078689325833 and S=1.630974075664.

## originality

PASS

The source authors introduced parameterized control, polynomial basis least-squares fitting, and qualitative non-Zeno guarantees, but the complete 2023 full conference article explicitly leaves analytic optimum fitting horizon for future work (p.8). It does not establish this scalar specific grazing/nonattainment branch. 2024 paper likewise does not state exact critical formula.

## value

PASS

PASS: A sharp and counterintuitive finite-horizon optimization failure for a specific published control design, despite universal event-time positivity and geometric stability. The discontinuous objective is a motivated design warning and complete scalar classification, not a claim that every control problem lacks an optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
