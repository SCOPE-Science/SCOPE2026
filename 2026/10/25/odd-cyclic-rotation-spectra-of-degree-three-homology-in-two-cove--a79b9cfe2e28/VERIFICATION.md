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

The complete infinite proof is in `RESULT.md`: (i) classify complete graph-edge orbits under each nonidentity odd-order rotation, (ii) compute exact minimum vertex-cover obstructions, (iii) enumerate the exceptional invariant triangles for order three, (iv) apply reduced simplicial Lefschetz and established adjacent-degree homology character, and (v) take the finite cyclic Fourier transform. The homology concentration and degree-four character are named dependencies, not recomputed or claimed original.

The accompanying reproducibility files are `verify_rotation.py` (Python 3 standard library, no dependencies) and `verify_rotation.out`. Run `python3 verify_rotation.py` from this directory; expected output must match `verify_rotation.out` byte-for-byte and end in `VERIFY_OK`.

Exact integer checks cover the orbit-cost classification for 304 odd-order nonidentity rotations, full signed augmented-chain Lefschetz sums for 28 small cases, and all integer nonnegative eigen-multiplicity formulas for 49 odd sizes from 5 to 101. Numerical complex Fourier reconstructions are supplementary floating-point checks; they are not claimed to be exact linear-algebra certificates. The theorem for all odd integers follows only from the displayed proof and the cited results, not extrapolation from tests.

The older homology-theorem full paper was not accessible in its entirety; the exact indexed rank and concentration statements were available, and the absence of unindexed equivalent character results cannot be guaranteed. Independent audit has not been performed.
