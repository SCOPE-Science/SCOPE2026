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

# Reproducibility and verification

Execute the bundled standalone `check.py` using Python 3 standard library, e.g. `python3 check.py` from the directory containing this package. In direct execution of the packaged candidate, the script reports `PASS: 7870 exact-rational or floating algebra/block/witness checks. Universal claims proved separately.`

The checker uses `fractions.Fraction` to validate the exact zero-frequency trace and determinant identities on 101 rational displacement samples, and the half-cell matrix and \((1,3)\) equality witness. It checks complex-block invariants at selected unit phases, all discrete Fourier blocks for eight periodic cell counts and 99 interior displacement fractions, and signed-grid displacement consistency at 132 sampled cases. These are finite checks and are not a computer certificate for the continuum of phases, arbitrary grid sizes, or arbitrary real Courant numbers.

The mathematical proof in `RESULT.md` independently covers all those infinite quantifiers by symbolic invariants, a strict quadratic comparison at nonzero Fourier frequencies, monotonicity on the full admissible displacement interval, and unitary mesh permutations/reflection. This status does not constitute independent validation or peer review.

The scientific limitations include the distinction between unweighted nodal norm and weighted physical finite-element norm and inaccessible full text of a plausible 2007 source.
