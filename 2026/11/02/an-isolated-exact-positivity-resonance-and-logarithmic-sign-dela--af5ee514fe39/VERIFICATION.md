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

The standalone `verify.py` performs exact symbolic checks of the fixed-step characteristic factorization, the backward-Euler starter coincidence, and the conjugate-root quartic at \(r=\sqrt5\). It proves disjoint root disks by arithmetic bounds evaluated in \(\mathbb Q(\sqrt5)\) using a checked rational enclosure. These finite exact certificates support the spectral premises of the analytical proof in RESULT.md.

The program also runs 170-digit scalar recurrences on both sides of the resonance to test the predicted sign phenomenon and first-negative indices, as supplementary illustrations. Finite recurrence tests are not proofs of infinite sign changes or of the delay asymptotic; the needed Vandermonde and oscillation estimates are provided analytically in RESULT.md. No external independent audit has been performed.

Reproduce from this directory with `python verify.py` using SymPy and mpmath. The claim requires exact arithmetic and four backward-Euler starting steps; the code does not simulate roundoff stability or alternate starting procedures.
