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

# Reproducible checks

Run `python3 check_gradings.py` from the directory containing this file and the script. It exhaustively enumerates every linear subspace and complementary ordered pair, checks the bracket closure axioms directly, and stratifies by the degree of the central element. It also implements finite-field arithmetic of order four by reduction modulo a quadratic irreducible polynomial.

The verified examples are \((n,q)=(1,2),(1,3),(1,4),(1,5),(2,2)\). The resulting totals are \(17,46,97,176,577\), respectively. The check compares every central-parity stratum, including the even-center rank parameter, with exact integer formulas. The expected terminal output is `ALL_GRADING_COUNTS_PASSED 5`.

The proof for arbitrary \(n\) and prime-power \(q\) is the symplectic/Lagrangian classification and group-action argument in RESULT.md, not extrapolation from these tests. No formal proof assistant or independent expert validation is asserted.
