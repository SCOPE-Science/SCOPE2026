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

Verified against the primary publisher PDF: Table 2 bounds the newborn proportion by 0<=u1<1 and allows the adult rate u2>=0; §3.5 supplies dimensional Eq. (3.7) and explicitly uses epsilon=0.07 (the table's epsilon-row label alone is ambiguous); §3.6 sets u2=u3=u4=0 for the quoted threshold calculation and then discusses both first-dose variables. It really reports 1.02 and says choosing greater u1 would make the reproduction number subunit. The Finding extends that newborn-only calculation to the first-dose-only plane. Setting u3=u4=0 in Eq. (3.7), the resulting numerator factor is epsilon(u2+mu)+(1-epsilon)mu(1-u1). For finite admissible controls and epsilon<1 the second contribution stays positive, but tends to zero as u1 approaches one or u2 tends to infinity, proving the sharp infimum and the strict crossing criterion, including the equality case. Separate rational arithmetic using the §3.5 decimals yields K=20.0314888219, K epsilon=1.4022042175, and u1,c=1.0215898907, consistent with the printed rounded equation but outside the admissible domain. The frozen checker was inspected, not executed. This is a reproduction-number result at the stated parameter point, not an eradication forecast for actual populations or for strategies including additional controls.

## originality

PASS

The established leaky-vaccine threshold and residual-risk floor are not original. The supported distinct finding is the feasibility correction for the verified Rahmayani–Aldila–Handari experiment, including that varying the adult first-dose control within the two-control plane cannot salvage the reported crossing at the stated values. The inspected original text gives the ingredients and the formal newborn root but not the infeasibility conclusion; it instead describes a subunit threshold beyond the domain. The checked conceptual and measles-specific comparators do not evaluate or correct this experiment.

## value

PASS

There is a substantive motivation for this otherwise elementary calculation: it corrects an impossible numerical intervention condition that a published analysis presents as a path to subunit reproduction. The positive floor margin rules out using the other first-dose control as a workaround in that exact sensitivity model, rather than merely noticing a percentage-format error. The value is narrow and does not extend to policy inference, incidence reduction, or the combined-dose-and-treatment system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
