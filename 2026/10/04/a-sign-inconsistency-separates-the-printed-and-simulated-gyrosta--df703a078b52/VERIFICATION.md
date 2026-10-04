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
# Verification

The algebraic certificate is finite and exact. `verify.py` uses Python's standard-library `Fraction` type and checks:

1. \(F_{1m}=1/3\) and \(F_{3m}=1\) are realized by \(I_x:I_y:I_z=3:2:1\).
2. The printed middle inertial term yields \(F_{2m}=+1\), while Table 1 yields \(F_{2m}=-1\).
3. The cubic coefficient in \(\dot H\) is \(0\) for the table sign and \(4\) for the literal printed sign.
4. The rounded linear gyroscopic coefficients satisfy \(3b_{13}=b_{31}\) exactly at the printed precision and \(3b_{12}-2b_{21}=-10^{-4}\), consistent with decimal rounding.

The proof concerns the equations as printed and does not require numerical trajectory integration. It does not certify the source's basin, Lyapunov, Poincaré, or synchronization computations. Independent audit has not been performed.
