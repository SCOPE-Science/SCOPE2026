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

The proof uses the exact positive-band criterion of arXiv:1804.01414 rather than a finite enumeration. The accompanying `verify.py` supplies independent finite-index checks of the algebra and asymptotics.

The checker performs four kinds of tests:

1. It compares the source inequality (32), evaluated directly, with the factorized condition (34) at representative points in even and odd cells.
2. It locates the two finite-cell band edges by bisection and evaluates the exact energy-measure fraction.
3. It compares those finite-cell fractions with the theorem's limiting function for multiple edge lengths and for scaling constants below, at, and above the pinch.
4. It verifies that the source's exact collapse parameter satisfies the claimed scaled limit.

Representative results for the canonical sequence \(t_m=\tau/m\) include, for \(\ell=1\) and \(m=1000\), limiting value \(0.515524233636626\) versus finite-cell fractions \(0.515524185707415\) and \(0.515524306519799\) at reciprocal sides of the pinch, while at \(\tau=4/\pi^2\) the finite-cell fraction is \(0.000318208581673\) and tends to zero.

Running `python3 verify.py` returns `VERIFY_OK`.

These computations are consistency checks only. They do not replace the analytic uniform-threshold argument, and they do not certify an optimal convergence rate or any statement outside the scope given in `RESULT.md`.
