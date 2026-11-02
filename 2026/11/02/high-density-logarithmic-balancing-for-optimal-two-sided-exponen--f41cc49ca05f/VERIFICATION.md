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

# Verification of the high-density exponential Gabor asymptotics

The exact input is the already-published pair of frame-bound formulas and the global uniqueness/localization theorem from Faulhuber–Shafkulovska, *Gabor Frame Bound Optimizations*, Equation (8.1), Theorem 2.7. These are explicitly prior results, not assertions verified anew by the numerical checker.

The new proof is by explicit factorization of the frame condition number, uniform expansions for \(\eta\asymp\log q\), and an asymptotic derivative balance. The key nonstandard calculation is the cancellation of the \(e^{-\eta}\) term under differentiation: differentiating \(4(1+\eta)e^{-\eta}\) produces \(-4\eta e^{-\eta}\). The positive \(\eta/q^2\) contribution competes with this negative term, giving \(e^{-\eta}=1/(4q^2)(1+O((\log q)^2/q^2))\).

The independent algebraic identity \(b(x)/a(x)=\cosh x\) and the exact formula for the derivative of the logarithm of the frame-condition number are documented in the proof. Replacing the optimized parameter then yields the coefficients of \(\log^2(2q)\), \(\log(2q)\), and the constant term with a total error \(O((\log q)^4/q^4)\).

Run `python check_asymptotic.py` to reproduce high-precision stationary-point comparisons for thirteen integer redundancies from 2 through 16384. It tests the exact critical equation and reports the signed residual in the three-term asymptotic. These computations are supplementary; checking thirteen values does not certify a limit over all integers.

Scope: fixed normalized real window \(e^{-|t|}\), rectangular Gabor lattices, integer redundancy \(q\to\infty\). No statement on nonrectangular lattice optimizers, arbitrary totally positive windows, or finite-density closed forms is intended. The earlier uniqueness theorem is an explicit input. Independent mathematical audit: not performed.
