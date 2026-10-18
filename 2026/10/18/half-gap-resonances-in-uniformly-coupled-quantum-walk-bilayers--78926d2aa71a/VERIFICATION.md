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

# Reproducible exact checks and mathematical limits

Run `python3 verify.py` using Python 3 and its standard library from the directory containing the file. The verifier uses exact `fractions.Fraction` arithmetic and explicit polynomial spectral projectors. It first constructs single-layer eigenspace projectors from known exact spectra, then independently builds the doubled Hamiltonian's joint spectral projectors by collecting coincident summed energies. It computes the Cesàro mixing matrix as the sum of entrywise projector squares, compares each entry against the half-gap block formula, and checks the rank decomposition by exact Gaussian elimination.

A completed run returned `VERIFY_OK exact_profiles= 42 resonant_profiles= 14 matrix_entries= 2520`. Six distinct intralayer matrices were tested, including complete graphs, cycles and two rationally weighted symmetric matrices. Seven coupling strengths per matrix covered zero, selected exact resonances and nonresonances. The checker does not assume the rank formula while constructing the doubled spectral projectors.

The unrestricted proof is algebraic: tensor exponential, finite spectral Fourier expansion, Cesàro orthogonality, orthogonal layer blocks and Schur positivity. The finite verification is not an exhaustive classification of all real-symmetric matrices or real couplings. It does not address near-resonances over finite observation windows, unequal layers or nonuniform interlayer couplings.
