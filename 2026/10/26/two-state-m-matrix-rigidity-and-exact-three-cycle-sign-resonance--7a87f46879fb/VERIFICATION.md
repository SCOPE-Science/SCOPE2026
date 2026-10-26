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

# Reproduction

Install the declared package dependency using `python -m pip install -r requirements.txt`, then run `python verify.py` with Python 3. The checker implements the matrix function by summing \(\varphi_1(X)=\sum_{k\ge0}X^k/(k+1)!\), without relying on the analytic circulant inverse formula. It compares both constructions at 13 positive time values, verifies matrix inverse identities and sign patterns, checks five exact sine-resonance times, 20 Taylor positivity coefficients, and four two-state generators including absorbing and zero-rate cases. Expected output: `VERIFY_OK 88`.

# Analytical certificate

The identity \(F_t tQ=e^{tQ}-I\) proves strict ordering of the three integrated Poisson residue weights. The inverse Fourier formula gives the exact positive two-jump coefficient. Its numerator has only positive nonzero even-power Taylor coefficients for all positive arguments, with the first nonzero term at degree four. This proves the strict sign without any finite search or floating-point inequality. The sine factor establishes the complete resonance set. Two-state inversion follows from \(Q^2=-(a+b)Q\).

# Scope of the check

Floating-point calculations and finitely many Taylor coefficient tests are independent consistency checks, not certificates for all positive real arguments. The general proof is in `RESULT.md`. No independent external audit was conducted.
