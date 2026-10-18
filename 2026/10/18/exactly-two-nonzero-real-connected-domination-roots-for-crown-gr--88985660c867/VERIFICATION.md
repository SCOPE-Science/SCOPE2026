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
# Verification and mathematical limits

Recompute by running `python3 verify_crown.py` with Python 3.8 or newer; no external libraries are needed. The verifier constructs the edges \(a_i b_j\) for \(i\ne j\), evaluates domination as a union of closed neighborhoods, computes induced connectivity using graph traversal, and enumerates every subset for each \(n=3,4,5,6,7,8\). It independently builds the predicted connected-domination coefficients via the two-shore binomial convolution and the unique paired obstruction, and asserts exact coefficient-by-coefficient agreement. The check covers complete universes of \(2^{2n}\) subsets for these six fixed orders, not every order.

The script also bisects both real roots for illustrative orders \(3,4,5,6,10,21,50,101,200,301\). These numerical calculations do not establish a uniform root theorem, root uniqueness, or the asymptotic constant. The symbolic proof relies instead on the second-order integral representation of \(R_n\), strict monotonicity for odd degree, strict positivity/convexity for even degree, and exact parity-separated exponential identities at the left root. The results are conditional only on the explicitly stated graph and polynomial definitions; no unproved probabilistic, spectral or independence assumption is used.

For \(n=3\) the polynomial equals \(x^4(x^2+6x+6)\), with the two nonzero roots \(-3\pm\sqrt3\), consistent with the strict intervals. Boundary \(n=2\) is intentionally excluded because the crown is disconnected. The complex zeros other than the two real nonzero roots are not localized. No independent external audit has been performed.
