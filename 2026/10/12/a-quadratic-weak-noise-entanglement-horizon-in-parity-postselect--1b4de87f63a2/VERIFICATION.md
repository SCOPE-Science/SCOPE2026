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

# Reproducibility

Install dependencies listed in `requirements.txt` and run `python artifacts/verify.py` from the root of the extracted package. The script is self-contained and builds its own exact matrices and quantum-circuit enumeration. It checks the four second-order perturbation coefficients by exact symbolic arithmetic, sixteen noiseless boundary identities, and direct physical state evolution for every two-layer edge-erasure pattern at four probabilities. It compares four independently calculated conditional two-terminal matrices to the proposed asymptotic profile, then checks partial-transpose eigenvalues and solves the positive critical root.

Recorded successful output:

`VERIFY_OK 4 exact Taylor sectors, 16 exact boundary identities, 4096 weighted physical branches over 4 noise levels, 4 scaling limits, negativity, cutoff 0.458661867647`

These finite computations independently check the algebraic inputs. The unlimited layer-depth statements follow from the analyticity of the isolated leading eigenvalue and the transfer spectral gap proved in `RESULT.md`; a finite numerical trace does not certify an infinite asymptotic theorem by itself. The model assumes ideal state preparation, measurements, and byproduct correction apart from independently missing CZ edges.
