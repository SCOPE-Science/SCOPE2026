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
# Reproduction

Run the standalone script `verify.py` using Python 3.10 or newer. It requires only the Python standard library.

## Checks performed
The script evaluated 770 exact-rational checks across 35 rational amplitude choices and 22 finite population sizes, verifying that the two density Fourier-power profiles coincide and that the conditional-overlap variance contrast equals the displayed cubic coefficient. It tested 250 additional rational point configurations by two independent methods: direct integration of the circular counting function and the pairwise-kernel formula. Finally, independent finite-grid three-sample quadrature converged toward the exact gap with grid sizes 24, 48, and 96, using amplitude \(\varepsilon=1/4\): respectively approximately \(0.00097349928\), \(0.00096518867\), and \(0.00096312323\), versus the exact continuum value \(0.00096243584\).

## Proof versus numerical scope
The proof in `RESULT.md` establishes the formula for every integer \(N\ge1\) by pair-interaction decomposition, conditional expectation, and a two-frequency identity. Computation checks finite cases and implementation consistency only; grid quadrature is not an infinite or exhaustive proof. No independent audit or external validation has been carried out.
