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

# Reproducibility and actual checks

Use `python verify.py` with Python 3 and NumPy. The checker directly constructs the multiplicative-exponent hyperplane sample matrix and checks its normalized complex Gram spectra against the closed occupancy formula. It separately enumerates all diagonal-shift orbits, compares with multinomial occupancy counting, and checks the orthogonality and interpolation thresholds.

The recorded execution completed **124** independent occupancy/orbit/threshold parameter cases and **56** direct complex-character Gram diagonalizations. The maximum direct spectral discrepancy was \(6.661338147750939\times10^{-15}\), below the specified numerical tolerance. Representative cases include a square orthonormal ternary half-band at \((q,d,k)=(3,5,2)\) and a genuinely redundant complete band at \((q,d,k)=(4,4,2)\), with nonzero Gram eigenvalue multiplicities \(\mu_1=21\), \(\mu_2=6\).

The code is finite corroboration only: it checks small multiplicative group orders and dimensions, not all prime powers. The general proof rests on exact character orthogonality and elementary occupancy counting, and is independent of floating-point spectra. No independent mathematical audit or external proof certification has occurred.
