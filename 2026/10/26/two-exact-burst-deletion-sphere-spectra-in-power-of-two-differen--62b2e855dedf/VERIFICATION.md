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

Run `python3 verify.py` (Python standard library only). The stored `verification_output.txt` was generated from this source file, and the execution ended with `DVT_BURST_SPECTRA_VERIFY_OK`.

The direct enumerator constructs every word and set of all distinct adjacent-two-deletion outputs at source lengths 4, 8, and 16. It checks every syndrome against each claimed polynomial, the local transition-count identity, and the total perfect-covering incident count for each class. An independent integer dynamic program on the first `n-1` difference bits checks all syndrome residues and polynomial coefficients at `n = 4, 8, 16, 32, 64`. The DP visits each possible syndrome, terminal difference bit, and transition count, using only exact integers.

These are exhaustive only at the stated finite lengths; the theorem for arbitrarily large powers of two rests on the Fourier/orbit proof in `RESULT.md`. No independent audit has occurred, and no verification of coding performance beyond the stated mathematical invariant is claimed.
