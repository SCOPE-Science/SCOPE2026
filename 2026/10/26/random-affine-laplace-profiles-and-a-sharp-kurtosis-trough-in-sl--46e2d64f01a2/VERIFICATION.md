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

# Verification record

Run `python CHECK.py` using Python with NumPy, SciPy and SymPy in the same directory. The saved output is in `CHECK_OUTPUT.txt`: `PASS 487 exact/static/characteristic/moment/OU-matching checks`.

The checker reconstructs inverses of the exact tridiagonal stiffness matrices for 13 chain lengths, checks Brownian-reset versus Ornstein–Uhlenbeck wall covariance amplitudes for nine parameter pairs, checks exact Laplace fourth-cumulant and sharp range formulas at 15 sets of chain and wall strengths, and numerically verifies the covariance limit via continuous-time Lyapunov equations for three finite chain lengths and three small resetting scales each. The test script is included in full; it reads no external research files and generates no dependencies. It was executed from its actual packaged path before final packing.

The proof in `RESULT.md` covers **all** fixed finite lengths at least two and positive parameters. The numerical experiments do not verify infinite parameter ranges or prove that no earlier literature contains the result. Independent audit has not been performed.
