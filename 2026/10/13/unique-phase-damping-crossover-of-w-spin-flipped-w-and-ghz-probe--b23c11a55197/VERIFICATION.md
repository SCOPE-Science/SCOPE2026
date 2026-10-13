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

# Reproducibility checks

The standalone `verify.py` builds the dephased density matrix from the computational-bitstring Hamming-distance rule instead of from the reported \(2n\)-state uniform/orthogonal decomposition. It computes the fixed-axis quantum Fisher information using a full numerical eigendecomposition and the two-sided SLD formula. Successful execution with NumPy prints `VERIFY_OK 207`.

Checks comprise 100 numerical spectral-QFI comparisons at \(n=3,\ldots,12\) and ten noise values including both endpoints, 30 algebraic root brackets, five larger-size asymptotic tests, and 72 numerical monotonicity tests. Exact symbolic differentiation and the analytical small-parameter expansion are stated and proved in `RESULT.md`; finite numeric checks do not certify those steps for every dimension. The code does not claim to test experimental apparatus or independent validation.
