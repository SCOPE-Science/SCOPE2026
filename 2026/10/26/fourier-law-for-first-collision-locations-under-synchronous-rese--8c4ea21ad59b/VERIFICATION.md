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

# Reproducibility and proof boundary

Run `python3 verify_collision.py` with Python 3, NumPy and SciPy available. The program independently assembles every nonabsorbing **ordered pair** on odd cycles of sizes \(3,5,7,9\), builds its Markov transition and absorption matrices, solves for expected collision time and the full collision-location probability vector, and checks both against the formulas in `RESULT.md` at four reset probabilities and several initial pairs. A separate set of finite differences checks the zero-reset derivative for sizes \(5,7,9,11,21,51\). Its successful output is `VERIFIED 242 independent exact-state Markov and derivative comparisons`.

The original-pair linear solve and the Fourier expression are computed independently. The finite-difference tests at very small reset rates have floating-point cancellation; the script chooses a size-dependent step and tolerance appropriate for these diagnostics. These tests support the algebra but do not constitute an infinite-size certificate. Arbitrary-size validity follows from the coordinate bijection, exact Fourier boundary recurrence and renewal identity proved in `RESULT.md`.

The finite set does not check parameter values \(r\ge1\), any even-cycle absorbing sector, or a spatially heterogeneous step law. No independent audit has been performed.
