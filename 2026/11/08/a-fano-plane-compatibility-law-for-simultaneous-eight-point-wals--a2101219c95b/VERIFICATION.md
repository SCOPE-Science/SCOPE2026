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

# Verification evidence and boundaries

The standalone `CHECK.py` enumerates all three-dimensional binary subspaces in seven coordinates with every nonzero word of weight four; it verifies that exactly thirty occur. By direct Walsh sums on both eight-element supports, it checks all 480 projected orthogonal spectra against each of the 64 allowed displacement vectors. The run completed with:

`CHECK_OK subspaces=30 spectra=480 mutations=64 direct_pair_tests=860160 incidence_vectors=128`

It separately confirms the thirty-subspace incidence profile for each of all 128 possible seven-bit vectors. Computation uses exact Python integers and makes no floating-point orthogonality tests.

The exhaustive loops establish the stated finite checks; they are not a substitute for the proof that *every* eight-frequency orthogonal system is a Fano-plane simplex-code coset. That is established in `RESULT.md` by the Steiner triple-system argument. The ambient dimension \(d\ge7\) follows analytically from independent character lifts.

The scientific review is same-model only. No independent mathematical audit, external formal certification, or exhaustive historical priority check has been performed.
