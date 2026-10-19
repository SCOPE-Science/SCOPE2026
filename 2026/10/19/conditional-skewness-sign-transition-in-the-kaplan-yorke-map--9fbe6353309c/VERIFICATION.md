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

The argument is an exact calculation using the Perron operator of the doubling map. Specifically, \(P\cos(2\pi n x)=0\) for odd \(n\) and equals \(\cos(2\pi(n/2)x)\) for even \(n\). Substituting the first two conditional moments into the third transfer recurrence yields an inhomogeneous polynomial with constant and second-harmonic coefficients \(3\alpha^2/4\). Its resolvent gives \(\kappa_3\) exactly for every \(|\alpha|<1\).

To reproduce additional exact checks, use Python 3 and run `python verify.py`. The checker uses only the Python standard library (`fractions`) and tests signed rational coefficients \(\alpha\in\{0,\pm1/5,\pm3/5,\pm9/10\}\). It checks the Fourier recurrences and global moments with exact rational arithmetic and prints `VERIFY_OK` on success. These finitely many rational tests are supplementary: the proof's convergent Neumann-series and Fourier calculation establish the result on the continuum of real parameters.

The supplementary sign check uses the strict inequalities at \(x=0\) and \(x=1/2\) for negative \(\alpha\) and does not assert an uncountable computation. All scientific bibliographic limitations are stated in the result and review. This document does not claim an external independent audit.
