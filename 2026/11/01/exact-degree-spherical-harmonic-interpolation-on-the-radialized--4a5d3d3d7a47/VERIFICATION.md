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

From the directory containing `verify.py`, run `python3 verify.py`. For a fresh modular residue file, run `python3 verify.py --write-certificate` and compare the generated `determinants.csv` with the supplied file. Python 3 standard-library arithmetic suffices; no approximate eigenvalue tests are used for acceptance.

The checker constructs the twelve exact icosahedral vectors, enumerates all twenty equilateral triangular faces, and obtains their twenty exact dual directions. It builds the sixteen-by-sixteen Gram matrices in the quartic number field, checks the precise ranks for degrees 0 through 44, and verifies strict rational interval enclosures of the dot products. It then checks 205 nonzero determinants mod 1201 or 1229 for degrees 45 through 249, with the exceptional first-prime residues at degrees 86 and 174 handled by the second prime. Finally, the analytical Bernstein bound proves the full-rank tail for every degree at least 250.

This is a finite exact computational verification combined with an analytical infinite argument; it is not an independent audit and does not certify originality outside the literature comparisons stated in `REVIEW.md`.
