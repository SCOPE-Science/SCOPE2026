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

# Reproducibility and limitations

The exact checker `verify_conic_erasures.py` requires Python 3 and no external package. Run `python3 verify_conic_erasures.py` in the directory containing the checker; successful output terminates with `VERIFY_OK`. It enumerates both quadratic square classes at field orders \(3,5,7,9,11\), enumerates **all \(6,810\)** nonempty masks across those ten conics, and verifies: the cardinalities \(q-1\) and \(q+1\), the absence of multiple unordered nonzero two-sums, the Gaussian-integer convolution identity, one deterministic Gaussian-integer inequality check and a sharpness witness for each mask. For \(q=9\), the code implements \(\mathbb F_3[i]\) explicitly with \(i^2=-1\).

The arbitrary-field and arbitrary-mask claims are established by the algebraic argument in `RESULT.md`, not by finite enumeration. The checker does not constitute an independent mathematical audit or external certification. The theorem does not establish sharp Fourier norms for characteristic two, for higher even moments, or for arbitrary algebraic curves.
