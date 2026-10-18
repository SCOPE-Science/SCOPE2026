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

The exact certificate `spectrum_certificate.json` records all rational coefficients \(a_q\) for \(0\le q\le19\) and all corresponding fully invertible Gram ratios for \(3\le q\le19\). Run `python3 check_sic_spectrum.py` beside that certificate. The checker uses standard-library rational arithmetic for the Jacobi–Legendre recurrence and the extremal ratio, plus independent floating-point SIC vector checks for three distinct angles and sampling kernel spot checks.

The full infinite-degree theorem is proved analytically by the Legendre integral bound \(|P_n(x)|\le1\), giving \(|a_q|\le 4/[3(q+1)]\) for every \(q\ge20\). Finite experiments cannot establish that tail, and a successful checker run alone does not prove the theorem. Independent mathematical audit has not been performed.
