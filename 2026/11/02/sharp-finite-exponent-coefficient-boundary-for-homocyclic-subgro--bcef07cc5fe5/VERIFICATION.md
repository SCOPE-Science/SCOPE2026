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

# Reproduction of polynomial and coefficient checks

Run the self-contained `verify.py` using Python 3.9 or later, from the directory containing this file. No third-party modules, online services, or source downloads are needed. The output is recorded in `verify_output.txt`.

The program implements Delsarte's subgroup-type sum by direct enumeration of all conjugate-height chains, with exact integer Gaussian-binomial polynomials. A separate transfer recurrence independently constructs the reversed polynomial from successive height transitions. Both entire polynomials were compared for every rank from \(2\) through \(8\) and exponent from \(1\) through \(7\), 49 full-polynomial comparisons.

For even ranks \(2,4,6,8\) and exponents \(1\) through \(7\), a third computation expands \(\begin{bmatrix}2s\\s\end{bmatrix}_t\prod_{j=1}^s(1-t^j)^{-2}\) and verifies exact agreement through degree \(a\) and the first difference \(2a+3\), 28 checks. The program also checks the parity-specific first coefficients and finite-difference vanishing in the asserted odd stable range. All arithmetic is integral. The final marker is `VERIFY_OK`.

These checks do not exhaust all ranks, exponents, or codegrees. The universal statements rely on the explicit noncentral-pattern insertion argument and bounded central-switch proof in `RESULT.md`, and on the established Delsarte and bounded Durfee identities cited there. Neither code execution nor this record constitutes independent validation.
