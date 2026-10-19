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

# Verification record

The analytical verification concerns the continuous periodic symbol \(2(1-\sin s/s)(b+s^{-2})\) with all \(s>0\), \(b>0\), and horizons \(\delta>0\). Its unique robust tuning is the single root of \(N(s)\) in \((5\pi/2,3\pi)\) transformed by \(F(s)\). The exact comparison uses the low-frequency limiting eigenvalue \(1/6\), strict derivative inequalities on the positive-sinc lobe, and the frequency-band separation proved in RESULT.md.

Run `python3 check.py` with Python 3 and no third-party dependencies. The program checks analytical derivative identities using finite differences, computes the critical root using bisection, independently locates numerical extrema on the first oscillation band, reproduces the sharp condition number and fixed-mass lower bound, and tests numerous sampled Fourier frequencies. Its diagnostic output includes \(b_*=0.174777992381\ldots\), \(\mathcal K(b_*)=1.700200564562\ldots\), and \(6Q_{1/2}(4)=4.013552105416\ldots\).

Numerical sampling does not prove the infinite frequency bounds or priority. Those claims rely respectively on the displayed analytical proof and the documented scholarly comparisons. Independent external validation has not been performed.
