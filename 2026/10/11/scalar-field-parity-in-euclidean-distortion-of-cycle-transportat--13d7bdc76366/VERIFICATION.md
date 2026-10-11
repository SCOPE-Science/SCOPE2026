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
# Verification notes

The script `verify_cycle_hilbert.py` uses Python's standard library only. It enumerates the vertices of the real zero-sum cube section exhaustively at every integer dimension from \(3\) through \(11\). It checks the parity-dependent squared Euclidean extrema with exact arithmetic, confirms the normalized Cauchy–Schwarz witness with `Fraction`, and checks the derived squared Banach–Mazur distance against its symbolic formula. It also verifies the roots-of-unity witness for the complex case to floating-point tolerance in the same finite range.

Execute `python verify_cycle_hilbert.py` from the directory containing this file and the verifier. A successful run concludes with `CYCLE_HYPERPLANE_CHECK_OK`.

The mathematical proof is independent of finite enumeration: it proves optimality among every positive-definite quadratic or Hermitian form by permutation averaging, the common lower extremum by Cauchy–Schwarz, the real upper extremum by general vertex structure, and the complex upper extremum by an exact geometric-series identity. No infinite-dimensional statement or arbitrary edge-weighted cycle claim is asserted. The executable verifies finite identities and does not provide an external certification of the all-dimensional proof.
