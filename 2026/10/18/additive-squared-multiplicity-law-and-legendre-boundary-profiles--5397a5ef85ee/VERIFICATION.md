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

# Verification and reproducibility

## Analytic checks

The proof independently establishes the exact Hermite divisibility constraints and the minimum-norm formula \(a=A^*(AA^*)^{-1}b\), including full Hermite-row rank for each finite degree. It derives the diagonal scaling of the Gramian, the \(O_f(K^{-1})\) oscillatory off-diagonal bound, the fixed-block Hilbert inverse estimate, and the shifted Legendre reproducing polynomial. Together these give the claimed uniform coefficient and squared-error asymptotics for all sufficiently large degrees under the stated fixed-root hypotheses.

## Finite reproducibility

The accompanying `verify.py` uses exact rational SymPy Hilbert matrices to verify the first four Legendre reproducers and numerical NumPy Gram matrices for two configurations with genuinely distinct nodes and a repeated zero. It checks all original interpolation constraints at each tested degree and compares normalized squared errors and the entire coefficient profile with the theorem. The execution output is supplied in `checks.txt`.

For \(f(z)=(1-z)^2(1+z)^3\), the theorem predicts normalized squared-error limit \(13\), and the output reaches about \(12.7112\) at \(K=286\). For the roots \(1\) and \(e^{2\pi i/3}\) of multiplicities \(2\) and \(1\), the predicted limit is \(5\) and the output reaches about \(4.9649\) at \(K=284\). The coefficient residual discrepancies also decrease in both sequences.

## Limits of the checks

These finite calculations are consistency checks only. They neither establish the asymptotic limit nor exclude hidden equivalent literature. The mathematics relies on the proof in `RESULT.md`; no independent scientific audit is claimed.
