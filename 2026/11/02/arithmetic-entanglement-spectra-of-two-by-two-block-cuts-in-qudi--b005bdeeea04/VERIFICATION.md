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

# Reproduction and limits

Run `python3 verify_rook.py` with Python 3.9 or newer in the directory containing the standalone script. The script uses no third-party package and independently constructs each cut-adjacency matrix from pairs of rook-board coordinates, not from the analytic margin factorization.

The replay produces `GF_P_CUT_RANK_OK 1168`, covering every positive block-size quadruple up to four for primes 2, 3, 5, plus 400 seeded cases through prime 7. It produces `DIRECT_QUANTUM_PURITY_OK 4` after constructing graph-state amplitudes, tracing out the complementary subsystem and comparing purity against the asserted Schmidt rank. It also prints four exact modulus-sensitive example checks and `VERIFICATION_OK`. The actual record is in `CHECK_OUTPUT.txt`.

The mathematical proof of the infinite family is the surjectivity of the row/column margin map, the two-scalar characterization of the cut kernel, and the exact finite-field character sum giving the flat reduced-state spectrum (RESULT.md). Those analytical arguments—not the finite program—justify the universal quantifiers. No claim is made about untested gate weights, arbitrary partitions, or prior-literature completeness.
