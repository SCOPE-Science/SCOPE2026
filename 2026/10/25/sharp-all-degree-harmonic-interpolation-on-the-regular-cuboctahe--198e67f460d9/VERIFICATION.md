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
# Mathematical verification
The normalized Gram identity follows from the degree-specific addition formula with probability surface measure. The even and odd symmetry decompositions in `RESULT.md` are analytic identities; for the odd sector the exact signed operator has eigenvalues \(\pm2\) each threefold.

Run `python check.py` with the declared dependencies. It computes every finite spectral branch for degrees zero through nineteen with exact rational fractions, checks ranks and the sharp positive minimum, independently constructs the full twelve-vertex Gram matrices for degrees zero through sixty and compares every eigenvalue, and verifies the signed operator with exact symbolic arithmetic. Recorded output is in `CHECK_OUTPUT.txt`.

The analytical tail uses Bernstein's Legendre bound for every degree at least twenty. It implies each strictly positive eigenvalue in that tail exceeds \(1/30\), while the unique global minimum is \(65/32768\), at degree ten. This is a proof for every degree, not an extrapolation of the finite checker.

Limitations: no independent validation has been performed; publication-priority risk remains for historical cubic-symmetry literature not available in full.
