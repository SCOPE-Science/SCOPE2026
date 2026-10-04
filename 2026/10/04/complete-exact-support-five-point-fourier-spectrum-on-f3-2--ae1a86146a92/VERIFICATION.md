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

Run `python3 artifacts/verify.py` with the standard Python library. The checker uses exact `Fraction` arithmetic for \(\mathbb Q(\omega)\) with \(\omega^2+\omega+1=0\).

It verifies all \(126\) five-subsets of \(\mathbb F_3^2\) lie in two affine orbits of sizes \(54\) and \(72\). For each canonical representative it exhausts all \(512\) candidate Fourier-zero row subsets, computes exact ranks and row-span closures, checks that exact spatial support is compatible with the kernel, and confirms that the only attainable zero counts are \(0,1,2,3,4\). It also directly evaluates explicit Eisenstein-integer coefficient vectors realizing each zero count on each representative.

The finite computation proves only the stated nine-point theorem; no extrapolation to larger fields or dimensions is made.
