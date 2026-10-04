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

The theorem is proved analytically in `RESULT.md`. The finite checker is corroborative and uses exact arithmetic only.

Running `python3 artifacts/verify.py` constructs \(\mathbb Q(\omega)\) with \(\omega^2+\omega+1=0\), evaluates the five explicit witness polynomials on all nine pairs of third roots, and confirms zero counts \(0,1,2,3,5\). It then checks all \(\binom94=126\) choices of four prescribed zero locations in the local Fourier evaluation matrix. Every rank-three nullspace whose four physical coefficients are all nonzero actually vanishes at five grid points, matching the factorization proof that four zeros cannot occur.

The checker does not extrapolate finite data to arbitrary \(d\). The passage to all \(d\ge2\) is the proved character-restriction statement: the transform depends only on two quotient coordinates and each local value repeats on exactly \(3^{d-2}\) frequencies.
