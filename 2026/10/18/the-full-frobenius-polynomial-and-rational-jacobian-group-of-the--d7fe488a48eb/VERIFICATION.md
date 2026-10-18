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

The standalone `verify.py` runs using only Python 3's standard library. It exactly tests irreducibility of the three finite-field moduli, constructs \(\mathbb F_{3^{2m}}\) for \(m=1,2,3\), computes every affine solution by two independent iteration orders, and checks point-count triples \((1,109,892)\). It verifies the first three Frobenius power sums, reconstructs all six coefficients with the Weil functional equation, expands the factorization, and checks Jacobian cardinality \(343\). The literal machine-readable output is embedded in `counts.json`.

The abstract structure \(\operatorname{Jac}(C)(\mathbb F_9)\cong(\mathbb Z/7\mathbb Z)^3\) is proved mathematically from Tate-module semisimplicity, the polynomial \(U^2-3U+9\), and the count \(343\); it is not purported to have been exhaustively checked by enumerating Jacobian divisor classes. The finite-field computation proves exactly the three extension-field counts needed for the genus-three Weil reconstruction; the claims for all extension degrees follow from the resulting zeta polynomial. The projective uniqueness of the one-point class is a cited prior theorem. Full external independent audit has not been performed.
