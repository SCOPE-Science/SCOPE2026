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

Run `python3 artifacts/verify_gp.py` from the extracted package root. Only the Python standard library is required. Its saved stdout is in `artifacts/verification_output.txt`.

The exact cyclic width-two min-plus dynamic program checks all fifteen values `n=8,12,...,64` against the proposed energy and multiplicity, without relying on the independent-set construction. The constructive test enumerates the independent sets and both inner-spin signs for seven sizes through `n=32`, tests exact energy, zero total magnetization, uniqueness of every reconstructed spin configuration and the complete count by number of frustrated even spokes. The `n=8` test exhaustively enumerates all `2^16=65536` labelled configurations.

The proof's five-cycle bound, exact odd-spin minimizer, cyclic run counting and magnetization identities are analytic and universally quantified. The computations are finite cross-checks and do not certify priority or all infinite cases. No separate independent audit has been performed.
