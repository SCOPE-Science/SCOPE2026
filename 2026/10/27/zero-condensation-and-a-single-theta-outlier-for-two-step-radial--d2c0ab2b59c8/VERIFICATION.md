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

Run `python check.py` with Python 3 and `mpmath` installed. The executable `check.py` and its exact recorded output are included alongside this file. It tests finite parameter cases, not the infinite proof.

The analytic verification consists of five steps: (i) monomial moments yield \(\mathcal K_N(s)\) with correct normalization; (ii) the Laurent-shift convergence has explicit geometric majorants on every compact subannulus; (iii) the classical Ramanujan \({}_1\psi_1\) product has exactly one simple zero in \(q<|s|<1\); (iv) winding numbers plus the factor \(s^N\) establish the count; (v) a second limit on \(|s|<q\) excludes roots there.

All hypotheses require fixed \(0<q<1\), \(1<\tau<1/q\) and fixed radius \(r\in(q,1)\setminus\{1/\tau\}\). No numerical test certifies asymptotic uniformity or a global whole-disk count. Priority has not been independently confirmed.
