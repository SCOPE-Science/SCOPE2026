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

The mathematical proof reduces the symmetric normalized-Laplacian evolution on a regular double cone to one antisymmetric eigenvector and a \(2\)-dimensional symmetric invariant subspace. Its two nontrivial normalized-Laplacian eigenvalues are calculated by exact trace/determinant identities. Strict positivity of both symmetric spectral weights makes exact phase alignment necessary as well as sufficient. Coprime parity then establishes the full if-and-only-if criterion and **all** positive perfect-transfer times, independently of numerical tests.

To reproduce supplementary checks, execute `python3 verify.py` with Python 3 and the standard library. The script verifies exact rational formulas and valuations across 7,450 allowed base-parameter cases for both apex-edge variants; its expected final line is `VERIFY_OK exact_reduced_eigenvalues_and_valuation_tests=7450 examples=6`. The finite sweep cannot establish validity for all integer parameters and is not presented as such. The statement excludes irregular bases, other transfer pairs, decoherence, and other Hamiltonians.
