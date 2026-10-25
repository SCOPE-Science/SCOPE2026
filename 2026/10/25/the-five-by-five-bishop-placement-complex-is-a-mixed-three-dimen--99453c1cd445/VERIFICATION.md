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

Run `python verify_bishops5.py` with Python 3 and `sympy==1.14.0`. The script has no internet dependency, no preloaded face table and no external program inputs. It builds all faces from the exact bishop move rule; performs all elementary free-face collapses; constructs the oriented cellular triangular relators, including a BFS spanning tree and freely reduced edge words; checks every one-generator elimination algebraically; checks every remaining attaching word reduces to the identity; derives the join sphere counts; and constructs the original integer signed boundary matrices and their Smith normal forms. A successful complete run ends with `VERIFY_OK_BISHOP5_MIXED_WEDGE_HOMOTOPY`. The separately supplied output record is included for reproducibility, but it is not a substitute for running or inspecting the code.

The computations exhaust the finite \(5\times5\) instance. Nothing here proves a result for larger chessboards. In particular, the Smith calculations independently check integral Betti numbers and non-torsion; the explicit word-level CW cancellations are the certificate for the stronger homotopy decomposition. No independent scientific audit has been performed.
