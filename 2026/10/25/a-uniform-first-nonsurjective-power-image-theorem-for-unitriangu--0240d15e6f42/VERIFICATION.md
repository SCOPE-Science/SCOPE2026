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

The package contains `power_first_threshold_verify.cpp`, a C++17 implementation of the path-expansion map \(N\mapsto N^p\) on the only relevant first three source superdiagonals of size \(p+3\). Its functions enumerate every allowed six-coordinate target, explicitly construct source entries using field arithmetic, and compare the evaluated power with the target. It also exhaustively enumerates **all** effective first-three-superdiagonal source coordinate arrays in these instances:

* \((p,q)=(2,2)\): 512 parameter arrays; 52 distinct images.
* \((p,q)=(2,4)\): 262144 parameter arrays; 3376 distinct images.
* \((p,q)=(3,3)\): 531441 parameter arrays; 585 distinct images.

In addition it exhaustively checks all *permitted target tuples and their constructed witnesses* (not all source arrays) for \((p,q)=(5,5)\) and \((7,7)\), yielding 13225 and 103537 distinct targets respectively. The implementation models \(\mathbb F_4\) in the polynomial basis modulo \(X^2+X+1\). To repeat: `g++ -O2 -std=c++17 power_first_threshold_verify.cpp -o verify && ./verify`. Observed final line: `VERIFY_OK_UNIFORM_P_POWER_FIRST_FAILURE`.

The universal proof is algebraic, by nonzero path products and explicit source constructions; finite tests neither certify the theorem for arbitrary primes nor constitute an independent review. No independent audit has been performed.
