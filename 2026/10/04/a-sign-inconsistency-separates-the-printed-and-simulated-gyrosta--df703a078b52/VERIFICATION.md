---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Table 1 values \(F_{1m}=1/3\) and \(F_{3m}=1\) force \(I_x:I_y:I_z=3:2:1\). Literal normalization of the printed middle inertial term \((I_x-I_z)xz\) therefore gives \(F_{2m}=+1\), while the table defines \((I_z-I_x)/I_y=-1\). For \(H=(3x_1^2+2x_2^2+x_3^2)/2\), the cubic inertial coefficient is exactly 0 for the table sign and 4 for the printed sign. Independent rational arithmetic reproduced these identities.

## originality

PASS

Direct inspection of the 2022 paper and fresh semantic searches found no prior published statement of the equation-to-table sign inconsistency or the exact energy-cancellation consequence. The 2019 gyrostat energy source motivates the structural check but does not cover the later paper’s mismatch.

## value

PASS

The sign changes the nonlinear vector field and destroys exact inertial energy cancellation by adding \(4x_1x_2x_3\). Since the paper’s basin, Lyapunov, Poincare and synchronization calculations are tied to System (2)/Table 1, the distinction is materially important for reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
