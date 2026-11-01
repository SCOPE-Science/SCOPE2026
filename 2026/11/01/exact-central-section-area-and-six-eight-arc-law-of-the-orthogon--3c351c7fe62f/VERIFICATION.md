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

# Reproducibility and limits

The package includes `verify.py`, an ordinary Python 3 standard-library program. Execute `python3 verify.py`. It constructs candidate section corners from cylinder-pair equality lines, counts active arcs for deterministic Gaussian viewing directions, computes the exact elementary sector formula, and compares it with independently sampled planar polar integrals. It also runs a seeded random-orientation comparison against the exact solid-angle probability.

The executed program reported 2,000 exact-pattern arc-count agreements, a maximum 64-case area discrepancy of approximately \(1.63\times10^{-8}\) at unit radius with 25,000-point quadratures, and 100,000-direction frequency 0.64643 against exact 0.649040687816... . These are checks of finite test cases, **not** a certificate of the general proof. The proof of exhaustive breakpoints, exact area, and spherical probability is supplied in `RESULT.md`. All methods are standard mathematics and numerical testing; no external or independent scientific validation was performed.
