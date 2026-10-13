# Self-review

## Correctness
**PASS.** Axial averaging is an orthogonal Hilbert--Schmidt projection that preserves the spin-coherent convex hull, so a diagonal target has a diagonal closest classical state. The symmetric two-qubit partial-transpose calculation gives the exact diagonal classical region \(x^2+2b\le1\). For a nonclassical target, projection to that region reduces to the one-variable function
\[F(y)=\frac12(x-y)^2+\frac32\left(b-\frac{1-y^2}{2}\right)^2.\]
Its stationary cubic has exactly one real root in \((-1,1)\): monotonicity handles \(b\ge1/6\), while for \(0<b<1/6\) nonclassicality makes the depressed-cubic discriminant strictly positive. The root-of-unity coherent decomposition is exact, and rank three proves minimal length. The bundled checker reproduces the algebraic identities and representative projections with `VERIFY_OK`.

Risk: the finite replay checks are not an exhaustive proof; the continuum claim rests on the analytic convexity, twirling, PPT, and cubic-uniqueness arguments given in `RESULT.md`.

## Originality
**PASS.** The 2015 direct source gives exact pure-state formulas but computes general mixed-state quantumness numerically by coherent-state sampling and quadratic programming. It analytically covers a special pure-state/closest-classical segment; in the present diagonal class that includes the ray \(x=0\), \(b>1/2\), which is explicitly acknowledged. The off-axis two-parameter formula, unique cubic optimizer, and minimal three-coherent realization were not found in the inspected source or targeted database searches. The 2011 paper parameterizes the classical body, and general Hilbert--Schmidt closest-separable papers optimize over all separable two-qubit states rather than the symmetric-separable spin-classical subset.

Risk: a differently phrased Euclidean-projection calculation may exist, and the full body of the 2011 parametrization paper was not available through the successful text route. Its indexed contribution and targeted searches did not show the claimed distance theorem.

## Value
**PASS.** The diagonal family is the full axially invariant mixed spin-1 slice up to rotations, not an arbitrary parameter cut. Replacing a numerical closest-classical-state optimization by a closed cubic projection gives a useful exact benchmark and structural preparation result. The minimum coherent decomposition length is also fixed exactly at three for every nonclassical state in the family.

The claim remains deliberately limited to diagonal spin-1 mixtures and does not assert the arbitrary-mixed upper-bound conjecture.

Self-review: passed. Independent audit: not yet performed.
