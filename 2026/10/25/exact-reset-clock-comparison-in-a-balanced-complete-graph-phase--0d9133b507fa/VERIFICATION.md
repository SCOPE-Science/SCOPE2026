---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Independent full-generator reconstruction shows both stationary means omega/(r+gamma). Common reset gives S=sum_i X_i=0 and D_S=2A/((r+gamma)(r+2gamma)). For independent clocks, the S^2 jump generator gives E S^2=E||X||^2/2 and D_I=A(2N-1)/((r+gamma)(N r+(2N-1)gamma)). Their exact difference is A r/((r+gamma)(r+2gamma)(N r+(2N-1)gamma))>0. Contraction under coupled reset clocks and Foster quadratic drift establish finite-moment stationary uniqueness; common-mode variance is zero only in the synchronous protocol. I separately solved all full symmetric second-moment equations in 24 rational cases (two protocols each).

## originality

PASS

Bressloff (2024) distinguishes local and global resetting and derives exact Dean-Kawasaki equations plus mean-field phase dynamics; it does not state the finite-N balanced real-linear stationary disagreement/strict cost-matched rational comparison. General resetting and linearized coupling are acknowledged as prior. Obtaining the claimed exact inequality requires an explicit finite-size second-moment closure; no already-stated equivalent was found in inspected sources.

## value

PASS

Clock correlation is a natural controlled variable at identical per-node reset budgets: independent clocks improve relative-phase agreement but create collective fluctuations, a real quantitative tradeoff even when individual means coincide. The all-N positive formula is not a normalization/type check; it separates two modes and permits exact rate comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
