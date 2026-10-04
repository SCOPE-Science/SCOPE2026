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
Run `python verify.py`. A successful run prints `VERIFY_OK`.

The verifier uses exact rational interval arithmetic for the bounded prefix \(5\le d\le26\). Its square-root enclosures are produced from integer square roots at fixed decimal scale, so every interval endpoint is rational and outward enclosing.

For \(d\ge27\), the verifier constructs the algebraic lower bound \(L_d\), eliminates the two square roots by exact resultants, and uses exact Sturm root counts to prove that neither \(L_d\) nor \(z-1\) has a zero on the required half-line; direct exact-algebraic evaluation fixes their signs at \(d=27\). For the lower endpoint inequality, it analogously constructs \(N_d\), eliminates the square roots, and proves no zero on \([14,\infty)\), fixing the positive sign at \(14\). It also checks the exact polynomial determining the endpoint crossing.

The verifier requires Python and SymPy. No stochastic simulation, numerical quadrature, or finite extrapolation is used to establish an infinite statement. The finite prefix is exhaustive only for the explicitly bounded range; the tail conclusions come from exact algebraic root certificates.
