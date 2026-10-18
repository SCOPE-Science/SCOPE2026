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

Use Python 3 with no third-party dependencies and run `python3 verify.py` from the directory containing the extracted files. The executable must print `CERTIFICATE_OK` after checking the \(22\times22\) Sylvester determinant, the complete factorization into \(23,67,89,199\), all constraints on the prime-field eleventh roots, every root of the first reciprocal-moment polynomial, the two possible second-moment polynomial evaluations, and the explicit characteristic-\(23\) permutation.

For \(p=67\), the four possible \(\zeta\) values leave six first-moment roots and twelve joint cases; for \(p=89\), two and four; for \(p=199\), four candidate \(\zeta\) values leave four first-moment roots and eight joint cases. Each joint case has nonzero second moment. No external files or snapshots are inputs.

The verifier does not enumerate unbounded fields. Its exhaustiveness applies to the **finite prime-field obstruction** to which every hypothetical extension-field permutation is reduced by the proof in `RESULT.md`. Analytical identities and the quotient-map implication must be checked mathematically; the script cannot certify those implications independently. A publication-priority check also remains non-independent.
