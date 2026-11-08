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

# Verification scope

The theorem has two complementary reproducible checks. The integer-only transfer certificate constructs every one of the \(81\) local boundary states, verifies the exact cubic vector identity component by component, prints the \(27\) global-color-shift representatives, and checks all indicated recurrence values through \(n=40\). This exact finite identity is a proof step for **all** lengths, not a finite-time extrapolation.

The independent direct simulator checks the full three-update transformation on every configuration of the graphs \(P_n^2\) for \(3\le n\le11\), a total of \(265707\) states. Both the dynamical period-three test and the independently formulated neighbor-phase predicate agree exactly, and the resulting populations agree with the recurrence. Run the extracted files as `python3 verify_transfer.py` and `python3 verify_direct.py`; exact completed outputs are included.

No claim is made about non-three temporal periods, long-time attraction basins, or independent human certification. Numerical approximations to the dominant root do not participate in the proof of the exact population formula.
