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
# Mathematical verification

The theorem's positive direction is a finite, exact Gram-matrix argument: the sign-cube vectors fit in \(S^d\) precisely under the stated degree condition, positivity of the restricted convolution matrix forces nonnegative Walsh Fourier coefficients, and binomial expectation gives the nonnegative ordinary power expansion. Tensor powers then show universal-sphere positivity. The negative direction reconstructs the top Gegenbauer coefficient from the centered \(n\)-th finite difference, with the normalization explicitly displayed in RESULT.md.

## Reproducible supplementary checks

Run `python CHECK.py` in an environment with Python 3.10 or later and SymPy. The checker evaluates exact normalized Gegenbauer samples for representative dimensions, degrees and basis orders, matches each Bernstein power coefficient with its Walsh layer sum, checks nonnegativity, and independently compares the top Gegenbauer coefficient with the closed obstruction formula. A direct run returned `PASS: 2298 exact rational assertions`. The separate symbolic formula comparison covered \(2\le d\le8\) and \(1\le n\le10\). The checker is not claimed to enumerate every dimension, degree or continuous input; it supplements the analytical proof.

## Scope of verification

The proof is not formalized in a proof assistant and has not undergone independent mathematical review. The standard Schoenberg characterization and classical Gegenbauer normalization are assumed. Literature searches may miss implicit equivalent results in unindexed sources. No assertion of external certification, exhaustive publication coverage, or numerical proof of universal quantifiers is made.
