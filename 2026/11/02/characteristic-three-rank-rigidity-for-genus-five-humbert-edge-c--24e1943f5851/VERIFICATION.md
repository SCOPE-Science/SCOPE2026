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

# Verification details

The proof uses tame multiquadratic function fields, Riemann–Hurwitz, elliptic Legendre Hasse invariants in characteristic \(3\), and a pullback/norm isogeny with kernel killed by \(8\). These steps prove the entire algebraically closed field statement without extrapolating from finite experiments.

The exact symbolic command `python verify_loci.py`, with SymPy 1.14.0, returned `PAIRWISE_SATURATION_OK 10` and `COUNT_POLYNOMIAL_OK`. It tests the ten pairwise saturated intersections of the five equations by Gröbner bases over \(\mathbf F_3\), certifying geometric disjointness on the allowed parameter surface.

The independent command `python verify_finite_fields.py`, using only the Python standard library, returned `FINITE_FIELD_OK` with \(q=9\) counts \((12,30)\) for ordinary/nonordinary and \(q=27\) counts \((480,120)\). All five nonordinary components have respectively \(6\) and \(24\) rational parameter pairs over these fields. Direct cross-ratio and algebraic-divisor tests agreed for every pair.

The finite checks do not establish the characteristic-three isogeny theorem, the uniform count for every extension, or uniqueness over algebraic closures. These are justified in the mathematical proof. No independent external audit or validation has been performed.
