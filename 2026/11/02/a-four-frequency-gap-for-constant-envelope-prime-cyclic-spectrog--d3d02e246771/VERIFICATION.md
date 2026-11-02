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

The analytical argument is self-contained apart from elementary Fourier inversion on \(\mathbb Z_p\). Fourier-row normalization, the zero-autocorrelation consequence of constant modulus, the singleton-difference obstruction for Fourier supports of sizes two and three, the cocycle/subgroup dichotomy, and the matched-curvature chirp parametrization are explicitly derived in `RESULT.md`.

Execute `python artifacts/verify.py` from the package root using Python 3 and the standard library. In the reviewed package, it completed 446 finite checks over primes 5, 7 and 11, including every two- and three-point frequency set at those primes. These checks are supplementary, not a proof of all primes; they also do not show that support size \(4p-3\) is attained.

Literature overlap was checked against the 2022 exact-minimizer theorem, a published all-signal \(p\)-versus-\(2p\) support gap and a distinct phase-only sparse-input Fourier theorem. Earlier phase-code literature could contain unindexed equivalents. Independent external review and validation have not been performed.
