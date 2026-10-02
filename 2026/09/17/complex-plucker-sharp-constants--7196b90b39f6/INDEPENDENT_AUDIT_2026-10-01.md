---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

For the complex Plücker-coordinate multilinear map on \(\ell^p\), the optimal constant is \(1\) for \(0<p\le2\), \(n^{n(1/2-1/p)}\) for \(2<p<\infty\), and \(n^{n/2}\) at \(p=\infty\); the complex formula also forces right-continuity at \(2\) and yields the stated real comparison.

## Correctness — PASS

The supercritical proof was reconstructed independently. At \(p=2\), Cauchy–Binet plus Gram-Hadamard gives norm one. At \(p=\infty\), determinant Hadamard gives the upper bound \(n^{n/2}\), while the complex Fourier matrix attains it in every order. Multilinear complex interpolation therefore gives the stated upper bound for every \(p>2\), and the same Fourier frame attains it. Independent numerical checks of Fourier determinants for orders 2, 3, and 5 matched \(n^{n/2}\) and the finite-\(p\) ratios.

**Evidence:** package RESULT.md; D. V. Feldman, arXiv:2608.00983; J. Bergh and J. Löfström, Interpolation Spaces; Tadej–Życzkowski, arXiv:quant-ph/0512154

**Residual risk:** The scalar-field distinction is essential: the exact formula is for complex scalars; the real constant can remain smaller in non-Hadamard orders.

## Originality — PASS

The recent primary source explicitly states that exact \(p>2\) constants and right-continuity at \(2\) are open and ties its lower bound to the real maximal-determinant problem. Its own framework uses complex multilinear interpolation and complex Plücker geometry. Searches under Plücker coordinates, exterior powers, compound matrices, minor norms, and complex-Hadamard extremizers found no earlier statement of the exact complex constant. The package's scalar-field separation therefore appears to be a genuine correction/resolution rather than a restatement.

**Equivalent formulations.** The relevant equivalent formulation is an \(n\)-linear determinant/minor map norm; searches did not uncover the sharp complex norm.

**Broader coverage.** Generic boundedness does not imply the exact Fourier-saturated constant.

**Exact database or table.** The exact value comes from a universal construction, not a finite table.

**Claim versus prior implication.** The missing step is the complex \(p=\infty\) extremizer available in every order; the checked source does not state the resulting equality.

**Checked sources:** https://arxiv.org/abs/2608.00983; https://arxiv.org/abs/quant-ph/0512154; targeted searches for exterior-power/compound-matrix sharp norms

**Residual risk:** Older tensor-norm or compound-matrix literature could encode the same sharp norm without Plücker terminology; targeted searches found no such statement, and Feldman likewise reports not locating the sharp constant in print.

## Value — PASS

The theorem gives a closed-form exact norm for a natural multilinear invariant, resolves an explicit recent open regime, and cleanly separates the complex problem from the real Hadamard obstruction. The field distinction also settles a natural continuity question.

**Residual risk:** The proof is short once the scalar-field distinction is noticed, but the result resolves a natural exact constant rather than an arbitrary slice.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
