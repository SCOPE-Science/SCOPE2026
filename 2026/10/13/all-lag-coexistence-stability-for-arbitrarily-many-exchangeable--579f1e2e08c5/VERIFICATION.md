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
# Verification and limits

The public proof in `RESULT.md` establishes the proposition by strict scalar monotonicity and positive cubic Hurwitz determinants. No finite search or floating-point test is used as evidence of infinite-dimensional or parameter-uniform validity.

Run `python3 verify.py` using Python 3's standard library. Actual package check: `VERIFY_OK 2916 exact rational characteristic-polynomial and invariant-mode checks`. This reconstructs the three-by-three determinant, independently calculates the four coefficients, checks the exact Routh factorization, and evaluates the full linearization on common/zero-sum perturbations for each representative rational tuple. Each quantity is a Python `Fraction`; no float approximation, optimizer, network request, or external dependency is involved.

Scientific limits: the symbolic proof requires common pathogen parameters, a finite number of pathogens, positive finite rates \(a,b,c,\beta_0\), sensitivity \(k\ge0\), and fraction \(0\le s\le1\). The claimed equilibrium exists only for \(\mathcal R_0>1\). Stability is strictly local, not a statement that every initial condition converges or that limit cycles cannot exist away from the coexistence equilibrium. Independent validation is not performed.
