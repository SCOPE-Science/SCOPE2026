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

The analytic verification uses three facts: the four BCABE vertices form a regular Pauli tetrahedron; the global Pauli strings commute for an even number of qubits and have four equal-dimensional joint eigenspaces; and partial transposition changes the sign of the \(Y\) factor once for each transposed qubit. These give the complete spectrum and degeneracy without enumeration.

The bundled `verify.py` was executed from its packaged path before assembly. It constructs the matrix representatives for \(N=1,2,3\), checks projector normalization and mutual orthogonality, applies partial transposition for each nontrivial subset size, and compares the numerical spectra with the analytic even/odd formulas for four weight vectors. The execution returned:

`VERIFY_OK parity_spectra=60 levels=3 test_weights=4`

The computation is a finite regression check only. It is not used to infer the infinite statement. The proof in `RESULT.md` supplies the quantifiers over every integer \(N\ge1\), every probability vector, and every nontrivial transposed subset.

The verification does not test or claim separability of arbitrary even-size cuts, nor does it infer distillability from negativity.
