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

The mathematical claim is \(\operatorname{EDdeg}(\mathcal S_{1,n-1})=6n-14\) for every integer \(n\ge4\), for the affine rank-two orthogonal-projector realization and generic complex symmetric data. The proof establishes a smooth spectral curve of genus \(n-2\), a rational critical-value map of degree \(2(n-2)\), and identifies all its generic ramification with genuine ED critical points after excluding isotropic and defective-eigenvalue boundary points.

Run `python -m pip install -r requirements.txt` followed by `python check_spectral.py`. The checker constructs exact arrowhead-characteristic polynomials over the rationals for \(m=2,3,4,5,6,7\). It verifies their squarefree degree-\(2m+2\) hyperelliptic branch polynomials, squarefree degree-\(m\) finite-isotropic-pole polynomials, and nonzero slope at both eigenvalue-infinity corners. It prints the Riemann–Hurwitz values \(10,16,22,28,34,40\), ending in `SPECTRAL_SPECIALIZATION_CHECKS_OK`. The first three values agree with the source's numerical Table 1.

These finite computations cannot establish all \(m\), generic Morse transversality, or uniqueness relative to all literature. Those items are handled by the proof and the scientifically limited literature comparison respectively. No independent audit was performed.
