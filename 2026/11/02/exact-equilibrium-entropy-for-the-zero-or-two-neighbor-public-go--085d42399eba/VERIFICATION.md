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

# Verification of the exact triangular-strip equilibrium census

Run `python verify.py` in the same directory, with Python 3.10+ and SymPy 1.12+.

The supplied script constructs each of the 64 states and 4096 potential entries directly from the stated binary game. An exact symbolic characteristic-polynomial calculation verifies the factorization, including multiplicities; there are exactly 69 nonzero transitions. Exact matrix-power traces yield \(21,9,3,45,3,33,75,39,69,153\) for lengths three through twelve.

A separately implemented direct graph-neighbor test exhaustively checks all \(2^{3n}\) binary profiles for each \(n=3,4,5,6\), agreeing with the respective transfer counts \(21,9,3,45\). The script also checks the full designated strongly connected 18-state block, its factored characteristic polynomial and two coprime directed cycle witnesses. The unique positive root of \(z^3-z^2-1\) is approximated for display, not used as a numerical substitute for the exact theorem.

The finite enumerations do not establish an infinite-family claim on their own. For arbitrary \(n\ge3\), the proof uses the local-condition/closed-walk bijection, the finite exact determinant identity, and Perron–Frobenius theory. Literature uniqueness and independent validation are not established by this checker.
