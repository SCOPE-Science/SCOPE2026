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

# Reproducible mathematical checks

Execute `python3 verify_lacunary.py` in the folder containing this file. The program uses only the Python standard library and exact `fractions.Fraction` arithmetic and integer square roots. It exactly enumerates 27 cubic tuples of the frequency packet \(\{0,1,3\}\), confirming nine distinct cubic Fourier fibers and a single off-diagonal collision; the sum of squared fiber multiplicities at equal coefficients is \(99\).

The entire coefficient simplex \(A,B,C\in[1/5,1/2]\) with \(A+B+C=1\) is covered by 51 feasible grid rectangles, and exact interval operations verify strict negativity of \(H+I_2\). The minimum certified determinant interval for \(-H-I_2\) exceeds \(180\), and both diagonal minors are strictly positive. The second part forms a rational enclosure of the scalar polynomial and gradient at an explicit rational point; the strong-concavity error bound gives \(3.67669<M<3.67670\). This checks the critical continuum Hessian lemma and sharp bracket, not merely samples.

A passing invocation prints a single line beginning `VERIFY_OK Fourier_fibers=9 Hessian_interval_cells=51`. The analytic proof in RESULT.md supplies the normalization, exact cubic-convolution identity, boundary localization, existence and exhaustive phase equality cases. The program is a reproducible certificate for the nonstandard interval lemmas. The result concerns continuous Haar integration only and no conclusion about other exponents or longer blocks is inferred.
