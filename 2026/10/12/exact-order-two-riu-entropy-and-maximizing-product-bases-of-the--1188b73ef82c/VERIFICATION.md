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

The theorem is established analytically in `RESULT.md`. The accompanying checker is an exact replay of the algebraic ingredients, not evidence from a finite parameter search.

Running `python3 artifacts/verify.py` checks the following with exact rational arithmetic in \(\mathbb Q(i,\sqrt3)\):

1. normalization of the six Higuchi–Sudbery amplitudes;
2. vanishing of every one-body Pauli expectation;
3. all six two-body correlation tensors \(-\delta_{ab}/3\);
4. all four three-body tensors as signed copies of \(\epsilon_{abc}/\sqrt3\);
5. all eighty-one four-body Pauli components of the isotropic pairing tensor;
6. the expanded four-vector Gram identity used in the proof.

The universal inequality over continuous local measurement axes is proved by the frame-operator eigenvalue argument in `RESULT.md`; finite replay is not used to infer it.

The result does not establish global optimality of the Higuchi–Sudbery state among all four-qubit states, nor any statement for Rényi orders other than \(2\).
