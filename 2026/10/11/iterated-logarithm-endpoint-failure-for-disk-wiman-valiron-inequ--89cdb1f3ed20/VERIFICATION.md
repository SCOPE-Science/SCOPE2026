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

# Analytic verification

For real \(x\ge2000\), set \(u=\log x\), \(L=\log u\), and \(g(x)=x/L\). Direct symbolic differentiation independently confirmed
\[
g'(x)=\frac1L-\frac1{uL^2},\qquad
g''(x)=-\frac{1-1/u-2/(uL)}{xuL^2},\qquad
g(x)-xg'(x)=\frac{x}{uL^2}.
\]
The symbolic differences of each pair of expressions simplified to exactly zero. For all sufficiently large \(x\), the derivative is positive and decreasing and the second derivative is negative.

The proof uses a block of indices \(\bigl|k-x\bigr|\le\lfloor\sqrt{x\log x}\log\log x/10\rfloor\); Taylor's theorem bounds each block term below by \(\exp(H-1/100)\). The precise lower bound on the critical quotient is \(\log\log x/(40e\sqrt2)\) for sufficiently large \(x\). Since \(\log_3 A(r)\sim\log\log x\), the normalized ratio diverges and has the stated liminf.

Run `python3 check_saddle.py` to reproduce standard-library, finite-parameter consistency checks. These diagnostics verify finitely many inequalities but are not invoked to justify uniformity over all radii. No external reviewer, independent audit, or formal verification is represented.
