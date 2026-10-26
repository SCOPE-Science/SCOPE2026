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
# Reproducibility and limits

The analytical verification rests on the frequency decomposition \(E_m\), the exactly computed shifted-Jacobi coefficients \(a_{1,m}\) and \(a_{2,m}\), and the beta-moment bounds for Taylor remainders. The singular-value ordering argument is infinite-dimensional and is part of the proof.

The attached standalone script `verify_radial_commutator.py` uses only Python's standard library. Run `python3 verify_radial_commutator.py`. It passed 224 exact-rational and high-precision finite checks: rational weights including a negative exponent, finite-frequency commutator identities, zero self-commutators, and large-frequency normalization for multiple polynomial symbols. The finite tests cannot establish the claimed \(m\to\infty\) or \(j\to\infty\) limits; those follow from the proof in `RESULT.md`.

The comparison with a 2025 article on bianalytic Toeplitz commutativity was abstract-level because full text could not be retrieved. This limits priority confidence, not the algebraic derivation of the claimed asymptotics.

Independent external audit and validation have not been performed.
