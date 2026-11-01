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

# Verification of the cubic maximum-modulus theorem

Executed `python check.py` with the dependencies in `requirements.txt`. Exact symbolic Laurent coefficients reproduce
\[\log|f(rw)|=Cr^3(1+|s|^2)-\frac{Cr^3}{2}|w^3-sw^2+\overline s w-1|^2,\quad |w|=1,\]
when \(B=-2Crs\) and \(A=Cr^2(s^2+2\overline s)\). Symbolic expansion also verifies \(\operatorname{disc}(Q_s)=|s|^4+18|s|^2-8\operatorname{Re}(s^3)-27\). The checker checks the exact three-point example \(\exp(8z-4z^2+z^3)\) on \(|z|=1\) and the independent real-coefficient example \(\exp(z-z^2+z^3)\) at radius \(3/4\).

Observed output:

`CHECK_OK: exact Laurent factorization, cubic discriminant, two sharp examples`

The analytic argument, not finite experimentation, proves uniqueness of the possible exceptional radius and the all-radius restriction. The discriminant root-type proof uses reciprocal-conjugate symmetry and the sign of the squared-root-difference product. No independent mathematical audit has occurred.
