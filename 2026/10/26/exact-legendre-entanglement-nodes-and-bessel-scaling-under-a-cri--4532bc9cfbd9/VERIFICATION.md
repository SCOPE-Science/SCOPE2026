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

# Reproduction and verification

Run `python3 verify_legendre.py` with Python 3 and installed `numpy`, `scipy`, and `mpmath`. The mathematical proof and domain are given in `RESULT.md`; the program tests finite instances only.

The exact age-state recursion uses `fractions.Fraction`, verifies the specified clock against the closed-form weights for every integer horizon \(0\le t\le23\), and tests normalization. The script compares direct complex weighted sums to \(e^{it\theta/2}P_t(\cos(\theta/2))\) at eight phases for every horizon. It independently builds the physical \(4\times4\) mixed density matrix and evaluates Wootters' spin-flip spectrum at 40 parameter pairs, matching the Legendre-modulus concurrence. It counts all numerically represented Legendre roots for degrees 5, 10, 20, 40, 80, and 160, and compares the small-phase limit for \(t=500\) with \(J_0(s/2)\).

A successful run prints `PASS`. Standard floating-point root and special-function checks are approximate; exact finite recurrence tests are rational arithmetic. None of these checks independently certifies the infinite-horizon Bessel limit, full real-root count, or novelty. Those follow analytically from the stated standard generating identities and root/asymptotic theorems.
