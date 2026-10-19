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

# Reproduction and verification
Run `python3 verify.py` in a directory containing the embedded source file; no third-party packages are required. It uses exact rational arithmetic to check all formulas and feasibility, the full transition matrices, an explicit spanning list of eigenvectors, and an independent finite-size three-variable linear program solved by exhaustive rational vertex enumeration. One completed execution produced:

`VERIFY_OK 453 exact matrix designs, 311949 eigen-equation coordinates, 151 independent LP vertex enumerations`

The sampled parameters are \(2\le p\le12\) and \(2\le q\le14\), together with eight additional widely separated size pairs. A finite computation does not establish a general theorem. The full proof is the symmetry argument, exact invariant spectral decomposition, analytic one-variable minimax argument, and equality analysis in `RESULT.md`. These checks do not provide third-party or independent mathematical validation.
