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

The proof of the full infinite theorem uses unique differences, the rank-one Floquet matrix, and a finite-root avoidance lemma; finite verification is supplementary.

To reproduce, run `python3 artifacts/verify.py` using Python 3 standard library after extracting the file from this package. Expected output begins with `VERIFY_OK isolated_negative_flat_bands`. The program verifies exact integer edge displacement multiplicity, the coefficient-by-coefficient Floquet identity, and the actual finitely supported adjacency eigenvector recurrence, not just the eigenspectrum. It computes polynomial greatest common divisors modulo the prime 1009 for specific cases \(2\le r\le5\). Since the two integer polynomials are monic, coprimality modulo 1009 certifies coprimality over \(\mathbb Q\) for those finite examples. It also verifies the exact Laurent identity yielding the global lower bound and equality for the explicit \(r=3\) example.

The modular checks cover only the stated sizes and exponents. They are not evidence that polynomial zeros can be separated for *all* \(r\); that is established by the finite complex-zero set and root-of-unity argument in RESULT.md. No independently performed audit is claimed.
