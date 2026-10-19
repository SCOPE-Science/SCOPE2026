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

# Verification evidence

Extract `RESULT.md` and `verify.py` into the same directory and run `python verify.py` using Python 3. The checker requires only the standard library. It runs 17 parameter profiles with star sizes 2, 3, and 4 and positive integer effective frequencies, including isolated and overlapping resonance relations. Across these profiles it compares 9,193 matrix entries **exactly** as fractions, using (i) Fourier-supported tensor-projector reconstruction and (ii) independently grouped Hamiltonian spectral projectors with Schur squares. Exact fraction-valued Gaussian elimination also confirms each rank. The tester additionally enforces the full-rank threshold and the isotropic \(P_3\)-power formula within tested profiles.

The successful execution terminates with `VERIFY_OK exact_profiles= 17 matrix_entries= 9193 methods=spectral_projectors,fourier_tensor,exact_rational_rank`. The mathematical proof in `RESULT.md` is valid for arbitrary positive real weights; finite exact tests do not certify unrestricted correctness or novelty.
