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

## Analytic checks
1. Strict cyclic row dominance implies a uniform positive eigenvalue interval \([1-\delta,1+\delta]\); no real power encounters zero.
2. Every term of the characteristic determinant is phase-independent except the two oriented full-cycle permutations; their exact combined contribution is \(-2R\cos\phi\).
3. For simple eigenvalues the derivative of the spectral power trace equals an order-\(m-1\) divided difference of \(x^{p-1}\). Its Hermite--Genocchi integrand has sign \(\operatorname{sgn}\prod_{k=1}^{m-1}(p-k)\).
4. The discriminant has only finitely many exceptional phase parameters, permitting strict extension by continuity. At integer exponents \(1,\ldots,m-1\), the divided difference vanishes identically.
5. Integrating from \(-1\) to \(1\) and bounding the simplex integrand by the positive spectral interval gives the stated quantitative gap. At \(p=m\), the exact gap is \(4mR\).
6. The maximal-root derivative has positive sign, establishing the strict operator-norm ordering.

## Reproducibility
Run `python check_phase.py` with Python 3, NumPy, and SymPy. The companion program passed 82 supplementary checks: symbolic cycle-characteristic polynomials, positive definite spectra, sign changes across exponent intervals, exact integer phase blindness, and the order-\(m\) gap. These computations test finite parameter instances and do not certify the universal theorem.

## Limitations
No independent audit or external validation was performed. The proof covers strict diagonal dominance and single-cycle overlap graphs; the numeric gap fences need not be optimal.
