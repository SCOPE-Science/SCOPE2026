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

Run `python check_600cell.py` with NumPy installed according to `requirements.txt`. The checker is packaged as a complete source file and uses no external data or network calls.

The first tier constructs all 120 icosian vertices exactly as elements of \(\frac12\mathbb Z[\varphi]^4\), verifies their exact norms, antipodal pairs and closure under quaternion multiplication, and identifies the 60 antipodal classes and their four nonidentity inner-product classes. The second tier verifies exact character orthogonality and nonnegative integer multiplicities for all 30 even degrees below 60, the finite rank table, the shift identity at 60, and the unique tight rank-59 degree. The independent third tier constructs the degreewise Chebyshev kernel Gram matrix from the actual coordinates and checks its full numerical eigenvalue multiset against the character-table prediction for even degrees 0 through 60. It additionally checks the exact form of the degree-58 projector numerically.

Direct 60-by-60 eigenspectrum calculations are finite corroboration of the separately written algebraic proof, not a proof for all degrees. The rank cutoff for every even degree beyond 60 follows from the exact periodic multiplicity identity. Orthogonality is for Haar probability measure on \(S^3\); the sample target uses an **unnormalized** sum over 60 lines. A different normalization rescales every stated eigenvalue.
