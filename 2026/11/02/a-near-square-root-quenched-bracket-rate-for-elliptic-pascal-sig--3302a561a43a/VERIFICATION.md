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

## Analytic verification
The proof in `RESULT.md` independently derives the Lucas parity/submask equivalence, the exact product-moment identity, the Boolean symmetric-difference bound, the quasi-polylogarithmic exceptional-index estimate, a dyadic maximal second-moment inequality, and the almost-sure transfer through independent geometric holding lengths. The fair-bit triangular invertibility and ordinary renewal-reward central limit theorem furnish the sharpness example. The infinite almost-sure theorem relies on these analytical steps, not on finite testing.

## Finite checker
Run `python3 check.py` with a standard Python 3 installation. The checker uses exact `fractions.Fraction`, `math.comb`, and exhaustive finite products: it verifies 10,912 assertions for binomial parity, submask distances, biased exact sign-product moments, interval moment bounds and the inverse of the fair Pascal transform. Actual output is included in `check_output.txt`. No random sampling, external dependencies, or network access is used.

## Scientific limitations
The bound controls the polynomial exponent optimally but does not identify the smallest possible subpolynomial factor. The fair-case lower-bound argument is under the joint law, which suffices to preclude any uniform smaller almost-sure exponent; it is not a claim of an explicit lower bound for each nonstationary parameter profile. The result is not independently audited or externally certified.
