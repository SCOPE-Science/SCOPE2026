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

# Verification and reproducibility

The critical mathematical identity is the Hermite–Genocchi representation of the divided-difference remainder for the exponential, integrated with the ordinary simplex measure of mass \(1/m!\). The exact factorization of the top-mode interpolant is \(p_{m-1,t}(L)e^{tL}=1-(-1)^m H_m(t,L)\). Its parity, monotonicity, and unique even-depth zero follow analytically; no finite computation is used to assert infinite validity.

To reproduce numerical cross-checks, run `python3 verify.py` with installed NumPy and SciPy. The checker constructs nonterminal Krylov bases and tests all depths from one to the number of distinct eigenvalues minus one for positive diagonal systems with 5, 6, and 8 distinct eigenvalues. It tests strict Ritz separation, the correct parity sign of the first Lagrange coefficient, odd-depth sign preservation at a finite grid of times, and an even-depth bracketing root with opposite signs. Expected result: `VERIFY_OK 16`.

These finite examples are not a proof of monotonicity of the integral, uniqueness of every root, or any uniform finite-precision stability. The mathematical proof of those properties is contained in the accompanying result. No independent mathematical audit has been performed.
