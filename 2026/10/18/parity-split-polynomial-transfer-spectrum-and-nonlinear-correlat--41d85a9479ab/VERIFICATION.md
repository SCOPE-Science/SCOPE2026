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

# Verification and reproducibility

Run `python verify.py` with Python 3 and SymPy. The checker requires no network, external files, numerical tolerances or randomized seeds.

Its exact symbolic checks establish \(P1=1\), \(P(x-1/2)=0\), the quadratic identity \(Pg=\lambda g+\beta(x-1/2)\), \(\int_0^1g^2=1/180\), and the sharp rate \(\lambda=3(d-1/4)^2+1/16\). Odd-degree annihilation and even-degree leading coefficients are symbolically checked through degree fourteen. Seven rational parameters, including \(13/100\), \(1/4\), and \(27/100\), are each checked at fourteen time lags via exact integration of successive transfer-operator iterates (98 tests). The conjugating polynomial, invariant density and transformed sixth-degree moment are checked independently.

These tests are not a substitute for the displayed all-degree, all-lag proof. No arbitrary-precision simulation, cryptographic analysis, full Banach-space spectral claim or independent review is included. Earlier literature with potentially broader covariance machinery has not all been inspected in full.
