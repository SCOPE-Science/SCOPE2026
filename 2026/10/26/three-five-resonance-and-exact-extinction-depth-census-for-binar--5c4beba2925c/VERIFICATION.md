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
# Verification and reproducing the checks

Run `python3 verification/verify_gp.py` with Python 3.10+ (the implementation uses built-in binary integers, with no third-party dependencies). The script constructs all \(2n\) rows directly from the open-neighbour edges of \(P(n,2)\), independently of the polynomial decomposition in the proof. It repeatedly applies the adjacency matrix to standard basis vectors and computes exact elimination ranks over \(\mathbb F_2\) for \(5\le n\le96\).

It also exhaustively simulates every labelled initial configuration for \(n=5\) and \(n=6\) and checks its first time of reaching a periodic orbit against the claimed cumulative formula. The recorded output is contained in `verification/verification_output.txt` and must terminate with `GP_PARITY_VERIFICATION_OK states= 5120`.

The checks cover \(642\) power-rank cases and exactly \(5120\) initial states. Both computations are finite tests and do **not** imply the universal theorem for all \(n\); that conclusion uses the local algebra proof in `RESULT.md`. The proof assumes no special numerical behaviour beyond the conditions stated there.
